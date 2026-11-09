# Aura Forge UX output contract — reference for Codex

Instructions here are **in English**. Generated UX summaries, HTML UI text and JSON human-readable values must be **in French**. Stable IDs, JSON property names, file names and controlled values remain English.

## Design artifacts and their roles

**HTML** is the approved visual/interaction example; it is offline-capable, non-production and navigable. **`UX-CONTRACT.json`** is the structured, implementation-independent UX behavior and traceability source used by later agents. **`UX-SUMMARY.md`** provides a concise overview for the user, without copying each screen's content. **`ux/DESIGN-GUIDELINES.md`** is optional and describes stable shared patterns only when validated. No standard `USER-FLOWS.md`, `SCREEN-INVENTORY.md` or `ux/screens/<screen>.md` is needed. Exceptional complex-pattern notes are permitted when they add genuinely unique context; reference them from the summary.

Use the existing documentation root (`docs/docs-project` or `docs/docs-projet`), never both. An approved preview begins in `.scratch/project-ux/<project>/<version>/preview/` and **the same files** are copied to `<DOCS_ROOT>/versions/<version>/ux/mockups/` after explicit visual approval. No final asset/URL may point to `.scratch`. Local HTML screens have `id="SCREEN-001"` and usable `href="#SCREEN-001"` navigation. A screen may link to the previous version's promoted HTML if unchanged; no duplicate gallery is needed merely for documentation.

## Final file tree

```text
<DOCS_ROOT>/
├── PROJECT.md                             # existing, maintained by functional scoping
├── FUTURE-FEATURES.md                     # existing roadmap
├── modules/<module>/<feature>.md           # canonical functional features
├── ux/
│   └── DESIGN-GUIDELINES.md               # optional
└── versions/<version>/
    ├── VERSION.md                         # approved feature scope
    └── ux/
        ├── UX-SUMMARY.md
        ├── UX-CONTRACT.json
        └── mockups/
            ├── index.html                # only if new/changed UI
            ├── style.css                 # if needed by HTML
            └── app.js                    # if needed by HTML
```

Do not create empty folders or force every HTML file to have external CSS/JS. Keep version history, but avoid per-screen documentation and duplicate data.

## UX-SUMMARY.md — compact user-facing format

```markdown
---
version: v1
status: draft
scope: versions/v1/VERSION.md
---

# Conception UX/UI — V1

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
  "schemaVersion": 1,
  "version": "v1",
  "status": "draft",
  "scope": "versions/v1/VERSION.md",
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
  "futureConsiderations": [
    {
      "source": "FUTURE-FEATURES.md",
      "item": "Phases ultérieures du projet",
      "navigationImplication": "Prévoir une navigation pouvant accueillir les nouvelles phases sans les activer dans cette version"
    }
  ]
}
```

**Required top-level fields:** `schemaVersion` (integer `1`), `version` (`vN`), `status` (`draft` or `approved`), `scope` (`versions/<version>/VERSION.md`), `flows`, `screens`, `featureCoverage`, `futureConsiderations` (arrays, possibly empty when roadmap has no known implication).

**Flow:** `id` (`FLOW-###`), `name` (French), `featureIds`, `screenIds`, `steps` (objects with `screenId`, `action`, `result`), `alternatives` (French strings; may be empty). Flows with UI must reference at least one scoped feature and screen. Keep stable flow IDs across versions when a journey evolves.

**Screen:** `id` (`SCREEN-###`), `name`, `featureIds` and `flowIds` (only current-version relevant connections), `change` (`new`, `modified`, `reused`), `mockup` (relative file path ending in `.html#SCREEN-###`, potentially a **prior version's** approved gallery), `states` (nonempty list of states), `interactions` (objects with unique `ACT-###` IDs, `trigger`, `result`), and `accessibilityNotes` (array, possibly empty). HTML screen elements must have the exact matching `id`. The mockup can be a reused prior-version link such as `../../v1/ux/mockups/index.html#SCREEN-001`. Simulated HTML behavior is illustrative, while this contract records the **approved observable behavior**.

**Coverage:** one entry for **every `FEAT-*` in the target version's `VERSION.md`**, and none for future-only or untouched historic features. Each entry has `featureId`, `coverage` and `screenIds` / `flowIds` arrays. `covered` requires at least one screen and flow and matching reciprocal references; `no_ui` requires empty arrays plus a meaningful **user-approved** `justification`; `unresolved` is allowed only while `draft` and blocks approval. Never use `no_ui` to hide missing design.

**Future considerations:** optional entries with `source` pointing to an **existing** project/roadmap source, `item`, `navigationImplication`. These entries cannot create current-version `FEAT-*`, screens, journeys, Issue scope or clickable future features. They preserve future-aware navigation decisions without mocking future phases.

**JSON is the authoritative UX *data* handoff**, but the validated `VERSION.md` and feature cards remain the functional truth; never overwrite them merely because JSON or prototype code suggests new behavior. The `UX-SUMMARY.md` summarizes instead of duplicating fields, allowing the future architecture/planning skill to use the JSON without re-parsing long Markdown tables.

## Incorporating approved functional refinements discovered during UX

For a **not-yet-delivered version**, update the canonical feature card and its existing version-specific section **in place**, the module description, the version `VERSION.md` and relevant living indexes (only where affected). Example: if the user explicitly approves a general project discussion as part of V1 during UX, the existing V1 project-discussion feature should simply contain that general discussion behavior and its acceptance criteria. Do not insert a paragraph like “Complément V1 acté pendant la revue UX — D17”, “Source complémentaire”, `SCOPING-ADDENDUM.md`, or any narrative provenance inside the feature/module pages. The existing requirements should read as a unified, current specification. Mention the scope refinement in the **conversation and Git diff**, not as an addendum in user documentation. Preserve the original `SCOPING-SUMMARY.md` as the historical first synthesis unless the user explicitly approves editing it.

For an **already delivered version**, keep its functional baseline unchanged; document genuinely new behavior under the next version's normal scope. If it is uncertain whether a change belongs in the current or a later version, ask before finalization. Never invent approval or change a feature ID to disguise a scope change.

## Validation rules

Run `scripts/validate_ux_docs.py <DOCS_ROOT> --version <version>` from the repository root. Validate coverage, IDs and cross-references, file and anchor links, and scratch isolation. HTML cannot be fully behavior-tested by static validation; manually open the final gallery and compare it to the user-approved preview. Review changes to functional docs in the Git diff before asking for separate commit and push permissions. Do not auto-delete legacy Markdown files; when upgrading an existing UX output, propose removal of obsolete files **only after** all references have been updated and the user agrees.
