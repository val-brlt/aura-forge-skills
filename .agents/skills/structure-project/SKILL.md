---
name: structure-project
description: "Turn an approved functional scoping summary into a reviewable catalogue and modular project documentation with Modules, Feature cards, MVP scope and deferred ideas. Use after an approved scoping interview or when auditing existing scoping documentation."
---

# Aura Forge — Structure Project

**Role:** Convert an approved functional summary to a reviewable, traceable documentation structure. This is a **model-invoked** skill so `project-scoping` can call it. You may also invoke it directly for experiments.

Communicate with the user in French. Respect the repository `AGENTS.md` and the terms in `GLOSSARY.md` (including existing bilingual conventions).

**Mandatory output language:** Produce every new **user-facing functional document** in **French**: `PROJECT.md`, `MVP.md`, `FUTURE-FEATURES.md`, `modules/*/MODULE.md`, and all canonical Feature cards. Translate section headings, titles, feature/module display names, descriptions, observable behaviors, functional rules, acceptance criteria, dependencies, open questions and all index descriptions. Do **not** inherit English prose from an English-language scoping source. Keep stable `AURA-*` IDs, filesystem slugs/file names, YAML keys and machine-readable values (`approved`, `mvp`, etc.) in English. Glossary canonical terms and ADRs must follow existing repo conventions instead of being translated automatically.

**Source-preserving exception:** `SCOPING-SUMMARY.md` is a faithful copy of the approved summary, retaining its original language and content. Do not translate it without separate approval. Cite the English source using references in French prose when necessary. Review/approval messages to the user are also in French.

## Inputs and modes

- Required: path to an **approved** scoping summary or explicitly user-approved source material.
- Optional: path to an approved catalogue and existing `docs/docs-project/` tree.
- `mode=preview`: **read-only**. Analyze and propose catalogue; do not write final documents.
- `mode=apply`: write/update documents **only after explicit user approval of the proposed catalogue**.
- `mode=audit`: read-only consistency check of an existing tree.

If the input is missing, unapproved, or contradictory, report it instead of inventing approval. Do not run `to-spec` or publish GitHub Issues: this phase produces *product documentation*, not development tasks.

## How to derive the catalogue

1. Read the full approved summary, relevant glossary and ADRs, and current module/feature docs if present.
2. Extract all **explicit** user needs, features, known exclusions, business rules and version choices. Group related features into coherent **functional** Modules (not code packages). Present new module groupings as proposals, not retroactive user decisions.
3. Create stable unique identifiers `AURA-001`, `AURA-002`, ... . Reuse existing identifiers for existing features. Do not change an ID due to renaming or moving a feature.
4. Keep the following two dimensions **separate**:
   - `decision_status`: `approved`, `proposed`, `rejected`, or `unresolved`.
   - `release_bucket`: `mvp`, `future`, or `none`.
   - `future` means retained for possible reconsideration, not promised delivery. `rejected` must never be in `mvp` or `future`; `mvp` requires `approved`.
5. Include a functional goal and observable behavior for each Feature. Provide acceptance criteria **only when supported by approved context**; otherwise label them as *proposed criteria* outside the approved portion. List functional blockers/dependencies and explicit open questions.
6. Trace each feature back to a section of the validated summary. When traceability is missing, label the feature as proposed/unresolved instead of presenting it as validated.
7. Deduplicate overlapping Features, checking that different user outcomes are not incorrectly merged.

### Preview gate

In `mode=preview`, show a concise **French-language** table with module, Feature ID/nom, statut de décision, cible de version, source et dépendances. Show missing coverage, duplicates, contradictory decisions, and a complete proposed file manifest. Request the user's approval **before writing**. If a module decomposition is debatable, present options rather than silently choosing.

## Document tree and format

After approval, produce `docs/docs-project/` using the exact guidance in `references/document-formats.md`:

- `SCOPING-SUMMARY.md` — immutable snapshot or faithful copy of the **approved** functional summary and its approval metadata (source of traceability).
- `PROJECT.md` — concise project overview, users, goals, constraints, functional modules and links.
- `MVP.md` — index of **approved** MVP features, linking to their canonical Feature cards.
- `FUTURE-FEATURES.md` — separate sections for *future possibilities*, *unresolved proposals*, and *rejected/out-of-scope* items (do not suggest rejected = future).
- `modules/<module-slug>/MODULE.md` — domain and feature index.
- `modules/<module-slug>/<feature-slug>.md` — **one canonical record per Feature**, each with stable machine-readable fields and source reference.

Reference the canonical cards instead of repeating requirements in indexes. Create no empty `src/` folder, API design, DB schema, tickets or tech-stack choices. Do not modify unrelated files.

`mode=apply` must be idempotent: update in place, preserve unique IDs and user edits, and report conflicts before overwrite. Never replace approved content with an AI guess.

## Consistency and completeness gate

Audit both content and structure **and confirm that all headings and user-facing text are in French (except the source-preserving `SCOPING-SUMMARY.md`)**:

- Every known feature is included in **exactly one** module and has a single canonical Feature card.
- Every card has a stable ID, a module, decision status, release bucket, objective, behavior, source, and clearly separated open questions.
- `MVP.md` includes **all and only** approved MVP Features.
- `FUTURE-FEATURES.md` retains all other recorded Features in distinct sections, without promoting rejected work.
- Every module and feature is reachable from its index; links resolve.
- No features conflict with the approved summary, glossary, or ADRs.
- No unexplained assumptions, duplicated requirements, missing dependencies, or unreviewed reclassification.

Use the optional deterministic check when Python is available:

`python .agents/skills/structure-project/scripts/validate_docs.py docs/docs-project`

On Windows, `py` may be used instead of `python`. If the script is unavailable (for example because an installer placed the skill elsewhere), locate the installed skill folder and use that script; otherwise perform the structural checklist manually and disclose the limitation. This check does **not** replace human semantic review.

Present the manifest, audit warnings and changes to the caller for **user approval**. Do not commit or push.
