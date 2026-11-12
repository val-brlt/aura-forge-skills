#!/usr/bin/env python3
"""Validate a UX JSON contract and promoted HTML gallery.

Standard library only. Static checks do not establish design quality, visual
approval, runtime JavaScript correctness or delivery status.

Usage:
    python .agents/skills/project-ux/scripts/validate_ux_docs.py docs/docs-project --version v1
    python .agents/skills/project-ux/scripts/validate_ux_docs.py docs/docs-project
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

FEAT = re.compile(r"FEAT-\d{3,}\Z")
FLOW = re.compile(r"FLOW-\d{3,}\Z")
SCREEN = re.compile(r"SCREEN-\d{3,}\Z")
ACT = re.compile(r"ACT-\d{3,}\Z")
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "project-scoping/scripts"))
from validate_delivery import delivery_errors, schema_errors
from documentation_paths import resolve_backlog

UX_SCHEMA = Path(__file__).resolve().parents[1] / "references/ux-contract.schema.json"
FEAT_FIND = re.compile(r"FEAT-\d{3,}\b")
HEADING = re.compile(r"^##\s+(.+?)\s*$", re.M)
STATUS = {"draft", "approved"}
COVERAGE = {"covered", "no_ui", "unresolved"}
CHANGE = {"new", "modified", "reused"}
HTML_ASSET_TAGS = {"script", "img", "source", "iframe", "audio", "video"}


class HTMLDetails(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.screens: set[str] = set()
        self.nav: set[str] = set()
        self.assets: list[str] = []
        self.external: list[str] = []
        self.image_screens: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        screen_id = a.get("id") or ""
        if SCREEN.fullmatch(screen_id):
            self.screens.add(screen_id)
            if tag in {"img", "svg", "canvas", "picture"}:
                self.image_screens.add(screen_id)
        href = a.get("href") or ""
        if tag == "a" and href.startswith("#") and SCREEN.fullmatch(href[1:]):
            self.nav.add(href[1:])
        urls: list[str] = []
        if tag == "link" and href:
            urls.append(href)
        if tag in HTML_ASSET_TAGS:
            if a.get("src"):
                urls.append(a["src"] or "")
            if tag == "video" and a.get("poster"):
                urls.append(a["poster"] or "")
        for url in urls:
            parsed = urlsplit(url)
            if parsed.scheme and parsed.scheme != "data" or url.startswith("//"):
                self.external.append(url)
            elif parsed.path:
                self.assets.append(unquote(parsed.path))


class Validation:
    def __init__(self, docs_root: Path) -> None:
        self.root = docs_root.resolve()
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.html_cache: dict[Path, HTMLDetails] = {}

    def err(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root))
        except ValueError:
            return str(path)

    def read(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as ex:
            self.err(f"{self.rel(path)} unreadable: {ex}")
            return None

    def frontmatter(self, path: Path, text: str) -> dict[str, str]:
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
        if match is None:
            self.err(f"{self.rel(path)}: YAML frontmatter missing")
            return {}
        result: dict[str, str] = {}
        for line in match.group(1).splitlines():
            m = re.fullmatch(r"([a-z][a-z0-9_]*):\s*(.*?)\s*", line)
            if m:
                result[m.group(1)] = m.group(2).strip("\"'")
        return result

    def scope_features(self, path: Path, text: str) -> set[str]:
        found: set[str] = set()
        heads = list(HEADING.finditer(text))
        wanted = {"Fonctionnalités incluses", "Évolutions des fonctionnalités existantes"}
        for i, h in enumerate(heads):
            if h.group(1).strip() in wanted:
                end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
                found.update(FEAT_FIND.findall(text[h.end():end]))
        if not found:
            self.err(f"{self.rel(path)}: no FEAT-* IDs in the functional scope's included/evolving sections")
        return found

    def canonical_features(self) -> set[str]:
        result: dict[str, Path] = {}
        for path in (self.root / "modules").glob("**/*.md"):
            if path.name == "MODULE.md":
                continue
            contents = self.read(path)
            if contents is None:
                continue
            metadata = self.frontmatter(path, contents)
            fid = metadata.get("id", "")
            if not FEAT.fullmatch(fid):
                self.err(f"{self.rel(path)}: missing/invalid canonical FEAT ID")
            elif fid in result:
                self.err(f"Duplicate feature {fid} in {self.rel(path)} and {self.rel(result[fid])}")
            else:
                result[fid] = path
        return set(result)

    def require_str(self, obj: dict[str, Any], key: str, context: str, nonempty: bool = True) -> str:
        val = obj.get(key)
        if not isinstance(val, str) or (nonempty and not val.strip()):
            self.err(f"{context}: {key} must be a nonempty string")
            return ""
        return val

    def require_list(self, obj: dict[str, Any], key: str, context: str) -> list[Any]:
        val = obj.get(key)
        if not isinstance(val, list):
            self.err(f"{context}: {key} must be an array")
            return []
        return val

    def id_list(self, obj: dict[str, Any], key: str, context: str, regex: re.Pattern[str]) -> set[str]:
        vals = self.require_list(obj, key, context)
        result: set[str] = set()
        for val in vals:
            if not isinstance(val, str) or not regex.fullmatch(val):
                self.err(f"{context}: invalid {key} ID {val!r}")
            elif val in result:
                self.err(f"{context}: duplicate {key} ID {val}")
            else:
                result.add(val)
        return result

    def local_path(self, base: Path, url: str, context: str, want_html: bool = False) -> tuple[Path, str] | None:
        if ".scratch/" in url or ".scratch\\" in url:
            self.err(f"{context}: final artifact links to scratch ({url})")
            return None
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.query:
            self.err(f"{context}: expected local relative file path, got {url!r}")
            return None
        target = (base / unquote(parsed.path)).resolve()
        if not target.is_relative_to(self.root):
            self.err(f"{context}: path leaves DOCS_ROOT: {url!r}")
            return None
        if not target.is_file():
            self.err(f"{context}: missing file {self.rel(target)}")
            return None
        if want_html and target.suffix.lower() != ".html":
            self.err(f"{context}: mockup is not HTML: {url!r}")
            return None
        return target, unquote(parsed.fragment)

    def html_check(self, path: Path, expected_screen: str) -> None:
        if path not in self.html_cache:
            contents = self.read(path)
            if contents is None:
                return
            if ".scratch/" in contents or ".scratch\\" in contents:
                self.err(f"{self.rel(path)}: references scratch")
            detail = HTMLDetails()
            try:
                detail.feed(contents)
            except Exception as exc:
                self.err(f"{self.rel(path)}: invalid HTML: {exc}")
                return
            self.html_cache[path] = detail
            if not detail.screens:
                self.err(f"{self.rel(path)}: no id=SCREEN-* HTML containers")
            for sid in detail.image_screens:
                self.err(f"{self.rel(path)}: {sid} is an image/canvas, not an HTML screen container")
            for sid in detail.screens - detail.nav:
                self.err(f"{self.rel(path)}: missing navigation href=\"#{sid}\"")
            for url in detail.external:
                self.err(f"{self.rel(path)}: external dependency {url!r}; must work offline")
            for url in detail.assets:
                self.local_path(path.parent, url, self.rel(path))
        if path in self.html_cache and expected_screen not in self.html_cache[path].screens:
            self.err(f"{self.rel(path)}: missing HTML container #{expected_screen}")

    def check_version(self, version: str | None, available_features: set[str], contract_path: Path | None = None) -> None:
        contract_path = (contract_path or self.root / "versions" / str(version) / "ux/UX-CONTRACT.json").resolve()
        if not contract_path.is_relative_to(self.root):
            self.err("Contract path leaves DOCS_ROOT")
            return
        contract_txt = self.read(contract_path)
        if contract_txt is None:
            return
        try:
            data = json.loads(contract_txt)
        except json.JSONDecodeError as exc:
            self.err(f"{self.rel(contract_path)}: invalid JSON: {exc}")
            return
        schema = json.loads(UX_SCHEMA.read_text(encoding="utf-8"))
        shape_errors = schema_errors(data, schema, UX_SCHEMA)
        if shape_errors:
            self.errors.extend(shape_errors)
            return
        legacy = data["schemaVersion"] == 1
        version = version or data["version"]
        scope_url = f"versions/{version}/VERSION.md" if legacy else data["scope"]
        checked_scope = self.local_path(self.root, scope_url, "scope")
        if checked_scope is None:
            return
        scope_path = checked_scope[0]
        summary_path = contract_path.parent / "UX-SUMMARY.md"
        scope_txt = self.read(scope_path)
        summary_txt = self.read(summary_path)
        if any(x is None for x in (scope_txt, summary_txt, contract_txt)):
            return
        assert scope_txt is not None and summary_txt is not None and contract_txt is not None
        scope_meta = self.frontmatter(scope_path, scope_txt)
        if (legacy and scope_meta.get("version") != version) or scope_meta.get("status") not in {"approved", "delivered"}:
            self.err(f"{self.rel(scope_path)}: UX requires approved/delivered scope for {version}")
        included = self.scope_features(scope_path, scope_txt)
        for missing in sorted(included - available_features):
            self.err(f"{version}: {missing} has no canonical feature card")
        summary_meta = self.frontmatter(summary_path, summary_txt)
        if summary_meta.get("version") != version:
            self.err(f"{self.rel(summary_path)}: version metadata mismatch")
        if summary_meta.get("scope") != scope_url:
            self.err(f"{self.rel(summary_path)}: wrong scope path")
        if summary_meta.get("status") not in STATUS:
            self.err(f"{self.rel(summary_path)}: status must be draft or approved")
        for heading in ["Objectifs et parcours principaux", "Navigation et décisions de conception", "Maquettes validées", "Anticipation des évolutions futures (hors périmètre)"]:
            if re.search(r"^##\s+" + re.escape(heading) + r"\s*$", summary_txt, re.M) is None:
                self.err(f"{self.rel(summary_path)}: missing ## {heading}")
        if ".scratch/" in summary_txt or ".scratch\\" in summary_txt:
            self.err(f"{self.rel(summary_path)}: links to scratch")
        if data.get("version") != version or data.get("scope") != scope_url:
            self.err(f"{self.rel(contract_path)}: version or scope mismatch")
        if data.get("status") not in STATUS:
            self.err(f"{self.rel(contract_path)}: status must be draft or approved")
        if data.get("status") != summary_meta.get("status"):
            self.err(f"{version}: summary and contract approval status differ")
        approved = data.get("status") == "approved"
        if ".scratch/" in contract_txt or ".scratch\\" in contract_txt:
            self.err(f"{self.rel(contract_path)}: references scratch")

        flows: dict[str, dict[str, set[str]]] = {}
        for raw in self.require_list(data, "flows", version):
            if not isinstance(raw, dict):
                self.err(f"{version}: flow must be object")
                continue
            fid = self.require_str(raw, "id", "flow")
            if not FLOW.fullmatch(fid):
                self.err(f"{version}: invalid flow id {fid!r}")
                continue
            if fid in flows:
                self.err(f"{version}: duplicate flow {fid}")
            self.require_str(raw, "name", fid)
            feature_ids = self.id_list(raw, "featureIds", fid, FEAT)
            screen_ids = self.id_list(raw, "screenIds", fid, SCREEN)
            if not feature_ids or not screen_ids:
                self.err(f"{version}: {fid} needs featureIds and screenIds")
            steps = self.require_list(raw, "steps", fid)
            if not steps:
                self.err(f"{version}: {fid} has no steps")
            for step in steps:
                if not isinstance(step, dict):
                    self.err(f"{fid}: step must be object")
                    continue
                sid = self.require_str(step, "screenId", fid)
                if sid not in screen_ids:
                    self.err(f"{fid}: step screen {sid} not in flow screenIds")
                self.require_str(step, "action", fid)
                self.require_str(step, "result", fid)
            for value in self.require_list(raw, "alternatives", fid):
                if not isinstance(value, str):
                    self.err(f"{fid}: alternatives must be strings")
            flows[fid] = {"features": feature_ids, "screens": screen_ids}

        screens: dict[str, dict[str, set[str]]] = {}
        used_actions: set[str] = set()
        for raw in self.require_list(data, "screens", version):
            if not isinstance(raw, dict):
                self.err(f"{version}: screen must be object")
                continue
            sid = self.require_str(raw, "id", "screen")
            if not SCREEN.fullmatch(sid):
                self.err(f"{version}: invalid screen id {sid!r}")
                continue
            if sid in screens:
                self.err(f"{version}: duplicate screen {sid}")
            self.require_str(raw, "name", sid)
            features = self.id_list(raw, "featureIds", sid, FEAT)
            flow_ids = self.id_list(raw, "flowIds", sid, FLOW)
            if not features or not flow_ids:
                self.err(f"{sid}: must link to at least one feature and flow")
            change = self.require_str(raw, "change", sid)
            if change not in CHANGE:
                self.err(f"{sid}: change must be new/modified/reused")
            url = self.require_str(raw, "mockup", sid)
            checked = self.local_path(contract_path.parent, url, sid, want_html=True) if url else None
            if checked is not None:
                path, anchor = checked
                if anchor != sid:
                    self.err(f"{sid}: mockup URL fragment must be #{sid}")
                self.html_check(path, sid)
                if change in {"new", "modified"} and path != (contract_path.parent / "mockups" / "index.html").resolve():
                    self.err(f"{sid}: new/modified screen must point to this contract's approved mockups/index.html")
            states = self.require_list(raw, "states", sid)
            if not states or any(not isinstance(x, str) or not x.strip() for x in states):
                self.err(f"{sid}: states must be a nonempty string list")
            interactions = self.require_list(raw, "interactions", sid)
            for interaction in interactions:
                if not isinstance(interaction, dict):
                    self.err(f"{sid}: interaction must be an object")
                    continue
                action_id = self.require_str(interaction, "id", sid)
                if not ACT.fullmatch(action_id):
                    self.err(f"{sid}: invalid ACT id {action_id!r}")
                elif action_id in used_actions:
                    self.err(f"{version}: duplicate action id {action_id}")
                used_actions.add(action_id)
                self.require_str(interaction, "trigger", action_id)
                self.require_str(interaction, "result", action_id)
            for val in self.require_list(raw, "accessibilityNotes", sid):
                if not isinstance(val, str):
                    self.err(f"{sid}: accessibilityNotes must be strings")
            screens[sid] = {"features": features, "flows": flow_ids}

        for fid, info in flows.items():
            for sid in info["screens"]:
                if sid not in screens:
                    self.err(f"{fid}: unknown screen {sid}")
                elif fid not in screens[sid]["flows"]:
                    self.err(f"{fid}: {sid} does not link back to the flow")
            for feat in info["features"]:
                if feat not in included:
                    self.err(f"{fid}: feature {feat} not in {version}'s scope")
        for sid, info in screens.items():
            for fid in info["flows"]:
                if fid not in flows:
                    self.err(f"{sid}: unknown flow {fid}")
                elif sid not in flows[fid]["screens"]:
                    self.err(f"{sid}: {fid} does not link back to screen")
            for feat in info["features"]:
                if feat not in included:
                    self.err(f"{sid}: feature {feat} not in {version}'s scope")

        coverage_seen: set[str] = set()
        for raw in self.require_list(data, "featureCoverage", version):
            if not isinstance(raw, dict):
                self.err(f"{version}: coverage entry must be object")
                continue
            feat = self.require_str(raw, "featureId", "coverage")
            if not FEAT.fullmatch(feat):
                self.err(f"{version}: invalid coverage feature {feat!r}")
                continue
            if feat in coverage_seen:
                self.err(f"{version}: duplicate coverage for {feat}")
            coverage_seen.add(feat)
            if feat not in included:
                self.err(f"{version}: {feat} covered but not in functional scope")
            kind = self.require_str(raw, "coverage", feat)
            sids = self.id_list(raw, "screenIds", feat, SCREEN)
            fids = self.id_list(raw, "flowIds", feat, FLOW)
            if kind == "covered":
                if not sids or not fids:
                    self.err(f"{feat}: covered requires SCREEN and FLOW references")
                for sid in sids:
                    if sid not in screens or feat not in screens[sid]["features"]:
                        self.err(f"{feat}: {sid} missing or does not link back to this feature")
                for fid in fids:
                    if fid not in flows or feat not in flows[fid]["features"]:
                        self.err(f"{feat}: {fid} missing or does not link back to this feature")
                    elif not sids.intersection(flows[fid]["screens"]):
                        self.err(f"{feat}: {fid} has no screen in {feat}'s coverage")
            elif kind == "no_ui":
                if sids or fids:
                    self.err(f"{feat}: no_ui requires empty screenIds and flowIds")
                note = raw.get("justification")
                if not isinstance(note, str) or len(note.strip()) < 15:
                    self.err(f"{feat}: no_ui requires a meaningful user-approved justification")
            elif kind == "unresolved":
                if approved:
                    self.err(f"{feat}: unresolved coverage blocks approved status")
            else:
                self.err(f"{feat}: invalid coverage {kind!r}")
        for fid in sorted(included - coverage_seen):
            self.err(f"{version}: missing featureCoverage entry for {fid}")

        if "delivery" in data:
            required_items = included | set(flows) | set(screens) | used_actions
            allowed = available_features | set(flows) | set(screens) | used_actions
            delivery_issues = delivery_errors(data["delivery"], allowed)
            self.errors.extend(delivery_issues)
            if not delivery_issues:
                delivery = data["delivery"]
                if delivery["scope"]["path"] != scope_url or set(delivery["scope"]["feature_refs"]) != included:
                    self.err(f"{version}: delivery functional scope differs from canonical scope")
                item_refs = {item["ref"] for item in delivery["items"]}
                for ref in sorted(required_items - item_refs):
                    self.err(f"{version}: missing delivery progress item for {ref}")
        elif legacy:
            self.warn(f"{version}: legacy contract; implementation/release state remains unknown")

        considerations = self.require_list(data, "futureConsiderations", version)
        for idx, raw in enumerate(considerations):
            ctx = f"{version} futureConsiderations[{idx}]"
            if not isinstance(raw, dict):
                self.err(f"{ctx}: must be an object")
                continue
            source = self.require_str(raw, "source", ctx)
            self.require_str(raw, "item", ctx)
            self.require_str(raw, "navigationImplication", ctx)
            if source:
                self.local_path(self.root, source, ctx)
        try:
            backlog = resolve_backlog(self.root)
        except ValueError as exc:
            self.err(str(exc))
            backlog = None
        if backlog is not None and backlog.is_file() and not considerations:
            self.warn(f"{version}: futureConsiderations is empty; verify whether the backlog has relevant future needs (outside-change does not imply future)")

        if screens:
            # The user-facing summary must point to a real gallery, including
            # a prior version's approved gallery for wholly reused screens.
            links = re.findall(r"\]\(([^)]+\.html(?:#[^)]*)?)\)", summary_txt)
            if not links:
                self.err(f"{self.rel(summary_path)}: must link to a final HTML gallery")
            for link in links:
                self.local_path(summary_path.parent, link, self.rel(summary_path), want_html=True)
        if approved and summary_meta.get("status") != "approved":
            self.err(f"{version}: contract approved, summary not approved")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docs_root", type=Path)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--version", help="Check an existing document baseline directory (legacy v1 or X.Y.Z)")
    selection.add_argument("--contract", type=Path, help="Contract path relative to working directory; accepts global MVP UX")
    args = parser.parse_args()
    root = args.docs_root
    if not root.is_dir():
        print(f"ERROR: documentation root not found: {root}", file=sys.stderr)
        return 2
    check = Validation(root)
    features = check.canonical_features()
    if args.contract:
        contracts = [(None, args.contract)]
    elif args.version:
        if re.fullmatch(r"(?:v\d+(?:\.\d+)*|(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*))", args.version) is None:
            print("ERROR: invalid version directory", file=sys.stderr)
            return 2
        contracts = [(args.version, None)]
    else:
        contracts = [(None, p) for p in sorted(root.rglob("UX-CONTRACT.json"))]
    if not contracts:
        print("ERROR: no UX contract versions found", file=sys.stderr)
        return 2
    for version, path in contracts:
        check.check_version(version, features, path)
    for warning in check.warnings:
        print("WARNING:", warning)
    for error in check.errors:
        print("ERROR:", error)
    print(f"Checked {len(contracts)} contract(s): {len(check.errors)} error(s), {len(check.warnings)} warning(s)")
    return 1 if check.errors else 0


if __name__ == "__main__":
    sys.exit(main())
