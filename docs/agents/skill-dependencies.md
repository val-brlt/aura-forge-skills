# Skills utilisés par les workflows de projet

Copier ensemble `project-scoping`, `project-ux`, `project-architecture` et `structure-project`, avec leurs références, schémas et scripts. `project-scoping` fournit les conventions et les validateurs partagés ; `structure-project` fournit la procédure et les formats fonctionnels.

Les dépendances méthodologiques ci-dessous sont déjà présentes dans cette collection. Leurs sources et chemins d'import sont enregistrés dans [skills-lock.json](../../skills-lock.json).

| Skill à conserver ou ajouter | Source | Utilisation |
| --- | --- | --- |
| `grilling` | `mattpocock/skills` | Questions non résolues pendant le cadrage, l'UX ou l'architecture. |
| `domain-modeling` | `mattpocock/skills` | Vocabulaire métier, glossaire et décisions de domaine. |
| `frontend-design` | `anthropics/skills` | Création des maquettes HTML. |
| `design-critique` | `anthropics/knowledge-work-plugins` | Revue des maquettes rendues. |
| `codebase-design` | `mattpocock/skills` | Responsabilités, profondeur et interfaces des modules. |
| `software-architecture` | `magnus919/agent-skills` | Qualités, topologie, compromis et comportement du système. |
| `research` | `mattpocock/skills` | Selon le besoin : vérifier des faits techniques auprès de sources primaires. |
| `prototype` | `mattpocock/skills` | Selon le besoin : exploration jetable pour résoudre une incertitude. |

La facilitation des décisions est intégrée à la [référence locale de comparaison technique](../../.agents/skills/project-architecture/references/technical-comparisons.md), directement utilisée par `project-architecture`. Cette référence autonome conserve la provenance de la méthode ; elle ne nécessite aucun skill supplémentaire.

`writing-for-agents` sert à entretenir cette collection ; `create-readme` sert à sa documentation. Ils ne sont pas des dépendances d'exécution des trois workflows de projet.
