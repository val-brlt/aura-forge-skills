---
name: project-ux
description: "Design and validate the UX/UI of an approved Aura Forge project version using interactive HTML mockups, roadmap-aware navigation, an approved UX contract for later architecture/planning, and human-controlled functional updates and Git actions."
disable-model-invocation: true
---

# Aura Forge — UX/UI design for one product version

This is a **user-started workflow**, not a production implementation agent. Run after the target version has been functionally scoped with `project-scoping`. Reuse it for V1, V2, V3, etc. Talk to the user **in French** and follow `AGENTS.md`. Read `references/document-formats.md` before writing final files.

**Core principle:** The user reviews **interactive HTML mockups**, not one Markdown document per screen. Preserve three complementary outputs:
1. Validated, browser-viewable HTML/CSS/JavaScript mockups: the visual reference.
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
- `PROJECT.md`, `FUTURE-FEATURES.md` for the **full product vision** and later phases.
- `versions/<version>/VERSION.md` and the linked `modules/**/<feature>.md` for the **approved version scope**.
- UX outputs and mockups from earlier versions, when present.

Treat the future backlog as context for an extensible information architecture, **not** permission to create future screens or implement deferred features. Do not infer delivery from `status: approved`. For V2+, distinguish reused, changed and new screens; do not redesign unchanged interfaces by default.

In scope: journeys, navigation, screen responsibilities, content and visual hierarchy, interaction patterns, error/empty/loading/success states, accessibility, responsive expectations and mockups. Out of scope: backend/API/schema/framework selection, production code, development tickets and GitHub publication. The UX contract specifies **observable behavior**, not implementation design.

### Functional refinements discovered during UX

UX review often reveals a legitimate feature change. **Do not treat the earlier scope as frozen against a new, explicit user decision.** When the user requests a new or changed behavior:

1. Identify the impacted `FEAT-*`, module, target `VERSION.md`, and any `PROJECT.md`, `MVP.md` or `FUTURE-FEATURES.md` indexes. Say briefly in the conversation what functional scope would change and whether it belongs in the current version. Clarify substantive ambiguity with targeted `grilling`; don't restart the entire scoping workflow. **Obtain clear user approval of the functional change before recording it as approved.** A visual gallery approval alone is not sufficient for an ambiguous or novel functional change.
2. For an **approved change to a version that has not been delivered**, **edit the existing canonical functional docs in place**: update the affected feature's normal behavior, its `### V1` (or current-version) requirements/acceptance criteria, the module description where relevant, the current `VERSION.md` scope/index and any affected living project/backlog indexes. Incorporate the new behavior naturally as part of the approved functional definition. Keep the stable `FEAT-*` ID; only add a new feature ID if it truly represents a separate concept.
3. **Do NOT append an “addendum D17”, “complément UX”, “source complémentaire”, or a pointer to `SCOPING-ADDENDUM.md` inside the feature/module/normal scope prose. Do not create a `SCOPING-ADDENDUM.md` just for this.** If a pre-existing feature or module contains such an appendix-style paragraph for the very change being normalized, fold its approved content into the ordinary existing sections and remove that redundant paragraph/link. Do not delete the underlying addendum file or break other references without a separate, reviewed cleanup approval. Do not add a provenance annotation explaining that a requirement came from the UX review. Tell the user what was integrated in the chat, and show the Git diff before commit; Git history provides change provenance. Keep the originally approved `SCOPING-SUMMARY.md` as the original snapshot unless the user explicitly requests and approves a correction to it.
4. If a version is **already delivered**, preserve its approved historical behavior: scope the enhancement to a later version and record it in that later version's normal feature section / `VERSION.md`. Never silently rewrite a delivered V1. If the requested change crosses into a new major version or reopens broad functional scope, refer the unresolved part to `project-scoping` rather than inventing a decision.
5. Update the UX gallery, `UX-CONTRACT.json` and `UX-SUMMARY.md` to match the now-approved functional scope. Reconfirm affected visuals when their design changes. Do not mark a proposal approved until its functional decision and visual review (if applicable) are explicit.

These edits are **regular canonical documentation changes**. The final documents should describe the **current accepted behavior**, not the process by which it was discovered. Do not leave contradictory old text elsewhere in the feature or module.

## Workflow

### 0. Load context and resume

Identify the version and verify approved scope. Read roadmap and previous UX. Keep resumable working notes, decisions and previews in `.scratch/project-ux/<project-slug>/<version>/`. Show which features are in scope and which future capabilities affect navigation design. Do not create future-phase UI or project-level dummy routes.

### 1. Resolve UX questions

