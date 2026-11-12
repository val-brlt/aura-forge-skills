#!/usr/bin/env python3
"""Audit a functional scope; --legacy selects unchanged historical V1/V2 trees.

Usage: python .agents/skills/structure-project/scripts/validate_docs.py DOCS_ROOT
       [--scope MVP.md | --legacy]
Read-only, Python stdlib only. Keep project-scoping's shared validator packaged.
"""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docs_root", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--scope", help="Functional source relative to DOCS_ROOT (default: MVP.md)")
    mode.add_argument("--legacy", action="store_true", help="Audit an unchanged legacy version tree")
    args = parser.parse_args()
    scripts = Path(__file__).resolve().parent
    validator = (scripts / "validate_legacy_docs.py" if args.legacy else
                 scripts.parents[1] / "project-scoping/scripts/validate_scope.py")
    if not validator.is_file():
        print(f"ERROR: missing packaged validator: {validator}")
        return 2
    command = [sys.executable, "-B", str(validator), str(args.docs_root)]
    if not args.legacy:
        command.extend(["--scope", args.scope or "MVP.md"])
    return subprocess.call(command)


if __name__ == "__main__":
    sys.exit(main())
