---
id: FEAT-006
module: version-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-006 — Rouvrir un cadrage approuvé avant livraison

## Objectif utilisateur

Corriger un cadrage déjà approuvé avant livraison, en conservant la référence approuvée et en maîtrisant les conséquences sur les versions suivantes.

## Comportement attendu

Un cadrage approuvé peut être rouvert tant que la version n’est pas livrée. Son état approuvé précédent est conservé et les éléments affectés nécessitent une nouvelle validation. Les mêmes règles s’appliquent aux modifications manuelles et aux changements issus du dialogue avec l’IA.

Si une version suivante est déjà active en cadrage, l’utilisateur revient explicitement sur la précédente non livrée et suspend la suivante. Les éléments de la suivante affectés par la modification de sa référence doivent être revus ; ses décisions ne sont pas réécrites automatiquement. Après livraison, les évolutions fonctionnelles appartiennent à une nouvelle version.

## Historique fonctionnel par version

### V1

**Comportement validé :** réouverture avant livraison avec conservation de l’état approuvé, nouvelle validation des éléments affectés et suspension du cadrage suivant si nécessaire.

**Critères d’acceptation validés :**

- L’utilisateur peut rouvrir un cadrage approuvé pour une version non livrée.
- L’état précédemment approuvé reste consultable après réouverture et modification.
- Les éléments affectés par les corrections nécessitent une nouvelle validation, quelle que soit l’origine manuelle ou conversationnelle du changement.
- Si V2 est en cadrage lors d’un retour explicite sur V1 non livrée, V2 est suspendue ; les deux versions ne restent pas actives en cadrage simultanément.
- Après modification de V1, les éléments affectés de V2 doivent être revus sans réécriture automatique de ses décisions.
- Une évolution fonctionnelle postérieure à la livraison est portée par une nouvelle version.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), D07, D11 et D15.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](prepare-project-versions.md) : version concernée et unique cadrage actif.
- [FEAT-005 — Déclarer la livraison d’une version](declare-version-delivery.md) : distinction entre version non livrée et livrée.
- [FEAT-010 — Valider les trois étapes du cadrage](../functional-scoping/approve-scoping-stages.md) : nouvelle validation des éléments affectés.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : conservation de l’état approuvé précédent.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D07 et D15, avec application de D11 aux modifications manuelles. Son découpage a été approuvé avec le catalogue. Les exemples V1/V2 concernent les versions d’un projet géré.
