# Aura Forge UX Document Formats — Version-Aware UX/UI Design

This is **agent-facing documentation in English**. The examples below intentionally use **French prose**, because the generated user-facing UX documents must be written in **French**. Stable identifiers, YAML keys/controlled values, file names and paths stay in English.

## Purpose and canonical relationships

The UX output must be readable by people **and** deterministically consumable by a later architecture/planning skill. It is not a GitHub Issue specification and must not pick an implementation stack.

- `FEAT-001`: canonical functional feature ID from `modules/**/<feature>.md` and the approved `versions/<version>/VERSION.md`.
- `FLOW-001`: stable UX flow ID. Its **version-specific approved behavior** is recorded under each `versions/<version>/ux/USER-FLOWS.md`; reuse the ID when a previously defined journey evolves.
- `SCREEN-001`: stable conceptual screen ID. Its **single living canonical card** is `ux/screens/<screen-slug>.md`. Extend its `## Évolutions par version` section; do not delete V1 content to describe V2.
- The **version's** `SCREEN-INVENTORY.md` is the index and machine-readable crosswalk connecting `FEAT-*`, `SCREEN-*`, `FLOW-*`, and the screen card files. It must include **every feature explicitly in this version's approved scope**, including ones without a UI.
- The **version's** `UX-SUMMARY.md` is the approval record: `draft` until the final UX document approval, then `approved`. This status never means software delivery.
- In V2+, retain the old `versions/v1/ux/` docs untouched and reference existing screens without copying their cards.

Identifiers use `FEAT-001`, `FLOW-001`, `SCREEN-001` (minimum three digits). Do not reuse an ID for a different concept or renumber existing IDs. All paths in the tables and cards must resolve relative to their document.

## Output tree

```text
docs/docs-project/
├── ux/
│   ├── DESIGN-GUIDELINES.md                # optional: approved shared rules only
│   └── screens/
│       └── create-project.md               # one canonical card for SCREEN-001
└── versions/
    ├── v1/
    │   ├── VERSION.md                      # existing approved functional scope
    │   └── ux/
    │       ├── UX-SUMMARY.md
    │       ├── USER-FLOWS.md
    │       └── SCREEN-INVENTORY.md
    └── v2/
        └── ux/                             # only when V2 UX is being designed
            ├── UX-SUMMARY.md
            ├── USER-FLOWS.md
            └── SCREEN-INVENTORY.md
```

Do **not** create empty future-version folders or force images/prototypes. Store actual approved wireframe/prototype assets in an agreed location; reference them by a real relative link/URL. Never invent asset paths.

## `versions/<version>/ux/UX-SUMMARY.md` (version UX approval record)

```markdown
---
version: v1
status: draft
scope: versions/v1/VERSION.md
---

# Conception UX/UI — V1

## Objectifs de l'expérience
Permettre à l'utilisateur de créer et retrouver ses projets sans perdre le contexte.

## Source fonctionnelle
[Périmètre validé de V1](../VERSION.md)

## Utilisateurs et tâches prioritaires
<Description des utilisateurs et de leurs objectifs validés>

## Navigation et organisation des informations
<Organisation validée, sans choisir de framework>

## Écrans et parcours
- [Parcours de la version](USER-FLOWS.md)
- [Inventaire des écrans et couverture fonctionnelle](SCREEN-INVENTORY.md)

## Direction visuelle et décisions validées
<Choix validés, ou mention qu'aucune direction visuelle détaillée n'est définie>

## Nouveautés et changements de la version
<Pour V1 : première expérience. Pour V2 : différences UX par rapport à V1>

## Accessibilité et adaptation
<Comportements attendus et décisions actées>

## Questions ouvertes et limites
<Points non bloquants ou points à trancher avant approbation>

## Vérification de couverture
<Résumé de la revue de cohérence et de ses limites>
```

**Metadata:**
- `version`: version directory (e.g. `v1`, `v2`).
- `status`: `draft` or `approved` only; set `approved` solely after **explicit human approval** and a passed audit.
- `scope`: project-root-relative path to the **approved** functional scope for this same version.

## `versions/<version>/ux/USER-FLOWS.md` (one section per flow)

A flow can be shared conceptually by later versions, but its **scenario for each version** lives in the corresponding version file. Every flow has a unique `FLOW-*` heading **within that version**.

```markdown
---
version: v1
---

# Parcours utilisateurs — V1

## FLOW-001 — Créer un projet

**Fonctionnalités :** FEAT-001
**Écrans :** SCREEN-001, SCREEN-002
**Décision :** approved

### Déclencheur
L'utilisateur choisit l'action « Nouveau projet ».

### Objectif et résultat attendu
Créer un projet et accéder à sa vue principale.

### Parcours principal
1. L'utilisateur ouvre l'écran de création.
2. Il saisit les informations demandées.
3. Il confirme et accède au projet créé.

### Variantes et interruptions
<Retour arrière, annulation, reprise, permissions, etc.>

### Erreurs et retours utilisateur
<États visibles pour les données invalides, les erreurs et la confirmation>

### Décisions et questions ouvertes
<Éléments validés ou questions clairement signalées>
```

