---
name: project-ux
description: "Design and validate the global MVP UX and progressive deliveries through HTML mockups, a UX contract and separate human approvals."
disable-model-invocation: true
---

# MVP UX/UI and progressive delivery

This is a **user-started workflow**, not a production implementation agent. Run after the MVP or requested functional change is approved with `project-scoping`. Preserve a coherent UX for the **whole MVP**, with progressive delivery subsets when already approved. Talk **in French** and follow `AGENTS.md`. Read `references/document-formats.md` and [shared versioning conventions](../project-scoping/references/versioning.md) before writing; the shared reference owns path, backlog, progress and re-entry rules.

**Core principle:** For scopes with UI, the user reviews **interactive HTML mockups**, not one Markdown document per screen. Preserve these complementary outputs:
1. Validated, browser-viewable HTML/CSS/JavaScript mockups when the scope has UI: the visual reference.
2. A short French `UX-SUMMARY.md`: human-readable design rationale, main journeys/navigation, roadmap awareness, and links.
3. `UX-CONTRACT.json`: the **machine-readable UX handoff** for architecture, issue planning and implementation, with feature/flow/screen/interaction/preview links.

Optionally maintain `ux/DESIGN-GUIDELINES.md` for decisions shared across versions. **Do not generate `USER-FLOWS.md`, `SCREEN-INVENTORY.md`, or per-screen Markdown files by default.** Existing files may be read as previous context; do not delete or duplicate them without reviewing references and user approval. A separate screen/pattern explanation is exceptional, only when a complex decision cannot be captured adequately by the HTML, contract and summary.

## Skills and tool compatibility

- Use `grilling` for **targeted** unanswered UX questions, not a repeat of the functional scoping interview. Use `domain-modeling` only when needed for terminology.
- Use the installed `frontend-design` guidance when building HTML mockups, and `design-critique` to review rendered screens before user review and after substantial visual changes. Assume these are already installed; **do not introduce dependency-installation checks**.
- Matt Pocock's `prototype` can inform narrowly scoped exploratory variants if needed. Its optional branch/commit procedure does **not** grant Git permission in this workflow. Do not run speculative prototype branches/commits automatically.
- Codex may not offer a callable `Skill` tool. Read the installed skills' `SKILL.md` files and apply the guidance directly instead of failing or claiming to have called an unavailable tool.

## Inputs and boundaries

Determine `DOCS_ROOT` by locating the project's **existing authoritative** approved documentation, e.g. `docs/docs-project/` or `docs/docs-projet/`; never create both. Read:
- `PROJECT.md`, `MVP.md` and the canonical backlog for global product context; distinguish existing approved features outside this change from future-only needs.
- The authoritative approved scope (`MVP.md`, an existing `versions/<baseline>/VERSION.md`, or an approved change scope) and linked canonical feature cards. Read release plans only if already approved; no release number is required for global design.
- UX outputs and mockups from earlier versions, when present.

Use backlog entries as navigation context according to their actual status. Distinguish reused, changed and new screens. UX `covered` means designed; record FEAT/FLOW/SCREEN/ACT progress and incremental slices using the shared model.

In scope: journeys, navigation, screen responsibilities, content and visual hierarchy, interaction patterns, error/empty/loading/success states, accessibility, responsive expectations and mockups. Out of scope: backend/API/schema/framework selection, production code, development tickets and GitHub publication. The UX contract specifies **observable behavior**, not implementation design.

### Functional refinements discovered during UX

UX review often reveals a legitimate feature change. **Do not treat the earlier scope as frozen against a new, explicit user decision.** When the user requests a new or changed behavior:

1. Identify affected FEAT, module, canonical MVP/change scope and living indexes. Explain the functional change and scope; clarify only unresolved ambiguity. **Obtain explicit functional approval before recording a change as approved.** Visual approval alone does not approve novel functional behavior.
2. For an **approved refinement to undelivered behavior**, update the affected canonical requirements/acceptance, module, MVP/change scope and relevant indexes **in place**. Keep existing historical headings and stable FEAT IDs; do not invent version sections or release assignments. Only create a FEAT for a separate concept.
3. Integrate the approved behavior into the ordinary canonical sections. Fold any redundant appendix for this same refinement into those sections and remove its duplicate paragraph/link; removing an underlying source file or affecting other references requires reviewed cleanup approval. Explain provenance in the conversation and scoped diff. Preserve the original approved `SCOPING-SUMMARY.md` unless a correction is explicitly approved.
4. Apply shared preservation rules to delivered behavior and slices. Escalate broad unresolved functional scope to `project-scoping`.
5. Update the UX gallery, `UX-CONTRACT.json` and `UX-SUMMARY.md` to match the now-approved functional scope. Reconfirm affected visuals when their design changes. Do not mark a proposal approved until its functional decision and visual review (if applicable) are explicit.

These edits are **regular canonical documentation changes**. The final documents should describe the **current accepted behavior**, not the process by which it was discovered. Do not leave contradictory old text elsewhere in the feature or module.

## Workflow

### 0. Load context and resume

Identify the approved functional scope, existing document baseline and any verified release context. Read MVP, roadmap, prior UX and scratch state. Reuse `.scratch/project-ux/<project-slug>/<scope-id>/` (including existing version-named workspaces). Show MVP-wide journeys and currently approved delivery subsets separately. Never repeat approved discovery or create future-phase dummy routes.

