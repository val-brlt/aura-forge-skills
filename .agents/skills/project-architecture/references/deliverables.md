# Deliverable conventions (architecture phase)

Read this reference when producing or revising documentation. These are **logical roles**; never duplicate a repository's existing canonical documents merely to match example filenames.

Read [shared versioning conventions](../../project-scoping/references/versioning.md). MVP objective, software version, actual release and milestone are independent. Existing `versions/v1/` is an approved scope baseline without an inferred software version.

## First discover current paths

Use the repository's existing docs root. If it is `docs/docs-project`, relative targets below are rooted there. Otherwise substitute the discovered root; do not create competing `docs-project` / `docs-projet` directories. Respect an existing architecture or ADR directory and numbering scheme.

```text
<existing-docs-root>/
├── architecture/
│   ├── ARCHITECTURE.md
│   ├── adr/                           # existing ADR path takes precedence
│   │   └── NNNN-relevant-decision.md   # only when warranted
│   ├── TECHNICAL-DESIGN.md             # new global MVP, or reuse an existing design path
│   └── ARCHITECTURE-CONTRACT.json      # same rule; no forced release partition
└── versions/<existing-baseline>/architecture/  # retained when already present
```

## Scratch comparisons (not canonical architecture deliverables)

Before a consequential new technical recommendation is submitted for approval, maintain its comparison in `.scratch/project-architecture/<scope-id>/comparisons/<choice>.md` (reuse an existing version-named workspace). See [technical-comparisons.md](technical-comparisons.md). Keep alternatives, recommendation, trade-offs, criteria, primary sources, uncertainties and actual decision status current in the same file.

These scratch files are **working review materials**. They do not imply a validated decision, do not substitute for the rationale in an ADR or the canonical architecture, and should not be included in Git commits by default. A decision affecting several independent technologies should have separate comparisons; avoid a single approval that bundles unrelated trade-offs.

## ARCHITECTURE.md (global architecture, human-facing French)

Keep short, factual, canonical and organized by **subject**, never by a chronology of appended corrections. Suggested sections when relevant:

1. Purpose, scope, relationship to current shipped code and approved target state.
2. Context and system topology; clear external dependencies.
3. Architectural principles and key technical choices (links to existing ADRs).
4. Major modules, responsibilities, allowed dependencies/interfaces.
5. Data ownership and high-level data lifecycle.
6. Authentication/security/privacy and relevant trust boundaries.
7. Runtime/deployment/operations, observability, backup/recovery if applicable.
8. Link to approved version-specific designs and version boundaries.

Keep version-specific diffs out of this document. When current shipped code differs from the approved target, label both rather than silently implying the target is already delivered.

## TECHNICAL-DESIGN.md (MVP foundations and bounded deltas, French)

Recommended sections (omit irrelevant ones):

1. Functional scope ID/path, document approval status, verified inputs and optional already-approved release context.
2. Global MVP goals/foundations versus requested change, non-goals and accepted constraints; no future-only implementation.
3. Architecture delta: `new`, `modified`, `unchanged`, `deprecated` by module versus actual code/approved baseline. Initial foundations do not imply an initial release.
4. Design and responsibilities, high-impact data model relationships, contracts and critical technical flows. Reference IDs/diagrams/approved mockups.
5. Security, failure handling, data migration and operational constraints applicable now.
6. Risks, verification strategy, required compatibility, acceptance/evidence needed for planning.
7. Short decision index with links to ADRs and unresolved `blocking`/`nonblocking` questions.
8. Known functional/UX/technical dependencies, independently testable slices and acceptance, public-contract compatibility and explicit stability criteria. Release intentions and evidence of actual delivery remain separate and may be unknown.

For a compatible PATCH without consequential architectural change, retain the existing design and ADRs. Record only bounded impact, affected invariants/interfaces/UX if any, verification and rollback concerns and the structured change slice. Do not generate a full new design or repeat comparisons merely for a number increment. A verified major impact reopens only the affected decisions.

