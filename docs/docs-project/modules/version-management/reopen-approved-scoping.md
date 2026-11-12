---
id: FEAT-006
module: version-management
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-006 — Rouvrir un cadrage approuvé avant livraison

## Objectif utilisateur

Corriger un cadrage déjà approuvé avant livraison, en conservant la référence approuvée et en maîtrisant les conséquences sur les versions suivantes.

## Comportement attendu

Les règles ci-dessous décrivent la référence V1 approuvée. Le [MVP global](../../MVP.md) est indépendant des releases ; l’adaptation de ces règles dans l’application est présentée dans les critères proposés et questions ouvertes, sans approbation implicite.

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

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Adaptation au MVP indépendant des releases — **proposition à valider**, sans modification des critères historiques approuvés :

- Corriger le reliquat non livré d’un périmètre approuvé en conservant les copies approuvées et les critères/comportements déjà livrés ; revalider uniquement les éléments affectés.
- Lorsqu’une tranche est livrée, porter toute modification de son comportement livré dans une évolution distincte à planifier ; ne pas réécrire rétroactivement cette livraison.
- Transposer la suspension et la revue de D15 aux périmètres dépendants, en gardant la référence exacte et sans réécriture automatique des décisions.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](prepare-project-versions.md) : version concernée et unique cadrage actif.
- [FEAT-005 — Déclarer la livraison d’une version](declare-version-delivery.md) : distinction entre version non livrée et livrée.
- [FEAT-010 — Valider les trois étapes du cadrage](../functional-scoping/approve-scoping-stages.md) : nouvelle validation des éléments affectés.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : conservation de l’état approuvé précédent.

## Questions ouvertes

À valider : une livraison partielle doit-elle verrouiller seulement son contenu plutôt que tout le périmètre MVP ? La proposition ci-dessus protège les tranches livrées et autorise la reprise du reliquat ; elle n’est pas couverte par D07/D15. La règle V1 interdisant la réouverture d’une version livrée reste la référence approuvée.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D07 et D15, avec application de D11 aux modifications manuelles. Son découpage a été approuvé avec le catalogue. Les exemples V1/V2 concernent les versions d’un projet géré.
