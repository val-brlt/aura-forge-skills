# Technical option comparisons (working documents)

This reference governs **the analysis shown to the user before approval** and its persistent scratch copy. It incorporates discussion-first facilitation adapted from Tikalk's `architect-specify`; the procedure below is self-contained. `project-architecture` owns phase boundaries, approvals and artifacts.

## Purpose and scope

- One consequential, separable choice = one comparison. For a stack, normally compare **frontend**, **backend/runtime**, **persistence**, **Codex integration** and **deployment** separately when the choices are independent. If end-to-end architectures are truly inseparable, compare integrated alternatives and spell out their boundaries.
- First examine the option space across credible ecosystems, not just tools in a familiar programming language. Include JVM/Java, Python, .NET, Go or other families **when actually relevant**, not as mandatory checkboxes. Evaluate frameworks within the shortlisted ecosystem(s) as necessary.
- Aim for 2–4 credible candidates; eliminate obviously incompatible options briefly, with an explicit reason if the exclusion matters. Do not invent weak options or pretend a single option is objectively best without explaining project constraints.
- A comparative table should be understandable by the user without reading source code or opening the scratch file. The scratch copy retains more detail and sources for session continuity.
- Prefer qualitative comparison unless measured values and meaningful weights are known. Avoid invented ratings, costs, scales, benchmarks or deployment promises.
- An approved choice should not be relitigated for variety. Reopen only for a verified conflict, new requirement, failed assumption or an explicit user request.
- Compare technologies independently of what is installed on the user's machine. Existing shipped architecture and verified hosting constraints matter; incidental local tool availability never selects a stack.

## Decision procedure

1. **Frame:** connect the specific choice to approved functional/UX requirements, current code, accepted constraints and material migration concerns. Distinguish hard requirements, preferences and assumptions; use team familiarity only when known. State reversibility and choose the few criteria that discriminate among viable options.
2. **Research:** use the option-space rules above. Compare equivalent decisions, explaining scope differences between integrated and standalone solutions. Verify consequential claims about integrations, pricing, licenses, feature support, deployment, version compatibility, performance and security against primary documentation/source code. Record URLs and verification dates. Label estimates and unavailable verification explicitly.
3. **Prepare and present:** write the scratch comparison using the convention below **before** asking for approval. Show a concise French table and recommendation in the conversation, including why alternatives lose, accepted costs/risks, when another option wins and effects on other decisions. Invite the user to suggest another viable option. If an unanswered constraint could change the recommendation, resolve that question before requesting approval. A link alone is insufficient. If persistence is unavailable, show the full comparison inline and report that limitation.
4. **Decide:** ask one targeted approval question at a time and wait for explicit acceptance. Record `proposed`, `accepted`, `rejected` or `deferred` with verifiable approval evidence. Preserve the original recommendation and user feedback if another option is chosen; update the same file's current decision and consequences. Summarize the user's choice and consequences before moving to the next independent decision. New constraints or alternatives return to the comparison before approval.
5. **Integrate:** put accepted decisions in canonical architecture sections and a sparse ADR only when warranted. Preserve essential context, alternatives, rationale and consequences there independently of scratch. Draft proposals remain visibly proposed. Settle cross-module/shared-data contracts, security boundaries, deployment and difficult migrations before planning; a consequential deferred blocker keeps the handoff non-ready.

Local, low-impact implementation conventions need no full comparison or human decision. When a consequential choice has only one credible option, document the constraint, attempted alternative search and reason the option is forced, then obtain approval. Reuse already-approved choices unless a verified conflict, changed requirement or explicit user request reopens them.

## Exact scratch convention

Default relative to **repository root**:

```text
.scratch/
└── project-architecture/
    └── <scope-id>/
        └── comparisons/
            ├── frontend-framework.md
            ├── backend-runtime-and-framework.md
            ├── data-store.md
            └── codex-integration.md
```

These filenames are **illustrative**, not mandatory deliverables. `<scope-id>` can be `mvp`, an existing legacy baseline or an already-approved release. Preserve existing workspaces; a new software version does not duplicate comparisons. Write only for real open consequential decisions, with a project slug when needed to avoid collisions.

Before asking for user approval, create/update the choice's Markdown file. Use a **stable kebab-case slug** to update the same comparison after discussion. No date-stamped duplicate files or addenda. If the choice is rejected, revised, or approved, update its status and decision record in the same file. Do not turn a discussion draft into an accepted ADR without approval. Existing files from older attempts should be revised in place, never wholesale overwritten without reading their decisions first.

Treat scratch as noncanonical working history. Keep it available for resuming the conversation, but do **not** reference it as the only explanation of an approved decision: the canonical architecture document or a justified ADR must contain the essential reasoning. Inspect `.gitignore` and `git status` as appropriate; avoid committing scratch files or leaking local secrets. If scratch is not ignored, tell the user and suggest a repository-appropriate ignore rule; don't quietly include scratch in the next commit.

## Recommended content per file

```markdown
# [Choice title]

- Project/scope: [existing ID] / [MVP, change or existing baseline; release only if approved]
- Status: proposed | accepted | rejected | deferred
- Current recommendation: [option or explicitly provisional]
- User decision: [none yet / approved option + exact verifiable reference]
- Last reviewed: YYYY-MM-DD  # only if actual date is known

## What is being decided
[One choice, not multiple independent technologies bundled together.]

## Requirements and evidence
- [Functional/UX/architecture source and known constraint]
- [Hard constraint vs preference vs unresolved assumption]

## Options screened
[Brief note on plausible families considered, and meaningful exclusions.]

## Comparison
| Option | Relevant strengths | Relevant weaknesses / risks | Fit for this project |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Recommendation and rationale
[Decisive reasons, implications, trade-offs, when another choice wins.]

## Effects on other decisions and planning
[What this constrains or leaves open; migration/deployment considerations when material.]

## Sources and uncertainty
- [Official documentation/source URLs, and verification dates where available]
- [Unverified assumptions or test/spike still required]

## Decision and feedback
[What the user actually said; status and consequences. Do not invent approval.]
```

All visible comparison explanations are normally **French** for Aura Forge; the template's headings may be translated. Be concrete, not verbose for its own sake. A one-screen table and a short recommendation may suffice for a medium decision; higher-risk decisions deserve more depth and source checking.

## Review checklist

- [ ] Scope: one understandable question, not three independent tools bundled into one approval.
- [ ] Option space: relevant competing approaches and ecosystems surveyed.
- [ ] Comparability: credible, same-purpose candidates and project-specific differentiating criteria.
- [ ] Evidence: material claims sourced, estimates labeled, important unknowns transparent.
- [ ] Judgment: clear recommendation, why alternatives lose, accepted compromises.
- [ ] Persistence: scratch Markdown exists and reflects the **current** user-visible comparison.
- [ ] Status: approval is explicit; draft recommendations do not become canonical decisions.
