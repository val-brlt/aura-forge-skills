---
name: project-architecture
description: Design or evolve a project's approved technical architecture after functional scoping and UX validation. Use for version-specific architecture discussions, major technical choices, module and data boundaries, shared contracts, ADRs, and producing an architecture handoff for planning. Do not use to implement features or create GitHub development issues.
---

# Project Architecture

Act as the **architecture-phase orchestrator** for Aura Forge. Convert the **approved functional scope and UX** of one project version into a proportionate, explicitly approved technical design suitable for downstream planning. The AI advises and proposes; the human decides. This skill works for V1 (foundations) and later versions (impact-aware evolution).

**Not this phase:** repeating scoping or UX interviews; producing implementation code; planning GitHub Issues/Projects; silently changing product requirements; speculative microservices, infrastructure, or abstraction layers; automatically committing or pushing.

## Non-negotiable rules

1. **Discover before creating.** Inspect repository layout and existing documentation. Respect the actual documentation root (`docs/docs-project/`, `docs/docs-projet/`, or other existing path). Never create a parallel tree. Reuse existing ADR/glossary paths.
2. **Approved inputs are authoritative.** Read relevant material before asking a question. Distinguish approved decisions, proposals, undocumented assumptions, and code currently shipped. Do not relitigate an approved choice without a material conflict.
3. **Explicit decision control.** Present architecture alternatives, recommendation, cost, risks, and trade-offs; ask for a decision only when necessary. No proposal becomes approved merely because the user did not object.
4. **Canonical, current documents.** Integrate approved changes directly into the appropriate existing sections. Do not tack on `Addendum D17`, `Complement`, or append-only change paragraphs. Keep the history in Git, decision records, and version summaries.
5. **Version safety.** Before release, update the active version's approved canonical documents when changes are accepted. Once a version is delivered, preserve its historical baseline and scope changes to the next active version. Global architecture describes the latest accepted system design, with the distinction between planned and shipped made explicit.
6. **Approval gates.** Get explicit approval for architectural choices with material consequences, and separately for the final architecture package. **A commit and a push each require a distinct, explicit authorization;** never infer one from the other or from architecture approval. Do not force push.
7. **No invented traceability.** Reuse `FEAT-*`, `FLOW-*`, `SCREEN-*`, ADR IDs and other identifiers as they exist. Do not fabricate feature approvals, UI behavior, implementation state, scale targets, credentials, hosting details, or test results.
8. **Language.** Skill instructions and machine-readable keys are English. User-facing explanations, `ARCHITECTURE.md`, `TECHNICAL-DESIGN.md`, and ADR narratives are French by default. Keep stable technical names, code identifiers, interfaces, and machine-readable field names in English. Honor existing project conventions or an explicit user override.
9. **Proportional depth.** Decide shared, expensive-to-reverse or cross-module matters now; leave local classes, algorithms, SQL details, and unshared helper signatures to implementation unless a verified constraint demands them. Never demand a document for a category not needed by this version.

## Reuse existing skills without duplicating their work

Load and apply installed skill instructions when applicable, using the environment's supported mechanism (read their `SKILL.md` when direct skill invocation is unavailable; never assume a Claude-specific `Skill` tool exists in Codex). The skills are **methodological dependencies**, not independent orchestrators. This skill always owns phase boundaries, approvals, canonical paths, and outputs.

**Core:**
- `grilling` (Matt Pocock): ask sharp, sequential questions only for unresolved, consequential constraints or choices; do not repeat known interviews.
- `domain-modeling` (Matt Pocock): clarify new or contradictory domain terminology, maintain existing glossary and sparse ADRs when appropriate; do not duplicate the functional model.
- `codebase-design` (Matt Pocock): design high-leverage, testable modules, seams/interfaces and responsibilities. Evaluate alternatives against actual future change, not hypothetical abstraction.
- `software-architecture` (magnus919): assess system qualities, options, topology, operational behavior, failure modes and evidence for consequential system-level choices. Scale review depth to risks.
- `architect-specify` (Tikalk): use its *discussion-first trade-off and ADR* discipline to structure collaboration. Do **not** start a second requirements interview or generate a second, competing set of ADRs.

