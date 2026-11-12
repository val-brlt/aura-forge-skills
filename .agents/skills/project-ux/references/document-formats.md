# Aura Forge UX output contract — reference for Codex

Instructions here are **in English**. Generated UX summaries, HTML UI text and JSON human-readable values must be **in French**. Stable IDs, JSON property names, file names and controlled values remain English.

## Design artifacts and their roles

**HTML** is the approved visual/interaction example; it is offline-capable, non-production and navigable. **`UX-CONTRACT.json`** is the structured, implementation-independent UX behavior and traceability source used by later agents. **`UX-SUMMARY.md`** provides a concise overview for the user, without copying each screen's content. **`ux/DESIGN-GUIDELINES.md`** is optional and describes stable shared patterns only when validated. No standard `USER-FLOWS.md`, `SCREEN-INVENTORY.md` or `ux/screens/<screen>.md` is needed. Exceptional complex-pattern notes are permitted when they add genuinely unique context; reference them from the summary.

Read [shared versioning conventions](../../project-scoping/references/versioning.md). Use the existing DOCS_ROOT, never a second tree. Work in `.scratch/project-ux/<project>/<scope-id>/preview/`. After explicit visual approval promote **the same files** to the existing canonical UX directory, or `<DOCS_ROOT>/ux/mockups/` for a new global MVP. Keep approved legacy paths and stable SCREEN anchors/navigation. Reused screens link to approved HTML; release partitioning never requires another gallery or renewed design of unchanged screens. Final files cannot reference scratch.

## Final file tree

```text
<DOCS_ROOT>/
├── PROJECT.md                             # existing, maintained by functional scoping
├── FUTURE-FEATURES.md                     # existing roadmap
├── modules/<module>/<feature>.md           # canonical functional features
├── MVP.md                                 # indispensable global scope, independent of releases
└── ux/                                    # or existing versions/<baseline>/ux/, preserve paths
    ├── DESIGN-GUIDELINES.md               # optional
    ├── UX-SUMMARY.md
    ├── UX-CONTRACT.json
    └── mockups/
        ├── index.html                    # only if new/changed UI
        ├── style.css                     # if needed by HTML
        └── app.js                        # if needed by HTML
```

Do not create empty folders or force every HTML file to have external CSS/JS. Keep version history, but avoid per-screen documentation and duplicate data.

## UX-SUMMARY.md — compact user-facing format

```markdown
---
version: mvp
status: draft
scope: MVP.md
---

# Conception UX/UI — Objectif MVP

## Objectifs et parcours principaux
<Description brève des tâches et parcours retenus, pas de fiche par écran>

## Navigation et décisions de conception
<Organisation globale, raisons des décisions qui ne ressortent pas de la maquette>

## Maquettes validées
[Ouvrir les maquettes HTML](mockups/index.html)

## Anticipation des évolutions futures (hors périmètre)
<Impacts sur la navigation de la vision du produit et des fonctionnalités futures, sans nouveaux écrans maquettés>

## Accessibilité, limites et questions ouvertes
<Conventions et exceptions utiles, ou « Aucun point bloquant »>
```

For a version with **no new/changed UI**, replace the mockup link with a real link to the previous approved version's HTML as appropriate. `status` is `draft` until the **actual HTML** is approved and the structured contract passes validation, then `approved`. Do not claim the software was delivered.

## UX-CONTRACT.json — required machine-readable format

Use the following schema shape. This is an *illustrative* dataset, not a claim that these features are actually in the project. Do not add behaviors or fields that were not validated.

```json
{
  "schemaVersion": 2,
  "version": "mvp",
  "status": "draft",
  "scope": "MVP.md",
  "flows": [
    {
      "id": "FLOW-001",
      "name": "Créer un projet",
      "featureIds": ["FEAT-001"],
      "screenIds": ["SCREEN-001"],
      "steps": [
        {"screenId": "SCREEN-001", "action": "Saisir la description", "result": "Le formulaire est renseigné"}
      ],
      "alternatives": ["En cas de description vide, afficher une erreur de validation"]
    }
  ],
  "screens": [
    {
      "id": "SCREEN-001",
      "name": "Création du projet",
      "featureIds": ["FEAT-001"],
      "flowIds": ["FLOW-001"],
      "change": "new",
      "mockup": "mockups/index.html#SCREEN-001",
      "states": ["initial", "validation-error", "submitting", "success"],
      "interactions": [
        {"id": "ACT-001", "trigger": "Cliquer sur Créer", "result": "Le projet est créé ou une erreur est affichée"}
      ],
      "accessibilityNotes": ["Les erreurs sont annoncées et associées au champ concerné"]
    }
  ],
  "featureCoverage": [
    {"featureId": "FEAT-001", "coverage": "covered", "screenIds": ["SCREEN-001"], "flowIds": ["FLOW-001"]}
  ],
  "delivery": {
    "scope": {"id": "mvp", "kind": "mvp", "path": "MVP.md", "feature_refs": ["FEAT-001"]},
    "items": [
      {"ref": "FEAT-001", "scope": "mvp", "decision_status": "approved", "acceptance_criteria": ["Le projet valide peut être créé"], "planned_versions": [], "development_status": "unknown", "delivery_status": "unknown", "delivered_versions": [], "evidence_refs": []},
      {"ref": "FLOW-001", "scope": "mvp", "decision_status": "approved", "acceptance_criteria": ["Le parcours de création aboutit"], "planned_versions": [], "development_status": "unknown", "delivery_status": "unknown", "delivered_versions": [], "evidence_refs": []},
      {"ref": "SCREEN-001", "scope": "mvp", "decision_status": "approved", "acceptance_criteria": ["Le formulaire présente les états validés"], "planned_versions": [], "development_status": "unknown", "delivery_status": "unknown", "delivered_versions": [], "evidence_refs": []},
      {"ref": "ACT-001", "scope": "mvp", "decision_status": "approved", "acceptance_criteria": ["La création affiche un résultat ou une erreur"], "planned_versions": [], "development_status": "unknown", "delivery_status": "unknown", "delivered_versions": [], "evidence_refs": []}
    ],
    "releases": [], "dependencies": [],
    "milestones": [{"id": "MVP", "kind": "mvp", "criteria": ["Les fonctionnalités indispensables satisfont les critères approuvés"], "status": "open", "evidence_refs": []}],
    "public_contracts": [], "stability_criteria": [], "stability_approval_ref": null
  },
  "futureConsiderations": [
    {
      "source": "FUTURE-FEATURES.md",
      "item": "Phases ultérieures du projet",
      "navigationImplication": "Prévoir une navigation pouvant accueillir les nouvelles phases sans les activer dans cette version"
    }
  ]
}
```

