---
name: project-ux
description: "User-started Aura Forge UX/UI design workflow for an approved project version (V1, V2+): roadmap-aware navigation, mandatory local interactive HTML mockups with scratch-to-docs promotion, targeted UX questions, frontend-design/design-critique guidance, planning handoff, and separate Git approvals."
disable-model-invocation: true
---

# Aura Forge — UX/UI Design for a Product Version

This is a **user-invoked orchestration skill**, not an implementation agent. Run it **after** `project-scoping` has approved the functional scope for a specific version. Reuse the workflow for V1, V2, V3, ... and design **only the change needed by that version**, respecting previous approved UX decisions. Communicate with the user **in French** and follow the repository's `AGENTS.md`.

Read `references/document-formats.md` before drafting any final files. Its instructions are English; **all user-facing UX documentation is French**, including headings, interactions, error text and acceptance-oriented behaviors. Machine-readable keys, file names, stable IDs and controlled metadata values remain English. Preserve scoping summaries in their original language; do not change them. **Design the current version with awareness of the product roadmap, not as if its current phase were the entire application.**

## Design skill integration

Use `frontend-design` to build or refine the visual mockups in phase 2, respecting previously approved UI conventions for V2+. Use `design-critique` on the actual visual previews before they are shown to the user, and again only if substantial revisions warrant it. Both are integral practices of the design workflow; do not add installation checks or dependency-management steps. Draw on each skill's instructions directly in Codex when no dedicated invocation tool is available.

Use visual-design guidance without writing production UI code. **A navigable, runnable HTML/CSS/JavaScript gallery is the required primary mockup deliverable for every new or changed user-facing screen**, not images, PDFs, screenshots, Figma exports or static Markdown. Images may supplement the HTML only. A separate experimental prototype for one unresolved question remains optional and requires its own user approval. Critique actual rendered designs rather than prose when possible. The user reviews the visuals, not a stack of Markdown screen cards. Never silently approve design changes on the user's behalf.

## Boundary and inputs

**Required:** an identified target version, an **approved** `<DOCS_ROOT>/versions/<version>/VERSION.md` (or explicitly approved equivalent legacy baseline), and the relevant canonical `modules/**/<feature>.md` cards. **Also read `<DOCS_ROOT>/FUTURE-FEATURES.md` and `PROJECT.md` for roadmap context**, including later product phases and deferred capabilities when documented. Read any existing UX docs and previous version UX decisions. If the functional scope is not approved, **stop and refer back to `project-scoping`**; do not promote proposed functionality. Do not assume a version was delivered merely because its functional scope is approved. When the target version is not clear for an existing project, resolve it before producing version-scoped assets.

**In scope:** user goals and scenarios, journeys, **navigation/information architecture that can accommodate documented future product phases**, screen definitions, interaction behavior, validation and feedback, empty/loading/error/permission states, responsive/accessibility expectations, content hierarchy, UX writing, visual screen mockups collected in a browsable gallery, visual direction and small **optional** interaction prototypes to answer precise questions. For V2+, distinguish *unchanged*, *modified* and *new* screens and flows.

**Out of scope:** **mocking or implementing future-version features or screens**, treating deferred proposals as approved, changing functional requirements without another scoping decision, backend/system architecture, persistence schemas, APIs, framework selection, production implementation, development tickets, GitHub Issues/Projects publication. A prototype is **disposable evaluation material**, never the production deliverable; no requirement to build one for every screen.

## Documentation root and output medium

Before any generation, resolve `DOCS_ROOT` to the **existing** approved functional documentation root, normally `docs/docs-project/` in this workflow or `docs/docs-projet/` if that is the actual path used by the repository. **Never create two parallel documentation trees** because of the spelling difference. If both exist and their authority is unclear, resolve that discrepancy before writing files; do not move functional files without permission. All final mockups must live **inside the chosen `DOCS_ROOT`**, not in `.scratch` or an unrelated `public/` folder.