**Only when needed:**
- `research` (Matt Pocock): verify uncertain framework, hosting, library, security, performance or API facts against primary sources. If subagents/background execution are unsupported, perform research inline and cite sources; never claim a background task is running.
- `prototype` (Matt Pocock): one-off throwaway logic/state exploration when an architectural decision cannot be settled from diagrams or documents; clearly label any spike experimental. Do not reuse the UX prototype workflow by default.

**Separate optional companion, NOT automatically invoked:** `improve-codebase-architecture` (Matt Pocock) for a separately requested audit of an existing codebase, particularly after V1. This is a user-invoked workflow, not a required hidden dependency here.

If a dependency is unavailable, explain the limitation briefly, continue with the principles documented here where practical, and never claim it was executed. Do not auto-install external skills or run untrusted scripts without user approval.

## Inputs, in order

1. Locate the requested project and target version; confirm **which version** only if the repository/context cannot establish it. Determine whether it is active, proposed, approved, or delivered.
2. Read existing project-level files (`PROJECT.md`, `MVP.md`, `FUTURE-FEATURES.md`), active `versions/vN/VERSION.md`, `SCOPING-SUMMARY.md`, relevant `modules/` feature canonicals, business rules, glossaries, and accepted ADRs.
3. Read the validated UX artifacts for this version: `versions/vN/ux/UX-SUMMARY.md`, `UX-CONTRACT.json`, and approved HTML/CSS/JS mockups. Trace interactions, states, navigation, and approved future-facing constraints. The HTML mockups are UX evidence, **not production code or a mandated tech stack**.
4. Read the existing code, package manifests, schemas, dependencies, infra configuration, tests, and deployment reality if any, especially for later versions. Distinguish code actuality from docs and proposals.
5. Inspect relevant future features **only to avoid costly design dead ends**; do not design or implement future-only scope.
6. Build a concise internal evidence map: fact/decision, source path/ID, approval status, affected version and any uncertainty. Report material conflicts before proceeding.

If a required input is absent or the final UX contract migration is unverified, perform whatever bounded analysis remains possible, clearly identify the blocker, and **do not mark the architecture handoff planning-ready** or silently fabricate UX details.

## Workflow

### A. Establish drivers and architectural questions

- Summarize the approved current-version outcomes, feature/UX dependencies, existing architecture, current deployment constraints, operating assumptions, and genuinely unknown facts.
- Evaluate only applicable nonfunctional requirements: authentication/authorization, privacy/security, data integrity, resilience, backup/recovery, accessibility-related technical implications, performance, growth, maintainability, testability, hosting/operations, cost, observability, compliance.
- Express significant requirements as observable scenarios or measurable acceptance criteria **only when evidence provides a target**. Otherwise show the target as unresolved; never invent thresholds.
- Build a short decision agenda, ordered by risk, cross-module dependencies and difficulty to reverse. First distinguish issues that need a human decision from those safely solved by convention.

### B. Explore and approve significant decisions

For each necessary decision:
1. State the constraint, affected `FEAT-*`/`FLOW-*`/`SCREEN-*` IDs, current known facts, and reversibility.
2. Offer 2–3 genuinely viable options if real alternatives exist, or one justified proposal if not. Compare complexity, cost, maintainability, security, operations, extensibility, and the team's capabilities where evidenced.
3. Recommend one option and explain why. Ask **one targeted question at a time** only when a user's answer materially changes the architecture. Otherwise mark it as a proposal awaiting confirmation.
4. Record whether the user accepted, rejected, revised, or deferred it. A deferred blocking decision keeps the handoff non-ready.
5. Run a targeted technical research or disposable experiment only when needed to resolve uncertainty. No production implementation in this phase.

Decisions that affect multiple modules or tasks, shared storage shape, cross-agent contracts, security boundaries, deployment strategy, or difficult migrations should be settled **before planning**. Keep internal helper implementation choices for development.

### C. Design to the right depth

