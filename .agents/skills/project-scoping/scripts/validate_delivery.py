#!/usr/bin/env python3
"""Read-only checks shared by the three project skills. Python stdlib only.

Checks the JSON Schema keywords used in the bundled local schemas and delivery
invariants. Evidence presence does not verify its contents or human authority.
Usage: python validate_delivery.py CONTRACT.json
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

SCHEMA = Path(__file__).resolve().parents[1] / "references/delivery.schema.json"
SEMVER = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")


def schema_errors(value, schema, schema_path, label="$", root=None):
    """Validate only local, trusted schemas; never fetch remote schema resources."""
    root = schema if root is None else root
    errors = []
    if "$ref" in schema:
        filename, _, fragment = schema["$ref"].partition("#")
        if filename:
            schema_path = (schema_path.parent / filename).resolve()
            root = json.loads(schema_path.read_text(encoding="utf-8"))
        target = root
        for key in fragment.lstrip("/").split("/") if fragment else []:
            target = target[unquote(key).replace("~1", "/").replace("~0", "~")]
        return schema_errors(value, target, schema_path, label, root)
    if "anyOf" in schema and not any(not schema_errors(value, s, schema_path, label, root) for s in schema["anyOf"]):
        errors.append(f"{label}: does not match any allowed shape")
    for rule in schema.get("allOf", []):
        errors.extend(schema_errors(value, rule, schema_path, label, root))
    if "if" in schema and not schema_errors(value, schema["if"], schema_path, label, root):
        errors.extend(schema_errors(value, schema.get("then", {}), schema_path, label, root))
    types = {"object": isinstance(value, dict), "array": isinstance(value, list),
             "string": isinstance(value, str), "boolean": type(value) is bool,
             "integer": type(value) is int, "null": value is None,
             "number": type(value) in (int, float)}
    expected = schema.get("type")
    if expected and not any(types[t] for t in ([expected] if isinstance(expected, str) else expected)):
        return errors + [f"{label}: expected {expected}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{label}: expected {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{label}: invalid value {value!r}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{label}: missing {key}")
        props = schema.get("properties", {})
        for key, child in value.items():
            if key in props:
                errors.extend(schema_errors(child, props[key], schema_path, f"{label}.{key}", root))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{label}: unknown property {key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{label}: too few entries")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            errors.append(f"{label}: duplicate entries")
        for i, child in enumerate(value):
            errors.extend(schema_errors(child, schema.get("items", {}), schema_path, f"{label}[{i}]", root))
    if isinstance(value, str):
        if len(value.strip()) < schema.get("minLength", 0):
            errors.append(f"{label}: empty or too short")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{label}: invalid format {value!r}")
        if schema.get("format") == "date":
            try:
                if datetime.date.fromisoformat(value).isoformat() != value:
                    raise ValueError()
            except ValueError:
                errors.append(f"{label}: expected YYYY-MM-DD date")
    return errors


def delivery_errors(data, allowed_refs=None):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = schema_errors(data, schema, SCHEMA, "delivery")
    if errors:
        return errors  # Semantic checks below may safely rely on the shape.

    def index(entries, key, label):
        result = {}
        for entry in entries:
            identity = entry[key]
            if identity in result:
                errors.append(f"{label}: duplicate {identity}")
            result[identity] = entry
        return result

    items = index(data["items"], "ref", "items")
    releases = index(data["releases"], "version", "releases")
    milestones = index(data["milestones"], "id", "milestones")
    changes = {}
    change_versions = {}
    for version, release in releases.items():
        if release["status"] != "proposed" and not release["approval_ref"]:
            errors.append(f"{version}: planned/developed/delivered requires human approval_ref")
        if release["status"] in {"developed", "delivered"} and not release["evidence_refs"]:
            errors.append(f"{version}: developed/delivered requires evidence_refs")
        current = tuple(map(int, version.split(".")))
        if current[0] >= 1 and release["status"] != "proposed":
            if not all(data[k] for k in ("public_contracts", "stability_criteria", "stability_approval_ref")):
                errors.append(f"{version}: stable release needs contracts, stability criteria and approval")
        baseline = release["baseline_version"]
        previous = tuple(map(int, baseline.split("."))) if baseline else None
        if previous and current <= previous:
            errors.append(f"{version}: must be newer than baseline {baseline}")
        for change in release["changes"]:
            cid = change["id"]
            if cid in changes:
                errors.append(f"Duplicate change {cid}; a change belongs to one release")
            changes[cid] = change
            change_versions[cid] = version
            if release["status"] != "proposed" and change["compatibility"] == "unknown":
                errors.append(f"{cid}: compatibility must be assessed before release assignment approval")
            for ref in change["item_refs"]:
                if ref not in items:
                    errors.append(f"{cid}: unknown item {ref}")
                elif release["status"] != "proposed" and version not in items[ref]["planned_versions"]:
                    errors.append(f"{cid}: {ref} missing reciprocal planned_versions assignment")
            if previous and current > previous:
                breaking = change["compatibility"] == "breaking"
                feature = change["kind"] == "feature"
                if previous[0] == 0 and current[0] == 0:
                    if (breaking or feature) and current[1] <= previous[1]:
                        errors.append(f"{cid}: 0.x feature/breaking change requires MINOR increment")
                elif previous[0] >= 1:
                    if breaking and current[0] <= previous[0]:
                        errors.append(f"{cid}: incompatible public contract requires MAJOR increment")
                    if feature and current[:2] <= previous[:2]:
                        errors.append(f"{cid}: compatible functionality requires at least MINOR increment")
                if current[0] > previous[0] and current[1:] != (0, 0):
                    errors.append(f"{version}: MAJOR increment resets MINOR/PATCH")
                elif current[1] > previous[1] and current[2] != 0:
                    errors.append(f"{version}: MINOR increment resets PATCH")

    scope_refs = set(data["scope"]["feature_refs"])
    if not scope_refs or any(not re.fullmatch(r"FEAT-\d{3,}", r) for r in scope_refs):
        errors.append("scope.feature_refs: requires canonical FEAT-* IDs")
    for ref in scope_refs:
        if ref not in items:
            errors.append(f"Scope feature {ref} missing progress item")
        elif data["scope"]["kind"] == "mvp" and items[ref]["scope"] != "mvp":
            errors.append(f"{ref}: indispensable MVP feature must have scope=mvp")
        elif items[ref]["scope"] == "future":
            errors.append(f"{ref}: future-only feature cannot enter functional scope")
    for ref, item in items.items():
        if allowed_refs is not None and ref not in allowed_refs:
            errors.append(f"Unknown contract item {ref}")
        if ref.startswith("FEAT-") and item["scope"] == "mvp" and ref not in scope_refs:
            errors.append(f"{ref}: MVP feature absent from scope.feature_refs")
        if item["decision_status"] == "approved" and not item["acceptance_criteria"]:
            errors.append(f"{ref}: approved item needs acceptance criteria")
        assigned = item["planned_versions"] or item["delivered_versions"]
        if assigned and item["decision_status"] != "approved":
            errors.append(f"{ref}: assignments require approved decision")
        if item["scope"] == "future" and (assigned or item["development_status"] not in {"unknown", "not_started"} or item["delivery_status"] not in {"unknown", "not_delivered"}):
            errors.append(f"{ref}: future context cannot imply assignment/development/delivery")
        for field in ("planned_versions", "delivered_versions"):
            for version in item[field]:
                release = releases.get(version)
                if release is None or release["status"] == "proposed":
                    errors.append(f"{ref}: {field} references missing/unapproved release {version}")
                    continue
                if not any(ref in c["item_refs"] for c in release["changes"]):
                    errors.append(f"{ref}: no matching change in {version}")
                if field == "delivered_versions" and (release["status"] != "delivered" or version not in item["planned_versions"]):
                    errors.append(f"{ref}: delivered_versions requires delivered release and planned assignment")
        actual = item["delivery_status"] in {"partial", "delivered"}
        if item["development_status"] in {"in_progress", "complete"} and not item["evidence_refs"]:
            errors.append(f"{ref}: development progress requires evidence_refs")
        if actual != bool(item["delivered_versions"]):
            errors.append(f"{ref}: delivery_status and delivered_versions disagree")
        if actual and (not item["evidence_refs"] or item["development_status"] in {"unknown", "not_started"}):
            errors.append(f"{ref}: actual delivery needs implementation and evidence")
        if item["delivery_status"] == "delivered" and (item["development_status"] != "complete" or not item["acceptance_criteria"]):
            errors.append(f"{ref}: whole-item delivery needs complete development and full acceptance criteria")

    edges = set()
    for dep in data["dependencies"]:
        edge = (dep["from_ref"], dep["to_ref"], dep["kind"])
        if edge in edges:
            errors.append(f"Duplicate dependency {edge}")
        edges.add(edge)
        if dep["from_ref"] not in items or dep["to_ref"] not in items or dep["from_ref"] == dep["to_ref"]:
            errors.append(f"Invalid dependency {edge}")
    for cid, change in changes.items():
        for prerequisite in change["depends_on"]:
            if prerequisite not in changes or prerequisite == cid:
                errors.append(f"{cid}: invalid prerequisite {prerequisite}")
            elif tuple(map(int, change_versions[prerequisite].split("."))) > tuple(map(int, change_versions[cid].split("."))):
                errors.append(f"{cid}: prerequisite is in a later release")
    # A change dependency cycle makes incremental planning impossible.
    visiting, visited = set(), set()
    def visit(cid):
        if cid in visiting:
            errors.append(f"Cyclic change dependency at {cid}")
            return
        if cid in visited or cid not in changes:
            return
        visiting.add(cid)
        for dep in changes[cid]["depends_on"]:
            visit(dep)
        visiting.remove(cid)
        visited.add(cid)
    for cid in changes:
        visit(cid)
    for milestone in milestones.values():
        if milestone["status"] == "achieved":
            if not milestone["evidence_refs"]:
                errors.append(f"{milestone['id']}: achievement needs evidence")
            if milestone["kind"] == "mvp" and (data["scope"]["kind"] != "mvp" or any(items.get(r, {}).get("delivery_status") != "delivered" for r in scope_refs)):
                errors.append(f"{milestone['id']}: MVP achievement requires every indispensable feature delivered")
    return errors


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "delivery" not in data:
            print("ERROR: expected contract with explicit delivery metadata")
            return 1
        errors = delivery_errors(data["delivery"])
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    for error in errors:
        print("ERROR:", error)
    print(f"Delivery checks: {len(errors)} error(s); verify evidence contents manually")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
