# Module — Gestion des projets

## Objectif

Permettre à une personne de conserver plusieurs projets distincts et de gérer leur identité, leur description et leur archivage.

## Périmètre

V1 couvre la création et la consultation de projets, la modification de leur description libre et l’archivage réversible. Un projet archivé reste consultable ; il doit être restauré avant toute modification ou poursuite du cadrage.

L’usage reste personnel, sans authentification ni gestion de plusieurs utilisateurs. La suppression définitive, les pièces jointes, l’import et l’amélioration dédiée de la description par IA sont reportés.

## Fonctionnalités

- [FEAT-001 — Créer et consulter plusieurs projets](create-and-view-projects.md).
- [FEAT-002 — Modifier la description d’un projet](edit-project-description.md).
- [FEAT-003 — Archiver et restaurer un projet](archive-and-restore-project.md).

## Dépendances et points ouverts

Les projets portent leurs versions, définies dans le module [Gestion des versions](../version-management/MODULE.md). Leurs informations et décisions sont conservées dans le cadre du module [Continuité du travail](../continuity/MODULE.md).

Aucune question fonctionnelle bloquante consignée. Sources : description initiale et D01, D04, D10, D14, D16 de la [synthèse V1](../../versions/v1/SCOPING-SUMMARY.md).
