"""Regression checks for legacy/new handoffs, delivery truth and read-only re-entry.

Run: python -B .agents/skills/project-scoping/tests/test_contracts.py
Examples are illustrative, not project approval or real release assignments.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

SKILLS = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("delivery_checks", SKILLS / "project-scoping/scripts/validate_delivery.py")
SHARED = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SHARED)
ARCH = json.loads((SKILLS / "project-architecture/references/architecture-contract.example.json").read_text(encoding="utf-8"))
UX_TEXT = (SKILLS / "project-ux/references/document-formats.md").read_text(encoding="utf-8")
UX = json.loads(re.search(r"```json\n(.*?)\n```", UX_TEXT, re.S).group(1))


def run(script, *args):
    return subprocess.run([sys.executable, "-B", str(SKILLS / script), *map(str, args)], capture_output=True, text=True, encoding="utf-8")


class ContractChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.arch = copy.deepcopy(ARCH)
        self.ux = copy.deepcopy(UX)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def architecture(self, contract=None):
        path = self.write("ARCHITECTURE-CONTRACT.json", json.dumps(contract or self.arch, ensure_ascii=False))
        return run("project-architecture/scripts/validate_contract.py", path)

    def ux_docs(self, legacy=False, directory=None):
        if legacy:
            self.ux.pop("delivery", None)
            self.ux.update(schemaVersion=1, version="v1", scope="versions/v1/VERSION.md")
        directory = directory or ("versions/v1/ux" if legacy else "ux")
        scope = self.ux["scope"]
        self.write(scope, f"---\nversion: {self.ux['version']}\nstatus: approved\n---\n\n## Fonctionnalités incluses\n- FEAT-001\n")
        self.write("modules/projects/create.md", "---\nid: FEAT-001\n---\n# Créer un projet\n")
        self.write("FUTURE-FEATURES.md", "# Fonctions futures\nAucun engagement de livraison.\n")
        headings = ["Objectifs et parcours principaux", "Navigation et décisions de conception", "Maquettes validées", "Anticipation des évolutions futures (hors périmètre)"]
        self.write(f"{directory}/UX-SUMMARY.md", f"---\nversion: {self.ux['version']}\nstatus: {self.ux['status']}\nscope: {scope}\n---\n" + "\n".join(f"## {h}\n" for h in headings) + "\n[Maquettes](mockups/index.html)\n")
        self.write(f"{directory}/mockups/index.html", '<!doctype html><html lang="fr"><a href="#SCREEN-001">Créer</a><main id="SCREEN-001"><form><label>Projet<input></label><button>Créer</button></form></main></html>')
        return self.write(f"{directory}/UX-CONTRACT.json", json.dumps(self.ux, ensure_ascii=False))

    def check_ux(self, **options):
        path = self.ux_docs(**options)
        return run("project-ux/scripts/validate_ux_docs.py", self.root, "--contract", path)

    def assert_ok(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_error(self, result, message):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_new_global_ux_without_release(self):
        self.assert_ok(self.check_ux())

    def test_legacy_ux_stays_valid_and_unknown(self):
        path = self.ux_docs(legacy=True)
        result = run("project-ux/scripts/validate_ux_docs.py", self.root, "--version", "v1")
        self.assert_ok(result)
        self.assertIn("remains unknown", result.stdout)
        self.assert_ok(run("project-ux/scripts/validate_ux_docs.py", self.root, "--contract", path))

    def test_semver_directory_and_discovery(self):
        self.ux["version"] = "0.2.0"
        self.ux_docs(directory="versions/0.2.0/ux")
        self.assert_ok(run("project-ux/scripts/validate_ux_docs.py", self.root, "--version", "0.2.0"))
        self.assert_ok(run("project-ux/scripts/validate_ux_docs.py", self.root))

    def test_new_architecture_without_release(self):
        self.assert_ok(self.architecture())

    def test_legacy_architecture_stays_valid(self):
        self.arch.pop("delivery")
        self.arch["schema_version"] = "1.0"
        self.arch["version"]["id"] = "v1"
        result = self.architecture()
        self.assert_ok(result)
        self.assertIn("remains unknown", result.stdout)

    def test_new_formats_require_delivery(self):
        self.ux.pop("delivery")
        self.assert_error(self.check_ux(), "missing delivery")
        self.arch.pop("delivery")
        self.assert_error(self.architecture(), "missing delivery")

    def test_missing_ux_progress_cannot_pass(self):
        self.ux["delivery"]["items"].pop()
        self.assert_error(self.check_ux(), "missing delivery progress item for ACT-001")

    def test_scope_mismatch_rejected(self):
        self.ux["delivery"]["scope"]["path"] = "FUTURE-FEATURES.md"
        self.assert_error(self.check_ux(), "functional scope differs")

    def test_html_and_scratch_checks_preserved(self):
        self.ux["screens"][0]["mockup"] = ".scratch/index.html#SCREEN-001"
        self.assert_error(self.check_ux(), "links to scratch")

    def test_missing_coverage_and_no_ui_justification(self):
        self.ux["featureCoverage"] = []
        self.assert_error(self.check_ux(), "missing featureCoverage")
        self.ux["featureCoverage"] = [{"featureId": "FEAT-001", "coverage": "no_ui", "screenIds": [], "flowIds": []}]
        self.assert_error(self.check_ux(), "user-approved justification")

    def test_future_feature_cannot_enter_flows(self):
        self.ux["flows"][0]["featureIds"] = ["FEAT-999"]
        self.assert_error(self.check_ux(), "not in mvp's scope")

    def test_malformed_architecture_exits_cleanly(self):
        for key, val in [("modules", [None]), ("open_questions", {}), ("delivery", None), ("traceability", "invalid")]:
            with self.subTest(key=key):
                contract = copy.deepcopy(ARCH)
                contract[key] = val
                result = self.architecture(contract)
                self.assert_error(result, "ERROR")

    def test_existing_architecture_refs_and_gate_preserved(self):
        self.arch["modules"][0]["depends_on"] = ["MOD-missing"]
        self.assert_error(self.architecture(), "unknown internal reference")
        self.arch["modules"][0]["depends_on"] = []
        self.arch["handoff"].update(planning_ready=True, blockers=[])
        self.assert_error(self.architecture(), "requires approval.status")

    def test_planning_ready_needs_no_release_assignment(self):
        self.arch["open_questions"] = []
        self.arch["handoff"].update(planning_ready=True, blockers=[])
        self.arch["approval"].update(status="approved", evidence_ref="review:human-design-acceptance")
        self.arch["version"]["status"] = "approved"
        self.assert_ok(self.architecture())

    def delivery(self):
        return copy.deepcopy(UX["delivery"])

    def partial_delivery(self):
        data = self.delivery()
        data["releases"] = [{"version": "0.2.0", "baseline_version": "0.1.0", "status": "delivered", "approval_ref": "review:release-slice", "evidence_refs": ["release:0.2.0"], "changes": [{"id": "CHANGE-create-basic", "kind": "feature", "compatibility": "compatible", "item_refs": ["FEAT-001"], "summary": "Première tranche de création", "acceptance_criteria": ["La création simple est utilisable"], "depends_on": []}]}]
        data["items"][0].update(planned_versions=["0.2.0"], development_status="in_progress", delivery_status="partial", delivered_versions=["0.2.0"], evidence_refs=["acceptance:basic-slice"])
        return data

    def test_partial_slice_does_not_complete_feature_or_mvp(self):
        data = self.partial_delivery()
        self.assertEqual(SHARED.delivery_errors(data), [])
        data["items"][0]["delivery_status"] = "delivered"
        self.assertTrue(any("whole-item delivery" in e for e in SHARED.delivery_errors(data)))
        data["items"][0]["delivery_status"] = "partial"
        data["milestones"][0].update(status="achieved", evidence_refs=["review:MVP"])
        self.assertTrue(any("every indispensable feature" in e for e in SHARED.delivery_errors(data)))

    def test_mvp_achievement_is_independent_of_stable_version(self):
        data = self.partial_delivery()
        data["items"][0].update(development_status="complete", delivery_status="delivered")
        data["milestones"][0].update(status="achieved", evidence_refs=["review:MVP-criteria"])
        self.assertEqual(SHARED.delivery_errors(data), [])

    def test_approval_is_not_delivery(self):
        data = self.delivery()
        data["items"][0]["delivery_status"] = "delivered"
        self.assertTrue(SHARED.delivery_errors(data))

    def test_future_context_cannot_claim_development(self):
        data = self.delivery()
        item = copy.deepcopy(data["items"][0])
        item.update(ref="FEAT-999", scope="future", development_status="complete")
        data["items"].append(item)
        self.assertTrue(any("future context" in e for e in SHARED.delivery_errors(data)))

    def test_duplicate_ids_and_unapproved_assignments_rejected(self):
        data = self.delivery()
        data["items"].append(copy.deepcopy(data["items"][0]))
        self.assertTrue(any("duplicate FEAT-001" in e for e in SHARED.delivery_errors(data)))
        data = self.partial_delivery()
        data["releases"][0]["approval_ref"] = None
        self.assertTrue(any("human approval_ref" in e for e in SHARED.delivery_errors(data)))

    def test_invalid_semver_and_false_patch_rejected(self):
        data = self.partial_delivery()
        data["releases"][0]["version"] = "01.2.0"
        self.assertTrue(any("invalid format" in e for e in SHARED.delivery_errors(data)))
        data = self.partial_delivery()
        release = data["releases"][0]
        release.update(version="0.1.1")
        release["changes"][0]["compatibility"] = "breaking"
        self.assertTrue(any("MINOR increment" in e for e in SHARED.delivery_errors(data)))
        release.update(version="1.1.1", baseline_version="1.1.0")
        self.assertTrue(any("MAJOR increment" in e for e in SHARED.delivery_errors(data)))

    def test_stable_version_requires_criteria_and_human_acceptance(self):
        data = self.partial_delivery()
        data["releases"][0]["version"] = "1.0.0"
        self.assertTrue(any("stability criteria" in e for e in SHARED.delivery_errors(data)))

    def test_unknown_refs_and_cycles_rejected(self):
        data = self.partial_delivery()
        change = data["releases"][0]["changes"][0]
        change["depends_on"] = ["CHANGE-missing"]
        self.assertTrue(any("invalid prerequisite" in e for e in SHARED.delivery_errors(data)))
        second = copy.deepcopy(change)
        second.update(id="CHANGE-second", depends_on=[change["id"]])
        change["depends_on"] = [second["id"]]
        data["releases"][0]["changes"].append(second)
        self.assertTrue(any("Cyclic" in e for e in SHARED.delivery_errors(data)))

    def test_second_run_is_read_only_and_deterministic(self):
        self.ux_docs()
        self.write("architecture/ARCHITECTURE-CONTRACT.json", json.dumps(self.arch))
        def inventory():
            return {str(p.relative_to(self.root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob("*") if p.is_file()}
        before = inventory()
        first = run("project-ux/scripts/validate_ux_docs.py", self.root)
        second = run("project-ux/scripts/validate_ux_docs.py", self.root)
        self.assert_ok(first)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(before, inventory())
        path = self.root / "architecture/ARCHITECTURE-CONTRACT.json"
        for _ in range(2):
            self.assert_ok(run("project-architecture/scripts/validate_contract.py", path))
        self.assertEqual(before, inventory())

    def functional_docs(self):
        self.write("PROJECT.md", "# Projet\n[MVP](MVP.md)\n[Projets](modules/projects/MODULE.md)\n")
        self.write("MVP.md", "---\nscope_id: mvp\nstatus: approved\n---\n# Objectif MVP\n## Objectifs et critères de réussite\nCréer et retrouver un projet.\n## Fonctionnalités incluses\n- [FEAT-001 — Créer](modules/projects/create.md)\n## Source de cadrage\n[Synthèse](SCOPING-SUMMARY.md)\n")
        self.write("SCOPING-SUMMARY.md", "# Synthèse approuvée\nCréer un projet.\n")
        self.write("FUTURE-FEATURES.md", "# Fonctionnalités futures\nAucune planifiée.\n")
        self.write("modules/projects/MODULE.md", "# Projets\n[FEAT-001 — Créer](create.md)\n")
        self.write("modules/projects/create.md", "---\nid: FEAT-001\nmodule: projects\ndecision_status: approved\nsource: SCOPING-SUMMARY.md\n---\n## Objectif utilisateur\nCréer un projet.\n## Comportement attendu\nLa saisie valide crée un projet.\n## Critères d'acceptation validés\nLe projet apparaît dans la liste après création.\n## Questions ouvertes\nAucune.\n")

    def test_global_functional_audit_needs_no_versions_directory(self):
        self.functional_docs()
        script = "project-scoping/scripts/validate_scope.py"
        first = run(script, self.root)
        self.assert_ok(first)
        before = {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(first.stdout, run(script, self.root).stdout)
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        self.assertFalse((self.root / "versions").exists())

    def test_functional_audit_preserves_catalogue_controls(self):
        self.functional_docs()
        script = "project-scoping/scripts/validate_scope.py"
        card = self.root / "modules/projects/create.md"
        card.write_text(card.read_text(encoding="utf-8").replace("decision_status: approved", "decision_status: proposed"), encoding="utf-8")
        self.assert_error(run(script, self.root), "only approved features")
        self.write("modules/projects/duplicate.md", card.read_text(encoding="utf-8"))
        self.assert_error(run(script, self.root), "duplicate canonical FEAT")

    def test_shared_reference_links_exist(self):
        for skill in ["project-scoping", "project-ux", "project-architecture"]:
            for path in (SKILLS / skill).rglob("*.md"):
                # Skip illustrative code blocks, which describe generated project docs.
                text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
                for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                    if not target.startswith(("https://", "http://", "#")):
                        self.assertTrue((path.parent / target).is_file(), f"{path}: broken reference {target}")
if __name__ == "__main__":
    unittest.main(verbosity=2)
