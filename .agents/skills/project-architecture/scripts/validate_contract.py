#!/usr/bin/env python3
"""Validate Aura Forge architecture contract structure, references and handoff gate.

Usage: python scripts/validate_contract.py path/to/ARCHITECTURE-CONTRACT.json
Requires only Python stdlib; installs no dependencies. If jsonschema is already
available, also checks the complete JSON Schema. This does not verify that external
FEAT/FLOW/SCREEN references or approval evidence actually exist in the repository.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "references" / "architecture-contract.schema.json"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_contract.py PATH_TO_CONTRACT.json")
        return 2
    path = pathlib.Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    errors = []
    try:
        import jsonschema  # optional
        jsonschema.Draft202012Validator(schema).validate(data)
        print("Schema validation: OK (jsonschema)")
    except ImportError:
        print("NOTICE: jsonschema not installed; checking core structure and references only")
        if not isinstance(data, dict):
            errors.append("Contract must be a JSON object")
        else:
            for key in schema['required']:
                if key not in data:
                    errors.append(f"Missing required key: {key}")
            if data.get('schema_version') != '1.0':
                errors.append("schema_version must be '1.0'")
            for key in ('modules', 'decisions', 'open_questions'):
                if not isinstance(data.get(key), list):
                    errors.append(f"{key} must be an array")
    except Exception as exc:
        errors.append(f"JSON Schema violation: {exc}")

    if not isinstance(data, dict):
        for msg in errors:
            print("ERROR:", msg)
        return 1

    modules = data.get('modules') or []
    interfaces = data.get('interfaces') or []
    entities = data.get('data_entities') or []
    decisions = data.get('decisions') or []
    if not all(isinstance(items, list) for items in (modules, interfaces, entities, decisions)):
        errors.append("Modules, interfaces, entities and decisions must be arrays")
        modules, interfaces, entities, decisions = [], [], [], []

    def ids(items, label):
        result = [item.get('id') for item in items if isinstance(item, dict)]
        if None in result or len(result) != len(items):
            errors.append(f"{label}: every entry needs an ID")
        if len(result) != len(set(result)):
            errors.append(f"{label}: duplicate IDs")
        return set(result)

    mid = ids(modules, 'modules')
    iid = ids(interfaces, 'interfaces')
    eid = ids(entities, 'data_entities')
    did = ids(decisions, 'decisions')
    ids(data.get('open_questions') or [], 'open_questions')

    def check_refs(label, refs, allowed):
        for ref in refs or []:
            if ref not in allowed:
                errors.append(f"{label}: unknown internal reference {ref!r}")

    for m in modules:
        if not isinstance(m, dict):
            continue
        check_refs(m.get('id', 'module') + '.depends_on', m.get('depends_on'), mid)
        check_refs(m.get('id', 'module') + '.decision_refs', m.get('decision_refs'), did)
        if m.get('id') in (m.get('depends_on') or []):
            errors.append(f"Module {m['id']} cannot depend on itself")
    for itf in interfaces:
        if not isinstance(itf, dict):
            continue
        check_refs(itf.get('id', 'interface') + '.provider_module', [itf.get('provider_module')], mid)
        check_refs(itf.get('id', 'interface') + '.consumer_modules', itf.get('consumer_modules'), mid)
    for ent in entities:
        if isinstance(ent, dict):
            check_refs(ent.get('id', 'entity') + '.owner_module', [ent.get('owner_module')], mid)
    for tr in data.get('traceability') or []:
        if isinstance(tr, dict):
            label = str(tr.get('feature_ref', 'traceability'))
            check_refs(label + '.module_refs', tr.get('module_refs'), mid)
            check_refs(label + '.interface_refs', tr.get('interface_refs'), iid)
            check_refs(label + '.data_entity_refs', tr.get('data_entity_refs'), eid)
    impact = data.get('change_impact') or {}
    if isinstance(impact, dict):
        check_refs('change_impact.affected_module_refs', impact.get('affected_module_refs'), mid)

    approval = data.get('approval') or {}
    handoff = data.get('handoff') or {}
    questions = data.get('open_questions') or []
    ready = handoff.get('planning_ready') is True if isinstance(handoff, dict) else False
    if ready:
        if not isinstance(approval, dict) or approval.get('status') != 'approved':
            errors.append("planning_ready=true requires approval.status='approved'")
        if not approval.get('evidence_ref'):
            errors.append("planning_ready=true requires approval.evidence_ref")
        if handoff.get('blockers'):
            errors.append("planning_ready=true requires zero handoff.blockers")
        if any(isinstance(q, dict) and q.get('blocking') is True for q in questions):
            errors.append("planning_ready=true with blocking open_questions")
        if any(isinstance(d, dict) and d.get('status') == 'proposed' for d in decisions):
            errors.append("planning_ready=true with proposed decisions")

    if errors:
        for msg in errors:
            print("ERROR:", msg)
        return 1
    print("Contract checks: OK")
    print("Reminder: verify external references, file paths and user approvals manually.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
