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
3. **Explicit decision control.** Before asking to approve a significant architectural choice, produce a decision-specific comparison of genuinely viable alternatives, a clear recommendation and its trade-offs. Do not confuse proposing a choice with approving it. No proposal becomes approved merely because the user did not object.
4. **Canonical, current documents.** Integrate approved changes directly into the appropriate existing sections. Do not tack on `Addendum D17`, `Complement`, or append-only change paragraphs. Keep the history in Git, decision records, and version summaries.
5. **Version safety.** Before release, update the active version's approved canonical documents when changes are accepted. Once a version is delivered, preserve its historical baseline and scope changes to the next active version. Global architecture describes the latest accepted system design, with the distinction between planned and shipped made explicit.
6. **Approval gates.** Get explicit approval for architectural choices with material consequences, and separately for the final architecture package. **A commit and a push each require a distinct, explicit authorization;** never infer one from the other or from architecture approval. Do not force push.
7. **No invented traceability.** Reuse `FEAT-*`, `FLOW-*`, `SCREEN-*`, ADR IDs and other identifiers as they exist. Do not fabricate feature approvals, UI behavior, implementation state, scale targets, credentials, hosting details, or test results.
8. **Language.** Skill instructions and machine-readable keys are English. User-facing explanations, `ARCHITECTURE.md`, `TECHNICAL-DESIGN.md`, and ADR narratives are French by default. Keep stable technical names, code identifiers, interfaces, and machine-readable field names in English. Honor existing project conventions or an explicit user override.
9. **Proportional depth.** Decide shared, expensive-to-reverse or cross-module matters now; leave local classes, algorithms, SQL details, and unshared helper signatures to implementation unless a verified constraint demands them. Never demand a document for a category not needed by this version.
10. **Compare before recommending.** Do not jump from constraints to a preferred technology without showing credible alternatives and why those alternatives win or lose **for this project**. Consider competing languages, frameworks, runtimes and deployment models when relevant, not merely packages in the first ecosystem that comes to mind. Do not manufacture alternatives to fill a quota.
11. **Persist comparisons in scratch.** Every consequential comparison must have an up-to-date, human-readable Markdown work file under the repository's `.scratch/project-architecture/<version>/comparisons/` **before** requesting approval. These files are reviewable working evidence, not approved specifications or an excuse to create addenda in canonical documents. Preserve/update them across session resumes; never automatically include them in Git commits.

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
- Break a bundled stack proposal into independently reversible, meaningfully different choices (e.g. frontend framework, backend runtime/framework, storage technology, Codex integration, deployment). Connect the choices through shared constraints, but do not demand a single yes/no for several unrelated technologies. A bundled comparison is acceptable only when the options are genuinely inseparable architectures.

### B. Research, compare, recommend and approve significant decisions

Read [references/technical-comparisons.md](references/technical-comparisons.md) before the first consequential technical proposal. Use that reference for format, scratch location, statuses and minimum quality.

For each consequential **unapproved** choice (technology, framework, runtime, architecture style, integration approach, persistence, deployment/security boundary, shared interface):

1. **Frame the specific decision.** Explain the goal and scope of the choice; connect real functional/UX requirements, accepted constraints, current code and architecture, future migration concerns (if material), and user/team skills **only when known**. Separate hard requirements, preferences and assumptions. State what would make the choice reversible or expensive to reverse.
2. **Explore the actual option space.** Check relevant competing approaches, including *other ecosystems* where sensible (e.g. compare Node/TypeScript with JVM/Java or Python for a backend, rather than only Fastify vs Express). Explicitly justify any important family excluded by hard constraints. Shortlist usually **2–4 genuinely viable options**; fewer only when context leaves fewer credible choices. Do not create an exhaustive framework catalog or force token alternatives. Compare equivalent decisions: do not conflate frontend, backend and database selection, or a full-stack framework with a backend-only framework without explaining their architectural scope.
3. **Verify material claims.** Where the comparison turns on current integrations, pricing, license, feature support, deployment constraints, version compatibility, performance, or security, consult trustworthy primary documentation/source code when accessible, recording URLs and the verification date. Distinguish verified facts from informed estimates or assumptions; never make up benchmarks or costs. If verification is unavailable, say so and flag what still needs confirming.
4. **Show the trade-off.** Present a concise user-facing table, usually with one row per alternative, explaining strengths, weaknesses and project-specific suitability. Compare against the *few criteria that actually discriminate*, such as integration with Codex, packaging/local runtime, complexity, security, cost, team familiarity (if evidenced), maintenance, future private hosting and migration costs. Weight criteria only when priorities are established; never invent numerical rankings. Identify both the rejected options and why they lose in this situation.
5. **Recommend, not just list.** Name a preferred solution and give its most decisive reasons, its costs/risks, situations where another option would be better, and the consequences/dependencies of accepting it. A recommendation may be provisional if an essential fact is unknown. Avoid the lazy explanation that one language is shared between frontend and backend unless this offers concrete, relevant value.
6. **Write the scratch comparison BEFORE requesting approval.** Create or update `<repo>/.scratch/project-architecture/<version>/comparisons/<stable-choice-slug>.md` using the reference template; match an existing `.scratch` convention if one exists. Put the same meaningful comparison in the discussion (a link alone is insufficient). Reuse the file for revisions to that decision; do not create a new dated comparison on every iteration. Keep source links, status, accepted/rejected option, and user feedback current. If the filesystem is read-only, show the complete comparison inline and explicitly report that scratch persistence failed.
7. **Discuss and approve the individual choice.** Ask one targeted question at a time, only when it can change the architecture. Present a clearly framed approval choice. Wait for explicit acceptance before treating the recommendation as accepted. Record `proposed`, `accepted`, `rejected` or `deferred` status in scratch, with only verifiable approval evidence. If the user rejects the preferred option, update the existing comparison with the chosen alternative and its trade-offs; do not silently overwrite the recommendation as though it had always been first.
8. **Update canonical materials only when appropriate.** After approval, incorporate the accepted decision in canonical architecture sections and, only if warranted, a sparse ADR. An ADR is not the entire scratch comparison; preserve the essential context, realistic alternatives, rationale and consequences in canonical prose without depending on scratch to remain available. A proposed architecture in a draft design must be clearly labeled *proposed*; do not mark it accepted or planning-ready. Do not change unrelated product documents simply to reflect an unaccepted technology proposal.

