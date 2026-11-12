# Shared scope, version and delivery conventions

Read this reference before changing functional, UX or architecture documents. All three project skills use this model; reading it does not invoke another workflow. Preserve existing canonical paths and approvals.

## Four independent concepts

- **MVP**: the global functional objective, indispensable `FEAT-*` and measurable success criteria in `MVP.md`. It may span several `0.x.y` deliveries. Keep future-only capabilities in `FUTURE-FEATURES.md`.
- **Software version**: an identified software state, normally `MAJOR.MINOR.PATCH`, without a `v` prefix. Historical identifiers such as `v1` remain documentation identities, without an inferred SemVer equivalent.
- **Release**: actual delivery of a version. Proposed/planned release records are intentions, not evidence of delivery.
- **Milestone**: a functional or delivery objective with success criteria. Achieving the MVP milestone is independent of declaring the first stable version.

`1.0.0` means the first stable public contract according to explicit, human-approved stability criteria, never automatically MVP completion. Record which APIs, events, file formats, integrations or other externally relied-on behavior constitute public contracts. Do not invent stability thresholds.

## SemVer policy

Follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html): incompatible public-contract changes increment MAJOR; compatible functionality (including public deprecation) increments MINOR; compatible fixes increment PATCH. Reset lower components on a MAJOR/MINOR increment. Feature importance, effort and commercial priority do not determine the bump. Published contents are immutable.

For `0.x.y`, use this explicit project convention until a different convention is approved: compatible fixes increment PATCH; new functionality or incompatible changes increment MINOR and reset PATCH. Document every incompatibility and migration even while MAJOR is zero. `0.x.y` contracts remain unstable. The first delivery number and release assignments stay undecided until dependency analysis and human validation. Store normal `X.Y.Z` numbers in the release ledger; prerelease/build labels, if needed, require an explicit extension of this model and must never be silently stripped.

## Canonicals, progress and partial delivery

- `MVP.md` links indispensable canonical feature cards and records global success criteria, exclusions, functional dependencies, unresolved decisions and the MVP milestone. It remains useful without any release number. It is not a pointer equating MVP with an initial version.
- One canonical card per `FEAT-*`, under the existing modules tree. Preserve source links, approved behavior and acceptance criteria. Integrate approved refinements into the ordinary sections with a reviewed diff, rather than addenda. Preserve delivered baselines and original summary snapshots.
- Separate decision (`approved`, `proposed`, `rejected`, `unresolved`), planned versions (possibly empty), development (`unknown`, `not_started`, `in_progress`, `complete`) and delivery (`unknown`, `not_delivered`, `partial`, `delivered`). Approval of scope, HTML or architecture proves none of implementation or shipment.
- Describe incremental slices as stable `CHANGE-*` entries with their own acceptance criteria and dependencies; they reference the same feature/flow/screen/interaction/module IDs. A released slice does not deliver the entire feature. Whole-item `delivered` requires all its approved acceptance criteria, complete development and verifiable delivery evidence. Keep partial progress explicit.
- Milestone achievement requires evidence for all success criteria and delivery of every indispensable MVP feature. Stability has its own criteria and approval. Neither follows from a percentage or a single release.
- Known dependency edges identify their kind (`functional`, `ux`, `technical`), reason and decision status. Unknown dependencies remain questions/blockers. Only the future planning workflow assigns releases after dependency analysis and human approval; these skills may record already-approved assignments without inventing a schedule, Issues or a new planning skill.

## Structured handoff and compatibility

New UX contracts use `schemaVersion: 2`; new architecture contracts use `schema_version: "1.1"`. Both add a `delivery` object conforming to [delivery.schema.json](delivery.schema.json). Old UX `1` and architecture `"1.0"` remain readable and valid; validators report that release state is unknown. Schema numbers describe the document format, not a software release.

Retain the legacy `version`, `scope`, `status`, sources, coverage and traceability fields. `version` / architecture `version.id` identify the existing **document baseline**, possibly `v1` or `mvp`; they do not assert delivery. `status` remains the document's approval state. `scope` remains the authoritative functional source path. Actual software versions occur only in `delivery.releases` and item assignments.

`delivery` fields:

| Field | Meaning |
| --- | --- |
| `scope` | Stable scope ID, `mvp` / `change` / `legacy` kind, existing canonical path relative to DOCS_ROOT, and in-scope `FEAT-*` IDs. Never derive scope from a filename alone. |
| `items` | One progress record per referenced item, stable `ref`, `scope` (`mvp`, `future`, `supporting`), approved acceptance criteria and independent decision/planning/development/delivery fields. Include features plus relevant FLOW/SCREEN/ACT or MOD/IFACE/DATA IDs. Future context alone does not create designed or developed items. |
| `releases` | Possibly empty ledger; unique SemVer numbers, verified baseline or `null`, proposal/planning/development/delivery status, approval and evidence references. Each change has stable ID, affected items, kind, compatibility, summary, slice acceptance criteria and prerequisite change IDs. |
| `dependencies` | Directed edges: `from_ref` depends on `to_ref`; both reference known items. Kind and reason preserve functional/UX/technical ordering inputs. |
| `milestones` | Stable objectives with criteria, status (`open` / `achieved`) and evidence. An MVP milestone is independent of a release. |
| `public_contracts`, `stability_criteria`, `stability_approval_ref` | Known compatibility boundary, criteria for stability and explicit human acceptance; empty arrays / `null` mean unresolved, never stable by default. |

`planned_versions` includes only human-approved assignments to non-proposed records; every assignment must have a matching release change. `delivered_versions` references actually delivered records and matching changes; `evidence_refs` supports actual progress. Future-only items have no release assignments or implementation claims in an MVP handoff. `no_ui` and UX `covered` concern design coverage only.

Validators check structure, IDs, reference consistency, evidence presence and common false-delivery claims. Humans still verify evidence contents, actual acceptance, external dependencies and approval authority. A structurally valid contract is not approval or shipment. Architecture `handoff.planning_ready` means dependencies and design are ready for planning; releases may still be empty.

Before handoff, compare UX and architecture scope IDs, shared FEAT/FLOW/SCREEN/ACT progress, release versions/statuses, change identities and evidence references. Shared records must agree; investigate a conflict instead of overwriting another phase's approval. These contracts are phase views of the same approved objective. The later planner owns the consolidated release proposal; neither phase infers it from the other. Approved global MVP membership stays in `MVP.md`, not in a second feature catalogue.

## Re-entry and idempotence

Read canonical documents, existing scratch state and approval evidence before asking questions. Match scopes by stable ID/path, features by FEAT ID, UX by FLOW/SCREEN/ACT ID, technical objects by existing IDs, changes by CHANGE ID, releases by exact SemVer, and milestones/dependency edges by stable identity. Update these same records in place. A second run with unchanged inputs must produce no new cards, galleries, scope folders, release records or comparisons. Release partitioning alone reuses approved design and HTML. Reapprove only changed decisions/design; preserve old approvals with their actual coverage.
