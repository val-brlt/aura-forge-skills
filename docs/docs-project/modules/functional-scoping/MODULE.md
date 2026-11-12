# Module — Cadrage fonctionnel

## Objectif

Accompagner l’utilisateur de l’idée ou des nouveaux besoins jusqu’à un cadrage fonctionnel explicitement validé pour une version précise.

## Périmètre

V1 couvre l’entretien avec l’IA à partir de textes : questions structurées, recommandations et réponses libres dont l’interprétation est confirmée avant décision. Les discussions liées aux questions et le fil général du projet permettent d’explorer les besoins. Ce fil suit le projet entre ses versions, sans modifier automatiquement ses décisions. L’assistant distingue le prévu, l’approuvé et le confirmé livré.

Le cadrage comprend l’arbitrage des propositions, la structuration du catalogue en modules et fonctionnalités, les critères d’acceptation et les modifications manuelles. Trois validations se succèdent : synthèse, catalogue et cadrage final. L’analyse préparatoire n’en constitue pas une quatrième.

Une règle indispensable non clarifiée bloque la validation finale ; l’utilisateur peut la préciser ou reporter la fonctionnalité. Les questions non bloquantes peuvent rester visibles. L’absence de réponse ne vaut jamais approbation.

Les parcours et écrans des projets gérés, leur architecture, leurs choix techniques et leurs tâches de réalisation appartiennent à des phases ultérieures. Les [livrables UX V1](../../versions/v1/ux/UX-SUMMARY.md) décrivent l’interface approuvée du produit Aura Forge.

## Fonctionnalités

- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](conduct-scoping-interview.md).
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](manage-proposals-and-backlog.md).
- [FEAT-009 — Structurer et modifier le catalogue fonctionnel](structure-feature-catalogue.md).
- [FEAT-010 — Valider les trois étapes du cadrage](approve-scoping-stages.md).

## Dépendances et points ouverts

Le cadrage est rattaché à une [version de projet](../version-management/prepare-project-versions.md). Il est [sauvegardé et reprenable](../continuity/save-and-resume-scoping.md), avec un [historique consultable](../continuity/view-functional-history.md).

Aucune question fonctionnelle bloquante pour la référence V1. Les [choix techniques et l’adaptation des skills](../../architecture/ARCHITECTURE.md) sont approuvés, sans intégration attestée. Le cadrage autonome et l’appartenance MVP indépendante des releases ont des conséquences proposées sur synthèse, catalogue et validations ; elles suivent la décision attendue dans FEAT-004/005/006 sans rouvrir les exigences historiques. Sources : description initiale et D02, D06, D07, D10 à D14 de la [synthèse V1](../../versions/v1/SCOPING-SUMMARY.md).