### 1. Resolve UX questions

Ask only questions needed for journeys, information architecture, interaction or visual decisions. Use `grilling` when helpful. Handle any user-requested **functional** changes through the canonical-update process above, before locking the corresponding UX choices. Propose a small set of main journeys/screens, with an overall navigation structure that can accommodate documented later phases.

**No-UI path:** if every scoped feature genuinely has no UI, obtain explicit approval of each `no_ui` justification, skip steps 2–3 and the visual promotion in step 4, then write the summary and contract. Use empty `flows`/`screens`, one `no_ui` coverage record per FEAT with empty screen/flow references, and FEAT-only delivery items. Under the summary's `Maquettes validées` heading explain that no mockup is applicable and link the approved functional source. Create no gallery or placeholder screen. **Done:** all no-UI justifications are approved, the audit passes and both documents can be marked approved. A scope with unchanged existing UI instead reuses its approved HTML; mixed scopes still review their UI normally.

### 2. Build and critique interactive mockups

Build a **real, offline-capable HTML/CSS/JavaScript gallery** under the same scratch scope's `preview/`. Use stable `id="SCREEN-001"` containers and `href="#SCREEN-001"` navigation, meaningful in-memory clicks/forms/states and French copy. Apply `frontend-design`, then `design-critique` on rendered previews.

- **First design:** create the approved scope's screens and journeys.
- **Modification:** inventory the existing gallery, local assets and approved contracts that reference it. Start the preview from a copy of that gallery and its assets; change only approved new/modified behavior. Retain unchanged screen containers, anchors, navigation and assets wherever the same canonical files will be replaced. Reused screens hosted in other approved galleries keep their existing links. Retained context adds no new feature coverage or approval claim.
- **Historical baseline:** when an existing gallery must remain immutable, prepare a distinct scope-specific UX location in the reviewed manifest, with its contract and new gallery together; retain links to the original gallery for reused screens.

**Done:** the complete resulting gallery works offline, all retained references resolve, and the visual critique covers the affected journeys. Screen removals or asset changes affecting an approved reference require an explicit reviewed decision.

### 3. Show the real HTML and get visual feedback

Present the working gallery path/URL and describe covered journeys and how the navigation accommodates known future phases **without implementing them**. Review by **journey group** when there are many screens, not file by file. Iterate until the user explicitly approves the actual HTML. Revisit functional documentation only when a separately approved functional scope change is needed. **Do not ask for mandatory approval of per-screen Markdown documentation.**

### 4. Promote approved visuals and write the handoff

For scopes with new/changed UI, promote the **exact approved complete gallery** and assets only to the reviewed destination. For a new global MVP use `<DOCS_ROOT>/ux/mockups/`; otherwise follow the existing or reviewed scope-specific location from step 2. Before replacement compare the preview with the baseline inventory: every retained screen, anchor, navigation link and local asset must still resolve. Final docs link to canonical HTML. Keep the original gallery when preserving a historical baseline.

Create or update **only**:

```text
<DOCS_ROOT>/
└── ux/                              # or existing versions/<baseline>/ux/, reused in place
    ├── DESIGN-GUIDELINES.md          # optional, shared approved conventions
    ├── UX-SUMMARY.md                 # concise French human-facing synthesis
    ├── UX-CONTRACT.json              # full structured planning handoff
    └── mockups/
        ├── index.html                # approved gallery, if this version changes UI
        └── ...                       # local CSS, JS, assets
```

Put approved observable behavior and FEAT/FLOW/SCREEN/ACT traceability in the JSON contract. Use `references/document-formats.md` for coverage records, delivery fields, schema and compatibility.

Do not generate an issue per screen or invent technical solutions. Later architecture and planning combine the functional scope, this JSON contract, the approved HTML and architecture decisions; the planning skill proposes vertical, testable work items and requests user approval before GitHub Issues publication.

### 5. Validate, report and hand off

Run:

`python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --contract <path-to-UX-CONTRACT.json>`

Legacy `--version <baseline>` and discovery remain supported. Paths passed to `--contract` are relative to the current working directory. When promoting over a shared gallery, also validate every contract identified in the baseline inventory, including contracts outside the current change.

Use `py` on Windows when needed. The script checks JSON shape/references/coverage, feature IDs, local HTML anchors/assets and forbidden scratch paths; it **cannot** decide design quality or confirm user approval. Correct discrepancies. If the JSON contradicts the approved HTML, correct the JSON; if the actual design needs changing, obtain renewed visual approval. Ensure any approved functional changes are integrated directly into canonical functional documents and reflected in the JSON. After passing audit and explicit approval of the applicable visuals or no-UI justifications, set UX summary and contract status to `approved` and rerun validation.

Give the user a short French report: approved preview or no-UI justifications, covered journeys/features, relevant future navigation implications, functional documents updated in place (if any), and genuinely unresolved points. **Do not require them to review the whole contract or a screen-by-screen document stack.** Show the complete relevant Git diff, including any canonical functional edits, for transparency.

### 6. Git actions: separate explicit approvals

Show `git status`, the relevant diff and unrelated changes. Stage **only** the documents, approved HTML and functional edits within scope; never `git add -A`. Ask explicit permission to **commit**, then request **independent push permission** with remote and branch confirmation. Declining either action leaves local files intact. No automatic branch creation, commit, push, architecture stage or GitHub Issue publication.
