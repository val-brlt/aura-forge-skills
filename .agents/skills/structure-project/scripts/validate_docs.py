#!/usr/bin/env python3
"""Validate structural integrity of Aura Forge functional scoping docs.

Only Python stdlib. Semantic correctness and user approvals still require review.
"""

from pathlib import Path
import re
import sys

ALLOWED_DECISIONS = {"approved", "proposed", "rejected", "unresolved"}
ALLOWED_BUCKETS = {"mvp", "future", "none"}
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FEATURE_ID = re.compile(r"AURA-\d{3,}$")


def markdown_links(path: Path) -> set[Path]:
    """Local Markdown link targets, resolved to absolute paths; omit external URLs."""
    if not path.exists():
        return set()
    result = set()
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        if target.startswith(("http:", "https:", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if target:
            result.add((path.parent / target).resolve())
    return result


def metadata(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "Missing plain YAML frontmatter"
    chunks = text.split("\n---\n", 1)
    if len(chunks) != 2:
        return None, "Unterminated YAML frontmatter"
    result = {}
    for line in chunks[0].splitlines()[1:]:
        if not line.strip():
            continue
        if ":" not in line:
            return None, f"Invalid frontmatter line: {line}"
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if not key or not value or key in result:
            return None, f"Empty or duplicate field: {key}"
        result[key] = value
    return result, None


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/docs-project").resolve()
    errors, warnings = [], []
    if not root.is_dir():
        print(f"ERROR: Documentation folder missing: {root}")
        return 2

    for name in ("SCOPING-SUMMARY.md", "PROJECT.md", "MVP.md", "FUTURE-FEATURES.md"):
        if not (root / name).is_file():
            errors.append(f"Missing file: {name}")

    modules_dir = root / "modules"
    if not modules_dir.is_dir():
        errors.append("Missing modules/ directory")
    features = {}
    per_module = {}
    if modules_dir.is_dir():
        for module_dir in sorted(p for p in modules_dir.iterdir() if p.is_dir()):
            module = module_dir.name
            module_index = module_dir / "MODULE.md"
            if not module_index.exists():
                errors.append(f"Missing module index: {module}/MODULE.md")
            features_in_module = set()
            for path in sorted(module_dir.glob("*.md")):
                if path.name == "MODULE.md":
                    continue
                features_in_module.add(path.resolve())
                data, err = metadata(path)
                if err:
                    errors.append(f"{path.relative_to(root)}: {err}")
                    continue
                for req in ("id", "module", "decision_status", "release_bucket", "source"):
                    if req not in data:
                        errors.append(f"{path.relative_to(root)}: missing {req}")
                fid = data.get("id", "")
                if not FEATURE_ID.fullmatch(fid):
                    errors.append(f"{path.relative_to(root)}: invalid feature ID '{fid}'")
                if fid in features:
                    errors.append(f"Duplicate ID {fid}: {features[fid][0]} and {path}")
                else:
                    features[fid] = (path.resolve(), data)
                if data.get("module") != module:
                    errors.append(f"{path.relative_to(root)}: module must be '{module}'")
                status = data.get("decision_status")
                bucket = data.get("release_bucket")
                if status not in ALLOWED_DECISIONS:
                    errors.append(f"{path.relative_to(root)}: unknown decision_status '{status}'")
                if bucket not in ALLOWED_BUCKETS:
                    errors.append(f"{path.relative_to(root)}: unknown release_bucket '{bucket}'")
                if bucket == "mvp" and status != "approved":
                    errors.append(f"{path.relative_to(root)}: MVP feature must be approved")
                if status == "rejected" and bucket != "none":
                    errors.append(f"{path.relative_to(root)}: rejected feature must have release_bucket none")
                source = data.get("source", "")
                if source and not (root / source).is_file():
                    errors.append(f"{path.relative_to(root)}: missing source '{source}'")
                for h in ("## User outcome", "## Expected behavior", "## Approved acceptance criteria", "## Functional dependencies", "## Open questions"):
                    if h not in path.read_text(encoding="utf-8"):
                        warnings.append(f"{path.relative_to(root)}: expected heading '{h}' not found")
            per_module[module_index.resolve()] = features_in_module

    mvp_expected = {path for path, d in features.values() if d.get("release_bucket") == "mvp"}
    other_expected = {path for path, d in features.values() if d.get("release_bucket") != "mvp"}
    mvp_links = markdown_links(root / "MVP.md")
    other_links = markdown_links(root / "FUTURE-FEATURES.md")
    all_feature_paths = {path for path, _ in features.values()}
    for file_name, expected, actual in (("MVP.md", mvp_expected, mvp_links), ("FUTURE-FEATURES.md", other_expected, other_links)):
        for path in sorted(expected - actual):
            errors.append(f"{file_name}: missing link to {path.relative_to(root)}")
        for path in sorted((actual & all_feature_paths) - expected):
            errors.append(f"{file_name}: incorrect feature link {path.relative_to(root)}")

    for index, expected in per_module.items():
        if not index.is_file():
            continue
        linked = markdown_links(index)
        for path in sorted(expected - linked):
            errors.append(f"{index.relative_to(root)}: missing link to {path.name}")
        for path in sorted((linked & all_feature_paths) - expected):
            errors.append(f"{index.relative_to(root)}: links to other module feature {path.relative_to(root)}")

    project_links = markdown_links(root / "PROJECT.md")
    for index in per_module:
        if index not in project_links:
            errors.append(f"PROJECT.md: missing module link to {index.parent.name}/MODULE.md")

    # Check all local markdown links within the generated project document tree.
    for path in root.rglob("*.md"):
        for dest in sorted(markdown_links(path)):
            if not dest.is_file():
                errors.append(f"{path.relative_to(root)}: unresolved link to {dest}")

    print(f"Feature cards: {len(features)} | modules: {len(per_module)}")
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    print(f"Result: {len(errors)} errors; {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
