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
├── FUTURE-FEATURES.md
└── modules/
    └── <module-slug>/
        ├── MODULE.md
        └── <feature-slug>.md
```

For an evolution reuse the existing approved scope and source paths. A new change document's path belongs in the reviewed manifest. Preserve existing historical scopes, summaries and delivered baselines; migration of approved paths/content follows the [reviewed migration procedure](../../project-scoping/references/migration.md).

## PROJECT.md

Describe purpose/users, outcomes and product scope. Link the global MVP, module indexes, active change scopes and future backlog. Keep existing legacy scopes, approved release plans and actual release evidence in separate indexes. Link only existing files.

## MVP.md and change scopes

`MVP.md` is the global indispensable scope, not a navigation pointer to a release. Example output (illustrative IDs):

```markdown
---
scope_id: mvp
scope_kind: mvp
status: draft
source: SCOPING-SUMMARY.md
---
# Objectif MVP
## Objectifs et critères de réussite
<Critères fonctionnels explicitement approuvés>
## Fonctionnalités incluses
- [FEAT-001 — Créer un projet](modules/project-management/create-project.md)
## Dépendances et décisions ouvertes
<Dépendances FEAT et questions non résolues>
## Limites et exclusions
<Fonctionnalités futures dans FUTURE-FEATURES.md>
## Avancement de l'objectif MVP
<Jalon ouvert ; preuves requises pour chaque critère>
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
<Besoin approuvé>
## Comportement attendu
<Comportement actuel accepté>
## Critères d'acceptation validés
<Critères explicitement approuvés>
## Dépendances fonctionnelles
<FEAT-xxx ou « Aucune documentée »>
## Questions ouvertes
<Points non tranchés ou « Aucune consignée »>
## Traçabilité
[Synthèse validée](../../SCOPING-SUMMARY.md)
```

`id` is globally unique (`FEAT-` plus at least three digits). `module` matches the containing directory. `decision_status` is `approved`, `proposed`, `rejected` or `unresolved`; it describes the concept, not every future enhancement. `source` is relative to DOCS_ROOT and points to an existing approved source. Use `scope: mvp` or `future` only when established; a legacy `release_bucket` does not establish membership.

Integrate approved undelivered refinements into ordinary sections with a reviewed diff. Preserve existing historical headings and attributable delivered requirements; a new requirement needs no invented version heading. Label proposed criteria separately. Record planning, development and actual delivery independently, using unknown when unverified; incomplete slices retain their remaining criteria.

## FUTURE-FEATURES.md

Separate deferred enhancements, approved future concepts without a schedule, proposals/unresolved decisions and rejected items. A pending enhancement may reuse an existing FEAT; name the pending change instead of relabeling the whole shipped feature. Link catalogue cards outside the selected scope from the appropriate backlog section.

## Historical scopes and approved release plans

Existing `versions/<legacy-id>/VERSION.md` and summaries retain their paths and approved baseline, without an inferred software release. After actual planning approval, `versions/<X.Y.Z>/VERSION.md` may index changes/slices, acceptance, dependencies, baseline, compatibility and evidence. Keep document approval and actual delivery separate. Historical `release_kind` remains readable; new releases do not use `release_kind: mvp`.
