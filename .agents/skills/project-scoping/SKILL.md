---
name: project-scoping
description: "Cadrer le MVP ou une évolution fonctionnelle indépendamment des releases SemVer, valider le catalogue et les documents, puis demander séparément les autorisations Git."
disable-model-invocation: true
---

# Aura Forge — Functional scoping and MVP

This is a **user-invoked orchestration skill**, not an autonomous coding agent. Scope the global MVP or an approved functional evolution independently of software releases. Communicate in **French**. Follow `AGENTS.md` and already approved decisions. Read [references/versioning.md](references/versioning.md) and [references/functional-documents.md](references/functional-documents.md) before preview/apply/audit. On legacy input read [references/migration.md](references/migration.md). A new release does not require a new scoping interview.

## Mandatory language contract

Write all **new user-facing functional documentation** in **French**: `PROJECT.md`, `MVP.md` (when relevant), `FUTURE-FEATURES.md`, `versions/<version>/VERSION.md`, module indexes and feature cards. This includes section titles, descriptions and acceptance criteria. Keep stable feature IDs, machine-readable frontmatter keys/values, slugs and file names in English. The **approved scoping summary is kept verbatim in its original language**. Preserve existing `GLOSSARY.md` conventions (English canonical terms plus *FR*) and ADR conventions. All review/approval exchanges are in French.

## Scope and dependencies

Scope **functional needs for the MVP or requested change**. Cover user goals, business rules, functional changes, dependencies, exclusions and acceptance criteria when user-approved. Keep future features separate. **Do not** impose technical release partitioning, assign definitive versions before dependency analysis/human validation, design UX flows/wireframes, select technologies, create schemas/APIs, implementation tasks or publish GitHub issues. Capture cross-phase topics for later.

Use Matt Pocock's installed **model-invoked** `grilling` and `domain-modeling` for unresolved interview/domain questions; do not modify Matt's skills. Read local `structure-project` and its references for catalogue methodology, applying the mandatory compatibility adapter in `references/functional-documents.md` to its preview/apply/audit procedures.

**Codex compatibility (mandatory):** Do **not** assume an executable tool named `Skill` exists. Codex can expose instructions/paths without it. Read the relevant installed `SKILL.md` files with available file tools and follow them in-session. For `structure-project`, read its instructions/references, then execute **the adapted preview/apply/audit in `references/functional-documents.md`**, which supersedes its legacy version templates for this workflow. A dedicated invocation tool is optional. Do not claim tool invocation merely for reading instructions, or report a missing `Skill` tool as an error when files are readable. If a required file truly cannot be found/read, identify that dependency and limit work accordingly while preserving every approval gate.

## Determine the functional scope and existing baseline first

Accept an idea, a source path, an existing MVP or a functional change request. Read relevant existing docs and `AGENTS.md`. Identify a stable `scope_id` (`mvp` for a new global MVP, otherwise an existing ID or approved change slug), not an invented software version.

- **New MVP:** read the description or `docs/product/00-IDEA.md`. Define indispensable features and success criteria in `MVP.md`, without choosing release numbers.
- **Existing project:** read `PROJECT.md`, `MVP.md`, existing `versions/*/VERSION.md`, canonical module/feature cards, backlog, glossary/ADRs and the request. Reuse the **approved baseline**, identify what is approved, planned, developed, actually delivered, deferred or unresolved. **Never infer delivery from approval or Git history.**
- Honor an explicitly approved release target as planning context; otherwise leave it unset. A legacy `v1` names an approved functional baseline, with no automatic `0.1.0` or `1.0.0` mapping. Never renumber or relocate it silently.
- Record `initial_scope` or `scope_evolution`, known delivery evidence and unresolved status. Prior delivery is not a prerequisite for planning ahead. Resume answered questions and decisions rather than repeating interviews.

Maintain resumable state under `.scratch/project-scoping/<project-slug>/<scope-id>/state.md`; reuse existing version-named workspaces when present. Track source paths, stage, findings, decisions, unanswered questions, summary/catalogue/doc approval, modified files and separate Git permissions. Read state first on restart. Keep drafts distinct from approved docs, never treat silence as consent, and do not store secrets.

## Workflow: independent gates for each scope change

### 1. Intake and focused functional interview

