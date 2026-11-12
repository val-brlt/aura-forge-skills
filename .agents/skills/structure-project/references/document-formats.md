# Canonical functional document formats

Read when previewing or applying an approved MVP or functional change. Use [shared scope and delivery conventions](../../project-scoping/references/versioning.md) for scope, progress, partial delivery and release semantics. For an unchanged historical audit only, use [legacy formats](legacy-document-formats.md).

## Language and paths

Write user-facing functional prose and headings in **French**. Keep stable IDs, metadata keys/controlled values, slugs and filenames in English. Preserve approved summaries verbatim in their original language and existing glossary/ADR conventions.

Discover and reuse DOCS_ROOT. A new global MVP has this layout, with no release assignment required:

```text
<DOCS_ROOT>/
├── PROJECT.md
├── MVP.md
├── SCOPING-SUMMARY.md
├── BACKLOG.md
└── modules/
    └── <module-slug>/
        ├── MODULE.md
        └── <feature-slug>.md
```

Include a new change document's path in the reviewed manifest. Resolve canonical paths and backlog compatibility using the shared conventions above.

## PROJECT.md

Describe purpose/users, outcomes and product scope. Link the global MVP, module indexes, active change scopes and canonical backlog. Keep existing legacy scopes, approved release plans and actual release evidence in separate indexes. Link only existing files.

## MVP.md and change scopes

`MVP.md` is the global indispensable scope, not a navigation pointer to a release. Output examples retain the required French labels; angle-bracket placeholders provide instructions in English. IDs are illustrative.

```markdown
---
scope_id: mvp
scope_kind: mvp
status: draft
source: SCOPING-SUMMARY.md
---
# Objectif MVP
## Objectifs et critères de réussite
<Explicitly approved functional criteria>
## Fonctionnalités incluses
- [FEAT-001 — Créer un projet](modules/project-management/create-project.md)
## Dépendances et décisions ouvertes
<FEAT dependencies and unresolved questions>
## Limites et exclusions
<Excluded items linked from the canonical backlog>
## Avancement de l'objectif MVP
<Open milestone; evidence required for each criterion>
## Source de cadrage
[Synthèse validée](SCOPING-SUMMARY.md)
```

A change scope uses `scope_kind: change`, its stable ID and an explicit baseline/delta. List approved new features under `## Fonctionnalités incluses` and approved changes under `## Évolutions des fonctionnalités existantes`, with links to the same canonical cards. Describe the change without duplicating their full criteria. Keep goals, exclusions, dependencies, open questions and summary link. Resolve paths relative to the document's actual location.

`status: draft` means catalogue approval is obtained and final documents await review; `approved` means explicit document approval. Actual delivery is separate. Preserve legacy `status: delivered` as historical metadata without inferring new progress from it.

## Approved summary

Keep the approved snapshot faithfully in its original language. Reuse an existing root or scope-specific summary rather than creating a conflicting copy. The live requirements may evolve through reviewed changes; the original summary remains attributable. A correction to its approved contents requires explicit approval.

## Module index and canonical feature card

`MODULE.md` contains `Objectif`, `Périmètre`, `Fonctionnalités` and `Dépendances et points ouverts`; link every canonical card in that module.

Feature example:

```markdown
---
id: FEAT-001
module: project-management
decision_status: approved
scope: mvp
source: SCOPING-SUMMARY.md
---
# FEAT-001 — Créer un projet
## Objectif utilisateur
<Approved need>
## Comportement attendu
<Current accepted behavior>
## Critères d'acceptation validés
<Explicitly approved criteria>
## Dépendances fonctionnelles
<FEAT-xxx or state in French that none are documented>
## Questions ouvertes
<Unresolved questions or state in French that none are recorded>
## Traçabilité
[Synthèse validée](../../SCOPING-SUMMARY.md)
```

`id` is globally unique (`FEAT-` plus at least three digits). `module` matches the containing directory. `decision_status` is `approved`, `proposed`, `rejected` or `unresolved`; it describes the concept, not every future enhancement. `source` is relative to DOCS_ROOT and points to an existing approved source. Use `scope: mvp` or `future` only when established; a legacy `release_bucket` does not establish membership.

Keep historical headings and label proposed criteria separately. Apply shared preservation and progress rules to refinements and incomplete slices.

## Canonical backlog (`BACKLOG.md` for new projects)

Use the shared backlog definition and compatibility rules. Link every canonical card outside the selected scope under the appropriate French section: `Fonctionnalités approuvées hors du changement`, `Besoins futurs et évolutions différées`, `Propositions et décisions ouvertes`, or `Éléments rejetés`. Empty sections may be omitted.

For each entry give the FEAT link, concise reason for exclusion, actual decision/development/delivery state (unknown where unverified), and original approved scope link when applicable. For example, an existing delivered FEAT omitted from a new search change stays linked to its approved MVP under the first section; it is not reclassified as future work. Reference acceptance criteria in the canonical card instead of copying them.

## Historical scopes and approved release plans

Existing `versions/<legacy-id>/VERSION.md` and summaries retain their paths and approved baseline, without an inferred software release. After actual planning approval, `versions/<X.Y.Z>/VERSION.md` may index changes/slices, acceptance, dependencies, baseline, compatibility and evidence. Keep document approval and actual delivery separate. Historical `release_kind` remains readable; new releases do not use `release_kind: mvp`.
