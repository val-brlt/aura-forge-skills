#!/usr/bin/env python3
"""Validate version-aware Aura Forge functional documents (Python stdlib only).

This is a structural check, not evidence of user approval, French prose quality,
or real software delivery. Does not modify files.
"""

from collections import defaultdict
from pathlib import Path
import re
import sys

VALID_DECISIONS = {"approved", "proposed", "rejected", "unresolved"}
VALID_VERSION_STATUSES = {"draft", "approved", "delivered"}
VALID_RELEASE_KINDS = {"mvp", "standard"}
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FEATURE_ID = re.compile(r"FEAT-\d{3,}")
VERSION_ID = re.compile(r"v\d+(?:\.\d+)*")


def links(path: Path, text: str | None = None) -> set[Path]:
    if text is None:
        if not path.is_file():
            return set()
        text = path.read_text(encoding="utf-8")
    targets = set()
    for target in LINK.findall(text):
        if target.startswith(("http:", "https:", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if target:
            targets.add((path.parent / target).resolve())
    return targets


def section(text: str, title: str) -> str:
    """Extract Markdown content under an exact h2 heading, excluding subsequent h2s."""
    marker = f"## {title}\n"
    start = text.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    next_heading = re.search(r"(?m)^## ", text[start:])
    return text[start : start + next_heading.start()] if next_heading else text[start:]


def frontmatter(path: Path) -> tuple[dict[str, str] | None, str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "missing plain YAML frontmatter"
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None, "unterminated YAML frontmatter"
    fields: dict[str, str] = {}
    for line in parts[0].splitlines()[1:]:
        if not line.strip():
            continue
        if ":" not in line:
            return None, f"invalid frontmatter: {line}"
        key, value = (s.strip() for s in line.split(":", 1))
        value = value.strip("\"'")
        if not key or not value or key in fields:
            return None, f"empty/duplicate field: {key}"
        fields[key] = value
    return fields, None


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/docs-project").resolve()
    errors: list[str] = []
    warnings: list[str] = []
    if not root.is_dir():
        print(f"ERROR: missing document directory: {root}")
        return 2

    for name in ("PROJECT.md", "FUTURE-FEATURES.md"):
        if not (root / name).is_file():
            errors.append(f"missing document: {name}")

    features: dict[str, tuple[Path, dict[str, str]]] = {}
    module_indices: set[Path] = set()
    modules = root / "modules"
    if not modules.is_dir():
        errors.append("missing modules/ directory")
    else:
        for module_dir in sorted(p for p in modules.iterdir() if p.is_dir()):
            index = module_dir / "MODULE.md"
            module_indices.add(index.resolve())
            if not index.is_file():
                errors.append(f"missing module index: {module_dir.name}/MODULE.md")
            for path in sorted(module_dir.glob("*.md")):
                if path.name == "MODULE.md":
                    continue
                rel = path.relative_to(root)
                meta, err = frontmatter(path)
                if err:
                    errors.append(f"{rel}: {err}")
                    continue
                assert meta is not None
                for field in ("id", "module", "decision_status", "source"):
                    if field not in meta:
                        errors.append(f"{rel}: missing field '{field}'")
                fid = meta.get("id", "")
                if not FEATURE_ID.fullmatch(fid):
                    errors.append(f"{rel}: malformed feature ID '{fid}'")
                elif fid in features:
                    errors.append(f"duplicate feature ID {fid}: {features[fid][0]} and {path}")
                else:
                    features[fid] = (path.resolve(), meta)
                if meta.get("module") != module_dir.name:
                    errors.append(f"{rel}: module field does not match parent folder")
                if meta.get("decision_status") not in VALID_DECISIONS:
                    errors.append(f"{rel}: invalid decision_status '{meta.get('decision_status')}'")
                source = meta.get("source", "")
                if source and not (root / source).is_file():
                    errors.append(f"{rel}: source does not exist: {source}")
                if "release_bucket" in meta:
                    warnings.append(f"{rel}: legacy release_bucket; migrate version membership into versions/*/VERSION.md after approval")
                body = path.read_text(encoding="utf-8")
                for heading in ("## Objectif utilisateur", "## Comportement attendu", "## Historique fonctionnel par version", "## Questions ouvertes"):
                    if heading not in body:
                        warnings.append(f"{rel}: missing French heading '{heading}'")
                if index.is_file() and path.resolve() not in links(index):
                    errors.append(f"{module_dir.name}/MODULE.md: missing link to {path.name}")

    versions = root / "versions"
    all_version_links: dict[str, set[Path]] = {}
    assignments: dict[Path, set[str]] = defaultdict(set)
    if not versions.is_dir():
        errors.append("missing versions/ directory (legacy V1 migration may be needed)")
    else:
        for version_dir in sorted(p for p in versions.iterdir() if p.is_dir()):
            vid = version_dir.name
            path = version_dir / "VERSION.md"
            if not VERSION_ID.fullmatch(vid):
                errors.append(f"invalid version directory: {vid}")
            if not path.is_file():
                errors.append(f"missing version scope: versions/{vid}/VERSION.md")
                continue
            meta, err = frontmatter(path)
            if err:
                errors.append(f"versions/{vid}/VERSION.md: {err}")
                continue
            assert meta is not None
            if meta.get("version") != vid:
                errors.append(f"versions/{vid}/VERSION.md: version metadata must be '{vid}'")
            if meta.get("status") not in VALID_VERSION_STATUSES:
                errors.append(f"versions/{vid}/VERSION.md: invalid status '{meta.get('status')}'")
            if meta.get("release_kind") not in VALID_RELEASE_KINDS:
                errors.append(f"versions/{vid}/VERSION.md: invalid release_kind '{meta.get('release_kind')}'")
            body = path.read_text(encoding="utf-8")
            for heading in ("## Objectif de la version", "## Référence précédente", "## Fonctionnalités incluses", "## Source de cadrage"):
                if heading not in body:
                    warnings.append(f"versions/{vid}/VERSION.md: missing French heading '{heading}'")
            scope = section(body, "Fonctionnalités incluses")
            if not scope:
                warnings.append(f"versions/{vid}/VERSION.md: empty feature scope")
            included = links(path, scope)
            all_version_links[vid] = included
            for feature_path in included:
                assignments[feature_path].add(vid)
            source_section = section(body, "Source de cadrage")
            if not links(path, source_section):
                errors.append(f"versions/{vid}/VERSION.md: missing link to approved summary")

    feature_paths = {p for p, _ in features.values()}
    for vid, included in all_version_links.items():
        for path in sorted(included - feature_paths):
            errors.append(f"versions/{vid}/VERSION.md: link in included features is not a canonical feature: {path}")
        for fid, (path, meta) in features.items():
            if path not in included:
                continue
            if meta.get("decision_status") != "approved":
                errors.append(f"versions/{vid}/VERSION.md: {fid} is not approved")
            body = path.read_text(encoding="utf-8")
            heading = f"### {vid.upper()}"
            if not re.search(rf"(?m)^### {re.escape(vid)}\s*$", body, re.IGNORECASE):
                errors.append(f"{path.relative_to(root)}: {fid} included in {vid} but missing version history heading '{heading}'")

    backlog_file = root / "FUTURE-FEATURES.md"
    backlog_links = links(backlog_file)
    for fid, (path, meta) in features.items():
        if path not in assignments and path not in backlog_links:
            errors.append(f"{path.relative_to(root)}: {fid} neither in a version scope nor in backlog")
        if meta.get("decision_status") == "rejected" and path in assignments:
            errors.append(f"{path.relative_to(root)}: rejected feature must not appear in a version scope")
        if len(assignments[path]) > 1:
            # A feature may legitimately evolve across releases, but every later
            # release must explicitly identify the change in its version index.
            ordered = sorted(assignments[path], key=lambda v: [int(n) for n in v[1:].split(".")])
            for later in ordered[1:]:
                scope_file = versions / later / "VERSION.md"
                evolution_section = section(scope_file.read_text(encoding="utf-8"), "Évolutions des fonctionnalités existantes")
                if path not in links(scope_file, evolution_section):
                    errors.append(f"versions/{later}/VERSION.md: {fid} also appears in an earlier version; link it under 'Évolutions des fonctionnalités existantes' and explain the version-specific delta")
    project_links = links(root / "PROJECT.md")
    for index in sorted(module_indices):
        if index not in project_links:
            errors.append(f"PROJECT.md: missing module link: {index.parent.name}/MODULE.md")
    for vid in all_version_links:
        scope_path = (versions / vid / "VERSION.md").resolve()
        if scope_path not in project_links:
            errors.append(f"PROJECT.md: missing link to version {vid}")

    # Verify every local Markdown link across all project docs.
    for path in sorted(root.rglob("*.md")):
        for destination in sorted(links(path)):
            if not destination.is_file():
                errors.append(f"{path.relative_to(root)}: broken local Markdown link to {destination}")

    print(f"Versions: {len(all_version_links)} | modules: {len(module_indices)} | feature cards: {len(features)}")
    for message in warnings:
        print("WARNING:", message)
    for message in errors:
        print("ERROR:", message)
    print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
