# Aura Forge Document Formats — Version-Aware Functional Scoping

This file is **agent-facing reference material**. Its instructions are in English, while the Markdown examples intentionally show the **French output** expected in project-facing documents.

## Non-negotiable conventions

- Write every **user-facing functional document in French**, including headings, descriptions, version changes, business rules, and acceptance criteria. The sole exception is the **approved scoping summary**, which must be preserved faithfully in its original language. Keep YAML metadata keys, machine-readable values, slugs, file names, and `FEAT-*` identifiers in English.
- Maintain **one canonical feature card per feature** under `modules/`, even when the feature evolves in V2 or later. Version-specific sections must never retroactively overwrite requirements approved for previous versions.
- Maintain **one scope record per version** at `versions/<version>/VERSION.md`. It links to canonical feature cards instead of duplicating their content. A version is considered delivered only when delivery is explicitly confirmed.
- Treat `PROJECT.md`, `FUTURE-FEATURES.md`, and canonical feature cards as living documents. Treat previously approved version scopes and scoping summaries as historical records. Any correction to approved historical records requires separate explicit authorization.
- Do not introduce technical specifications, implementation tickets, code, API schemas, or architecture during functional scoping.

## Reference document tree

```text
docs/docs-project/
├── PROJECT.md
├── MVP.md                         # optional pointer to the V1 scope
├── FUTURE-FEATURES.md
├── versions/
│   ├── v1/
│   │   ├── VERSION.md
│   │   └── SCOPING-SUMMARY.md       # unchanged, in the source language
│   └── v2/                         # create only when V2 is scoped
│       ├── VERSION.md
│       └── SCOPING-SUMMARY.md
└── modules/
    └── project-management/
        ├── MODULE.md
        └── create-project.md        # same canonical feature in V1 and V2
```

## `PROJECT.md` (living document)

**Example output in French:**

```markdown
# Présentation du projet — <nom>

## Objectif et utilisateurs
## Problèmes rencontrés et résultats attendus
## Périmètre fonctionnel
## Modules
- [<Nom français>](modules/<slug>/MODULE.md)
## Versions
- [V1 — MVP](versions/v1/VERSION.md) : <objectif en français>
- [V2](versions/v2/VERSION.md) : <objectif en français>  <!-- seulement si elle existe -->
## Évolutions futures et points à clarifier
Voir [le backlog](FUTURE-FEATURES.md).
## Décisions encore ouvertes
```

## `versions/<version>/SCOPING-SUMMARY.md`

Copy the **approved summary for this version faithfully**, preserving its original language and content. During an explicitly approved migration, avoid creating an unnecessary duplicate when an existing approved root-level summary is retained and linked. Never relabel an unapproved draft as approved.

## `versions/<version>/VERSION.md` (version scope snapshot)

**Example output in French:**

```markdown
---
version: v1
release_kind: mvp
status: draft
---

# Version V1 — MVP

## Objectif de la version
<Le bénéfice utilisateur qui motive cette version>

## Référence précédente
Première version du produit.

## Fonctionnalités incluses
- [FEAT-001 — Créer un projet](../../modules/project-management/create-project.md)

## Évolutions des fonctionnalités existantes
Aucune pour la première version.

## Limites et fonctionnalités reportées
<Limites expressément décidées>

## Dépendances et décisions ouvertes
<Questions fonctionnelles seulement>

## Source de cadrage
[Synthèse validée pour V1](SCOPING-SUMMARY.md)
```

For V2 and subsequent versions, update `version` (for example, `v2`), set `release_kind: standard` unless explicitly decided otherwise, and adapt the title, baseline, and change sections. Under **Fonctionnalités incluses**, list only new features and existing features with **changes actually included** in the target version. Under **Évolutions des fonctionnalités existantes**, summarize **what changes** without repeating the full acceptance criteria from the canonical feature card. Mention unchanged V1 capabilities only where useful; do not duplicate the full V1 feature list.

Allowed `status` values:

- `draft`: the feature catalogue has been approved, but the final version documentation has **not yet** been approved.
- `approved`: the user explicitly approved the version documentation and scope.
- `delivered`: delivery has been **explicitly confirmed** by the user or reliable evidence; never infer this from a completed scoping workflow.

