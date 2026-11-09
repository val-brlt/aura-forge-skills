# Deliverable conventions (architecture phase)

Read this reference when producing or revising documentation. These are **logical roles**; never duplicate a repository's existing canonical documents merely to match example filenames.

## First discover current paths

Use the repository's existing docs root. If it is `docs/docs-project`, relative targets below are rooted there. Otherwise substitute the discovered root; do not create competing `docs-project` / `docs-projet` directories. Respect an existing architecture or ADR directory and numbering scheme.

```text
<existing-docs-root>/
├── architecture/
│   ├── ARCHITECTURE.md
│   └── adr/
│       └── NNNN-relevant-decision.md    # only when warranted
└── versions/
    └── vN/
        └── architecture/
            ├── TECHNICAL-DESIGN.md
            └── ARCHITECTURE-CONTRACT.json
```

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

## TECHNICAL-DESIGN.md (version scoped, human-facing French)

Recommended sections (omit irrelevant ones):

1. Version/status, verified inputs and canonical links.
2. Goals and non-goals for this version; accepted assumptions and constraints.
3. Architecture delta: `new`, `modified`, `unchanged`, `deprecated` by affected module. V1 defines initial architecture instead.
4. Design and responsibilities, high-impact data model relationships, contracts and critical technical flows. Reference IDs/diagrams/approved mockups.
5. Security, failure handling, data migration and operational constraints applicable now.
6. Risks, verification strategy, required compatibility, acceptance/evidence needed for planning.
7. Short decision index with links to ADRs and unresolved `blocking`/`nonblocking` questions.

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

The structured contract is **an index/hand-off**, not a copy of the prose docs. Omitting an irrelevant optional category is better than inserting invented placeholder architecture. Use JSON `null` or omit optional fields to distinguish unknown from accepted values.

## When a requirement changes after approval

- If current version **not delivered**: update the canonical feature/UX document with authorized product decision, then update affected architecture sections, version design and contract. Maintain stable IDs.
- If version **delivered**: do not silently rewrite its approved historical version to include a new feature. Handle as proposed scope in a later version. The global architecture must accurately distinguish current deployed state from approved future target.
- Never write a bottom-of-file chronological patch block (e.g. "Complément suite à la revue D17"). Move the final decision into the right sections and retain traceability via ADR/Git.

## Planning gate checklist

- [ ] Target version and release state verified.
- [ ] Functional scope and UX inputs present and approved, including contract or transparent exception/blocker.
- [ ] Shared technical contracts sufficiently defined for dependent/parallel agents.
- [ ] Module ownership, dependencies and key invariants coherent.
- [ ] No future-only scope silently included.
- [ ] Significant trade-offs expressly accepted; ADRs written only when warranted.
- [ ] No unresolved blocking question, migration or interface conflict.
- [ ] Global and version architecture, UX, functional specs and JSON contract agree.
- [ ] Final architecture approval is verifiable, separate from Git permissions.
- [ ] Commit and push not performed without two distinct explicit approvals.
