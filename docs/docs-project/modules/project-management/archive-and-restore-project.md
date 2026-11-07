---
id: FEAT-003
module: project-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-003 — Archiver et restaurer un projet

## Objectif utilisateur

Mettre un projet de côté tout en conservant son contenu et la possibilité de le reprendre.

## Comportement attendu

Un projet peut être archivé puis restauré. Tant qu’il est archivé, il reste consultable avec son historique, mais toute modification ou poursuite du cadrage nécessite sa restauration. L’archivage ne modifie ni les validations ni les déclarations de livraison. La suppression définitive est reportée.

## Historique fonctionnel par version

### V1

**Comportement validé :** archivage réversible avec maintien de la consultation et restriction des modifications jusqu’à restauration.

**Critères d’acceptation validés :**

- L’utilisateur peut archiver un projet existant puis le restaurer.
- Le projet archivé et son historique restent consultables.
- Une modification ou la poursuite de son cadrage nécessite d’abord sa restauration.
- Archiver ou restaurer le projet ne change pas les validations déjà accordées ni ses déclarations de livraison.
- L’archivage conserve les informations nécessaires à la reprise du projet.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), D04 et D16.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-001 — Créer et consulter plusieurs projets](create-and-view-projects.md) : archivage d’un projet identifié.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : consultation maintenue pendant l’archivage.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. La suppression définitive reste hors périmètre et figure dans le [backlog](../../FUTURE-FEATURES.md).

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D04 et précisée par D16. Son découpage a été approuvé avec le catalogue. Aucun effet de l’archivage sur les validations ou la livraison n’est présumé.