1. State the **functional objective**, scope ID and approved starting baseline in French; distinguish any already-approved delivery context.
2. For a new MVP, define the global functional objective and success criteria. For an evolution, **focus on the delta**: capabilities, changed rules, carryovers, dependencies and exclusions. Do not reopen accepted decisions without an authorized revision. Release partitioning alone requires no new interview.
3. Follow the `grilling` skill instructions for focused discovery and the `domain-modeling` instructions for vocabulary/decision modeling, using the Codex-compatible procedure above. Update glossary and justified ADRs only when appropriate. Do not force a fixed questionnaire or re-ask already answered questions.
4. Keep cross-phase UX/architecture/implementation questions in a deferred list. Let the user stop an interview and declare coverage *partial* rather than pretending completeness.

### 2. Functional summary and approval gate

Update `.scratch/project-scoping/<project-slug>/<scope-id>/scoping-summary.md` covering:

- Scope ID, approved baseline, user goals, MVP success criteria and intended outcomes.
- Changes **relative to existing behavior**, and features entirely new to the product.
- Explicitly approved decisions, candidate proposals, rejected items and unresolved issues, with provenance.
- MVP/change inclusions, exclusions, deferred/future work and user-verified dependencies; release assignments remain optional.
- Delivery assumptions **marked as assumptions**; coverage assessment (*complete* or *partial*).

Keep this snapshot in its source language. Show it in French and request **explicit approval**. Approval of the summary does not approve proposed or unresolved requirements. Iterate on correction. Do not proceed without approval.

### 3. Catalogue, canonical structure and approval gate

Execute the adapted `structure-project` `mode=preview` (read-only) from `references/functional-documents.md`, with approved summary, scope ID/kind and existing DOCS_ROOT. Its legacy V1/MVP output rules do not apply. It must:

- Reuse **stable `FEAT-*` IDs** and one canonical card; allocate new IDs only for new concepts. Preserve attributable historical behavior/acceptance and approved source snapshots.
- Propose only requested functional changes; distinguish new/modified features and incremental slices. Approval, planning, development and actual delivery remain independent.
- Select indispensable MVP/change features **only with explicit approval**. Keep future/proposed/unresolved/rejected work separate; no automatic release allocation.
- Show proposed modifications to *existing approved content* as diffs; never silently rewrite it.

Present the proposed catalogue and file manifest in **French**; obtain explicit approval before generating final docs. If changed, revise the preview and seek approval again.

Execute the adapted `mode=apply` only after approval, then its adapted `mode=audit`. Preserve the original summary and historical baselines; update **living** project/MVP/module/feature/backlog sections in place without addenda. Check links, IDs, criteria, dependencies and truthful progress. Do not run the legacy validator as a gate that requires artificial version membership.

### 4. Document review and approval gate

Present files, exact FEAT set, functional delta, audit results and scoped Git diff, including existing cards used by historical baselines. Ask for **explicit document approval**; revise/re-audit corrections. On approval, update the current scope document's `status: draft` to `approved` and show the metadata diff; **never** change delivery/development state or rewrite unrelated approvals. No automatic transition into UX.

### 5. Git permissions: always separate

1. Show `git status`, the scoped diff, and unrelated preexisting changes. Stage **only** the approved functional docs and deliberately approved glossary/ADR updates. Do not use indiscriminate `git add -A`.
2. Suggest `docs(scoping): validate <scope-id> functional scope`.
3. Ask separately for **commit** permission. Commit only after approval, then report the hash. If declined, stop with the work tree intact.
4. Ask separately for **push** permission and destination remote/branch; push only if authorized. Commit permission never implies push permission.
5. Report functional cadrage as approved/complete **only if its gates passed**. This does not mean implementation, release or MVP milestone completion. UX may follow later when requested.

## Historical and delivery invariants

- `MVP.md` defines the global indispensable scope, independently of releases; an old `release_bucket: mvp` does not prove approval or delivery.
- `versions/v1/VERSION.md` and approved summaries remain at their existing paths. Revising historical approvals or moving files requires a separate, explicit reviewed decision; see `references/migration.md`.
- Do not mark a version `delivered`, or a feature as actually delivered, based on scoping approval. Require explicit evidence or user confirmation.
- A canonical card can evolve; earlier delivered rules and criteria remain attributable. A partial released slice never marks an incomplete whole feature delivered.
- Keep `FUTURE-FEATURES.md` as a **living backlog**; promote a deferred item into the MVP or an approved release only after explicit approval.
- Preserve an existing root `MVP.md` or `SCOPING-SUMMARY.md` during migration. Reorganize them only with documented user approval; do not create conflicting copies.
- Never publish issues, implement code, commit, push, merge, delete or overwrite unrelated user work without the appropriate permission.