**Exceptions:** Do not retroactively reopen already approved choices without a material conflict/new requirement. Local, low-impact implementation conventions do not need a full comparison file or human decision. For high-impact issues with no credible alternative, write a brief scratch note explaining the constraint, attempted option search and why the single proposal is forced, then seek approval. If a potentially important choice is deferred and blocks meaningful planning, keep the handoff non-ready.

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

Read [references/deliverables.md](references/deliverables.md) before writing files. Do not confuse **temporary scratch comparisons** with the canonical approved documents below. Scratch files are prepared during step B, not deferred to this step.

Default (adapt to actual existing documentation structure):
- `architecture/ARCHITECTURE.md`: **global, current approved architecture**, distinguish shipped and approved-for-current-version elements; update in place.
- `architecture/adr/NNNN-short-choice.md`: sparse ADRs for genuinely consequential, non-obvious, expensive-to-reverse choices; use existing ADR location and numbering/format.
- `versions/vN/architecture/TECHNICAL-DESIGN.md`: version-specific approved design, delta versus existing code, rationale, risks, implementation constraints and version-specific handoff.
- `versions/vN/architecture/ARCHITECTURE-CONTRACT.json`: version-specific structured planning handoff, with actual IDs and approved shared contracts. Validate against [references/architecture-contract.schema.json](references/architecture-contract.schema.json).

The **working comparisons** live in `.scratch/project-architecture/<version>/comparisons/` at the repository root, never in the docs tree. Keep them accessible across sessions without treating them as approved source-of-truth. Inspect whether `.scratch/` is Git-ignored; if not, warn before Git operations and suggest ignoring it according to repo conventions. **Never commit/push scratch materials without specific authorization.** Do not delete them automatically after approval.

Do **not** emit additional canonical files for each module, data entity, API or diagram by default. Only add separate machine-readable contracts (e.g. OpenAPI, database schema, event schema) when their precision is needed for coordination or a high-risk interface. Link them from existing documents, rather than duplicating their content.

### F. Consistency and handoff gate

- Cross-check each affected current-version feature against a responsible module and explicit dependency; check important UX flows/screens against technical handling, states, authorization and failure behavior.
- Verify no future-only scope is accidentally included in this version; existing accepted decisions and glossary remain consistent.
- Compare global architecture, version delta, ADRs and JSON contract for contradictory claims. Check file links exist and source IDs are real. Validate JSON syntax/schema and internal references using `python scripts/validate_contract.py <path-to-ARCHITECTURE-CONTRACT.json>` if Python is available. If dependencies are absent, manually verify without declaring automated validation passed.
- For each consequential decision newly proposed in this session, check that the scratch comparison was written and includes actual alternatives (or a documented single-option exception), relevant criteria, reasons, evidence/uncertainties, current status and user approval when accepted. A comparison file does not itself prove approval.
- Ensure blockers are transparent, acceptance is explicit, and version state is correct. Set `handoff.planning_ready` true **only after final user approval and zero blocking issues**. Never infer or fake approvals.
- Give a compact French completion summary: decisions, docs updated, any open issues, and whether planning can start. Ask separately whether a **commit** is authorized; after an expressly approved commit, seek a *new, distinct* **push** authorization. Never perform either unprompted.

## Re-entry and modifications

When revisited mid-workflow or after UX/functional changes, **resume from current repository state and approval evidence**. Compare affected requirements and UX elements, compute architectural impact, **reopen only impacted scratch comparisons if a choice is unapproved or new evidence materially changes a past decision**, update relevant ADRs, global canonical sections, version design and contract; rerun consistency checks. Preserve previously recorded options, sources and actual user decisions without replacing them with fabricated approval history. Do not restart interviewing the whole project. If the version was already delivered, preserve that historical version and start the work in its next version.

## Example invocation

> Run `project-architecture` for the active project version. Reuse the approved scoping and UX, propose only unresolved technical decisions, and prepare the architecture documents for downstream planning. No code implementation or Git writes without separate approvals.
