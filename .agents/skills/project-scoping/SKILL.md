---
name: project-scoping
description: "User-started Aura Forge functional scoping workflow: interview from an editable idea, review a summary, structure modules/features/MVP, obtain approvals, then prepare a Git commit and push."
disable-model-invocation: true
---

# Aura Forge — Project Scoping

This is a **user-invoked orchestration skill**, not an autonomous coding agent. Communicate with the user in French. Use the repository's `AGENTS.md` and approved documentation. Respect explicit user instructions over this workflow.

## User-facing documentation language (mandatory)

All **new functional documents intended for the French-speaking end user** must be written in **French**, regardless of the interview language or existing English templates: `PROJECT.md`, `MVP.md`, `FUTURE-FEATURES.md`, each `MODULE.md`, and every Feature card. This includes all headings, feature/module display names, descriptions, user journeys, behavior and acceptance criteria. English is allowed only for technical keys/identifiers (`AURA-001`, YAML field names/values, file names/slugs), external proper nouns, code, and necessary fixed domain terms. Do not translate the canonical English domain names in `GLOSSARY.md`; use the glossary's existing English-plus-*FR* format.

**Exception:** The approved scoping summary is an evidence snapshot and must retain its original language; do not automatically translate or paraphrase it when copying to `SCOPING-SUMMARY.md`. Keep ADRs and the glossary in their existing repository conventions. Present review tables, gate questions and approval summaries to the user in French. Before seeking approval, confirm the generated documents comply with these language requirements.

## Purpose and boundaries

Transform the user's software idea into an **approved functional catalogue**. Do not choose a stack, design databases/APIs/code organization, create implementation tickets/issues, or start production implementation. UX navigation and wireframes belong to the next phase. Record discovered out-of-scope questions for later; they are **not blockers** unless they affect an essential functional decision.

Use Matt Pocock's installed, **model-invoked** skills `grilling` and `domain-modeling` via the Skill tool (one invocation per skill). These are the same underlying mechanisms used by his user-invoked `grill-with-docs`. Do **not** attempt to invoke the user-invoked `grill-with-docs` or `to-spec` from this skill, and do not duplicate or modify Matt's skill files. If a required skill is unavailable, report it and ask the user to install it rather than pretending it ran.

When a validated scoping summary is ready, invoke the local **model-invoked** `structure-project` skill through the Skill tool. If its runtime is unavailable, explain the blocker; do not silently invent a substitute workflow.

## Input and resume

Accept either (a) pasted idea text or (b) a path to a Markdown description file. If no input was provided, look for `docs/product/00-IDEA.md`; if absent, request the idea. Never treat a document that does not exist as though it exists.

Create local working artifacts under `.scratch/project-scoping/<project-slug>/` only when needed; do not assume they are tracked by Git. On invocation, inspect that directory first. If it contains an unfinished session, **summarize its recorded state and ask whether to resume** rather than restarting automatically.

Maintain a concise `state.md` with the following data after each milestone:

- Project slug, description source and current workflow step.
- Source paths for the draft summary and catalog, where applicable.
- Explicitly approved decisions and their provenance (or references to the summary).
- Open questions, deferred UX/architecture topics, blockers and user approvals already received.
- Document changes proposed/applied, and whether Git commit/push approvals were obtained.

Do not record secrets in working artifacts. Keep draft records separate from approved decisions. Never convert a tentative statement into an approval.

## Workflow — stop at each gate

### 1. Intake and interview

1. Read the description, `AGENTS.md`, and the relevant existing glossary/ADRs. Do not read unrelated repository content unnecessarily.
2. Tell the user this session covers **functional scoping only**: audience, problem, outcomes, business concepts/rules, functional modules, feature needs, dependencies, and version/MVP boundaries.
3. Invoke `grilling` for its **round-based design-tree interview**; ask coherent frontiers of questions with recommendations, not an arbitrary fixed questionnaire. Invoke `domain-modeling` to refine domain language, update `GLOSSARY.md` as decisions crystallize, and offer ADRs only when genuinely justified.
4. If architecture, implementation or UX design questions arise, put them in `deferred-questions.md` with their intended later phase, and continue with functional questions.
5. The user may stop the interview at any moment. In that case, mark coverage as *partial* and continue to the synthesis gate; do not claim the scoping is comprehensive.

### 2. Summary and first user approval

Produce `.scratch/project-scoping/<project-slug>/scoping-summary.md` with:

- Initial problem, users, intended outcome and constraints.
- Functional decisions explicitly approved by the user, with sources/rationale when available.
- Candidate domains/modules and features **only if grounded in the conversation**, explicitly marked as approved, proposed, rejected, or unresolved.
- MVP inclusions and exclusions **only if explicitly settled**.
- Open functional questions and deferred later-phase questions.
- Functional success scenarios and a **coverage assessment** (complete / partial, and why).

Present a readable summary and ask for **explicit approval or corrections**. Approval here validates the summary; it does **not** automatically approve any proposed or unresolved item. If rejected, revise and ask again. Do not progress without approval.

### 3. Structure the approved summary

Call the `structure-project` skill with `mode=preview` and the approved summary path. That skill proposes a complete catalogue of Modules, Features, decision states, MVP/future scopes, stable IDs and dependencies **before writing final files**.

Present this catalogue **in French** and ask for explicit approval. Iterate as needed. No inferred feature may be marked approved without the user's decision.

Once the catalogue is approved, call `structure-project` with `mode=apply` and the approved catalogue. The skill writes **French-language** documents in `docs/docs-project/` (except the preserved scoping summary) and performs its consistency audit. Review warnings together with the user; do not suppress unresolved issues.

### 4. Documentation review and second approval

Show a concise manifest of created/modified files, structured catalogue, QA findings, and a **Git diff** (or equivalent when Git is unavailable). Verify that source summary was saved in the final docs and glossary/ADR changes are visible.

Ask the user to **approve the final documentation**. If edits are requested, apply them within scope and repeat the audit/review. Do not create GitHub issues; do not move on to UX automatically.

### 5. Git finalization — separate permissions

1. Show `git status` and the scoped diff. Identify pre-existing user changes and files that must **not** be staged. Stage only approved project-scoping files, never `git add -A` blindly.
2. Propose a commit message such as `docs(scoping): finalize functional scope and MVP`.
3. Ask for **explicit commit authorization**. If granted, commit only the approved staged files and report the commit hash; otherwise stop without committing.
4. Ask **separately** for explicit push authorization and target remote/branch, and push only if authorized. A commit approval does not imply a push approval.
5. Mark the workflow complete only when the user-approved scope is documented and the requested Git operations have been handled or explicitly deferred. Recommend UX design as the *next* stage without starting it.

## Never

- Treat a conversation as approval merely because the user stopped asking questions.
- Turn the user's original idea into a hidden new requirement.
- Generate an implementation-ready `to-spec` issue or development tickets during scoping.
- Commit, push, merge, delete or overwrite pre-existing work without appropriate authorization.
- Require an ADR for every decision or fill the glossary with implementation details.
