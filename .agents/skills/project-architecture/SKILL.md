---
name: project-architecture
description: "Design and validate the technical architecture of the MVP and its evolutions in preparation for planning."
disable-model-invocation: true
---

# Project Architecture

This workflow starts only at the user's explicit request. Act as the **architecture-phase orchestrator** for Aura Forge. Convert the **approved global MVP or functional evolution and UX** into proportionate, explicitly approved foundations and technical deltas suitable for planning. Read [shared conventions](../project-scoping/references/versioning.md) first for paths, backlog, progress, delivery and re-entry. The AI advises; the human decides.

**Not this phase:** repeating scoping or UX interviews; producing implementation code; planning GitHub Issues/Projects; silently changing product requirements; speculative microservices, infrastructure, or abstraction layers; automatically committing or pushing.

## Non-negotiable rules

1. **Discover before creating.** Locate the actual repository and documentation baseline using the shared conventions.
2. **Approved inputs are authoritative.** Read relevant material before asking a question. Distinguish approved decisions, proposals, undocumented assumptions, and code currently shipped. Do not relitigate an approved choice without a material conflict.
3. **Explicit decision control.** Before asking to approve a significant architectural choice, produce a decision-specific comparison of genuinely viable alternatives, a clear recommendation and its trade-offs. Do not confuse proposing a choice with approving it. No proposal becomes approved merely because the user did not object.
4. **Canonical documents.** Apply shared preservation rules; distinguish the approved target from actual shipped code.
5. **Approval gates.** Decision approval in B and package approval in E are separate; final Git authorizations belong to F.
6. **No invented traceability.** Reuse `FEAT-*`, `FLOW-*`, `SCREEN-*`, ADR IDs and other identifiers as they exist. Do not fabricate feature approvals, UI behavior, implementation state, scale targets, credentials, hosting details, or test results.
7. **Language.** Skill instructions and machine-readable keys are English. User-facing explanations, `ARCHITECTURE.md`, `TECHNICAL-DESIGN.md`, and ADR narratives are French by default. Keep stable technical names, code identifiers, interfaces, and machine-readable field names in English. Honor existing project conventions or an explicit user override.
8. **Proportional depth.** Decide shared, expensive-to-reverse or cross-module matters now; leave local classes, algorithms, SQL details and private helper signatures to implementation unless a verified constraint demands them. Require only documents needed by the actual functional scope/impact.

## Reuse existing skills without duplicating their work

For the methodological skills below, read and apply their instructions when their branch is relevant and direct invocation is unavailable. This workflow owns phase boundaries, approvals, canonical paths and outputs.

**Core:**
- `grilling` (Matt Pocock): resolve consequential unanswered constraints or choices using its frontier rounds.
- `domain-modeling` (Matt Pocock): clarify new or contradictory domain terminology, maintain existing glossary and sparse ADRs when appropriate; do not duplicate the functional model.
- `codebase-design` (Matt Pocock): design high-leverage, testable modules, seams/interfaces and responsibilities. Evaluate alternatives against actual future change, not hypothetical abstraction.
- `software-architecture` (magnus919): assess system qualities, options, topology, operational behavior, failure modes and evidence for consequential system-level choices. Scale review depth to risks.

**Only when needed:**
- `research` (Matt Pocock): verify uncertain framework, hosting, library, security, performance or API facts against primary sources. If subagents/background execution are unsupported, perform research inline and cite sources; never claim a background task is running.
- `prototype` (Matt Pocock): one-off throwaway logic/state exploration when an architectural decision cannot be settled from diagrams or documents; clearly label any spike experimental. Do not reuse the UX prototype workflow by default.

If a dependency is unavailable, explain the limitation briefly, continue with the principles documented here where practical, and never claim it was executed. Do not auto-install external skills or run untrusted scripts without user approval.

## Inputs, in order

