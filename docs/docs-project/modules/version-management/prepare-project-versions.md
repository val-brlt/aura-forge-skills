---
id: FEAT-004
module: version-management
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-004 — Préparer les versions successives d’un projet

## Objectif utilisateur

Cadrer une première version puis les suivantes d’un même projet sans repartir de zéro ni perdre les décisions précédentes.

## Comportement attendu

Les règles ci-dessous décrivent la référence V1 approuvée. Le [MVP global](../../MVP.md) est indépendant des releases ; l’adaptation de ces règles dans l’application est présentée dans les critères proposés et questions ouvertes, sans approbation implicite.

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

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Adaptation au MVP indépendant des releases — **proposition à valider**, sans modification des critères historiques approuvés :

- Cadrer le MVP global ou une évolution avec une identité de périmètre stable, sans numéro de release obligatoire ; conserver la même identité FEAT lors des évolutions.
- Maintenir un seul cadrage fonctionnel actif par projet, indépendamment des releases ; préparer une évolution par son delta sans répéter l’entretien approuvé. Cette transposition de D05 demande une validation explicite.
- Conserver une référence approuvée exacte et les états décision/développement/livraison ; l’affectation à une release reste absente jusqu’à une planification validée.

## Dépendances fonctionnelles

- [FEAT-001 — Créer et consulter plusieurs projets](../project-management/create-and-view-projects.md) : une version appartient à un projet.
- [FEAT-005 — Déclarer la livraison d’une version](declare-version-delivery.md) : la livraison est une information explicitement renseignée.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](../functional-scoping/manage-proposals-and-backlog.md) : sélection du périmètre suivant.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : contexte précédent conservé.

## Questions ouvertes

À valider pour adapter l’application : séparation entre périmètre fonctionnel, appartenance MVP et release ; transposition de l’activité unique et de la suspension. Le premier numéro SemVer et le découpage ne sont pas décidés. Les critères V1 restent approuvés et inchangés ; les nouveaux critères ci-dessus restent proposés.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D03, D05 et D12. Son découpage a été approuvé avec le catalogue. La prise en charge de versions successives des projets n’approuve aucune version ultérieure du produit Aura Forge lui-même.
