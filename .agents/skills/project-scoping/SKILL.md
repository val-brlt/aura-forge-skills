---
name: project-scoping
description: "Scope the MVP or a functional evolution independently of SemVer releases, validate the catalogue and documents, then request separate Git permissions."
disable-model-invocation: true
---

# Aura Forge — Functional scoping and MVP

This is a **user-invoked orchestration skill**, not an autonomous coding agent. Scope the global MVP or an approved functional evolution independently of software releases. Communicate in **French**. Follow `AGENTS.md` and already approved decisions. Read [shared conventions](references/versioning.md) before changing documents and [functional documentation](references/functional-documents.md) before preview/apply/audit.

## Mandatory language contract

Write all **new user-facing functional documentation** in **French**: `PROJECT.md`, `MVP.md` (when relevant), the canonical backlog, `versions/<version>/VERSION.md`, module indexes and feature cards. This includes section titles, descriptions and acceptance criteria. Keep stable feature IDs, machine-readable frontmatter keys/values, slugs and file names in English. The **approved scoping summary is kept verbatim in its original language**. Preserve existing `GLOSSARY.md` conventions (English canonical terms plus *FR*) and ADR conventions. All review/approval exchanges are in French.

## Scope and dependencies

Scope **functional needs for the MVP or requested change**. Cover user goals, business rules, functional changes, dependencies, exclusions and acceptance criteria when user-approved. Keep future features separate. **Do not** impose technical release partitioning, assign definitive versions before dependency analysis/human validation, design UX flows/wireframes, select technologies, create schemas/APIs, implementation tasks or publish GitHub issues. Capture cross-phase topics for later.

Use Matt Pocock's installed **model-invoked** `grilling` and `domain-modeling` for unresolved interview/domain questions. Use local [structure-project](../structure-project/SKILL.md) for the authoritative catalogue, document formats and preview/apply/audit procedures.

**Tool compatibility:** Read installed `SKILL.md` files and apply their instructions in-session when a dedicated invocation tool is unavailable. If a required file cannot be read, identify the missing dependency and limit the work accordingly while preserving approval gates.

## Determine the functional scope and existing baseline first

Accept an idea, a source path, an existing MVP or a functional change request. Read relevant existing docs and `AGENTS.md`. Identify a stable `scope_id` (`mvp` for a new global MVP, otherwise an existing ID or approved change slug), not an invented software version.

- **New MVP:** read the description or `docs/product/00-IDEA.md`. Define indispensable features and success criteria in `MVP.md`, without choosing release numbers.
- **Existing project:** read `PROJECT.md`, `MVP.md`, existing `versions/*/VERSION.md`, canonical module/feature cards, backlog, glossary/ADRs and the request. Reuse the **approved baseline** and identify evidenced progress using the shared conventions.
- Read already-approved release assignments as planning context using the shared conventions.
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

Follow [structure-project](../structure-project/SKILL.md) in `mode=preview` with the approved summary, `scope_id`, `scope_kind` and DOCS_ROOT. Its current procedure applies equally to direct use and this workflow.

**Done:** the user explicitly approves the catalogue and exact manifest, including diffs to approved content; `mode=apply` produces drafts and `mode=audit` resolves structural errors and reports semantic checks, warnings and downstream impacts. Return the audit package to step 4 for final document approval. Existing UX/architecture contracts are checked only when affected; their absence does not block an initial functional scope.

### 4. Document review and approval gate

Present files, exact FEAT set, functional delta, audit results and scoped Git diff, including existing cards used by historical baselines. Ask for **explicit document approval**; revise/re-audit corrections. On approval, update the current scope document's `status: draft` to `approved` and show the metadata diff; **never** change delivery/development state or rewrite unrelated approvals. No automatic transition into UX.

### 5. Git permissions: always separate

1. Show `git status`, the scoped diff, and unrelated preexisting changes. Stage **only** the approved functional docs and deliberately approved glossary/ADR updates. Do not use indiscriminate `git add -A`.
2. Suggest `docs(scoping): validate <scope-id> functional scope`.
3. Ask separately for **commit** permission. Commit only after approval, then report the hash. If declined, stop with the work tree intact.
4. Ask separately for **push** permission and destination remote/branch; push only if authorized. Commit permission never implies push permission.
5. Report functional scoping as approved/complete **only if its gates passed**. This does not mean implementation, release or MVP milestone completion. UX may follow later when requested.


Never publish issues, implement code, commit, push, merge, delete or overwrite unrelated user work without the appropriate permission.
