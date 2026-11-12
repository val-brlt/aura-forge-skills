# Module — Gestion des versions

## Objectif

Permettre de cadrer les versions successives d’un projet en conservant les références précédentes et en distinguant approbation du cadrage et livraison.

## Périmètre

Une seule version par projet est active en cadrage. Une version suivante peut être préparée avant livraison de la précédente. Le contexte réutilisé distingue le prévu du confirmé livré, et aucun élément reporté n’est automatiquement inclus.

L’utilisateur peut déclarer une livraison. Avant livraison, il peut rouvrir un cadrage approuvé en conservant l’état approuvé précédent. Si une version suivante est en cadrage, elle est suspendue lors du retour à la précédente et ses éléments affectés doivent ensuite être revus.

## Fonctionnalités

- [FEAT-004 — Préparer les versions successives d’un projet](prepare-project-versions.md).
- [FEAT-005 — Déclarer la livraison d’une version](declare-version-delivery.md).
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](reopen-approved-scoping.md).

## Dépendances et points ouverts

Une version appartient à un [projet](../project-management/create-and-view-projects.md). Son cadrage suit les validations du module [Cadrage fonctionnel](../functional-scoping/MODULE.md), avec un [historique consultable](../continuity/view-functional-history.md).

La référence V1 reste approuvée. La séparation documentaire entre [MVP](../../MVP.md), version logicielle et livraison est retenue ; les transitions applicatives d’activité, livraison partielle et réouverture du reliquat restent proposées dans FEAT-004/005/006. Elles nécessitent une décision fonctionnelle et une revue UX ciblée avant remplacement des règles ci-dessus. Sources historiques : D03, D05, D07, D12, D15 de la [synthèse V1](../../versions/v1/SCOPING-SUMMARY.md).