**The required mockup format is editable HTML/CSS/JS**, operable locally through `index.html` in a browser. No image-only storyboard, set of PNG/JPG mockups, screenshots, SVG-only posters, static design boards, or Markdown descriptions may satisfy the visual approval gate. A standalone gallery should work without a build step, backend, CDN or network connection. Use inline CSS/JS or local asset files. Real interactions may be simulated with local, in-memory data; do not implement production features. If Codex cannot build HTML in the active environment, report the blocker rather than silently replacing the requirement with images.

## Skill reuse and Codex compatibility

- When installed, read and follow Matt Pocock's model-invoked `grilling` instructions for **focused UX questions**, not a second full functional interview. Use `domain-modeling` only if UX terminology/decisions truly require it. Do not alter upstream skill files.
- For a **specific unresolved visual/interaction question**, consider Matt's `prototype` (visual variants or a small interactive logic demo). Read its actual `SKILL.md` before use. **Ordinary non-production HTML mockups are authorized by this UX workflow; a separate exploratory prototype requires user approval before writing prototype code or changing a route.** Its upstream post-prototype branch/commit workflow must not run without separate explicit permissions here. If the user's constraints make the upstream procedure incompatible, use its exploration principles directly instead of claiming the skill was invoked end-to-end.
- Apply `frontend-design` for visual direction and `design-critique` for structured reviews at the specified phases. Follow their applicable guidance without letting it override the scope or human-approval gates of `project-ux`.
- **Do not assume an executable `Skill` tool exists in Codex.** Find the installed skills' `SKILL.md` through available metadata/file tools, read them, then apply their procedures directly when no invocation tool exists. This is normal, not an error. Do not present merely reading instructions as invoking a specialized tool.

## Version-aware work state

Keep a resumable working note at `.scratch/project-ux/<project-slug>/<version>/state.md`, if the project uses scratch workspaces. Record target version, source paths **including the roadmap sources**, previously approved UX baseline, current phase, explicit user approvals, open UX questions, roadmap-related navigation constraints and generated assets. The source HTML gallery and all local assets remain under `.scratch/project-ux/<project-slug>/<version>/preview/` while being reviewed. **After explicit visual approval, copy the approved HTML/CSS/JS and its assets to `<DOCS_ROOT>/versions/<version>/ux/mockups/`**, preserving links and anchors, then generate the Markdown handoff that links to these final files. Do not leave the only usable HTML in scratch or document links that point to scratch. Document the approved result only after visual review. Keep no secrets and do not reset previous version approvals on resume. Read any existing state before restarting.

## Workflow and approval gates

### 0. Establish baseline (read-only)

1. Read the approved version scope and **derive the precise set of `FEAT-*` IDs** from the version's included features and evolutions; do not take the global backlog as a version commitment.
2. Read linked canonical feature cards and their **version-specific** behavior and acceptance criteria. Read approved existing UX docs, screen cards, glossary and any applicable decisions.
3. **Read `FUTURE-FEATURES.md` and the whole-project vision in `PROJECT.md`**. Identify documented future features, future product phases, and likely growth of navigation, without interpreting them as current-version commitments. Treat tentative/unapproved backlog items as *possibilities*, not decisions. If a source is missing, report the limited visibility instead of inventing a roadmap.
4. Present a French baseline: target version, UI-relevant features, existing reusable screens/flows, **upcoming phases/capabilities relevant to navigation**, known constraints and true open questions. Distinguish explicitly **"à concevoir maintenant"** from **"à anticiper, hors périmètre"**. Do not treat delivery as proven unless verified.
5. If a feature appears to require no UI, record a proposed `no_ui` justification, not an unreviewed omission.

### 1. Focused UX discovery (questions only when needed)

