---
id: FEAT-010
module: functional-scoping
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-010 — Valider les trois étapes du cadrage

## Objectif utilisateur

Contrôler les résultats importants du cadrage avant de poursuivre et empêcher qu’une proposition ou un résultat incomplet soit considéré comme approuvé par défaut.

## Comportement attendu

Le cadrage comporte trois validations explicites successives : synthèse de l’entretien, catalogue des modules et fonctionnalités, puis cadrage final consolidé. Le passage à l’étape suivante respecte la validation de la précédente.

Des questions non bloquantes peuvent rester ouvertes dans le résultat final. Une règle indispensable indéterminée sur une fonctionnalité retenue empêche la validation finale jusqu’à clarification ou report de la fonctionnalité. Les éléments affectés par une modification après approbation nécessitent une nouvelle validation, que la modification soit manuelle ou issue du dialogue avec l’IA.

## Historique fonctionnel par version

### V1

**Comportement validé :** trois validations successives, sans approbation implicite, avec contrôle des questions bloquantes et revalidation des éléments affectés.

**Critères d’acceptation validés :**

- L’utilisateur valide explicitement la synthèse avant la préparation du catalogue.
- Il valide explicitement le catalogue avant la consolidation finale du cadrage.
- Le cadrage final fait l’objet de sa propre validation explicite.
- Une absence de réponse, une suspension ou une erreur de l’assistant n’approuve aucun résultat.
- Une règle indispensable non clarifiée pour une fonctionnalité retenue empêche la validation finale ; l’utilisateur peut clarifier ou reporter cette fonctionnalité.
- Des questions non bloquantes peuvent rester visibles sans empêcher la validation finale.
- Après correction d’un cadrage approuvé avant livraison, les éléments affectés nécessitent une nouvelle validation.
- Une validation de cadrage ne déclare jamais automatiquement la version livrée.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), D03, D05, D06, D07, D09, D11, D13.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](conduct-scoping-interview.md) : production de la synthèse.
- [FEAT-009 — Structurer et modifier le catalogue fonctionnel](structure-feature-catalogue.md) : catalogue à valider.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](manage-proposals-and-backlog.md) : clarification ou report des éléments bloquants.
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](../version-management/reopen-approved-scoping.md) : règles de réouverture et de conservation de l’état précédent.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. La présentation des validations figure dans les [livrables UX approuvés](../../versions/v1/ux/UX-SUMMARY.md) ; leurs mécanismes techniques d’exécution restent à concevoir.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D06 et D13, avec application des règles de D07, D09 et D11. Son découpage a été approuvé avec le catalogue. Les validations de l’application sont distinctes des autorisations Git du workflow documentaire utilisé pour cadrer le produit.
