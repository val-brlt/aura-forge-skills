"""Canonical documentation paths shared by functional and UX audits."""
from pathlib import Path


def resolve_backlog(root: Path) -> Path:
    """Reuse a single existing backlog; new projects default to BACKLOG.md."""
    candidates = [root / name for name in ("BACKLOG.md", "FUTURE-FEATURES.md")]
    existing = [path for path in candidates if path.is_file()]
    if len(existing) > 1:
        raise ValueError("Both BACKLOG.md and FUTURE-FEATURES.md exist; resolve the canonical backlog before auditing")
    return existing[0] if existing else candidates[0]