Do not paste the full `UX-CONTRACT.json` or duplicate functional specs. Use stable links and concise rationale.

## ADR (sparse, existing format preferred)

Create only if **all** apply:
- Reversal later would be costly.
- A future maintainer would reasonably wonder why this choice was made.
- Real alternatives existed with consequential trade-offs.

Typical fields: status (`proposed`, `accepted`, `superseded`), context and drivers, alternatives, chosen option **only after approval**, consequences/risks, feature/version scope, evidence links, date/approval reference if verifiable. Revisions to accepted choices are a new superseding ADR or updated existing ADR only according to repo conventions; never forge historical sign-off.

## ARCHITECTURE-CONTRACT.json (agents/planning, English keys)

Schema is in `references/architecture-contract.schema.json`. Use *only validated identifiers and existing files*. Minimal but meaningful data:

- Version identity, status and paths to approved functional/UX inputs.
- Modules with actual responsibility, inter-module dependencies and source feature/UX IDs.
- Shared interfaces/events with provider, consumers and meaningful contract constraints.
- Data entities, ownership, relationships/invariants relevant to implementation ordering.
- Accepted ADR references, impactful nonfunctional requirements and crosscutting controls.
- Existing-to-target version delta and migration/compatibility notes where applicable.
- Traceability from functional features to modules and critical flows.
- Open questions and planning blockers, explicitly tracked.
- `approval.status` and `handoff.planning_ready`: true readiness only after verified user approval and no blockers.
- `schema_version: "1.1"` adds shared `delivery` metadata. Keep `version.id`, `version.status`, `technical_design_path`, baseline, sources and all existing IDs/traceability. `version.id` is the documentation baseline (e.g. `mvp` or legacy `v1`), not an automatic software version. `version.status` remains historical design/baseline status; new design approval uses `approval.status`. Actual delivery comes only from the delivery ledger and evidence.
- `delivery.scope.feature_refs` matches scoped module/traceability FEAT references. Progress items cover those FEATs and existing MOD/IFACE/DATA IDs plus linked FLOW/SCREEN/ACT as relevant. Do not invent UX items absent from the approved UX source. Global scope/dependencies can be planning-ready with `releases: []`.

Legacy `"1.0"` remains accepted without `delivery`; validators warn that software release/progress metadata is unavailable. Format updates must preserve existing data and verified approvals, use unknown progress and empty assignments unless evidenced, and undergo reviewed approval before replacing approved contracts. Shared schema dependency stays packaged with all three skills.

The structured contract is **an index/hand-off**, not a copy of the prose docs. Omitting an irrelevant optional category is better than inserting invented placeholder architecture. Use JSON `null` or omit optional fields to distinguish unknown from accepted values.

## When a requirement changes after approval

- If current version **not delivered**: update the canonical feature/UX document with authorized product decision, then update affected architecture sections, version design and contract. Maintain stable IDs.
- If version **delivered**: do not silently rewrite its approved historical version to include a new feature. Handle as proposed scope in a later version. The global architecture must accurately distinguish current deployed state from approved future target.
- Integrate the accepted decision into its canonical section and retain traceability via ADR/Git.

## Planning gate checklist

- [ ] Functional scope and document baseline verified; any release intentions and actual delivery state remain independently evidenced, possibly unknown.
- [ ] Functional scope and UX inputs present and approved, including contract or transparent exception/blocker.
- [ ] Shared technical contracts sufficiently defined for dependent/parallel agents.
- [ ] Module ownership, dependencies and key invariants coherent.
- [ ] No future-only scope silently included.
- [ ] Consequential newly proposed choices were compared in `.scratch/` before approval, with credible alternatives, recommendation and evidence; significant trade-offs expressly accepted; ADRs written only when warranted.
- [ ] No unresolved blocking question, migration or interface conflict.
- [ ] Global and version architecture, UX, functional specs and JSON contract agree.
- [ ] Final architecture approval is verifiable, separate from Git permissions.
- [ ] Commit and push not performed without two distinct explicit approvals.