Start from the **approved functional scope**, not a blank page. Identify the user's main journeys, navigation, new/modified/reused screens, priority states and known UX constraints. **Evaluate the overall navigation against documented upcoming capabilities**: can the user later move from scoping to UX design, architecture, planning and development (if those phases exist in the project roadmap), rather than being trapped in a "scoping-only" structure? Prefer extensible phase navigation, shared project context, and clear growth points over disposable layouts or screens designed for only one phase. This is navigation planning, **not** design approval or implementation of future phases. Use Matt Pocock's `grilling` discipline **only when a missing answer materially changes a screen or its behavior**; ask dependent questions, avoid a long mandatory interview and do not repeat already-approved functional decisions. A clear baseline may proceed directly to the mockups.

Internally draft stable `FLOW-*` and `SCREEN-*` references and a coverage map for **only** the version's `FEAT-*` IDs. Keep a separate small list of roadmap-informed UX considerations (source, anticipated navigation impact, what is and is not being built now). Reuse conceptual screen and flow IDs for V2+, distinguishing unchanged screens from new or modified ones. Treat any proposed change to business rules as a reason to return to `project-scoping`; do not quietly broaden scope.

**Do not impose an early approval of a Markdown screen inventory or user-flow document.** When a critical UX ambiguity cannot be reasonably visualized, ask a concise question first. Otherwise use explicit labeled assumptions in the draft previews and let the user react to something concrete.

### 2. Produce renderable mockups and run design critique

**Build actual editable HTML/CSS/JS files before requesting broad UX approval. HTML is mandatory, not a fallback or one visual format among others. Images may be included inside HTML but must never be the only screen representation.** Use `frontend-design` for visual direction, information hierarchy and screen layout. Produce concrete, viewable mockups for **every new or materially modified user-facing screen** in the current version. Reuse approved existing screens for unchanged V2+ surfaces rather than redrawing them. Use realistic sample French content, consistent navigation and representative normal/empty/error/confirmation states when they affect the interaction. Keep the scope proportional: **mock up only current-version, approved screens and interactions**; do not create mockups, `FLOW-*`/`SCREEN-*` deliverables, links or acceptance criteria for deferred capabilities. The current mockups should nevertheless demonstrate a navigation structure that remains coherent as documented future phases are added. Do not put clickable future steps, misleading active menus or "coming soon" placeholders into the V1 UI unless their *visibility and behavior* were approved for this version. A scalable layout can accommodate future features without showing them now.

Create a **single navigable HTML gallery grouped by user journey**, not images or a sequence of Markdown files. Make the working entry point `.scratch/project-ux/<project-slug>/<version>/preview/index.html` for **every project, including one with an existing frontend**. The gallery must open directly in a browser (`file://`) without build/server/CDN, using local HTML, CSS and optional JavaScript. Reuse existing visual conventions for V2+ but do not modify production routes for the UX deliverable. Simulate meaningful navigation, key actions, back/next steps and relevant UI states (normal/empty/validation/error/confirmation) with in-memory example data. Maintain a usable screen/journey switcher. Each new or modified screen must have a real HTML element with `id="SCREEN-001"` (adjusting the ID), reachable via an internal `href="#SCREEN-001"` link and consistent with the `FEAT-*`/`FLOW-*` coverage. Do not create image files and call them HTML prototypes via an `img` wrapper: the actual screen layout and interactive controls must be represented with HTML elements. Screenshots can be optional evidence **in addition to** the HTML.

If the user already received image-only mockups, treat them as **unapproved visual references**, not completed HTML UX deliverables. Rebuild the relevant screens in HTML before requesting visual approval; obtain renewed feedback on the HTML version.

Simple screen mockups do not need production functionality, databases, APIs, real user data or exhaustive code. A **separate interactive prototype**, particularly multiple visual variants or a logic/state exploration, is optional and requires user approval before creating prototype code or editing existing routes. For that use Matt Pocock's `prototype` exploration discipline while respecting the project's explicit Git permissions.

