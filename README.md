# Aura Forge Skills

**Des skills pour accompagner un projet logiciel, de l’idée à la livraison.**

Aura Forge rassemble des workflows pour agents IA autour des étapes d’un projet : cadrer le besoin, concevoir l’expérience utilisateur, définir l’architecture, puis préparer la planification et le développement. Chaque étape s’appuie sur des décisions humaines explicites et des livrables réutilisables par la suivante.

Le dépôt s’organise autour de **trois skills principaux** qui pilotent ces étapes. Des skills de soutien, principalement importés d’autres dépôts, apportent des méthodes spécialisées : questionnement, recherche, prototypage, design, architecture et documentation.

> [!NOTE]
> Le parcours actuel couvre le cadrage, l’UX et l’architecture. La planification avec GitHub Projects et l’orchestration du développement font partie des évolutions prévues.

## Les skills principaux

| Étape | Skill | Rôle et livrables |
| --- | --- | --- |
| Cadrage | [`project-scoping`](.agents/skills/project-scoping/SKILL.md) | Clarifier le MVP ou une évolution fonctionnelle, définir les critères de réussite et structurer les modules, fiches fonctionnalités et backlog. |
| UX/UI | [`project-ux`](.agents/skills/project-ux/SKILL.md) | Concevoir les parcours et les interactions avec des maquettes HTML interactives, une synthèse `UX-SUMMARY.md` et un contrat `UX-CONTRACT.json`. |
| Architecture | [`project-architecture`](.agents/skills/project-architecture/SKILL.md) | Comparer les solutions techniques, préparer l’architecture, le design technique, les ADR utiles et `ARCHITECTURE-CONTRACT.json`, puis valider le package avant son approbation finale. |

Ces étapes se lancent à la demande et se reprennent à partir des documents existants. Leurs livrables transmettent les besoins, les décisions et les dépendances à la suite du projet ; terminer une étape ne lance pas automatiquement la suivante.

## Principes de travail

- **L’IA conseille, l’humain décide.** Le périmètre, les maquettes et les choix d’architecture importants passent par des validations explicites.
- **Le MVP reste un objectif fonctionnel.** Il peut être livré progressivement sur plusieurs releases. Son achèvement et la première version stable sont deux décisions distinctes.
- **Les décisions restent traçables.** Les fonctionnalités conservent leurs identifiants `FEAT-*`, reliés aux parcours, écrans, interactions et éléments d’architecture.
- **Les documents évoluent avec le projet.** Les skills reprennent les chemins et décisions existants, mettent à jour les sections concernées et préservent les éléments déjà livrés.
- **Le backlog reste unique.** Un nouveau projet utilise `BACKLOG.md` ; un projet existant conserve son backlog canonique, y compris l’ancien nom `FUTURE-FEATURES.md`, jusqu’à une migration approuvée. Les besoins futurs et les fonctionnalités hors du changement courant y sont distingués avec leur état réel.
- **L’avancement reste explicite.** Validation, planification, développement et livraison sont suivis séparément ; une maquette approuvée ne prouve pas une fonctionnalité développée.
- **Les livrables destinés à l’utilisateur sont en français par défaut**, avec des identifiants et clés de contrats en anglais.

Les trois workflows principaux demandent des autorisations distinctes pour un commit et pour un push.

## Commencer

Utilisez un agent capable de lire et d’appliquer des instructions `SKILL.md` dans le dépôt de votre projet.

1. Récupérez cette collection :

   ```sh
   git clone https://github.com/val-brlt/aura-forge-skills.git
   ```

2. Copiez le contenu de `.agents/skills/` dans `.agents/skills/` du projet cible, en conservant les références, schémas et scripts associés. Les commandes de validation documentées utilisent ce chemin. Les skills de soutien sont déjà inclus : conserver l’ensemble de la collection fournit les dépendances des workflows. Configurez leur découverte selon votre agent.
3. Intégrez les conventions utiles de [`AGENTS.md`](AGENTS.md) et de [`docs/agents/`](docs/agents/) à celles du projet cible. Remplacez `NOM_GITHUB/NOM_REPO_GITHUB` par son dépôt GitHub et conservez ses règles et documents existants.
4. Demandez explicitement à l’agent d’utiliser le skill correspondant à votre étape, en lui donnant votre idée ou les documents déjà approuvés.

Exemple pour démarrer :

```text
Utilise project-scoping pour cadrer le MVP de mon projet.
Voici l’idée, les utilisateurs visés et les contraintes connues : …
```

Une fois le cadrage approuvé :

```text
Utilise project-ux à partir du cadrage approuvé et prépare les maquettes HTML.
```

Puis, après validation de l’UX :

