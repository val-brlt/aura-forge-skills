---
name: structure-project
description: "Structure approved MVP or functional change summaries into a feature catalogue and canonical documentation. Use to preview, apply or audit functional scopes, including legacy version trees, independently of release planning."
---

# Structure a Functional Scope

Convert an **approved functional summary** into a reviewable catalogue and canonical project documents. This model-invoked skill can be used directly or by `project-scoping`. Communicate in **French** and follow `AGENTS.md`, approved decisions and glossary conventions.

Read [shared scope and delivery conventions](../project-scoping/references/versioning.md) before preview/apply/audit. Read [document formats](references/document-formats.md) before proposing or writing files. For an unchanged historical V1/V2 audit only, read [legacy formats](references/legacy-document-formats.md).

## Inputs and modes

Required: approved summary path, stable `scope_id`, `scope_kind` (`mvp`, `change` or `legacy`) and `DOCS_ROOT`. Discover and reuse the authoritative documentation tree; for a new project use `docs/docs-project/`. A new global MVP uses `scope_id: mvp`. Reuse an existing scope ID/path for an evolution. `target_version` is optional context for an already-approved release assignment.

- `mode=preview`: read-only catalogue, exact file manifest and proposed diffs.
- `mode=apply`: write the approved catalogue as draft documents after explicit catalogue approval.
- `mode=audit`: read-only structural and semantic checks of the selected functional scope.

If summary approval or functional scope identity is unclear, obtain the missing decision before apply. A software version is not a prerequisite. Work stays within functional documentation; issues, technical design, implementation and Git actions belong to other workflows.

## 1. Preview and approve the catalogue

Read the complete approved summary, current project/MVP/backlog, relevant cards, existing scope baselines, glossary and ADRs. Classify each requested change as a new concept or evolution of an existing feature.

Map requirements to canonical FEAT cards and functional module slugs using the shared conventions. Put items outside the selected scope in the canonical backlog with their actual status and original scope links.

Present module, FEAT ID, French name, new/evolution, scope, decision state, provenance, approved acceptance criteria, dependencies and independent progress fields. Include assumptions, contradictions, the exact manifest and diffs to existing approved prose. Every approved requirement must trace to the summary or an explicit user decision; unsupported criteria remain proposed.

**Done:** the user explicitly approves the catalogue, manifest and any corrections to approved requirements. Revise and obtain approval again when the proposal changes.

## 2. Apply the approved catalogue

Use the current [document formats](references/document-formats.md):

1. Preserve the approved summary verbatim in its original language, at its existing canonical path or `SCOPING-SUMMARY.md` under DOCS_ROOT for a new MVP.
2. Create/update the authoritative functional scope with `status: draft` pending document review. `MVP.md` holds the global indispensable scope and success criteria, independently of releases. For a change, reuse its existing scope path or include a new scope path in the approved manifest.
3. Update `PROJECT.md`, module indexes, canonical feature cards and the canonical backlog in place, following the shared preservation rules. Index approved features outside this change separately from future/proposed work.
4. Record existing release assignments using the shared conventions; a new functional scope needs no release directory.

**Done:** every file in the approved manifest reflects the accepted catalogue, drafts are distinct from approvals, and the diff contains only authorized functional changes. Approval of documentation changes never proves development or delivery.

## 3. Audit the selected scope

From the **project repository root**, run:

`python .agents/skills/structure-project/scripts/validate_docs.py <DOCS_ROOT> --scope <scope-path>`

`--scope` defaults to `MVP.md` and is relative to DOCS_ROOT. Use `py` on Windows if needed, or resolve the actual installed skill path. This entry point uses the shared functional validator packaged in `project-scoping/scripts/validate_scope.py`.

For an **unchanged legacy V1/V2 tree**, use `--legacy` instead of `--scope`. This checks historical version membership and headings without converting documents. A revised global MVP uses the current audit, including when legacy snapshots coexist in the tree.

Manually check French prose, approval authority, source faithfulness, criteria, dependencies, independent progress, partial delivery and preservation of delivered behavior. Compare the diff with the approved preview. Validate existing UX/architecture contracts **only when affected** by the functional edits; new scoping work can finish before those contracts exist. Any impacted downstream design remains pending its phase review.

**Done:** all structural errors are resolved, semantic checks are reported, and warnings, missing evidence and downstream impacts are explicit. Automated checks verify neither real approvals nor shipment.

## 4. Document review and handback

Present the manifest, exact FEAT set, functional delta, audit results, unresolved questions and scoped diff. Obtain explicit document approval before updating only the current scope's approval metadata to `approved`; show that metadata diff. Preserve unrelated approvals and progress fields.

When called by `project-scoping`, return this package for its final document-review gate instead of requesting the same approval twice. Direct use performs the review here. The skill ends with the documentation package; commit and push are outside its scope.
