---
id: FEAT-008
module: functional-scoping
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-008 — Arbitrer les propositions et les éléments reportés

## Objectif utilisateur

Garder le contrôle sur les propositions de cadrage et distinguer les besoins retenus de ceux qui restent à discuter, sont refusés ou sont reportés.

## Comportement attendu

L’utilisateur peut discuter, modifier, accepter, refuser ou reporter les propositions. Les questions non résolues restent identifiées. Les décisions peuvent être modifiées manuellement, avec les mêmes règles de traçabilité et de nouvelle validation que les changements issus du dialogue.

Les éléments reportés alimentent les cadrages suivants sans inclusion automatique. L’acceptation d’une proposition, son inclusion dans une version, la validation du cadrage et la livraison restent distinctes.

## Historique fonctionnel par version

### V1

**Comportement validé :** arbitrage explicite des propositions et conservation des éléments reportés, refusés ou non résolus avec leur contexte.

**Critères d’acceptation validés :**

- Pour une proposition, l’utilisateur peut discuter son contenu, le modifier, l’accepter, le refuser ou le reporter.
- Une proposition non approuvée ou une question non résolue n’est pas présentée comme une exigence retenue pour la version.
- Les éléments reportés restent disponibles pour les cadrages suivants et n’y sont sélectionnés que sur décision explicite.
- Les décisions modifiées manuellement conservent leur traçabilité et les éléments affectés nécessitent une nouvelle validation.
- Une décision sur une proposition ne vaut pas validation implicite de l’ensemble du cadrage ni déclaration de livraison.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), description initiale et D06, D09, D11, D12.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](conduct-scoping-interview.md) : propositions issues de la discussion.
- [FEAT-004 — Préparer les versions successives d’un projet](../version-management/prepare-project-versions.md) : sélection explicite du périmètre d’une version.
- [FEAT-010 — Valider les trois étapes du cadrage](approve-scoping-stages.md) : validation des résultats consolidés.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : conservation des décisions et de leur attribution.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. Les contenus reportés propres au produit Aura Forge sont recensés dans son [backlog](../../FUTURE-FEATURES.md).

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D06, D11 et D12, dans le respect de l’absence d’approbation implicite de D09. Son découpage a été approuvé avec le catalogue.
