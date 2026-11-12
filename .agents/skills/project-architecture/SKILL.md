---
name: project-architecture
description: "Concevoir et valider l'architecture technique du MVP et de ses évolutions pour préparer la planification."
disable-model-invocation: true
---

# Project Architecture

This workflow starts only at the user's explicit request. Act as the **architecture-phase orchestrator** for Aura Forge. Convert the **approved global MVP or functional evolution and UX** into proportionate, explicitly approved foundations and technical deltas suitable for planning. Read [shared versioning conventions](../project-scoping/references/versioning.md) first, and the [migration plan](../project-scoping/references/migration.md) for legacy inputs. The AI advises; the human decides. Architecture can be planning-ready before any release number is assigned. Reuse validated architecture and ADRs across releases.

**Not this phase:** repeating scoping or UX interviews; producing implementation code; planning GitHub Issues/Projects; silently changing product requirements; speculative microservices, infrastructure, or abstraction layers; automatically committing or pushing.

## Non-negotiable rules

1. **Discover before creating.** Inspect repository layout and existing documentation. Respect the actual documentation root (`docs/docs-project/`, `docs/docs-projet/`, or other existing path). Never create a parallel tree. Reuse existing ADR/glossary paths.
2. **Approved inputs are authoritative.** Read relevant material before asking a question. Distinguish approved decisions, proposals, undocumented assumptions, and code currently shipped. Do not relitigate an approved choice without a material conflict.
3. **Explicit decision control.** Before asking to approve a significant architectural choice, produce a decision-specific comparison of genuinely viable alternatives, a clear recommendation and its trade-offs. Do not confuse proposing a choice with approving it. No proposal becomes approved merely because the user did not object.
4. **Canonical, current documents.** Integrate approved changes directly into the appropriate existing sections. Keep history in Git, decision records and version summaries.
5. **Baseline safety.** Integrate approved undelivered changes into canonical sections. Preserve delivered baselines/slices; scope enhancements as a new functional delta without requiring a new software number. Global architecture describes the latest accepted system design, explicitly distinguishing designed, planned, developed and shipped elements.
6. **Approval gates.** Get explicit approval for architectural choices with material consequences, and separately for the final architecture package. **A commit and a push each require a distinct, explicit authorization;** never infer one from the other or from architecture approval. Do not force push.
7. **No invented traceability.** Reuse `FEAT-*`, `FLOW-*`, `SCREEN-*`, ADR IDs and other identifiers as they exist. Do not fabricate feature approvals, UI behavior, implementation state, scale targets, credentials, hosting details, or test results.
8. **Language.** Skill instructions and machine-readable keys are English. User-facing explanations, `ARCHITECTURE.md`, `TECHNICAL-DESIGN.md`, and ADR narratives are French by default. Keep stable technical names, code identifiers, interfaces, and machine-readable field names in English. Honor existing project conventions or an explicit user override.
9. **Proportional depth.** Decide shared, expensive-to-reverse or cross-module matters now; leave local classes, algorithms, SQL details and private helper signatures to implementation unless a verified constraint demands them. Require only documents needed by the actual functional scope/impact.

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

If a dependency is unavailable, explain the limitation briefly, continue with the principles documented here where practical, and never claim it was executed. Do not auto-install external skills or run untrusted scripts without user approval.

## Inputs, in order

1. Locate the project, approved MVP/change scope and existing documentation baseline. A release target is optional; do not invent one. Separate approval, development and evidenced delivery; a legacy `v1` is a scope identity without SemVer equivalence.
2. Read `PROJECT.md`, `MVP.md`, backlog, existing scope/summary files, relevant canonical feature cards, business rules, glossary and accepted ADRs. Read global architecture and earlier technical designs before proposing new work.
3. Read validated UX summary, contract and applicable approved HTML at their actual canonical paths, including legacy `versions/<baseline>/ux/`. An entirely no-UI scope instead requires approved `no_ui` justifications for every scoped feature; no HTML is expected. Trace applicable global MVP journeys, progressive subsets, states and interactions. Mockups are UX evidence, **not production code or a mandated stack**; future context is not implemented scope.
4. Read the existing code, package manifests, schemas, dependencies, infra configuration, tests, and deployment reality if any, especially for later versions. Distinguish code actuality from docs and proposals.
5. Inspect relevant future features **only to avoid costly design dead ends**; do not design or implement future-only scope.
6. Build a concise internal evidence map: fact/decision, source path/ID, approval status, affected version and any uncertainty. Report material conflicts before proceeding.

If a required input is absent or the final UX contract migration is unverified, perform whatever bounded analysis remains possible, clearly identify the blocker, and **do not mark the architecture handoff planning-ready** or silently fabricate UX details.

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

