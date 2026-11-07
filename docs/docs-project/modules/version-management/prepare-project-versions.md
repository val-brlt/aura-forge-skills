---
id: FEAT-004
module: version-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-004 — Préparer les versions successives d’un projet

## Objectif utilisateur

Cadrer une première version puis les suivantes d’un même projet sans repartir de zéro ni perdre les décisions précédentes.

## Comportement attendu

Chaque cadrage se rapporte à une version précise du projet. Le premier part de l’idée initiale ; les suivants réutilisent le dernier cadrage approuvé et les éléments reportés. Une seule version par projet est active en cadrage. La préparation d’une version suivante est possible avant livraison de la précédente, en distinguant le prévu du confirmé livré.

Une fonctionnalité conserve son identité au fil des versions ; son comportement précédent reste identifiable. Le contexte réutilisé n’entraîne aucune inclusion automatique dans le nouveau périmètre.

## Historique fonctionnel par version

### V1

**Comportement validé :** gestion des cadrages successifs des projets dès le MVP d’Aura Forge, avec contexte de référence et distinction entre cadrage et livraison.

**Critères d’acceptation validés :**

- Pour un projet, l’utilisateur peut préparer un premier cadrage, puis celui d’une version suivante.
- Une seule version de ce projet est active en cadrage à un instant donné.
- La version suivante peut être préparée même si la précédente n’est pas encore déclarée livrée.
- L’assistant utilise le dernier cadrage approuvé et les éléments reportés comme contexte, en distinguant les fonctionnalités prévues de celles confirmées livrées.
- Un élément reporté n’est pas inclus dans la nouvelle version sans sélection explicite.
- L’évolution d’une fonctionnalité conserve son identité et l’attribution de ses comportements aux versions concernées.

**Source :** [Synthèse V1 — versions et continuité fonctionnelle](../../versions/v1/SCOPING-SUMMARY.md#4-versions-et-continuité-fonctionnelle), D03, D05, D12 et description initiale.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-001 — Créer et consulter plusieurs projets](../project-management/create-and-view-projects.md) : une version appartient à un projet.
- [FEAT-005 — Déclarer la livraison d’une version](declare-version-delivery.md) : la livraison est une information explicitement renseignée.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](../functional-scoping/manage-proposals-and-backlog.md) : sélection du périmètre suivant.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : contexte précédent conservé.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. Le cas d’une réouverture de la version précédente est couvert par [FEAT-006](reopen-approved-scoping.md).

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D03, D05 et D12. Son découpage a été approuvé avec le catalogue. La prise en charge de versions successives des projets n’approuve aucune version ultérieure du produit Aura Forge lui-même.
