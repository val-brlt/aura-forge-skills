---
name: project-scoping
description: "User-started Aura Forge workflow to functionally scope V1 (MVP) or any subsequent product version, obtain approvals, update version-aware project docs, then request separate Git commit and push permissions."
disable-model-invocation: true
---

# Aura Forge — Version Scoping

This is a **user-invoked orchestration skill**, not an autonomous coding agent. It can be relaunched for **V1, V2, V3, ...** of the same project. Communicate with the user in **French**. Follow the repository's `AGENTS.md` and already approved project decisions. A project is persistent; **each version gets its own scoping cycle**.

## Mandatory language contract

Write all **new user-facing functional documentation** in **French**: `PROJECT.md`, `MVP.md` (when relevant), `FUTURE-FEATURES.md`, `versions/<version>/VERSION.md`, module indexes and feature cards. This includes section titles, descriptions and acceptance criteria. Keep stable feature IDs, machine-readable frontmatter keys/values, slugs and file names in English. The **approved scoping summary is kept verbatim in its original language**. Preserve existing `GLOSSARY.md` conventions (English canonical terms plus *FR*) and ADR conventions. All review/approval exchanges are in French.

## Scope and dependencies

Scope **functional needs for the target version**, not the whole product every time. Cover user goals, business rules, functional changes, dependencies, exclusions and acceptance criteria when user-approved. **Do not** design UX flows/wireframes, select technologies, create schemas/APIs, implementation tasks or publish GitHub issues. Capture such topics for a later stage instead.

Use Matt Pocock's installed **model-invoked** `grilling` and `domain-modeling` as the interview and domain-modeling procedures. They underpin the user-invoked `grill-with-docs`. Do not automatically invoke `grill-with-docs` or `to-spec`; do not modify Matt's skills. Apply the local `structure-project` instructions for catalogue preview, apply, and audit.

**Codex compatibility (mandatory):** Do **not** assume an executable tool named `Skill` exists. Codex can expose skills as instructions and paths without providing such a tool. At the start of the workflow, inspect the available skill metadata/paths. Read the relevant `SKILL.md` for `grilling` and `domain-modeling` using the available file-reading/shell tools, then follow their instructions in the current session. When structuring docs, read `.agents/skills/structure-project/SKILL.md` (or its resolved installed path) and its indicated references, and execute its `preview`, `apply`, and `audit` procedures directly. If a dedicated skill-invocation tool is actually available, it may be used, but it is **not required**. Do not describe reading and following a skill as a tool-based invocation. Do not report a missing `Skill` tool as an error when the files are readable. If a required skill file truly cannot be found or read, report the specific missing dependency and limit the work accordingly. Continue to obey every approval gate.

## Determine the target version first

Accept a pasted idea, a path to an idea file, or instructions for an existing project version. Read only the relevant existing docs and `AGENTS.md`.

- **New project, V1:** read the provided description or `docs/product/00-IDEA.md` when it exists. V1 can be explicitly designated the **MVP**; it is still a version. No other release is assumed approved.
- **Existing project, V2+:** read `docs/docs-project/PROJECT.md`, the previous `versions/*/VERSION.md`, existing module/feature cards, `FUTURE-FEATURES.md`, the relevant glossary/ADRs, and any user-provided change requests. Use this **approved existing baseline**, not only the original idea. Identify what was delivered, deferred and not yet resolved. **Never infer actual delivery from an approved scope or Git history**; treat delivery as confirmed only when the user or a trusted project record says so.
- If the target version is specified, honor it. Otherwise, infer V1 only for an unquestionably new project. For a preexisting project, propose the next version from the recorded version list and request confirmation when ambiguous. Never overwrite or renumber old versions silently.
- Record whether this cycle is `initial_version` or `subsequent_version`, and whether the user has **confirmed** the preceding version was delivered. Do not require past delivery to be marked complete when the user is intentionally planning ahead; keep status truthful.

Maintain resumable state under `.scratch/project-scoping/<project-slug>/<version>/state.md` (one workspace **per version**). On restart, inspect it first and offer a summary/resumption of an incomplete cycle. Track source paths, stage, interview findings, explicit decisions, outstanding questions, summary/catalogue approval, modified files, and separately granted Git permissions. Never treat silence as consent. Keep drafts distinct from approved docs, and do not store secrets.

## Workflow: independent gates for each version

### 1. Intake and version-specific interview

