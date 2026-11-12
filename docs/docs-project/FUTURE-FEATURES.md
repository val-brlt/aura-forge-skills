# Évolutions futures et autres propositions

## Règle de lecture

Ce backlog canonique reste unique sous son nom existant `FUTURE-FEATURES.md`. Il distingue les besoins futurs, les propositions et refus, ainsi que les fonctionnalités approuvées hors d’un changement sélectionné. Une exclusion d’un changement ne retire pas une fonctionnalité de son MVP et ne change pas ses états réels. Les reports n’engagent ni une release future ni une réalisation.

Le [MVP global](MVP.md) conserve les douze fonctionnalités approuvées de la [référence historique V1](versions/v1/VERSION.md). Aucun numéro SemVer n’est attribué ; approbation, affectation de release, développement et livraison sont indépendants. Sans preuve de réalisation/livraison, ces deux derniers états restent `unknown`.

Les éléments ci-dessous proviennent de la [synthèse approuvée](versions/v1/SCOPING-SUMMARY.md). Les décisions D01 à D16 sont récapitulées dans la [fiche V1](versions/v1/VERSION.md).

## Évolutions futures envisagées, sans engagement

| Capacité reportée | Limite de V1 | Origine |
| --- | --- | --- |
| Plusieurs utilisateurs, authentification, partage et collaboration | Usage personnel, sans gestion de plusieurs utilisateurs ni authentification | D01 |
| Accompagnement de la conception UX/UI des projets gérés | Le résultat de V1 est un cadrage fonctionnel | D02 |
| Accompagnement de l’architecture technique des projets gérés | Aucun choix technique des projets gérés n’est produit par le cadrage | D02 |
| Planification du développement | Aucun découpage en tâches de réalisation | D02 |
| Intégrations GitHub : dépôts, Issues et Projects | Aucune intégration GitHub dans V1 | Description initiale, D02 |
| Développement délégué aux agents et suivi de leurs tests, commits et pull requests | Aucune délégation de développement dans V1 | Description initiale, D02 |
| Suppression définitive des projets | Archivage et restauration seulement | D04 |
| Pièces jointes et import de documents | Textes saisis ou collés seulement | D10 |
| Reformulation ou enrichissement dédié de la description initiale par IA | Cette fonction dédiée est reportée ; l’entretien de cadrage avec l’IA reste inclus | D10, D14 |

Les phases et capacités reportées ne sont pas détaillées en fiches de fonctionnalités dans ce cycle. Leur cadrage et leur éventuelle attribution à une version nécessiteront des décisions explicites.

## Fonctionnalités approuvées sans version prévue

Les douze fonctionnalités approuvées restent indexées dans le [MVP](MVP.md) et leur [périmètre d’origine V1](versions/v1/VERSION.md), sans release prévue ni livraison attestée. Elles ne sont pas reclassées en besoins futurs lorsque seule une adaptation de FEAT-004/005/006 est étudiée. Les critères et décisions restent dans leurs fiches canoniques, sans catalogue parallèle.

Aucun autre engagement fonctionnel distinct n’est consigné. Les capacités reportées ci-dessus restent envisagées sans engagement ; leurs règles détaillées ne sont pas approuvées, leur développement et leur livraison ne sont pas attestés.

## Propositions et points non résolus

- **Adaptation MVP/releases des fonctionnalités existantes** : voir les critères proposés de [FEAT-004](modules/version-management/prepare-project-versions.md), [FEAT-005](modules/version-management/declare-version-delivery.md) et [FEAT-006](modules/version-management/reopen-approved-scoping.md). La distinction conceptuelle est retenue ; les nouvelles transitions, l’UX et le modèle de données restent à valider. Ces propositions n’ajoutent aucune fonctionnalité au MVP et n’ont ni affectation de release ni preuve de développement/livraison.
- **Synchronisation avec un outil externe** : sujet évoqué dans la recommandation Q8, sans décision distincte de l’utilisateur. Non retenu pour V1 ; aucune capacité de synchronisation future n’est approuvée.

## Fonctionnalités refusées ou hors périmètre

- **Export Markdown du cadrage approuvé** : proposition refusée pour V1, décision D08. Aucun report vers une version future n’est déduit de ce refus.

## Promotion dans un périmètre et affectation de release

Lors d’un cadrage ultérieur, les éléments reportés peuvent alimenter la discussion, mais leur inclusion dans un MVP ou une évolution requiert une sélection et une validation fonctionnelles explicites. L’affectation à une release vient ensuite, après analyse des dépendances et validation de la planification ; la capacité d’un skill à traiter un sujet ne l’inclut pas au MVP. Leur éventuelle évolution doit rester distincte des comportements approuvés ou confirmés livrés auparavant. Voir [FEAT-008 — Arbitrer les propositions et les éléments reportés](modules/functional-scoping/manage-proposals-and-backlog.md).
