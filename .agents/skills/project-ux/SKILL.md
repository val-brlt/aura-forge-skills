---
name: project-ux
description: "User-started Aura Forge UX/UI design workflow for an approved project version (V1, V2+): user flows, navigation, screen inventory, visual direction and mandatory design critique using installed frontend-design and design-critique skills, traceable UX documentation and separate Git approvals."
disable-model-invocation: true
---

# Aura Forge — UX/UI Design for a Product Version

This is a **user-invoked orchestration skill**, not an implementation agent. Run it **after** `project-scoping` has approved the functional scope for a specific version. Reuse the workflow for V1, V2, V3, ... and design **only the change needed by that version**, respecting previous approved UX decisions. Communicate with the user **in French** and follow the repository's `AGENTS.md`.

Read `references/document-formats.md` before drafting any final files. Its instructions are English; **all user-facing UX documentation is French**, including headings, interactions, error text and acceptance-oriented behaviors. Machine-readable keys, file names, stable IDs and controlled metadata values remain English. Preserve scoping summaries in their original language; do not change them.

## Required third-party skills (preflight)

`frontend-design` (from `anthropics/skills`) and `design-critique` (from `anthropics/knowledge-work-plugins`) are **mandatory project dependencies** of this workflow. They are expected to be installed before `project-ux` is started. At the beginning of the session, locate and read **both** installed `SKILL.md` files, using the project-local `.agents/skills/` paths (or other Codex-recognized skill locations if the project uses symlinks). Do not rely on either upstream skill being silently available from a different harness.

- If either dependency cannot be found or read, **stop before the UX interview**, identify the missing skill and give the user its Codex installation command from `INSTALLATION.md` or the commands below. Never silently install, copy, or substitute a different skill, and never claim that the missing skill was used.
- `frontend-design` is **required in phase 2** to help develop or critically challenge a specific, deliberate visual direction for the approved journeys and relevant screens, including V2+ consistency with approved existing UI. **Do not turn this into mandatory production UI code:** adapt the skill's visual-design guidance to the current UX artifacts and make prototype code only under the separate prototype gate.
- `design-critique` is **required in phase 2 and phase 4**: review the proposed wireframes/design directions before gate B and audit the approved UX artifacts before gate C. Use actual evidence (wireframe, screenshot, prototype, or sufficiently detailed documented design) and project context. Report severity and concrete improvements. Do not claim measured accessibility conformance when it has not been measured.
- Resolve and record the critique's important findings before the corresponding approval gate, or explicitly mark accepted residual limitations. Do not silently approve the agent's own suggested fixes on the user's behalf.

Project-local installation commands (run manually from the repo root):

```bash
npx skills add anthropics/skills --skill frontend-design -a codex
npx skills add anthropics/knowledge-work-plugins --skill design-critique -a codex
```

## Boundary and inputs

**Required:** an identified target version, an **approved** `docs/docs-project/versions/<version>/VERSION.md` (or explicitly approved equivalent legacy baseline), and the relevant canonical `modules/**/<feature>.md` cards. Read `PROJECT.md`, any existing UX docs, and previous version UX decisions. If the functional scope is not approved, **stop and refer back to `project-scoping`**; do not promote proposed functionality. Do not assume a version was delivered merely because its functional scope is approved. When the target version is not clear for an existing project, resolve it before producing version-scoped assets.

**In scope:** user goals and scenarios, journeys, navigation/information architecture (UI sense), screen definitions, interaction behavior, validation and feedback, empty/loading/error/permission states, responsive/accessibility expectations, content hierarchy, UX writing, wireframes, visual direction and small **optional** prototypes to answer precise questions. For V2+, distinguish *unchanged*, *modified* and *new* screens and flows.

**Out of scope:** changing functional requirements without another scoping decision, backend/system architecture, persistence schemas, APIs, framework selection, production implementation, development tickets, GitHub Issues/Projects publication. A prototype is **disposable evaluation material**, never the production deliverable; no requirement to build one for every screen.

## Skill reuse and Codex compatibility

