---
id: FEAT-009
module: functional-scoping
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-009 — Structurer et modifier le catalogue fonctionnel

## Objectif utilisateur

Disposer d’une représentation cohérente des modules et fonctionnalités de la version et pouvoir corriger les propositions de l’IA.

## Comportement attendu

À partir de la synthèse validée, l’assistant propose une organisation en modules fonctionnels et fonctionnalités. Les fonctionnalités retenues possèdent des critères d’acceptation. Le catalogue distingue les nouvelles fonctionnalités, les évolutions des fonctionnalités existantes et le périmètre retenu pour la version.

L’utilisateur peut modifier manuellement les modules, fonctionnalités et critères d’acceptation. Les informations restent structurées, persistantes et liées à leur version ; les modifications suivent les mêmes règles de traçabilité et de nouvelle validation que les changements issus de l’IA. Une évolution conserve l’identité de la fonctionnalité et n’efface pas son comportement précédent.

## Historique fonctionnel par version

### V1

**Comportement validé :** catalogue fonctionnel proposé après validation de la synthèse, modifiable par l’utilisateur et soumis à validation distincte.

**Critères d’acceptation validés :**

- Le catalogue est proposé à partir de la synthèse explicitement validée.
- Les fonctionnalités sont regroupées en modules fonctionnels et chaque fonctionnalité retenue dispose de critères d’acceptation.
- Le catalogue distingue les nouvelles fonctionnalités, les évolutions et les éléments retenus pour la version.
- L’utilisateur peut modifier manuellement les modules, fonctionnalités et critères d’acceptation.
- Une modification manuelle conserve sa traçabilité et entraîne une nouvelle validation des éléments affectés.
- Une fonctionnalité évoluée conserve son identité et les comportements précédents restent attribuables à leurs versions.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), description initiale et D03, D06, D11.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](conduct-scoping-interview.md) : synthèse de référence.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](manage-proposals-and-backlog.md) : décisions sur le contenu retenu.
- [FEAT-010 — Valider les trois étapes du cadrage](approve-scoping-stages.md) : validation préalable de la synthèse et validation distincte du catalogue.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : conservation des comportements par version.

## Questions ouvertes

Aucune question fonctionnelle bloquante consignée. Le format technique des informations et leur présentation seront définis dans les phases ultérieures.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D06 et D11 et du principe d’identité stable des fonctionnalités de la description initiale. Son découpage a été approuvé avec le catalogue. Le workflow `structure-project` sert de référence fonctionnelle ; son adaptation technique reste à concevoir.
