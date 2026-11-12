# UX output contract — reference for Codex

Instructions here are **in English**. Generated UX summaries, HTML UI text and JSON human-readable values must be **in French**. Stable IDs, JSON property names, file names and controlled values remain English.

## Design artifacts and their roles

**HTML** is the approved visual/interaction example; it is offline-capable, non-production and navigable. **`UX-CONTRACT.json`** is the structured, implementation-independent UX behavior and traceability source used by later agents. **`UX-SUMMARY.md`** provides a concise overview for the user, without copying each screen's content. **`ux/DESIGN-GUIDELINES.md`** is optional and describes stable shared patterns only when validated. No standard `USER-FLOWS.md`, `SCREEN-INVENTORY.md` or `ux/screens/<screen>.md` is needed. Exceptional complex-pattern notes are permitted when they add genuinely unique context; reference them from the summary.

Use [shared conventions](../../project-scoping/references/versioning.md) for paths, backlog, progress and re-entry. Step 2 of the UX workflow owns gallery construction and preservation; promote that exact approved result. The paths below describe a new MVP; existing and reviewed scope-specific UX directories take precedence. Final files reference canonical HTML.

## Final file tree

```text
<DOCS_ROOT>/
├── PROJECT.md                             # existing, maintained by functional scoping
├── BACKLOG.md                             # or the existing canonical backlog
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
<Brief description of selected tasks and journeys, without per-screen documents>

## Navigation et décisions de conception
<Overall organization and rationale for decisions not evident from the mockup>

## Maquettes validées
[Ouvrir les maquettes HTML](mockups/index.html)

## Anticipation des évolutions futures (hors périmètre)
<Navigation implications of the product vision and future features, without new mockup screens>

## Accessibilité, limites et questions ouvertes
<Useful conventions and exceptions, or state in French that no blockers remain>
```

For a scope with **unchanged UI**, replace the mockup link with a real link to the existing approved HTML. For an **entirely no-UI scope**, retain `Maquettes validées` and explain that no mockup applies, linking the approved functional source and summarizing each user-approved `no_ui` justification; create no HTML or mockup folder. Its contract has empty `flows`/`screens`, one justified `no_ui` coverage record per scoped feature and only the corresponding FEAT delivery items. `status` stays `draft` until the applicable visuals or no-UI justifications are explicitly approved and validation passes, then becomes `approved`. Neither approval proves software delivery.

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
      "source": "BACKLOG.md",
      "item": "Phases ultérieures du projet",
      "navigationImplication": "Prévoir une navigation pouvant accueillir les nouvelles phases sans les activer dans cette version"
    }
  ]
}
```

**Required fields:** `schemaVersion` (integer `2` for new contracts, legacy `1` still accepted), `version` (stable documentation baseline ID, not software release), `status` (`draft` / `approved`), `scope` (existing canonical path relative to DOCS_ROOT), `flows`, `screens`, `featureCoverage`, `futureConsiderations` (arrays). New format `2` requires `delivery` using the shared schema. Validate the top-level envelope with [ux-contract.schema.json](ux-contract.schema.json), nested UX behavior with the UX validator and delivery invariants with the shared validator. Keep all old fields; do not rewrite approved data merely to upgrade its format.

**Flow:** `id` (`FLOW-###`), `name` (French), `featureIds`, `screenIds`, `steps` (objects with `screenId`, `action`, `result`), `alternatives` (French strings; may be empty). Flows with UI must reference at least one scoped feature and screen. Keep stable flow IDs across versions when a journey evolves.

**Screen:** `id` (`SCREEN-###`), `name`, `featureIds` and `flowIds` (only approved functional-scope connections), `change` (`new`, `modified`, `reused`), `mockup` (relative `.html#SCREEN-###` path, possibly an older approved gallery), nonempty `states`, interactions with unique `ACT-###` IDs / `trigger` / `result`, and `accessibilityNotes` (possibly empty). Exact matching HTML IDs are required. Reused paths may point to an existing approved gallery, including retained containers in the current gallery. New/modified screens point to this contract directory's promoted `mockups/index.html`, built with the workflow's preservation procedure. Prototype behavior is illustrative; JSON records approved observable behavior.

**Coverage:** one entry for **every FEAT in the canonical functional scope's `Fonctionnalités incluses` / `Évolutions des fonctionnalités existantes` sections**, whether global MVP or an approved change; none for future-only scope. Each entry has `featureId`, `coverage`, `screenIds` and `flowIds`. `covered` requires reciprocal screen/flow references; `no_ui` requires empty arrays and a meaningful **user-approved** justification; `unresolved` is draft-only and blocks approval. Coverage describes design completeness, not development or delivery.

**Delivery:** a progress item per scoped FEAT, FLOW, SCREEN and ACT. `delivery.scope.path` equals `scope`, and `feature_refs` matches functional coverage. Preserve MVP-wide journeys even when only a subset of their steps/interactions is in a release change. Change `item_refs` and slice acceptance criteria identify exactly what ships; remaining item criteria keep full delivery incomplete. UI mockups and `status: approved` never set development/delivery state. Known UX dependency edges and release-slice prerequisites are planning inputs, not a generated plan. Empty release/assignment arrays are valid, including after visual approval.

**Future considerations:** optional entries with `source` pointing to an **existing** project/roadmap source, `item`, `navigationImplication`. Choose only future/deferred needs for these entries; the backlog can also contain already-approved features outside this change. These entries cannot create current-version `FEAT-*`, screens, journeys, Issue scope or clickable future features. They preserve future-aware navigation decisions without mocking future phases.

**JSON is the authoritative UX *data* handoff**, but the approved MVP/change scope and feature cards remain the functional truth; never overwrite them merely because JSON or prototype code suggests new behavior. The `UX-SUMMARY.md` summarizes instead of duplicating fields, allowing the future architecture/planning skill to use the JSON without re-parsing long Markdown tables.

## Functional refinements

Use the functional-refinement procedure in [the UX workflow](../SKILL.md) when a user decision changes behavior during design; it owns canonical updates and the corresponding approvals.

## Validation rules

Run `python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --contract <contract-path>` (path relative to working directory). Legacy `--version <baseline>` is supported, including `v1`; SemVer directories are also accepted. With neither option, discover global and legacy contracts. Validate shape, coverage, IDs, dependency/delivery metadata, anchors/assets and scratch isolation. Static checks do not verify user authority, evidence contents, JavaScript behavior or visual quality; for UI scopes open final HTML and compare against the approved preview. For an entirely no-UI scope manually verify each justification and its explicit approval instead. Review functional edits in the scoped diff before separate commit/push permissions. Changes to approved documents/contracts or removal of historical files require an explicit reviewed diff and user approval.