```text
Utilise project-architecture à partir du cadrage et de l’UX approuvés.
Compare les choix techniques encore ouverts et prépare le passage à la planification.
```

Les scripts de validation fournis utilisent Python. Les opérations sur GitHub Issues suivent les conventions du projet et utilisent la CLI `gh` ; elles ne font pas partie des trois étapes principales actuelles.

## Skills de soutien

Les workflows principaux sélectionnent les méthodes utiles à leur étape. Certains skills de soutien peuvent aussi être lancés séparément pour un besoin précis.

| Besoin | Skills présents |
| --- | --- |
| Clarifier le besoin et le vocabulaire | [`grilling`](.agents/skills/grilling/SKILL.md), [`domain-modeling`](.agents/skills/domain-modeling/SKILL.md) |
| Rechercher et explorer | [`research`](.agents/skills/research/SKILL.md), [`prototype`](.agents/skills/prototype/SKILL.md) |
| Concevoir et évaluer l’interface | [`frontend-design`](.agents/skills/frontend-design/SKILL.md), [`design-critique`](.agents/skills/design-critique/SKILL.md) |
| Structurer la documentation fonctionnelle | [`structure-project`](.agents/skills/structure-project/SKILL.md) |
| Approfondir l’architecture | [`codebase-design`](.agents/skills/codebase-design/SKILL.md), [`software-architecture`](.agents/skills/software-architecture/SKILL.md) |
| Rédiger la documentation | [`writing-for-agents`](.agents/skills/writing-for-agents/SKILL.md), [`create-readme`](.agents/skills/create-readme/SKILL.md) |

La [liste des dépendances](docs/agents/skill-dependencies.md) précise les skills utilisés, leurs sources et leur rôle. `research` et `prototype` sont mobilisés selon les besoins de la phase.

`structure-project` fournit la procédure de structuration documentaire utilisée par `project-scoping`. La [référence fonctionnelle](.agents/skills/project-scoping/references/functional-documents.md) précise leur articulation ; les [conventions communes](.agents/skills/project-scoping/references/versioning.md) définissent le backlog, les états d’avancement et la séparation du MVP et des releases.

La méthode de discussion et de comparaison architecturale est intégrée à la [référence locale de comparaison technique](.agents/skills/project-architecture/references/technical-comparisons.md), directement utilisée par `project-architecture`.

Les origines des imports présents sont enregistrées dans [`skills-lock.json`](skills-lock.json) : [Matt Pocock](https://github.com/mattpocock/skills), [Anthropic Skills](https://github.com/anthropics/skills), [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins), [magnus919](https://github.com/magnus919/agent-skills) et [GitHub Awesome Copilot](https://github.com/github/awesome-copilot).

## Vérifier la collection

Depuis la racine du dépôt, lancez les tests des contrats, des références et de la compatibilité avec les anciens formats :

```sh
python -B .agents/skills/project-scoping/tests/test_contracts.py
```

Sous Windows, utilisez `py` si nécessaire. Chaque workflow indique aussi sa commande pour auditer les documents du projet accompagné ; l’approbation humaine porte sur les besoins, les maquettes et les décisions effectivement présentés.

## Évolutions prévues

| Étape | Direction envisagée | État |
| --- | --- | --- |
| `project-planning` | Exploiter le cadrage, l’UX, l’architecture et leurs dépendances pour organiser le travail avec GitHub Projects, les issues et les releases. | Prévu, absent du dépôt. |
| Volet développement | Orchestrer des agents pour l’implémentation, les tests, la revue de code, la sécurité et la préparation de la livraison. | À définir ; nom provisoire : `project-developpement`. |

Ces futurs workflows prolongeront le cadrage, l’UX et l’architecture en réutilisant leurs livrables approuvés. Le choix des skills de soutien et l’organisation des agents pour ces étapes restent à définir.

## Organisation du dépôt

```text
.agents/skills/
  project-scoping/       # Cadrage fonctionnel, références et validateurs
  project-ux/            # Conception UX, contrat et validateur
  project-architecture/  # Architecture, contrat et validateur
  structure-project/     # Méthode de structuration documentaire
  …                      # Skills de soutien et imports
docs/agents/             # Conventions pour les agents
AGENTS.md                # Point d’entrée des instructions du dépôt
GLOSSARY.md              # Vocabulaire partagé
skills-lock.json         # Provenance et empreintes des skills importés
```

Les conventions du dépôt couvrent le [suivi des issues](docs/agents/issue-tracker.md) et le [glossaire et les ADR](docs/agents/domain.md). Les livrables produits par les workflows se placent dans le projet accompagné, en respectant sa documentation existante.