- When installed, read and follow Matt Pocock's model-invoked `grilling` instructions for **focused UX questions**, not a second full functional interview. Use `domain-modeling` only if UX terminology/decisions truly require it. Do not alter upstream skill files.
- For a **specific unresolved visual/interaction question**, consider Matt's `prototype` (visual variants or a small interactive logic demo). Read its actual `SKILL.md` before use. Prefer simple wireframes first, and obtain user approval **before writing prototype code or changing a route**. Its upstream post-prototype branch/commit workflow must not run without separate explicit permissions here. If the user's constraints make the upstream procedure incompatible, use its exploration principles directly instead of claiming the skill was invoked end-to-end.
- Anthropic's `frontend-design` and `design-critique` are **required**, not conditional helpers. Follow the preflight rule above; use `frontend-design` for visual direction and `design-critique` for structured reviews at the specified phases. Respect any source skill guidance that applies without letting it override the scope or human-approval gates of `project-ux`. Never install third-party skills silently.
- **Do not assume an executable `Skill` tool exists in Codex.** Find the installed skills' `SKILL.md` through available metadata/file tools, read them, then apply their procedures directly when no invocation tool exists. This is normal, not an error. Do not present merely reading instructions as invoking a specialized tool.

## Version-aware work state

Keep a resumable working note at `.scratch/project-ux/<project-slug>/<version>/state.md`, if the project uses scratch workspaces. Record target version, source paths, previously approved UX baseline, current phase, explicit user approvals, open UX questions and generated assets. Drafts and experiments stay out of approved canonical files until their respective gates have passed. Keep no secrets and do not reset previous version approvals on resume. Read any existing state before restarting.

## Workflow and approval gates

### 0. Establish baseline (read-only)

1. Read the approved version scope and **derive the precise set of `FEAT-*` IDs** from the version's included features and evolutions; do not take the global backlog as a version commitment.
2. Read linked canonical feature cards and their **version-specific** behavior and acceptance criteria. Read approved existing UX docs, screen cards, glossary and any applicable decisions.
3. Present a French baseline: target version, UI-relevant features, existing reusable screens/flows, known constraints and true open questions. Do not treat delivery as proven unless verified.
4. If a feature appears to require no UI, record a proposed `no_ui` justification, not an unreviewed omission.

### 1. Targeted UX interview and journey design (gate A)

Ask **dependent, precise UX questions**: user context, entry points, navigation, most important tasks, alternate/error paths, information order, key content and accessibility/responsiveness expectations. Reuse accepted answers, and challenge conflicts with approved business rules. Record proposed UX decisions and identify cases requiring a visual experiment. No fixed questionnaire.

Propose, **in French**, the user journeys (`FLOW-*`), screen inventory (`SCREEN-*`), screen-to-feature coverage and navigation map. Reuse stable IDs for the **same conceptual screen/flow** across versions; allocate a new ID only for a genuinely new one, never renumber previous IDs. Compare V2+ changes with the existing UX baseline. Mark unknowns `unresolved`; do not invent resolutions. **Request explicit approval of journeys, navigation and screen inventory before proceeding.** If rejected, revise this proposal, not the functional scope silently.

### 2. Wireframes, visual exploration and evaluation (gate B)

For the approved journeys, make **lightweight wireframes** for screens where a visual representation meaningfully helps; document simple screens without unnecessary images or prototypes. Explain hierarchy, interaction and states. **Apply `frontend-design`** to propose or validate a deliberate, project-specific visual direction; for V2+, first respect existing approved patterns and focus on changes. Even when no detailed mockup is needed, explicitly review and record whether the existing visual direction remains suitable. For an uncertain layout/behavior, and only with user approval, create **small disposable prototypes** with 2–3 structurally distinct variants when useful. Do not convert prototype output into production implementation.

**Apply `design-critique`** to the proposed wireframes/directions, informed by the source functional goals and concrete design evidence. Present strengths, usability/hierarchy/consistency/accessibility issues and prioritized changes; iterate on significant findings **before requesting gate B approval**. When no rendered mockup exists, critique the available structured wireframe or sufficiently detailed screen description and **state the evidence limitations**.

Obtain **explicit approval** of the chosen interface direction, relevant wireframes and any experimental verdicts, after the critique. Record what was approved and why, including any consciously accepted caveats. Keep unchosen alternatives out of canonical docs; link approved evidence or explicitly note that no mockup was created. **No autonomous branch, commit, push, server deployment or production code changes.**

### 3. Produce traceable documents (draft)