Ask only questions needed for journeys, information architecture, interaction or visual decisions. Use `grilling` when helpful. Handle any user-requested **functional** changes through the canonical-update process above, before locking the corresponding UX choices. Propose a small set of main journeys/screens, with an overall navigation structure that can accommodate documented later phases.

### 2. Build and critique interactive mockups

Build a **real, offline-capable HTML/CSS/JavaScript gallery** under `.scratch/project-ux/<project-slug>/<version>/preview/` containing only the new or changed screens in the version. Use HTML screen containers with stable `id="SCREEN-001"` identifiers and navigable `href="#SCREEN-001"` links. Simulate meaningful clicks, forms and states with in-memory data. Use French UI copy. **Images alone, image-backed posters and static Markdown are not an acceptable preview.** Use `frontend-design`, then `design-critique` on the actual previews. The HTML is temporary design evidence, never production code.

### 3. Show the real HTML and get visual feedback

Present the working gallery path/URL and describe covered journeys and how the navigation accommodates known future phases **without implementing them**. Review by **journey group** when there are many screens, not file by file. Iterate until the user explicitly approves the actual HTML. Revisit functional documentation only when a separately approved functional scope change is needed. **Do not ask for mandatory approval of per-screen Markdown documentation.**

### 4. Promote approved visuals and write the handoff

After visual approval, copy the **exact approved** HTML and every local asset from scratch into `<DOCS_ROOT>/versions/<version>/ux/mockups/`. Check that `mockups/index.html` opens **independently of scratch, build tooling and network access** and that screen anchors/navigation work. For a fully reused screen, the contract may link to a previous version's approved HTML; do not duplicate it needlessly. Never link final docs to `.scratch`.

Create or update **only**:

```text
<DOCS_ROOT>/
├── ux/
│   └── DESIGN-GUIDELINES.md           # optional, shared approved conventions
└── versions/<version>/ux/
    ├── UX-SUMMARY.md                 # concise French human-facing synthesis
    ├── UX-CONTRACT.json              # full structured planning handoff
    └── mockups/
        ├── index.html                # approved gallery, if this version changes UI
        └── ...                       # local CSS, JS, assets
```

The contract is the **authoritative machine-readable reference for UX**. It contains: stable `FEAT-*` / `FLOW-*` / `SCREEN-*` references; one coverage record per scoped feature (`covered` or `no_ui`, or `unresolved` in drafts); each journey's steps and screen IDs; screens' approved mockup URL/anchor, states, interactions and relevant accessibility notes; and roadmap implications strictly separated from current scope. Put **observable** behavior in the JSON; don't duplicate the entire contract in Markdown. See the exact schema examples and constraints in `references/document-formats.md`.

Do not generate an issue per screen or invent technical solutions. Later architecture and planning combine the functional scope, this JSON contract, the approved HTML and architecture decisions; the planning skill proposes vertical, testable work items and requests user approval before GitHub Issues publication.

### 5. Validate, report and hand off

Run:

`python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --version <version>`

Use `py` on Windows when needed. The script checks JSON shape/references/coverage, feature IDs, local HTML anchors/assets and forbidden scratch paths; it **cannot** decide design quality or confirm user approval. Correct discrepancies. If the JSON contradicts the approved HTML, correct the JSON; if the actual design needs changing, obtain renewed visual approval. Ensure any approved functional changes are integrated directly into canonical functional documents and reflected in the JSON. After approved visual review and passing audit, set UX summary and contract status to `approved` and rerun validation.

Give the user a short French report: approved preview, covered journeys/features, relevant future navigation implications, functional documents updated in place (if any), and genuinely unresolved points. **Do not require them to review the whole contract or a screen-by-screen document stack.** Show the complete relevant Git diff, including any canonical functional edits, for transparency.

### 6. Git actions: separate explicit approvals

Show `git status`, the relevant diff and unrelated changes. Stage **only** the documents, approved HTML and functional edits within scope; never `git add -A`. Ask explicit permission to **commit**, then request **independent push permission** with remote and branch confirmation. Declining either action leaves local files intact. No automatic branch creation, commit, push, architecture stage or GitHub Issue publication.

## Hard rules

- **Human approval of functional scope changes and actual HTML visuals**; no implicit approvals.
- **No per-screen Markdown by default**; concise French UX summary + approved HTML + complete JSON contract. Optional design guidelines only when useful.
- **No addendum-style prose in canonical functional docs** for same-version refinements; update the real feature/module/version text and mention changes in the conversation/diff instead.
- Do not mutate delivered version history or the original scoping-summary snapshot automatically.
- Roadmap informs navigation, never expands the current version without authorization.
- Stable IDs and explicit FEAT/FLOW/SCREEN linkage for later issue planning; no stack/API assumptions.
- No unapproved Git operations.
