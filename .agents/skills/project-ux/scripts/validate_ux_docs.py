#!/usr/bin/env python3
"""Check Aura Forge version-aware UX document IDs and traceability.

Standard-library only. This checks consistency, NOT actual UX quality,
French prose, user approval, or software delivery.

Usage:
  python .agents/skills/project-ux/scripts/validate_ux_docs.py docs/docs-project --version v1
  python .agents/skills/project-ux/scripts/validate_ux_docs.py docs/docs-project
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ID_FEAT = re.compile(r"FEAT-\d{3,}\b")
ID_FLOW = re.compile(r"FLOW-\d{3,}\b")
ID_SCREEN = re.compile(r"SCREEN-\d{3,}\b")
FLOW_HEADING = re.compile(r"^##\s+(FLOW-\d{3,})\s*[—:–-]\s*.+$", re.M)
HEADING_2 = re.compile(r"^##\s+(.+?)\s*$", re.M)


class Audit:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.scanned_versions: List[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def relative(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root))
        except ValueError:
            return str(path)

    def read(self, path: Path) -> Optional[str]:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"Missing/unreadable {self.relative(path)}: {exc}")
            return None

    def frontmatter(self, path: Path, content: str) -> Dict[str, object]:
        """Parse the deliberately small YAML subset used by these templates."""
        if not content.startswith("---\n"):
            self.error(f"{self.relative(path)}: YAML frontmatter missing")
            return {}
        match = re.search(r"\A---\n(.*?)\n---\s*(?:\n|\Z)", content, re.S)
        if not match:
            self.error(f"{self.relative(path)}: unterminated YAML frontmatter")
            return {}
        result: Dict[str, object] = {}
        current: Optional[str] = None
        for line in match.group(1).splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            key_match = re.fullmatch(r"([a-z][a-z0-9_]*):\s*(.*?)\s*", line)
            if key_match:
                current, raw_value = key_match.groups()
                if current in result:
                    self.error(f"{self.relative(path)}: duplicate frontmatter key {current}")
                result[current] = raw_value.strip('"\'') if raw_value else []
                continue
            item_match = re.fullmatch(r"\s+-\s+(\S.*?)\s*", line)
            if item_match and current is not None and isinstance(result.get(current), list):
                cast_list = result[current]
                assert isinstance(cast_list, list)
                cast_list.append(item_match.group(1).strip('"\''))
                continue
            self.error(f"{self.relative(path)}: unsupported YAML syntax {line!r}; use the documented scalar/dash-list format")
        return result

    def section(self, content: str, heading: str) -> Optional[str]:
        pattern = re.compile(r"^##\s+" + re.escape(heading) + r"\s*$", re.M)
        match = pattern.search(content)
        if not match:
            return None
        following = HEADING_2.search(content, match.end())
        return content[match.end():following.start() if following else len(content)]

    def markdown_table(self, path: Path, content: str, heading: str, columns: List[str]) -> List[Dict[str, str]]:
        section = self.section(content, heading)
        if section is None:
            self.error(f"{self.relative(path)}: missing section ## {heading}")
            return []
        rows = []
        for line in section.splitlines():
            stripped = line.strip()
            if not (stripped.startswith("|") and stripped.endswith("|")):
                continue
            cells = [cell.strip() for cell in stripped[1:-1].split("|")]
            if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            rows.append(cells)
        if not rows:
            self.error(f"{self.relative(path)}: missing table under ## {heading}")
            return []
        if rows[0] != columns:
            self.error(f"{self.relative(path)}: expected columns {columns}, got {rows[0]}")
            return []
        parsed = []
        for index, row in enumerate(rows[1:], 1):
            if len(row) != len(columns):
                self.error(f"{self.relative(path)}: malformed row {index} under ## {heading}")
                continue
            parsed.append(dict(zip(columns, row)))
        return parsed

    def resolve_link(self, source: Path, cell: str) -> Optional[Path]:
        match = re.search(r"\]\(([^)#]+)(?:#[^)]+)?\)", cell)
        if not match:
            self.error(f"{self.relative(source)}: missing Markdown link in screen card column: {cell}")
            return None
        target = (source.parent / match.group(1)).resolve()
        if not target.is_relative_to(self.root):
            self.error(f"{self.relative(source)}: screen link leaves the docs root: {cell}")
            return None
        return target

    def canonical_features(self) -> Dict[str, Path]:
        found: Dict[str, Path] = {}
        for path in (self.root / "modules").glob("*/*.md"):
            if path.name == "MODULE.md":
                continue
            content = self.read(path)
            if content is None:
                continue
            meta = self.frontmatter(path, content)
            feature = meta.get("id")
            if not isinstance(feature, str) or ID_FEAT.fullmatch(feature) is None:
                self.error(f"{self.relative(path)}: missing/invalid canonical feature id")
                continue
            if feature in found:
                self.error(f"Duplicate canonical {feature}: {self.relative(found[feature])} and {self.relative(path)}")
            else:
                found[feature] = path
        return found

    def canonical_screens(self) -> Dict[str, Tuple[Path, Dict[str, object], str]]:
        found: Dict[str, Tuple[Path, Dict[str, object], str]] = {}
        for path in (self.root / "ux" / "screens").glob("*.md"):
            content = self.read(path)
            if content is None:
                continue
            meta = self.frontmatter(path, content)
            screen = meta.get("id")
            if not isinstance(screen, str) or ID_SCREEN.fullmatch(screen) is None:
                self.error(f"{self.relative(path)}: missing/invalid SCREEN id")
                continue
            if screen in found:
                self.error(f"Duplicate {screen}: {self.relative(found[screen][0])} and {self.relative(path)}")
            else:
                found[screen] = (path, meta, content)
            for field, regex in (("features", ID_FEAT), ("flows", ID_FLOW)):
                values = meta.get(field)
                if not isinstance(values, list) or not values:
                    self.error(f"{self.relative(path)}: {field} must be a non-empty YAML dash list")
                    continue
                for value in values:
                    if not isinstance(value, str) or regex.fullmatch(value) is None:
                        self.error(f"{self.relative(path)}: invalid {field} value {value!r}")
                if len(values) != len(set(values)):
                    self.error(f"{self.relative(path)}: duplicate {field} entries")
            for heading in ("Objectif de l'écran", "Contenu et hiérarchie", "Interactions et navigation", "États et retours", "Accessibilité et adaptation", "Évolutions par version"):
                if self.section(content, heading) is None:
                    self.warn(f"{self.relative(path)}: missing recommended ## {heading}")
        return found

    def version_features(self, path: Path, content: str) -> Set[str]:
        result: Set[str] = set()
        for heading in ("Fonctionnalités incluses", "Évolutions des fonctionnalités existantes"):
            section = self.section(content, heading)
            if section is not None:
                result.update(ID_FEAT.findall(section))
        if not result:
            self.error(f"{self.relative(path)}: no version-scoped FEAT IDs in the documented scope sections")
        return result

    def flows(self, path: Path, content: str) -> Dict[str, Dict[str, object]]:
        headings = list(FLOW_HEADING.finditer(content))
        if not headings:
            self.error(f"{self.relative(path)}: no ## FLOW-### — ... sections")
        result: Dict[str, Dict[str, object]] = {}
        for index, heading in enumerate(headings):
            flow_id = heading.group(1)
            body = content[heading.end():headings[index+1].start() if index + 1 < len(headings) else len(content)]
            if flow_id in result:
                self.error(f"{self.relative(path)}: duplicate flow {flow_id} within the version")
            def field(name: str) -> str:
                match = re.search(r"^\*\*" + re.escape(name) + r"\s*:\*\*\s*(.+?)\s*$", body, re.M)
                if not match:
                    self.error(f"{self.relative(path)}: {flow_id} missing **{name} :**")
                return match.group(1).strip() if match else ""
            features = set(ID_FEAT.findall(field("Fonctionnalités")))
            screens = set(ID_SCREEN.findall(field("Écrans")))
            decision = field("Décision")
            if not features or not screens:
                self.error(f"{self.relative(path)}: {flow_id} needs at least one FEAT and SCREEN")
            if decision not in {"approved", "proposed", "unresolved"}:
                self.error(f"{self.relative(path)}: {flow_id} invalid decision {decision!r}")
            result[flow_id] = {"features": features, "screens": screens, "decision": decision}
        return result

    def check_version(self, version: str, features: Dict[str, Path], screens: Dict[str, Tuple[Path, Dict[str, object], str]]) -> None:
        directory = self.root / "versions" / version
        scope_path = directory / "VERSION.md"
        ux_dir = directory / "ux"
        summary_path = ux_dir / "UX-SUMMARY.md"
        flows_path = ux_dir / "USER-FLOWS.md"
        inventory_path = ux_dir / "SCREEN-INVENTORY.md"
        texts = [self.read(path) for path in (scope_path, summary_path, flows_path, inventory_path)]
        if any(value is None for value in texts):
            return
        scope_text, summary_text, flows_text, inventory_text = texts  # type: ignore[misc]
        self.scanned_versions.append(version)
        scope_meta = self.frontmatter(scope_path, scope_text)
        if scope_meta.get("version") != version:
            self.error(f"{self.relative(scope_path)}: version frontmatter differs from directory")
        if scope_meta.get("status") not in ("approved", "delivered"):
            self.error(f"{self.relative(scope_path)}: UX requires an approved functional version scope")
        version_features = self.version_features(scope_path, scope_text)
        for feature in version_features:
            if feature not in features:
                self.error(f"{version}: {feature} in VERSION.md has no canonical feature card")
        for path, content in ((summary_path, summary_text), (flows_path, flows_text), (inventory_path, inventory_text)):
            meta = self.frontmatter(path, content)
            if meta.get("version") != version:
                self.error(f"{self.relative(path)}: version frontmatter differs from directory")
        summary_meta = self.frontmatter(summary_path, summary_text)
        status = summary_meta.get("status")
        if status not in ("draft", "approved"):
            self.error(f"{self.relative(summary_path)}: status must be draft or approved")
        expected_scope = f"versions/{version}/VERSION.md"
        if summary_meta.get("scope") != expected_scope:
            self.error(f"{self.relative(summary_path)}: scope must be {expected_scope}")

        defined_flows = self.flows(flows_path, flows_text)
        screen_rows = self.markdown_table(inventory_path, inventory_text, "Écrans de la version", ["Écran", "Rôle", "Fiche"])
        coverage_rows = self.markdown_table(inventory_path, inventory_text, "Couverture des fonctionnalités", ["Fonctionnalité", "Écrans", "Parcours", "Couverture"])
        inventory_screens: Set[str] = set()
        for row in screen_rows:
            screen_id = row["Écran"]
            if ID_SCREEN.fullmatch(screen_id) is None:
                self.error(f"{self.relative(inventory_path)}: invalid screen inventory id {screen_id!r}")
                continue
            if screen_id in inventory_screens:
                self.error(f"{self.relative(inventory_path)}: duplicate inventory screen {screen_id}")
            inventory_screens.add(screen_id)
            target = self.resolve_link(inventory_path, row["Fiche"])
            if screen_id not in screens:
                self.error(f"{version}: {screen_id} missing canonical screen card")
            elif target is not None and target != screens[screen_id][0].resolve():
                self.error(f"{version}: {screen_id} card link does not match canonical card")
            if target is not None and not target.is_file():
                self.error(f"{version}: broken screen card link {self.relative(target)}")

        for flow_id, info in defined_flows.items():
            referenced = info["screens"]
            assert isinstance(referenced, set)
            for screen_id in referenced - inventory_screens:
                self.error(f"{version}: {flow_id} uses {screen_id} absent from Écrans de la version")
            if info["decision"] != "approved" and status == "approved":
                self.error(f"{version}: approved UX summary contains {flow_id} decision={info['decision']}")
            for feature_id in info["features"]:
                if feature_id not in features:
                    self.error(f"{version}: {flow_id} references unknown {feature_id}")
        seen: Set[str] = set()
        no_ui_section = self.section(inventory_text, "Justifications sans interface")
        no_ui_reasons = dict(re.findall(r"^\s*-\s*(FEAT-\d{3,})\s*:\s*(.+?)\s*$", no_ui_section or "", re.M))
        for row in coverage_rows:
            feature_id = row["Fonctionnalité"]
            if ID_FEAT.fullmatch(feature_id) is None:
                self.error(f"{version}: invalid feature ID {feature_id!r} in coverage")
                continue
            if feature_id in seen:
                self.error(f"{version}: duplicate coverage row for {feature_id}")
            seen.add(feature_id)
            if feature_id not in version_features:
                self.error(f"{version}: coverage includes {feature_id}, not in approved version scope")
            status_coverage = row["Couverture"]
            referenced_screens = set(ID_SCREEN.findall(row["Écrans"]))
            referenced_flows = set(ID_FLOW.findall(row["Parcours"]))
            if status_coverage == "covered":
                if not referenced_screens or not referenced_flows:
                    self.error(f"{version}: {feature_id} covered but missing SCREEN/FLOW IDs")
                for screen_id in referenced_screens:
                    if screen_id not in inventory_screens:
                        self.error(f"{version}: {feature_id} references {screen_id} absent from inventory")
                    if screen_id in screens:
                        meta = screens[screen_id][1]
                        if feature_id not in (meta.get("features") or []):
                            self.error(f"{version}: {screen_id} card does not link back to {feature_id}")
                for flow_id in referenced_flows:
                    if flow_id not in defined_flows:
                        self.error(f"{version}: {feature_id} references undefined {flow_id}")
                        continue
                    flow = defined_flows[flow_id]
                    if feature_id not in flow["features"]:
                        self.error(f"{version}: {flow_id} does not link back to {feature_id}")
                    if not referenced_screens.intersection(flow["screens"]):
                        self.error(f"{version}: {feature_id} has no screen shared with {flow_id}")
                    for screen_id in referenced_screens.intersection(flow["screens"]):
                        if screen_id in screens and flow_id not in (screens[screen_id][1].get("flows") or []):
                            self.error(f"{version}: {screen_id} card does not link back to {flow_id}")
                    if flow["decision"] != "approved" and status == "approved":
                        self.error(f"{version}: {feature_id} linked to unapproved flow {flow_id}")
            elif status_coverage == "no_ui":
                if referenced_screens or referenced_flows or row["Écrans"] != "-" or row["Parcours"] != "-":
                    self.error(f"{version}: {feature_id} no_ui must use '-' for screens and flows")
                reason = no_ui_reasons.get(feature_id, "")
                if len(reason.strip()) < 12 or "<" in reason or "TODO" in reason.upper():
                    self.error(f"{version}: {feature_id} no_ui requires a meaningful user-approved justification")
            elif status_coverage == "unresolved":
                if status == "approved":
                    self.error(f"{version}: {feature_id} unresolved but UX summary is approved")
                self.warn(f"{version}: {feature_id} UX coverage unresolved; not ready for planning")
            else:
                self.error(f"{version}: {feature_id} invalid coverage {status_coverage!r}")
        for missing in sorted(version_features - seen):
            self.error(f"{version}: missing coverage row for scoped feature {missing}")
        for flow_id, info in defined_flows.items():
            for screen_id in info["screens"]:
                if screen_id in screens and flow_id not in (screens[screen_id][1].get("flows") or []):
                    self.error(f"{version}: {screen_id} card does not link to flow {flow_id}")
        self.warn(f"{version}: semantic UX review and explicit human approvals must still be verified manually")

    def run(self, version: Optional[str]) -> int:
        if not self.root.is_dir():
            print(f"ERROR: project docs root does not exist: {self.root}", file=sys.stderr)
            return 2
        features = self.canonical_features()
        screens = self.canonical_screens()
        if version:
            if not re.fullmatch(r"v\d+", version):
                print("ERROR: --version must look like v1, v2, etc.", file=sys.stderr)
                return 2
            versions = [version]
        else:
            versions = sorted(path.parent.name for path in (self.root / "versions").glob("*/ux/UX-SUMMARY.md"))
            if not versions:
                self.error("No versions/*/ux/UX-SUMMARY.md found")
        for target in versions:
            self.check_version(target, features, screens)
        for message in self.errors:
            print(f"ERROR: {message}")
        for message in self.warnings:
            print(f"WARN: {message}")
        print(f"AUDIT: {len(self.scanned_versions)} version(s), {len(features)} canonical feature(s), "
              f"{len(screens)} canonical screen(s), {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docs_root", type=Path, help="Path to docs/docs-project")
    parser.add_argument("--version", help="One version to check, e.g. v1")
    args = parser.parse_args()
    return Audit(args.docs_root).run(args.version)


if __name__ == "__main__":
    sys.exit(main())