Follow `references/document-formats.md`. For each approved target version, create or update only necessary files:

```text
docs/docs-project/
├── ux/
│   ├── DESIGN-GUIDELINES.md             # if shared visual/interaction rules were validated
│   └── screens/
│       └── <screen-slug>.md             # one canonical card per conceptual screen
└── versions/
    └── <version>/
        └── ux/
            ├── UX-SUMMARY.md           # version-specific summary / approval state
            ├── USER-FLOWS.md           # FLOW-* scenarios for this version
            └── SCREEN-INVENTORY.md     # SCREEN-* links + FEAT-* coverage table
```

**Planning handoff contract (mandatory):** every target-version feature (`FEAT-*`) is represented in `SCREEN-INVENTORY.md` with either `covered`, `no_ui` (explicitly justified) or `unresolved`. For `covered`, link actual `SCREEN-*` and `FLOW-*` IDs and the canonical screen file. Flow definitions describe trigger, user-visible steps, alternatives and error cases, and reference `FEAT-*` / `SCREEN-*`. Screen cards describe interactions, navigation, states, feedback, accessibility/responsive behavior and **version-labelled changes**. Include links to only genuinely existing, user-reviewed wireframes/prototypes. The docs should enable later architecture and planning without deciding their tasks or technologies.

Keep living screen cards under `ux/screens/`, preserving earlier version sections; historical `versions/<old>/ux/` snapshots are **not silently rewritten**. For V2+, an existing screen can be reused unchanged in the new version inventory without copying its card. If behavior evolves, append a clearly labeled V2 section after approval. Never silently migrate old UX docs; propose a reviewable mapping/diff first.

### 4. Cross-document audit and planning-readiness review (gate C)

Run:

`python .agents/skills/project-ux/scripts/validate_ux_docs.py docs/docs-project --version <version>`

or `py` on Windows, using the resolved installed path if needed. The validator checks required files, unique/stable IDs, scope coverage, screen/flow references and metadata consistency; **it cannot judge UX quality or whether decisions are truly approved**. **Apply the installed `design-critique` skill again** to the documented approved UX designs, including version changes and any actual mockups/prototypes, to assess usability, hierarchy, consistency and accessibility. Also independently check edge cases, French copy and whether current-version scenarios are implementable without inventing product behavior. Record the review's evidence, findings and resolution/accepted limitations in the final handoff; do not fabricate measured contrast or a compliance certification. Report **blocking** gaps separately from nonblocking recommendations.

If the UX scope is incomplete, keep `UX-SUMMARY.md` as `status: draft`, document unresolved items and do not call the phase complete. Show the file manifest, source references, prototype links and diff. Ask for **explicit final documentation approval**. After approval, update `UX-SUMMARY.md` to `status: approved`, rerun the validator and show that status change. Never mark a release `delivered` here.

### 5. Git permissions (always separate)

Show `git status` and the relevant diff; identify unrelated pre-existing work. Stage only the approved UX documentation, explicitly approved evidence and any separately approved glossary/ADR changes (never `git add -A`). Suggest `docs(ux): validate <version> UX design`.

1. Ask for **commit permission**, then commit only if expressly authorized; provide the hash.
2. Ask independently for **push permission** and confirm remote/branch, then push only if authorized.
3. If declined, retain local approved documents without performing the declined operation. Do not start architecture or publish Issues automatically.

## Hard invariants

- No implicit approval. Conversation summaries, design proposals and prototype selection are not approved merely because files exist.
- No new functional requirements via UX. Explicitly flag potential scope changes for `project-scoping`.
- Never infer delivery from the version's `status: approved` or from UX approval.
- IDs are stable: `FEAT-*` belongs to functional scope, `FLOW-*` to a user journey, `SCREEN-*` to a conceptual screen; avoid using screen count as ticket count.
- Earlier approved UX and functional version snapshots remain traceable. Changed canonical screens get version-labelled additions instead of overwriting earlier decisions.
- `frontend-design` and `design-critique` must be available and used in their defined phases. Skill presence is a prerequisite; it does not authorize prototype code or Git operations.
- Planning later combines **functional scope + UX handoff + validated architecture**. Do not publish implementation Issues here.
- Never overwrite unrelated files or take Git actions without authorization.