1. Locate the project, approved MVP/change scope and existing documentation baseline using the shared conventions.
2. Read `PROJECT.md`, `MVP.md`, backlog, existing scope/summary files, relevant canonical feature cards, business rules, glossary and accepted ADRs. Read global architecture and earlier technical designs before proposing new work.
3. Read validated UX summary, contract and applicable approved HTML at their actual canonical paths, including legacy `versions/<baseline>/ux/`. An entirely no-UI scope instead requires approved `no_ui` justifications for every scoped feature; no HTML is expected. Trace applicable global MVP journeys, progressive subsets, states and interactions. Mockups are UX evidence, **not production code or a mandated stack**; future context is not implemented scope.
4. Read the existing code, package manifests, schemas, dependencies, infra configuration, tests, and deployment reality if any, especially for later versions. Distinguish code actuality from docs and proposals.
5. Inspect relevant future features **only to avoid costly design dead ends**; do not design or implement future-only scope.
6. Build a concise internal evidence map: fact/decision, source path/ID, approval status, affected version and any uncertainty. Report material conflicts before proceeding.

If a required approved input is absent or inconsistent, perform whatever bounded analysis remains possible, clearly identify the blocker, and **do not mark the architecture handoff planning-ready** or silently fabricate UX details.

## Workflow

### A. Establish drivers and architectural questions

- Summarize global MVP foundations versus the requested functional/release delta, feature/UX/technical dependencies, existing architecture, deployment constraints, assumptions and unknowns. Design required MVP foundations without implementing future-only features or assigning releases prematurely.
- Evaluate only applicable nonfunctional requirements: authentication/authorization, privacy/security, data integrity, resilience, backup/recovery, accessibility-related technical implications, performance, growth, maintainability, testability, hosting/operations, cost, observability, compliance.
- Express significant requirements as observable scenarios or measurable acceptance criteria **only when evidence provides a target**. Otherwise show the target as unresolved; never invent thresholds.
- Build a short decision agenda, ordered by risk, cross-module dependencies and difficulty to reverse. First distinguish issues that need a human decision from those safely solved by convention.
- Break a bundled stack proposal into independently reversible, meaningfully different choices (e.g. frontend framework, backend runtime/framework, storage technology, Codex integration, deployment). Connect the choices through shared constraints, but do not demand a single yes/no for several unrelated technologies. A bundled comparison is acceptable only when the options are genuinely inseparable architectures.

### B. Research, compare, recommend and approve significant decisions

For each consequential **unapproved** choice, follow [technical comparisons](references/technical-comparisons.md): frame the decision, research credible alternatives, persist and present the comparison, then obtain an explicit individual decision before updating canonical materials.

**Done:** every consequential choice in the agenda has an up-to-date scratch comparison (or justified single-option exception), recommendation, evidence/uncertainties and a recorded user decision. Accepted decisions have verifiable approval and canonical rationale; rejected/deferred choices remain explicit. Deferred choices that block planning keep the handoff non-ready. Leave local, low-impact implementation conventions to development.

### C. Design to the right depth

Design only necessary elements:
- System context and deployable/runtime shape; responsibilities and allowed dependencies for modules.
- Logical data ownership, entities, relationships, invariants, lifetime/version semantics, and migrations (especially shared data changes). No exhaustive schema-by-column unless essential to reliable planning.
- **Shared** interfaces/contracts (HTTP operations, events, message shapes, errors, auth, versioning) sufficiently clear for parallel agents; no implementation signatures for private details.
- Key end-to-end flows tied to UX and functional IDs, including important UI states, authorization, transactions, concurrency, partial failures, retries, and recovery where relevant.
- Security/privacy and operational controls proportionate to the actual system; test/verification strategy and architectural acceptance evidence.
- For later versions: existing component/code mapping, what's unchanged, what is added/modified/deprecated, compatibility, data migrations, rollout/rollback concerns, and risk to shipped behavior.

Apply the shared compatibility/stability policy. Populate dependency edges and slice acceptance criteria for downstream planning.

