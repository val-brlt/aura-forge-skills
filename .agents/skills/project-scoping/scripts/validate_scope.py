#!/usr/bin/env python3
"""Audit global functional scope without requiring release folders (stdlib only).

Usage: python validate_scope.py DOCS_ROOT [--scope MVP.md]
Read-only structural checks; humans verify requirements, approvals and evidence.
Use structure-project/scripts/validate_docs.py --legacy only for unchanged legacy version trees.
"""
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

FEAT = re.compile(r"FEAT-\d{3,}\Z")
FIND_FEAT = re.compile(r"\bFEAT-\d{3,}\b")
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
DECISIONS = {"approved", "proposed", "rejected", "unresolved"}


def metadata(text):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    result = {}
    if match:
        for line in match[1].splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                if key in result:
                    raise ValueError(f"duplicate metadata key {key}")
                result[key] = val.strip().strip("\"'")
    return result


def section(text, title):
    match = re.search(r"^## " + re.escape(title) + r"\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match[1] if match else ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docs_root", type=Path)
    parser.add_argument("--scope", default="MVP.md", help="Canonical functional source relative to DOCS_ROOT")
    args = parser.parse_args()
    root = args.docs_root.resolve()
    errors, documents = [], {}
    if not root.is_dir():
        print("ERROR: documentation root not found")
        return 2
    scope_path = (root / args.scope).resolve()
    if not scope_path.is_relative_to(root):
        print("ERROR: scope leaves DOCS_ROOT")
        return 2
    for path in sorted(root.rglob("*.md")):
        try:
            documents[path.resolve()] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: {exc}")
    for required in [root / "PROJECT.md", root / "FUTURE-FEATURES.md", scope_path]:
        if required not in documents:
            errors.append(f"Missing document: {required.relative_to(root)}")
    def local_links(path, text):
        targets = set()
        for url in LINK.findall(text):
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_file():
                errors.append(f"{path.relative_to(root)}: missing local link {url}")
            targets.add(target)
        return targets
    links = {path: local_links(path, text) for path, text in documents.items()}
    features = {}
    for path in sorted((root / "modules").glob("**/*.md")):
        if path.name == "MODULE.md" or path not in documents:
            continue
        try:
            meta = metadata(documents[path])
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue
        fid = meta.get("id", "")
        if not FEAT.fullmatch(fid) or fid in features:
            errors.append(f"Invalid/duplicate canonical FEAT ID {fid!r}")
            continue
        features[fid] = (path, meta)
        if meta.get("module") != path.parent.name or meta.get("decision_status") not in DECISIONS:
            errors.append(f"{fid}: invalid module or decision_status")
        source = (root / meta.get("source", "")).resolve()
        if not source.is_relative_to(root) or not source.is_file():
            errors.append(f"{fid}: missing canonical source")
        index = path.parent / "MODULE.md"
        if path not in links.get(index, set()):
            errors.append(f"{fid}: missing module index link")
        if index not in links.get(root / "PROJECT.md", set()):
            errors.append(f"{fid}: missing project module link")
        for heading in ("Objectif utilisateur", "Comportement attendu", "Questions ouvertes"):
            if not re.search(r"^## " + re.escape(heading) + r"\s*$", documents[path], re.M):
                errors.append(f"{fid}: missing ## {heading}")
    scope_text = documents.get(scope_path, "")
    try:
        scope_meta = metadata(scope_text)
    except ValueError as exc:
        errors.append(str(exc))
        scope_meta = {}
    if scope_meta.get("status") not in {"draft", "approved", "delivered"}:
        errors.append("Scope requires explicit documentation approval status")
    included_text = section(scope_text, "Fonctionnalités incluses") + section(scope_text, "Évolutions des fonctionnalités existantes")
    included = set(FIND_FEAT.findall(included_text))
    if not included:
        errors.append("Functional scope contains no FEAT IDs")
    if args.scope == "MVP.md":
        if not section(scope_text, "Objectifs et critères de réussite").strip():
            errors.append("MVP requires explicit success criteria")
    if not local_links(scope_path, section(scope_text, "Source de cadrage")):
        errors.append("Scope requires a link to its approved summary")
    if scope_path not in links.get(root / "PROJECT.md", set()):
        errors.append("PROJECT.md must link the functional scope")
    for fid in sorted(included):
        if fid not in features:
            errors.append(f"{fid}: no canonical card")
            continue
        path, meta = features[fid]
        if path not in local_links(scope_path, included_text):
            errors.append(f"{fid}: scope must link its canonical card")
        if meta.get("decision_status") != "approved":
            errors.append(f"{fid}: only approved features belong in scope")
        if not section(documents[path], "Critères d'acceptation validés").strip():
            errors.append(f"{fid}: missing approved acceptance criteria")
    backlog_links = links.get(root / "FUTURE-FEATURES.md", set())
    for fid, (path, _) in features.items():
        if fid not in included and path not in backlog_links:
            errors.append(f"{fid}: outside scope and absent from future/proposal/rejected catalogue")
    for error in errors:
        print("ERROR:", error)
    print(f"Functional scope: {len(included)} feature(s), {len(errors)} error(s); verify approvals, history and evidence manually")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
