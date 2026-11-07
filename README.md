# Project Starter for Matt Pocock's Skills

This repository provides a starting point for projects using Matt Pocock's engineering skills. It includes the issue tracking, triage label, and domain documentation configuration these skills expect.

## Structure

```text
AGENTS.md                       # Entry point and configuration links
GLOSSARY.md                     # Domain vocabulary to fill in
docs/
└── agents/
    ├── issue-tracker.md         # GitHub Issues conventions
    ├── triage-labels.md         # Triage label mapping
    └── domain.md                # Glossary and ADR guidelines
```

Document architectural decisions in `docs/adr/` as the project evolves.

## Using This Starter

1. Copy this starter into a new repository and configure its GitHub remote.
2. Install Matt Pocock's skills in the tool you use to work on the project.
3. Replace `NOM_GITHUB/NOM_REPO_GITHUB` in `AGENTS.md` with the target repository's `owner/repo` and adapt the conventions in `docs/agents/`.
4. Create any missing GitHub labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`.
5. Expand the glossary and record architectural decisions as the domain becomes clearer.

Edit the configuration files directly to match your project's practices. The skills themselves are installed separately.