Assess compatibility against explicitly identified public contracts, independently of feature priority. Record stability criteria and their approval before proposing `1.0.0` as stable. Use the shared pre-1.0 convention. Populate dependency edges and slice acceptance criteria so a later planner can order functional, UX and technical work. Keep proposed release numbers/assignments unset until dependency analysis and human validation.

**PATCH path:** first perform a bounded impact check against accepted architecture, interfaces, data invariants, UX and operational risks. If a compatible fix introduces no consequential new choice, reuse accepted ADRs, design and mockups; update only affected sections, verification expectations, compatibility/rollback notes and the contract's change slice. Reuse the existing design path and document unchanged foundations. Do not require a full architecture cycle, new ADR or repeated technology comparisons. Escalate a real boundary/security/migration impact regardless of the requested PATCH label; a breaking fix is not automatically PATCH.

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

Read [references/deliverables.md](references/deliverables.md) before writing files. Do not confuse **temporary scratch comparisons** with the canonical approved documents below. Scratch files are prepared during step B, not deferred to this step.

Default (adapt to actual existing documentation structure):
- `architecture/ARCHITECTURE.md`: **global approved MVP/system architecture**, distinguish foundations, designed, developed and actually shipped elements; update in place.
- `architecture/adr/NNNN-short-choice.md`: sparse ADRs for genuinely consequential, non-obvious, expensive-to-reverse choices; use existing ADR location and numbering/format.
- Existing `TECHNICAL-DESIGN.md`: approved MVP foundations plus bounded change/release impacts, rationale, risks and implementation constraints. For a new MVP use `architecture/TECHNICAL-DESIGN.md`; retain legacy version paths and avoid duplicate designs for unchanged PATCH foundations.
- Existing `ARCHITECTURE-CONTRACT.json` (new MVP: `architecture/ARCHITECTURE-CONTRACT.json`): structured handoff with real IDs, approved interfaces and `delivery` separating functional scope, release intentions and actual state. Format `"1.1"` retains all old fields; legacy `"1.0"` remains valid. Validate with [references/architecture-contract.schema.json](references/architecture-contract.schema.json) and shared delivery invariants.

The **working comparisons** live in the same `.scratch/project-architecture/<scope-id>/comparisons/` workspace, never in the docs tree. Keep them across sessions without treating them as approved source-of-truth. Check Git ignore rules before Git actions. **Never commit/push scratch without specific authorization** or delete it automatically after approval.

Do **not** emit additional canonical files for each module, data entity, API or diagram by default. Only add separate machine-readable contracts (e.g. OpenAPI, database schema, event schema) when their precision is needed for coordination or a high-risk interface. Link them from existing documents, rather than duplicating their content.

### F. Consistency and handoff gate

- Cross-check each scoped MVP/change feature against a module and dependencies; map important FLOW/SCREEN/ACT to handling, states, authorization and failures. Check approved release subsets separately from the global design.
- Verify no future-only scope is accidentally included in this version; existing accepted decisions and glossary remain consistent.
- Compare global architecture, version delta, ADRs and JSON contract for contradictory claims. Check file links exist and source IDs are real. From the project repository root, validate JSON syntax/schema and internal references using `python .agents/skills/project-architecture/scripts/validate_contract.py <path-to-ARCHITECTURE-CONTRACT.json>`. Use `py` on Windows if needed or resolve the actual installed skill path. If Python is unavailable, manually verify without declaring automated validation passed.
- For each consequential decision newly proposed in this session, check that the scratch comparison was written and includes actual alternatives (or a documented single-option exception), relevant criteria, reasons, evidence/uncertainties, current status and user approval when accepted. A comparison file does not itself prove approval.
- Ensure blockers are transparent, acceptance explicit and progress truthful. Set `handoff.planning_ready` true **only after final approval and zero blockers**; an empty release ledger does not block readiness for future planning. Approval proves design readiness, never feature development, shipment, MVP achievement or stability. No planning skill or Issues are created here.
- Give a compact French completion summary: decisions, docs updated, any open issues, and whether planning can start. Ask separately whether a **commit** is authorized; after an expressly approved commit, seek a *new, distinct* **push** authorization. Never perform either unprompted.

## Re-entry and modifications

When revisited, **resume from canonical state, scratch and approval evidence**. Compute actual impact; reopen only unapproved or materially affected comparisons. Update the same applicable ADRs, canonical sections, technical design and contract with stable IDs. Partitioning into releases alone updates mappings and dependencies, not already-approved architecture. Preserve delivered baselines and original approvals; an enhancement is a new functional delta with release unset until approved planning. A second unchanged run creates no new ADRs, designs, comparisons, scopes or release records.

## Example invocation

> Run `project-architecture` for the active project version. Reuse the approved scoping and UX, propose only unresolved technical decisions, and prepare the architecture documents for downstream planning. No code implementation or Git writes without separate approvals.