Run **`design-critique` against the actual previews** before the user review. Include a **roadmap/extensibility check**: does the navigation remain understandable and adaptable when documented future phases arrive, without confusing users about what works today? Fix clear usability, hierarchy, coherence and accessibility problems; keep open issues visible instead of inventing answers. If you cannot actually render or open the mockups in the current environment, provide the real `index.html` path and instructions for opening it locally, and disclose any preview limitation. **Do not substitute image generation for the required HTML files.**

### 3. Show the mockups to the user and iterate (primary human approval gate)

Present **the working HTML gallery as the primary review surface**, with the local path/URL and instructions for opening it. Give a short French explanation of which user journeys the preview covers, which screens are new/modified/reused, **how the shared navigation anticipates the known later phases without mocking them**, and the few key decisions that need feedback. Clearly mark future roadmap context as *not implemented and not in the mockup scope*. **Do not ask the user to approve each screen's Markdown description or a large table.**

For manageable versions, show the complete gallery before asking for feedback. For many screens, organize review into a small number of coherent journey groups; an approval can cover a group, not each file. Ask for the user's opinion **when the relevant mockups are ready**, not only on abstract documents. Capture modifications, iterate on the visual previews, and reapply `design-critique` when the visual design substantially changes. Record precisely which visual baseline and user journeys were accepted, and any exceptions.

**Approval must explicitly cover the HTML gallery, not earlier image concepts. Visual approval is the UX design decision gate.** No approval is inferred from silence or the mere creation of a mockup. Do not treat each document, screen card, or individual screen as requiring a separate mandatory validation. If the user rejects the mockups, return to the designs and revise, not to a complete functional interview.

### 4. Generate structured UX handoff from the approved visuals

Only after explicit HTML gallery approval, **promote the actual working HTML files and all local assets from `.scratch` to `<DOCS_ROOT>/versions/<version>/ux/mockups/`**, then follow `references/document-formats.md` to write the minimal useful UX documents and preserve links to the **promoted HTML gallery**. Do not regenerate an unrelated lookalike gallery for the final docs; the finalized HTML must match exactly what the user approved. Document assets must be accessible independently of `.scratch`:

```text
<DOCS_ROOT>/
├── ux/
│   ├── DESIGN-GUIDELINES.md             # only when shared decisions were validated
│   └── screens/
│       └── <screen-slug>.md             # one canonical card per conceptual screen
└── versions/
    └── <version>/
        └── ux/
            ├── UX-SUMMARY.md           # version-specific handoff / approval status
            ├── USER-FLOWS.md           # FLOW-* journeys and behavioral cases
            ├── SCREEN-INVENTORY.md     # SCREEN-* and FEAT-* crosswalk
            └── mockups/
                └── index.html          # approved visual gallery for changed/new UI
```

The finalized gallery must include **all of its local CSS, JS, fonts-if-permitted, images and other required assets**, with **no external dependencies**; never copy only `index.html` if it relies on adjacent files. Do not copy abandoned drafts, unapproved variants or unrelated scratch files. Verify that opening the **final** `mockups/index.html` works independently of `.scratch`, that internal screen links/controls function, and that the screen anchors match the approved preview. Do not silently edit the promoted files after approval; if changes alter the visual baseline, return for user review. For a version with **no new or changed UI**, link to already-approved prior-version HTML mockups instead of creating a fake empty gallery. Keep the HTML as versioned design evidence, not production implementation. **Never link final Markdown to `.scratch`**.

**Mandatory planning handoff contract:** every target-version feature (`FEAT-*`) appears in `SCREEN-INVENTORY.md` as `covered`, `no_ui` (user-confirmed justification) or `unresolved`. **Future-only features must not be added to the current-version `SCREEN-INVENTORY.md`, flow definitions or screen cards.** In `UX-SUMMARY.md`, include a clearly separated `## Anticipation des évolutions futures (hors périmètre)` section citing the actual roadmap source(s), UX/navigation implications, and what remains explicitly excluded from this version. For `covered`, map the relevant `SCREEN-*` and `FLOW-*` IDs; flows describe user-visible steps, alternative routes and error cases; canonical screen cards record interactions, feedback, states, accessibility and version-specific changes. Include real links to approved gallery screens and prototypes; do not invent artifact paths. Preserve previous UX version snapshots. A reused screen should not have a duplicated card; any evolution must be marked in that card's new version section.

