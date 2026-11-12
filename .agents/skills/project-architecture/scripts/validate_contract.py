#!/usr/bin/env python3
"""Validate Aura Forge architecture contract structure, references and handoff gate.

Usage (repository root): python .agents/skills/project-architecture/scripts/validate_contract.py path/to/ARCHITECTURE-CONTRACT.json
Requires only Python stdlib; checks the bundled schema and shared delivery
invariants with no optional dependency or network access. This does not verify that external
FEAT/FLOW/SCREEN references or approval evidence actually exist in the repository.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "references" / "architecture-contract.schema.json"
sys.path.insert(0, str(ROOT.parent / "project-scoping/scripts"))
from validate_delivery import delivery_errors, schema_errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python .agents/skills/project-architecture/scripts/validate_contract.py PATH_TO_CONTRACT.json")
        return 2
    path = pathlib.Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    errors = schema_errors(data, schema, SCHEMA)
    if errors:
        for msg in errors:
            print("ERROR:", msg)
        return 1
    print("Bundled schema validation: OK (stdlib)")

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

    if "delivery" in data:
        features = {ref for m in modules for ref in m.get('feature_refs', [])}
        features.update(tr['feature_ref'] for tr in data.get('traceability', []))
        ux = {ref for m in modules for ref in m.get('ux_refs', [])}
        ux.update(ref for tr in data.get('traceability', []) for ref in tr.get('ux_refs', []))
        required = features | mid | iid | eid
        problems = delivery_errors(data['delivery'], required | ux)
        errors.extend(problems)
        if not problems:
            scoped = set(data['delivery']['scope']['feature_refs'])
            if scoped != features:
                errors.append("delivery.scope.feature_refs must match scoped module/traceability features")
            item_refs = {item['ref'] for item in data['delivery']['items']}
            for ref in sorted(required - item_refs):
                errors.append(f"Missing delivery progress item for {ref}")
    else:
        print("NOTICE: legacy 1.0 contract; implementation/release state remains unknown")

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