After the documentation review, the orchestrator may change `draft` to `approved` based on explicit user approval, and must include the change in the diff presented before commit. Do not mark a version `delivered` as part of this action.

## `modules/<module>/MODULE.md`

**Example output in French:**

```markdown
# Module — <nom en français>

## Objectif
## Périmètre
## Fonctionnalités
- [FEAT-001 — Créer un projet](create-project.md)
## Dépendances et points ouverts
```

## `modules/<module>/<feature>.md` (canonical, living document)

**Example output in French:**

```markdown
---
id: FEAT-001
module: project-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-001 — Créer un projet

## Objectif utilisateur
<Besoin en français>

## Comportement attendu
<Description fonctionnelle actuelle, en français, sans effacer l'historique>

## Historique fonctionnel par version
### V1
**Comportement validé :** <périmètre V1>
**Critères d'acceptation validés :** <uniquement les éléments approuvés>
**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md)

### V2
**Évolution validée :** <nouveau besoin approuvé en V2>
**Critères d'acceptation validés :** <les critères V2, sans réécrire ceux de V1>
**Source :** [Synthèse V2](../../versions/v2/SCOPING-SUMMARY.md)

## Critères d'acceptation proposés
<Propositions clairement identifiées, ou « Aucun »>

## Dépendances fonctionnelles
<FEAT-xxx ou « Aucune documentée »>

## Questions ouvertes
<Points non tranchés ou « Aucune consignée »>

## Traçabilité
<Origine initiale de la fonctionnalité et décisions d'évolution>
```

**Metadata rules:**

- `id`: stable and globally unique, format `FEAT-001` (at least three digits).
- `module`: slug matching the containing module directory.
- `decision_status`: one of `approved`, `proposed`, `rejected`, `unresolved`. Describes the feature concept decision, **not** whether every proposed future enhancement has been approved.
- `source`: path relative to `docs/docs-project/` that points to the approved source document.
- **No global `release_bucket: mvp`:** version membership is defined by the corresponding `VERSION.md`. A feature may be referenced in both V1 and V2 when V2 enhances it, without creating duplicate feature cards.

Preserve earlier approved version-specific requirements when a later version changes the feature. Record the new decision as an explicitly labelled **version delta**.

## `FUTURE-FEATURES.md` (living backlog)

**Example output in French:**

```markdown
# Évolutions futures et autres propositions

## Évolutions futures envisagées (sans engagement)
- [FEAT-003 — ...](modules/<module>/<feature>.md) : <changement différé>

## Fonctionnalités approuvées sans version prévue
- [FEAT-004 — ...](modules/<module>/<feature>.md)

## Propositions et points non résolus
- [FEAT-005 — ...](modules/<module>/<feature>.md)

## Fonctionnalités refusées ou hors périmètre
- [FEAT-006 — ...](modules/<module>/<feature>.md)
```

A fully delivered feature does **not** need to appear in the backlog. However, an enhancement to an already delivered feature may remain in the backlog when the **pending change** is explicitly identified. Every feature absent from all version scopes should appear in the backlog, including rejected proposals when they are kept in the catalogue.

## `MVP.md` (optional)

This is only a **historical navigation pointer** for readers familiar with the older layout, never a second feature catalogue.

**Example output in French:**

```markdown
# MVP de la V1

Le périmètre validé du MVP est consultable dans [la fiche de la version V1](versions/v1/VERSION.md).
```

Do not generate a new `MVP.md` for V2. Never overwrite an existing legacy `MVP.md` without explicit approval.

## Migration from earlier skill outputs

If root-level `SCOPING-SUMMARY.md` and `MVP.md` already exist, or feature cards still contain `release_bucket: mvp`, **propose a migration diff instead of applying it automatically**. Derive `versions/v1/VERSION.md` only from the approved V1 MVP scope, preserve existing feature IDs, and link to the original scoping summary without rewriting it if it must remain at the root. Never renumber features or alter V1 scope to accommodate V2. Obtain explicit user approval before making migration changes.