Controlled `**Décision :**` values: `approved`, `proposed`, `unresolved`. A `proposed`/`unresolved` flow is not planning-ready and must not silently appear as an accepted deliverable. A flow may reference existing baseline feature IDs, but its **new behavior for this version** must stay within the approved scope. If a reused flow changes in V2, document the **V2 delta** in its V2 record. A flow must reference at least one actual screen and feature.

## `ux/screens/<screen-slug>.md` (one canonical living card per conceptual screen)

```markdown
---
id: SCREEN-001
features:
  - FEAT-001
flows:
  - FLOW-001
---

# SCREEN-001 — Création de projet

## Objectif de l'écran
<Pourquoi cet écran existe et dans quel contexte il apparaît>

## Contenu et hiérarchie
<Informations, actions principales et secondaires, éléments prioritaires>

## Interactions et navigation
<Actions, transitions, confirmations, retour en arrière et sorties>

## États et retours
<Normal, vide, chargement, validation, erreur, permissions, succès>

## Accessibilité et adaptation
<Clavier, lisibilité, focus, formats d'écran, selon besoins validés>

## Évolutions par version
### V1
<Comportement et décisions UX approuvés en V1, avec références FEAT/FLOW>

### V2
<Seulement après décision V2 : ce qui change, sans effacer V1>

## Maquettes et prototypes validés
<Aucun si aucune maquette n'a été réalisée ; sinon vrais liens vers les assets et verdicts>

## Questions ouvertes
<Aucune ou liste explicite>
```

`features` and `flows` frontmatter arrays contain the **union of IDs actually referenced by this conceptual screen across versions**; they are not a claim that all those features were implemented in every version. Use simple YAML dash lists as shown, with IDs unquoted. Do not use undocumented alternatives to the field names. Screen ID is globally unique across canonical cards, and the same feature may be linked to multiple screens.

**Important:** Once a version's section is approved, a later iteration must **append/update the new version section**, not silently rewrite the previous one. If V1 documentation requires correcting, present the exact correction and ask for a distinct approval.

## `versions/<version>/ux/SCREEN-INVENTORY.md` (mandatory handoff contract)

The validator expects the **exact section headings and column names** below, but the prose itself remains French. Keep one **row per screen** and **one row per version-scoped feature**. Every `covered` row must provide at least one screen and one flow; use comma-separated IDs, not extra syntax. Use `-` when none.

```markdown
---
version: v1
---

# Inventaire des écrans — V1

## Écrans de la version

| Écran | Rôle | Fiche |
| --- | --- | --- |
| SCREEN-001 | Créer un projet | [Fiche](../../../ux/screens/create-project.md) |
| SCREEN-002 | Accéder au projet créé | [Fiche](../../../ux/screens/project-details.md) |

## Couverture des fonctionnalités

| Fonctionnalité | Écrans | Parcours | Couverture |
| --- | --- | --- | --- |
| FEAT-001 | SCREEN-001, SCREEN-002 | FLOW-001 | covered |
| FEAT-002 | - | - | no_ui |

## Justifications sans interface
- FEAT-002 : <Explication validée montrant pourquoi cette fonctionnalité ne nécessite pas d'interface>

## Écarts et points non résolus
Aucun.
```

Controlled coverage values: `covered`, `no_ui`, `unresolved` (English machine values; all human explanations French).

- `covered`: at least one listed `SCREEN-*` and `FLOW-*`; they must exist, refer back to the feature and be represented in the current version's flow definitions.
- `no_ui`: no screen/flow IDs; an **explicit, user-approved** justification in `## Justifications sans interface` is required. Do not use it merely to bypass a missing design.
- `unresolved`: not ready for planning; it is allowed in draft docs but **blocks final `approved` status**.
- Include any screen used by a current-version flow in `## Écrans de la version`, even if its canonical card was first created for V1.
- An unrelated feature outside the target version can be referenced by shared screens historically, but **must not be added as target-version work**.

## `ux/DESIGN-GUIDELINES.md` (optional)

```markdown
# Principes de conception UX/UI

## Principes d'ergonomie
<Comportements communs validés>

## Navigation partagée
<Conventions de navigation validées>

## Langage et messages
<Terminologie et règles de formulation en français>

## Composants et motifs d'interaction
<Patrons d'interaction observables, sans imposer une technologie>

## Accessibilité et adaptation
<Attentes applicables à tous les écrans>

## Historique des décisions
<Version d'origine et évolutions justifiées>
```

Do not invent visual tokens, colors, fonts, components, or design systems simply to fill this file. Create it only once shared decisions have been explicitly accepted.

## Review and handoff invariants

1. Version scope is approved **before** UX starts. The UX agent cannot broaden it.
2. Review journeys, navigation and screen inventory with the user **before** producing detailed wireframes.
3. Review the selected visual direction/prototype verdict separately.
4. Run `scripts/validate_ux_docs.py` plus a semantic review. The validator checks structure and references, **not actual UX quality**.
5. A `status: approved` UX summary is legal only after explicit approval and when every target-version feature is `covered` or justified `no_ui`, with approved flow decisions.
6. Documentation supplies inputs for **architecture and planning**. The planning skill will decide vertical development slices from functional needs, approved UX and validated architecture; it must **not create one GitHub Issue per screen**.
7. No automatic commit, push, branch creation, GitHub Issue creation or deployment.