**Required fields:** `schemaVersion` (integer `2` for new contracts, legacy `1` still accepted), `version` (stable documentation baseline ID, not software release), `status` (`draft` / `approved`), `scope` (existing canonical path relative to DOCS_ROOT), `flows`, `screens`, `featureCoverage`, `futureConsiderations` (arrays). New format `2` requires `delivery` using the shared schema. Validate the top-level envelope with [ux-contract.schema.json](ux-contract.schema.json), nested UX behavior with the UX validator and delivery invariants with the shared validator. Keep all old fields; do not rewrite approved data merely to upgrade its format.

**Flow:** `id` (`FLOW-###`), `name` (French), `featureIds`, `screenIds`, `steps` (objects with `screenId`, `action`, `result`), `alternatives` (French strings; may be empty). Flows with UI must reference at least one scoped feature and screen. Keep stable flow IDs across versions when a journey evolves.

**Screen:** `id` (`SCREEN-###`), `name`, `featureIds` and `flowIds` (only approved functional-scope connections), `change` (`new`, `modified`, `reused`), `mockup` (relative `.html#SCREEN-###` path, possibly an older approved gallery), nonempty `states`, interactions with unique `ACT-###` IDs / `trigger` / `result`, and `accessibilityNotes` (possibly empty). Exact matching HTML IDs are required. Reused paths may point to a legacy gallery; new/modified screens point to this contract directory's promoted `mockups/index.html`. Prototype behavior is illustrative; JSON records approved observable behavior.

**Coverage:** one entry for **every FEAT in the canonical functional scope's `Fonctionnalités incluses` / `Évolutions des fonctionnalités existantes` sections**, whether global MVP or an approved change; none for future-only scope. Each entry has `featureId`, `coverage`, `screenIds` and `flowIds`. `covered` requires reciprocal screen/flow references; `no_ui` requires empty arrays and a meaningful **user-approved** justification; `unresolved` is draft-only and blocks approval. Coverage describes design completeness, not development or delivery.

**Delivery:** a progress item per scoped FEAT, FLOW, SCREEN and ACT. `delivery.scope.path` equals `scope`, and `feature_refs` matches functional coverage. Preserve MVP-wide journeys even when only a subset of their steps/interactions is in a release change. Change `item_refs` and slice acceptance criteria identify exactly what ships; remaining item criteria keep full delivery incomplete. UI mockups and `status: approved` never set development/delivery state. Known UX dependency edges and release-slice prerequisites are planning inputs, not a generated plan. Empty release/assignment arrays are valid, including after visual approval.

**Future considerations:** optional entries with `source` pointing to an **existing** project/roadmap source, `item`, `navigationImplication`. These entries cannot create current-version `FEAT-*`, screens, journeys, Issue scope or clickable future features. They preserve future-aware navigation decisions without mocking future phases.

**JSON is the authoritative UX *data* handoff**, but the validated `VERSION.md` and feature cards remain the functional truth; never overwrite them merely because JSON or prototype code suggests new behavior. The `UX-SUMMARY.md` summarizes instead of duplicating fields, allowing the future architecture/planning skill to use the JSON without re-parsing long Markdown tables.

## Incorporating approved functional refinements discovered during UX

For approved **undelivered behavior**, update the canonical feature requirements, module, MVP/change scope and affected living indexes **in place**, preserving attributable delivered baselines. Integrate the behavior naturally into the accepted specification; retain historical headings without inventing new release sections. Show provenance in conversation/diff and preserve the original approved summary. Do not create appendix-style functional addenda.

For an **already delivered version**, keep its functional baseline unchanged; document genuinely new behavior under the next version's normal scope. If it is uncertain whether a change belongs in the current or a later version, ask before finalization. Never invent approval or change a feature ID to disguise a scope change.

## Validation rules

Run `python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --contract <contract-path>` (path relative to working directory). Legacy `--version <baseline>` is supported, including `v1`; SemVer directories are also accepted. With neither option, discover global and legacy contracts. Validate shape, coverage, IDs, dependency/delivery metadata, anchors/assets and scratch isolation. Static checks do not verify user authority, evidence contents, JavaScript behavior or visual quality; open final HTML and compare against the approved preview. Review functional edits in the scoped diff before separate commit/push permissions. Upgrading a document/contract or removing legacy files requires the reviewed migration procedure; never delete them automatically.