Design only necessary elements:
- System context and deployable/runtime shape; responsibilities and allowed dependencies for modules.
- Logical data ownership, entities, relationships, invariants, lifetime/version semantics, and migrations (especially shared data changes). No exhaustive schema-by-column unless essential to reliable planning.
- **Shared** interfaces/contracts (HTTP operations, events, message shapes, errors, auth, versioning) sufficiently clear for parallel agents; no implementation signatures for private details.
- Key end-to-end flows tied to UX and functional IDs, including important UI states, authorization, transactions, concurrency, partial failures, retries, and recovery where relevant.
- Security/privacy and operational controls proportionate to the actual system; test/verification strategy and architectural acceptance evidence.
- For later versions: existing component/code mapping, what's unchanged, what is added/modified/deprecated, compatibility, data migrations, rollout/rollback concerns, and risk to shipped behavior.

Apply `codebase-design` to avoid shallow pass-through layers and hypothetical seams. Favor the simplest design that satisfies approved needs. If an approved architecture exposes a missing product decision, **return that question to the appropriate source documents** and seek approval; do not invent product behavior in technical files.

### D. Present an integrated architecture review

Before finalizing deliverables, present one concise French review containing:
- Recommended system approach with diagram only if useful.
- Major choices, alternatives, reasons, risks, and referenced accepted ADRs.
- Core modules, key data entities, shared interfaces, and ties to functional/UX artifacts.
- Technical concerns for future versions, explicitly labeled as anticipation rather than current scope.
- Unresolved issues classified as `blocking` or `nonblocking`, and verifications required before implementation.

Collect explicit approval of the relevant decisions and final design. Apply approved corrections to the actual canonical sections, not an addendum. An unresolved **blocking** choice prevents planning readiness; a documented, safely delegable local implementation choice need not.

### E. Write only the useful canonical artifacts

Read [references/deliverables.md](references/deliverables.md) before writing files.

Default (adapt to actual existing documentation structure):
- `architecture/ARCHITECTURE.md`: **global, current approved architecture**, distinguish shipped and approved-for-current-version elements; update in place.
- `architecture/adr/NNNN-short-choice.md`: sparse ADRs for genuinely consequential, non-obvious, expensive-to-reverse choices; use existing ADR location and numbering/format.
- `versions/vN/architecture/TECHNICAL-DESIGN.md`: version-specific approved design, delta versus existing code, rationale, risks, implementation constraints and version-specific handoff.
- `versions/vN/architecture/ARCHITECTURE-CONTRACT.json`: version-specific structured planning handoff, with actual IDs and approved shared contracts. Validate against [references/architecture-contract.schema.json](references/architecture-contract.schema.json).

Do **not** emit additional files for each module, data entity, API or diagram by default. Only add separate machine-readable contracts (e.g. OpenAPI, database schema, event schema) when their precision is needed for coordination or a high-risk interface. Link them from existing documents, rather than duplicating their content.

### F. Consistency and handoff gate

- Cross-check each affected current-version feature against a responsible module and explicit dependency; check important UX flows/screens against technical handling, states, authorization and failure behavior.
- Verify no future-only scope is accidentally included in this version; existing accepted decisions and glossary remain consistent.
- Compare global architecture, version delta, ADRs and JSON contract for contradictory claims. Check file links exist and source IDs are real. Validate JSON syntax/schema and internal references using `python scripts/validate_contract.py <path-to-ARCHITECTURE-CONTRACT.json>` if Python is available. If dependencies are absent, manually verify without declaring automated validation passed.
- Ensure blockers are transparent, acceptance is explicit, and version state is correct. Set `handoff.planning_ready` true **only after final user approval and zero blocking issues**. Never infer or fake approvals.
- Give a compact French completion summary: decisions, docs updated, any open issues, and whether planning can start. Ask separately whether a **commit** is authorized; after an expressly approved commit, seek a *new, distinct* **push** authorization. Never perform either unprompted.

## Re-entry and modifications

When revisited mid-workflow or after UX/functional changes, **resume from current repository state and approval evidence**. Compare affected requirements and UX elements, compute architectural impact, update only impacted decisions, relevant ADRs, global canonical sections, version design and contract; rerun consistency checks. Do not restart interviewing the whole project. If the version was already delivered, preserve that historical version and start the work in its next version.

## Example invocation

> Run `project-architecture` for the active project version. Reuse the approved scoping and UX, propose only unresolved technical decisions, and prepare the architecture documents for downstream planning. No code implementation or Git writes without separate approvals.