**PATCH path:** first perform a bounded impact check against accepted architecture, interfaces, data invariants, UX and operational risks. If a compatible fix introduces no consequential new choice, reuse accepted ADRs, design and mockups; update only affected sections, verification expectations, compatibility/rollback notes and the contract's change slice. Reuse the existing design path and document unchanged foundations. Do not require a full architecture cycle, new ADR or repeated technology comparisons. Escalate a real boundary/security/migration impact regardless of the requested PATCH label; a breaking fix is not automatically PATCH.

Apply `codebase-design` to avoid shallow pass-through layers and hypothetical seams. Favor the simplest design that satisfies approved needs. If an approved architecture exposes a missing product decision, **return that question to the appropriate source documents** and seek approval; do not invent product behavior in technical files.

### D. Prepare the reviewable architecture package

Read [deliverable formats](references/deliverables.md), then prepare the actual documents and JSON contract at their canonical paths as a draft package. Accepted individual decisions retain their evidence; changed package content is pending final review. Keep `approval.status: draft` and `handoff.planning_ready: false` while preparing or revising the package. Scratch comparisons are already available from B.

Prepare the global `ARCHITECTURE.md`, applicable `TECHNICAL-DESIGN.md`, `ARCHITECTURE-CONTRACT.json` and justified ADRs using the paths and formats in the deliverable reference. Add separate machine-readable interface contracts only when their precision is needed for coordination. Scratch comparisons remain working materials in the workspace from B.

**Done:** the exact manifest, complete draft files and scoped diff are available for validation and user review; every material detail intended for the handoff is present.

### E. Validate and approve the exact package

1. Cross-check each scoped feature against modules/dependencies and applicable FLOW/SCREEN/ACT handling, states, authorization and failures. Compare functional docs, approved UX, architecture prose, ADRs and JSON, including shared delivery records. Check source IDs and file links against the actual approved inputs.
2. From the project repository root run `python .agents/skills/project-architecture/scripts/validate_contract.py <path-to-ARCHITECTURE-CONTRACT.json>`; use `py` on Windows or resolve the installed script path. If Python is unavailable, report manual checks rather than a passed automated audit. Resolve structural errors and blocking contradictions before requesting final approval.
3. Verify that every consequential decision from this session has its current scratch comparison, alternatives or justified exception, sources/uncertainties and actual decision evidence. Record safely delegable, nonblocking questions separately.
4. Present a concise French review of the approach, choices/alternatives/risks, modules/data/interfaces and functional/UX links. Show the exact file manifest, scoped diff, validation results and remaining nonblocking questions; make the complete draft package accessible. Request explicit final approval **of those files and their current content**.
5. Apply corrections to the draft, rerun affected checks and present the changed package for approval. Approval of a comparison or an earlier summary does not approve details written afterward.

**Done:** the reviewed package is validated, has zero blockers and explicit user approval attributable to its exact manifest/content. Substantive changes reopen this gate.

### F. Finalize the approved handoff

Record the package approval in `approval.status` and `approval.evidence_ref`, then set `handoff.planning_ready: true` only for the unchanged package approved in E. Rerun contract validation and show the approval/readiness metadata diff; any substantive correction returns to E. Use the shared model for release/progress semantics.

Give a compact French report of decisions, files, checks, remaining nonblocking points and readiness. Show scoped Git status/diff; stage only approved package files. Request **commit** permission if not already granted, then a distinct **push** authorization with destination remote/branch. Retain the working tree if either is declined. Planning begins only when requested; create no Issues here.

## Re-entry and modifications

Resume using the shared re-entry rules. Compute actual impact, reopen only unapproved or materially affected comparisons, and update the same relevant artifacts. Changed package content follows D–F; an unchanged approved package keeps its approval evidence.

## Example invocation

> Run `project-architecture` for the active project version. Reuse the approved scoping and UX, propose only unresolved technical decisions, and prepare the architecture documents for downstream planning. No code implementation or Git writes without separate approvals.