1. State the **target version** and its starting baseline in French.
2. For V1, scope the first usable release/MVP from the idea. For V2+, **focus on the delta**: new capabilities, enhancements to delivered features, changed rules, carryovers from backlog, dependencies and explicit exclusions. Do not reopen accepted V1 decisions without a user-requested revision.
3. Follow the `grilling` skill instructions for focused discovery and the `domain-modeling` instructions for vocabulary/decision modeling, using the Codex-compatible procedure above. Update glossary and justified ADRs only when appropriate. Do not force a fixed questionnaire or re-ask already answered questions.
4. Keep cross-phase UX/architecture/implementation questions in a deferred list. Let the user stop an interview and declare coverage *partial* rather than pretending completeness.

### 2. Version summary and approval gate

Draft `.scratch/project-scoping/<project-slug>/<version>/scoping-summary.md` covering:

- Version ID, baseline/previous version, user goals and intended outcomes.
- Changes **relative to existing behavior** (for V2+), and features entirely new to the product.
- Explicitly approved decisions, candidate proposals, rejected items and unresolved issues, with provenance.
- Target-version inclusions, exclusions, deferred/backlog work and user-verified dependencies.
- Delivery assumptions **marked as assumptions**; coverage assessment (*complete* or *partial*).

Keep this snapshot in its source language. Show it in French and request **explicit approval**. Approval of the summary does not approve proposed or unresolved requirements. Iterate on correction. Do not proceed without approval.

### 3. Catalogue, version structure and approval gate

Apply `structure-project` in `mode=preview` (read-only), with the approved summary path, target version and existing `docs/docs-project/`. Follow its `SKILL.md` directly if no dedicated invocation tool is provided. It must:

- Reuse existing **stable `FEAT-*` IDs** for the same feature; allocate new IDs only for genuinely new features. An enhancement of a V1 feature in V2 can reuse the same canonical card, with version-scoped behavior/history; do not lose V1 acceptance criteria.
- Propose only changes for the current version and clearly distinguish newly created versus modified features.
- Select target-version features **only with explicit user approval**. Keep remaining work in a backlog, with proposed, unresolved and rejected items distinguished.
- Show proposed modifications to *existing approved content* as diffs; never silently rewrite it.

Present the proposed catalogue and file manifest in **French**; obtain explicit approval before generating final docs. If changed, revise the preview and seek approval again.

Apply `structure-project` in `mode=apply` only after approval, then follow its `mode=audit` procedure. Write the current version's snapshot and update **living** project/module/feature/backlog indexes; preserve prior version snapshots. Run consistency audit and surface warnings.

### 4. Document review and approval gate

Present the added/modified files, feature coverage, version-specific delta, audit results and the relevant Git diff. Show exactly what changed in canonical feature cards already used by older versions. Ask for **explicit approval of the documentation**. If edits are requested, revise and re-audit. On explicit approval, update the current `versions/<version>/VERSION.md` status from `draft` to `approved` (if not already approved), and display that status change in the Git diff before requesting commit authorization; **never** change it to `delivered` here. No automatic transition into UX.

### 5. Git permissions: always separate

1. Show `git status`, the scoped diff, and unrelated preexisting changes. Stage **only** the approved functional docs and deliberately approved glossary/ADR updates. Do not use indiscriminate `git add -A`.
2. Suggest `docs(scoping): validate <version> functional scope`.
3. Ask separately for **commit** permission. Commit only after approval, then report the hash. If declined, stop with the work tree intact.
4. Ask separately for **push** permission and destination remote/branch; push only if authorized. Commit permission never implies push permission.
5. Report the target version's cadrage as approved/complete **only if its own approval gates have passed**. This does **not** mean the version was implemented or delivered. The UX phase for that version may follow later when requested.

## Historical and delivery invariants

- V1's MVP scope is **the V1 snapshot**, not a global `release_bucket: mvp` assigned permanently to a feature.
- `versions/v1/VERSION.md` and its approved summary remain historical references when scoping V2. Reopening/revising a historical version requires a **separate, explicit correction approval** with a visible diff.
- Do not mark a version `delivered`, or a feature as actually delivered, based on scoping approval. Require explicit evidence or user confirmation.
- A single canonical feature card can evolve, but earlier version-specific rules and acceptance criteria stay attributable to their original version. Do not retroactively claim that later V2 behavior was part of V1.
- Keep `FUTURE-FEATURES.md` as a **living backlog**; promote a deferred item into a later version only after explicit approval.
- Preserve an existing root `MVP.md` or `SCOPING-SUMMARY.md` during migration. Reorganize them only with documented user approval; do not create conflicting copies.
- Never publish issues, implement code, commit, push, merge, delete or overwrite unrelated user work without the appropriate permission.
