# Project Toolkit Skills

[![skills.sh](https://skills.sh/b/val-brlt/project-toolkit-skills)](https://skills.sh/val-brlt/project-toolkit-skills)

**Skills to guide a software project from idea to delivery.**

This collection provides AI agent workflows for each stage of a project: scoping requirements, designing the user experience, defining the architecture, and preparing for planning and development. Each stage relies on explicit human decisions and produces deliverables that the next stage can reuse.

The repository is organized around **three main skills** that guide these stages. Supporting skills, mostly imported from other repositories, provide specialized methods for interviewing, research, prototyping, design, architecture, and documentation.

> [!NOTE]
> The current workflow covers scoping, UX, and architecture. Planning with GitHub Projects and development orchestration are planned additions.

## Main skills

| Stage | Skill | Purpose and deliverables |
| --- | --- | --- |
| Scoping | [`project-scoping`](.agents/skills/project-scoping/SKILL.md) | Clarify the MVP or a functional change, define success criteria, and organize modules, feature cards, and the backlog. |
| UX/UI | [`project-ux`](.agents/skills/project-ux/SKILL.md) | Design user journeys and interactions with interactive HTML mockups, a `UX-SUMMARY.md` summary, and a `UX-CONTRACT.json` contract. |
| Architecture | [`project-architecture`](.agents/skills/project-architecture/SKILL.md) | Compare technical solutions, prepare the architecture, technical design, relevant ADRs, and `ARCHITECTURE-CONTRACT.json`, then validate the package before final approval. |

These stages run on request and can resume from existing documents. Their deliverables carry requirements, decisions, and dependencies forward; completing one stage does not automatically start the next.

## Working principles

- **AI advises; humans decide.** Scope, mockups, and significant architectural choices require explicit approval.
- **The MVP remains a functional goal.** It can be delivered incrementally across multiple releases. Completing the MVP and shipping the first stable version are separate decisions.
- **Decisions remain traceable.** Features retain their `FEAT-*` identifiers, linked to user journeys, screens, interactions, and architectural elements.
- **Documents evolve with the project.** Skills reuse existing paths and decisions, update the relevant sections, and preserve what has already been delivered.
- **There is one backlog.** New projects use `BACKLOG.md`; existing projects keep their canonical backlog, including the legacy name `FUTURE-FEATURES.md`, until a migration is approved. Future requirements and features outside the current change are recorded with their actual status.
- **Progress stays explicit.** Approval, planning, development, and delivery are tracked separately; an approved mockup does not mean a feature has been implemented.
- **User-facing deliverables are in French by default**, with identifiers and contract keys in English.

The three main workflows require separate permissions to commit and to push.

## Installation (30-second setup)

A plugin updates itself. [skills.sh](https://skills.sh/val-brlt/project-toolkit-skills) copies editable files into your project, and you update them manually. Choose one method per agent: installing both adds every skill twice.

This collection currently installs through [Skills CLI](https://github.com/vercel-labs/skills), which requires Node.js 22.20 or later. Run the commands from the root of your **target project**.

### 1. Get the skills

<details>
<summary><strong>Codex</strong></summary>

```bash
npx skills@latest add val-brlt/project-toolkit-skills --skill '*' --agent codex
```

To update, run `npx skills@latest update`. Run `add` again to pick up new skills in the collection.

</details>

<details>
<summary><strong>Other agents, or editable files</strong> (manual updates)</summary>

```bash
npx skills@latest add val-brlt/project-toolkit-skills -a <agent>
```

Omit `-a <agent>` to choose your agent in the installer. Available identifiers are listed in the [Skills CLI supported agents reference](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

When the installer asks which skills to install, select the entire collection to include the workflow dependencies. To update, run `npx skills@latest update`, then run `add` again to pick up new skills.

Dedicated integrations for other agents have not yet been prepared for this collection.

</details>

Keep the references, schemas, and scripts included with the skills. Workflow validation commands use the project's `.agents/skills/` path.

### 2. Configure your project

Merge the relevant conventions from [`AGENTS.md`](AGENTS.md) and [`docs/agents/`](docs/agents/) into your target project's conventions. These files are not installed by `skills add`. Replace `NOM_GITHUB/NOM_REPO_GITHUB` with your project's GitHub repository and preserve its existing rules and documents.

### 3. Run your first workflow

Explicitly ask the agent to use the skill for your current stage, providing your idea or previously approved documents.

To get started:

```text
Use project-scoping to scope my project's MVP.
Here are the idea, target users, and known constraints: …
```

Once the scope is approved:

```text
Use project-ux with the approved scope to prepare HTML mockups.
```

Then, after UX approval:

```text
Use project-architecture with the approved scope and UX.
Compare the remaining technical options and prepare the handoff to planning.
```

The included validation scripts use Python. GitHub Issues operations follow the project's conventions and use the `gh` CLI; they are outside the three main stages currently available.

## Supporting skills

The main workflows select the methods relevant to their stage. Some supporting skills can also be used independently for a specific task.

| Need | Included skills |
| --- | --- |
| Clarify requirements and vocabulary | [`grilling`](.agents/skills/grilling/SKILL.md), [`domain-modeling`](.agents/skills/domain-modeling/SKILL.md) |
| Research and explore | [`research`](.agents/skills/research/SKILL.md), [`prototype`](.agents/skills/prototype/SKILL.md) |
| Design and evaluate the interface | [`frontend-design`](.agents/skills/frontend-design/SKILL.md), [`design-critique`](.agents/skills/design-critique/SKILL.md) |
| Structure functional documentation | [`structure-project`](.agents/skills/structure-project/SKILL.md) |
| Refine the architecture | [`codebase-design`](.agents/skills/codebase-design/SKILL.md), [`software-architecture`](.agents/skills/software-architecture/SKILL.md) |
| Write documentation | [`writing-for-agents`](.agents/skills/writing-for-agents/SKILL.md), [`create-readme`](.agents/skills/create-readme/SKILL.md) |

The [dependency list](docs/agents/skill-dependencies.md) details the skills used, their sources, and their roles. `research` and `prototype` are used as needed during each stage.

`structure-project` provides the documentation structure procedure used by `project-scoping`. The [functional documentation reference](.agents/skills/project-scoping/references/functional-documents.md) explains how they work together; the [shared conventions](.agents/skills/project-scoping/references/versioning.md) define the backlog, progress states, and the distinction between the MVP and releases.

The method for discussing and comparing architectural options is included in the [local technical comparison reference](.agents/skills/project-architecture/references/technical-comparisons.md), used directly by `project-architecture`.

The sources of imported skills are recorded in [`skills-lock.json`](skills-lock.json): [Matt Pocock](https://github.com/mattpocock/skills), [Anthropic Skills](https://github.com/anthropics/skills), [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins), [magnus919](https://github.com/magnus919/agent-skills), and [GitHub Awesome Copilot](https://github.com/github/awesome-copilot).

## Verify the collection

From the repository root, run the tests for contracts, references, and compatibility with legacy formats:

```sh
python -B .agents/skills/project-scoping/tests/test_contracts.py
```

On Windows, use `py` if needed. Each workflow also documents its command for auditing the target project's documents; human approval applies to the requirements, mockups, and decisions actually presented.

## Planned additions

| Stage | Planned direction | Status |
| --- | --- | --- |
| `project-planning` | Use the scope, UX, architecture, and their dependencies to organize work with GitHub Projects, issues, and releases. | Planned; not yet included in the repository. |
| Development workflow | Orchestrate agents for implementation, testing, code review, security, and delivery preparation. | To be defined; provisional name: `project-developpement`. |

These future workflows will extend scoping, UX, and architecture by reusing their approved deliverables. Supporting skills and agent coordination for these stages are still to be defined.

## Repository structure

```text
.agents/skills/
  project-scoping/       # Functional scoping, references, and validators
  project-ux/            # UX design, contract, and validator
  project-architecture/  # Architecture, contract, and validator
  structure-project/     # Documentation structure method
  …                      # Supporting skills and imports
docs/agents/             # Agent conventions
AGENTS.md                # Entry point for repository instructions
GLOSSARY.md              # Shared vocabulary
skills-lock.json         # Sources and hashes of imported skills
```

The repository conventions cover [issue tracking](docs/agents/issue-tracker.md) and the [glossary and ADRs](docs/agents/domain.md). Workflow deliverables are saved in the target project, following its existing documentation structure.