**These Markdown documents are for continuity, architecture and future issue planning, not the user's primary review UI.** Do not ask the user to read and approve every screen card. The future planning skill will later present **concrete development tickets**, reviewed in manageable groups or individually before their publication to GitHub Issues. It must derive vertical features from functional scope + validated UX + validated architecture, **not one issue per screen**.

### 5. Audit the handoff (no duplicate per-file review gate)

Run:

`python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --version <version>`

or `py` on Windows. Verify unique/stable IDs, approved version feature coverage, references and `no_ui` justifications. The validator checks **document structure**, not human approval or design quality. Independently compare the generated documentation against the approved visual baseline and the approved functional scope, checking HTML `SCREEN-*` anchors, the actual final `index.html` files, working local assets, the absence of links to scratch, error states and French content. **Also verify that the future-looking UX summary is grounded in the actual roadmap, that navigation is extensible, and that no deferred feature leaked into current-version screen coverage, mockups or proposed work.** If documentation contradicts the approved mockups, **correct the documentation**; if resolving a contradiction requires changing the design, return to visual review and get approval again. Keep unapproved or unresolved blocking items `draft`.

When the **final HTML gallery was explicitly approved in scratch, promoted and verified inside DOCS_ROOT**, the documents faithfully match that HTML, and the audit passes, set the UX summary to `status: approved`; rerun the audit. This records approval of the **UX design**, not that the user individually reviewed every Markdown file or that software has been delivered. Give the user a **short French handoff report**: approved preview link, journey groups, feature coverage, meaningful unresolved concerns and file manifest. Do not demand a second exhaustive approval of the generated documents. Show the Git diff for transparency before the separate commit/push authorization gates.

### 6. Git permissions (always separate)

Show `git status` and the relevant diff; identify unrelated pre-existing work. Stage only the approved UX documentation, **promoted HTML/CSS/JS galleries and their local assets**, explicitly approved evidence and any separately approved glossary/ADR changes (never `git add -A`). Suggest `docs(ux): validate <version> UX design`.

1. Ask for **commit permission**, then commit only if expressly authorized; provide the hash.
2. Ask independently for **push permission** and confirm remote/branch, then push only if authorized.
3. If declined, retain local approved documents without performing the declined operation. Do not start architecture or publish Issues automatically.

## Hard invariants

- No implicit approval. The user approves **the browser-viewable HTML mockups**, not image-only concepts or the mere existence of preview files or generated documentation.
- Draft HTML stays in `.scratch`; once accepted, the **exact approved files** move into `<DOCS_ROOT>/versions/<version>/ux/mockups/` and are linked from final UX docs. No scratch paths in delivered documents; no final gallery dependent on scratch or the network.
- **Read the future backlog and project vision for context; anticipate growth of the navigation, not the implementation of future features.** No mockups for future-only screens, no implicit future feature approvals and no fake clickable stages.
- No new functional requirements via UX. Explicitly flag potential scope changes for `project-scoping`.
- Never infer delivery from the version's `status: approved` or from UX approval.
- IDs are stable: `FEAT-*` belongs to functional scope, `FLOW-*` to a user journey, `SCREEN-*` to a conceptual screen; avoid using screen count as ticket count.
- Earlier approved UX and functional version snapshots remain traceable. Changed canonical screens get version-labelled additions instead of overwriting earlier decisions.
- Use `frontend-design` to create **actual interactive HTML mockups** and `design-critique` on those files before human review. Static image output never substitutes for HTML. Their use does not authorize production code or Git operations.
- Planning later combines **functional scope + visually approved UX handoff + validated architecture**. Review proposed work per ticket at the planning stage; do not publish implementation Issues here.
- Never overwrite unrelated files or take Git actions without authorization.
