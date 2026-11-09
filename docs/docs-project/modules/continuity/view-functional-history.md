---
id: FEAT-012
module: continuity
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-012 — Consulter l’historique fonctionnel et les décisions

## Objectif utilisateur

Comprendre ce qui a été décidé pour chaque version d’un projet et retrouver les références précédentes sans confondre évolutions prévues et comportements livrés.

## Comportement attendu

Les cadrages et décisions antérieurs restent consultables avec leur attribution au projet et à la version concernés. L’historique permet de retrouver l’état approuvé précédent lors d’une réouverture et de distinguer les comportements successifs d’une fonctionnalité qui conserve son identité.

Les modifications manuelles suivent les mêmes règles de traçabilité que les changements issus du dialogue avec l’IA. Le prévu, l’approuvé et le confirmé livré restent distincts. L’archivage d’un projet ne retire pas la consultation de son historique.

## Historique fonctionnel par version

### V1

**Comportement validé :** consultation des cadrages, décisions et états approuvés précédents avec attribution aux projets, versions et fonctionnalités concernés.

**Critères d’acceptation validés :**

- L’utilisateur peut consulter les cadrages et décisions antérieurs d’un projet en identifiant les versions concernées.
- Lorsqu’un cadrage approuvé est rouvert et corrigé, son état approuvé précédent reste consultable.
- Lorsqu’une fonctionnalité évolue, ses comportements précédents restent attribuables à leurs versions sans perte de son identité.
- Les décisions modifiées manuellement conservent leur traçabilité au même titre que les changements issus du dialogue avec l’IA.
- La consultation distingue les capacités prévues ou approuvées des capacités confirmées livrées.
- L’historique reste consultable pour un projet archivé.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), description initiale et D03, D07, D11, D12, D15, D16.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](../version-management/prepare-project-versions.md) : attribution du contexte fonctionnel à une version.
- [FEAT-005 — Déclarer la livraison d’une version](../version-management/declare-version-delivery.md) : distinction entre approbation et livraison confirmée.
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](../version-management/reopen-approved-scoping.md) : conservation de la référence approuvée.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](../functional-scoping/manage-proposals-and-backlog.md) : décisions dont le contexte est conservé.

## Questions ouvertes

Aucune question fonctionnelle bloquante consignée. La présentation de l’historique figure dans les [livrables UX approuvés](../../versions/v1/ux/UX-SUMMARY.md) ; sa représentation technique reste à étudier.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de la description initiale et de D03, D07, D11, D12, D15, avec maintien de la consultation selon D16. Son découpage a été approuvé avec le catalogue. Cette fiche porte la consultation de l’historique ; elle n’ajoute pas de capacité de correction rétroactive des versions livrées.
