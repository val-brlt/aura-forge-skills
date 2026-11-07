# Aura Forge functional document format (version 1)

Use the structure below. Adapt explanatory French text to the project's documented language; keep identifiers and field keys in English. Never create fake approvals.

## `SCOPING-SUMMARY.md`

Copy faithfully from the approved summary. Prepend a brief header recording approval (date, approving party as described in the conversation, and source file) **only if the approval is evidenced**. Preserve substantive decisions and unresolved notes verbatim where practical. Do not silently upgrade proposals to approvals.

## `PROJECT.md`

```
# Project — <name>

## Purpose and audience
## Problems and outcomes
## Functional boundaries
## Modules
- [<Module>](modules/<module-slug>/MODULE.md): <one-sentence purpose>
## MVP overview
See [MVP](MVP.md).
## Future, unresolved and excluded items
See [Other features](FUTURE-FEATURES.md).
## Outstanding decisions
## Source
[Approved scoping summary](SCOPING-SUMMARY.md)
```

## `modules/<module-slug>/MODULE.md`

```
# Module — <name>

## Purpose
## Scope
## Features
- [AURA-001 — <name>](<feature-slug>.md)
## Dependencies and open points
```

## `modules/<module-slug>/<feature-slug>.md`

Each feature has a short plain YAML frontmatter with unquoted simple scalar values. Example:

```
---
id: AURA-001
module: project-management
decision_status: approved
release_bucket: mvp
source: SCOPING-SUMMARY.md
---

# AURA-001 — Create Project

## User outcome
<Functional goal>

## Expected behavior
<Observable behavior grounded in the approved summary>

## Approved acceptance criteria
- <Only agreed, testable functional criteria, or "Not yet defined">

## Proposed acceptance criteria
- <Clearly marked suggestions, if useful>

## Functional dependencies
- <Feature IDs or "None documented">

## Open questions
- <Questions or "None recorded">
```

**Metadata field contracts:**

- `id`: `AURA-` plus at least 3 digits; unique and stable.
- `module`: matches the containing module folder name.
- `decision_status`: one of `approved`, `proposed`, `rejected`, `unresolved`.
- `release_bucket`: `mvp`, `future`, `none`.
- `source`: basename or path of an approved summary; for this format use `SCOPING-SUMMARY.md` and add a heading or note in prose to locate the decision precisely.
- `mvp` is allowed **only** when `decision_status=approved`.
- `rejected` always uses `release_bucket=none`.
- `future` is for explicitly deferred possibilities and does not imply commitment.

Avoid formatting YAML fields as inline arrays or nested objects: this v1 format keeps metadata machine-readable with a small dependency-free checker.

## `MVP.md`

```
# MVP Scope

## Objective
<What the MVP proves>

## Included Features
- [AURA-001 — Create Project](modules/project-management/create-project.md)

## Scope notes
<Approved boundaries only>
```

## `FUTURE-FEATURES.md`

```
# Other Features and Future Possibilities

## Future possibilities (not committed)
- [AURA-002 — ...](modules/<module>/<feature>.md)

## Approved but unscheduled
- [AURA-003 — ...](modules/<module>/<feature>.md)

## Unresolved / proposed items
- [AURA-004 — ...](modules/<module>/<feature>.md)

## Rejected or out of scope
- [AURA-005 — ...](modules/<module>/<feature>.md)
```

All **non-MVP** feature cards must appear in this document, in an appropriate section. If the user prefers to separate rejected items into a different file later, revise the format and validator together, after approval.
