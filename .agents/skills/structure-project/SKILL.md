---
name: structure-project
description: "Model-invoked Aura Forge skill for previewing, applying and auditing version-aware functional docs: one canonical feature card per feature, immutable approved version scopes, living backlog, and V1 MVP/V2+ changes."
---

# Aura Forge — Structure a Product Version

**Role:** Convert the **approved functional summary for one target version** into a user-reviewable feature catalogue and traceable project docs. Can run for V1/MVP and be reused for V2, V3, etc. This skill is **model-invoked** so `project-scoping` can call it. Communicate with the user in **French** and respect `AGENTS.md`, approved docs and glossary conventions.

**Language contract:** Write all new *user-facing* docs in **French**, including titles, section headings, descriptions, version differences, business rules and acceptance criteria, regardless of source language. Keep `FEAT-*` IDs, file names/slugs, YAML frontmatter keys/values in English. Keep the approved summary **verbatim** in its original language. Do not automatically translate the glossary or ADRs.

## Inputs and modes

Required inputs: `target_version` (e.g. `v1`, `v2`), approved summary path and existing docs tree when present. Specify `release_kind=mvp` for the V1 MVP or `standard` for normal versions, based on explicit product decisions.

- `mode=preview`: **read-only** analysis, catalogue, proposed changes and exact file manifest.
- `mode=apply`: write/update after the user **explicitly approves the catalogue** and version boundary.
- `mode=audit`: inspect and validate without changing files.

If summary approval or version identity is unclear, stop and request a concrete decision; do not invent consent. Never publish issues, choose a stack or implement code.

## Catalogue and history rules

1. Read the full current approved summary, the previous version scopes and relevant existing functional docs, glossary and ADRs. Determine whether the input describes an **entirely new feature** or an **evolution of an existing feature**.
2. Propose coherent **functional** modules, not implementation packages. Keep each feature in **one canonical card** at `modules/<module>/<feature>.md`, and reuse stable IDs across versions. Never create a duplicate card for a V2 enhancement of the same feature.
3. Separate **decision state** (`approved`, `proposed`, `rejected`, `unresolved`) from **version scope** (membership in `versions/<version>/VERSION.md`) and from **delivery status** (explicitly confirmed by the user or trustworthy records, never presumed by this skill). Do not use the legacy `release_bucket: mvp` as a timeless global property.
4. Document changes to existing features as an **append-only, version-labelled section** in their canonical feature card: V1's agreed behavior/acceptance criteria remain identifiable after V2 introduces other rules. Avoid silently replacing or reinterpreting earlier approved requirements.
5. New approved version scopes include **only approved functional work**. Proposed/unresolved/rejected items are retained in their appropriate backlog sections but **not** represented as approved release commitments. A previous version's delivery status is not inferred from its scope.
6. Every feature, version-level decision and meaningful change must trace to an **approved summary or explicit user decision**. Unsupported acceptance criteria stay labelled *proposed*, and missing facts stay *unresolved*.
7. During `preview`, display module, stable feature ID, French name, new-versus-evolution, target version, decision state, provenance, affected files and diff impact. Show gaps, duplicates, contradictions and assumptions. **Wait for explicit approval.**

## Document tree

Follow `references/document-formats.md`. For a new project:

```text
docs/docs-project/
├── PROJECT.md                   # Living overview and index of versions
├── MVP.md                       # Optional compatibility pointer to V1 (not a second feature catalogue)
├── FUTURE-FEATURES.md           # Living backlog: deferred, proposed, unresolved, rejected
├── versions/
│   ├── v1/
│   │   ├── VERSION.md           # Approved V1 scope (MVP when designated)
│   │   └── SCOPING-SUMMARY.md   # Approved source snapshot in original language
│   └── v2/
│       ├── VERSION.md           # Approved V2 changes relative to baseline
│       └── SCOPING-SUMMARY.md
└── modules/
    └── <module-slug>/
        ├── MODULE.md
        └── <feature-slug>.md     # One canonical card per feature across all versions
```

Do **not** create future version folders until those versions have been scoped and approved. `versions/v1/VERSION.md` is the source of truth for V1, not root `MVP.md`; the latter is optional compatibility/navigation only. Versions have their own approved summary and scope. Feature cards/modules and `PROJECT.md` can be updated by later approved cycles; past version summaries/scopes must not be silently rewritten. `FUTURE-FEATURES.md` may continue listing an enhancement of an already delivered feature, but label the **pending change**, not the whole feature, as future.

### Compatibility with old V1-only docs

When legacy documents already exist at root (`MVP.md`, `SCOPING-SUMMARY.md`, feature `release_bucket: mvp`), **do not destroy or silently migrate them**. In preview, propose a one-time mapping from the approved V1 scope to `versions/v1/VERSION.md` and from `release_bucket` to explicit version membership. Preserve IDs and historical source links. The root summary can remain the source and be referenced by the V1 version index rather than duplicated; a version-specific summary is recommended for each **new** version. Perform migration only with explicit approval, then audit. If old and new scopes conflict, stop and report both.

## Apply, audit and handback

Only after the catalogue is approved:

1. Create/update the current version's `versions/<version>/SCOPING-SUMMARY.md` **faithfully**, avoiding an unnecessary duplicate of an existing approved root summary in an approved migration.
2. Create `versions/<version>/VERSION.md` with `status: draft` pending final documentation approval, approved goal, baseline, included new features and enhancements (link to canonical cards), exclusions, dependencies, open decisions and the source snapshot. Treat this as a **historical record** after approval, never an editable living backlog.
3. Update `PROJECT.md` as a **living product overview and index** to all versions. Update appropriate module/feature cards with version-labelled changes, preserving earlier history. Update `FUTURE-FEATURES.md` with deferred, unresolved and rejected work, without suggesting delivery.
4. For the initial V1 designated MVP, optionally add root `MVP.md` with a **link** to `versions/v1/VERSION.md`, never a duplicate catalogue. Do not generate a new root `MVP.md` for V2. Preserve an existing one unless its change was explicitly approved.
5. Compare affected files and show any updates to earlier approved content. Require a specific approval **before** changing a previously approved version snapshot.
6. Run the structural validator:

   `python .agents/skills/structure-project/scripts/validate_docs.py docs/docs-project`

   On Windows use `py` if needed; locate the actual installed skill path when necessary. This script checks version indices, links, stable IDs and basic approval constraints; it **cannot determine whether something was really shipped**, whether behavior is correct, or whether French prose is good. Conduct a separate semantic and linguistic review.
7. Return the file manifest, exact current-version feature set, diff summary, warnings and blockers to the orchestrator for **human documentation approval**. **Never commit or push.**

## Never

- Pretend the scoping snapshot for V1 is evidence that V1 was shipped.
- Automatically migrate backlog features into V2 or mark older features delivered.
- Create duplicate feature cards for version upgrades or rewrite earlier version-specific acceptance criteria.
- Update an approved historical `versions/<old>/VERSION.md` without separate explicit approval.
- Conflate MVP with every future version or infer version membership from a single global `mvp` flag.
- Invent product requirements, acceptance criteria, delivery evidence, GitHub tickets or technical architecture.
