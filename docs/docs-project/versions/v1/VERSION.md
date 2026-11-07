---
version: v1
release_kind: mvp
status: approved
---

# Version V1 — MVP d’Aura Forge Project AI

## Objectif de la version

Permettre à une personne de passer d’une idée de logiciel à un cadrage fonctionnel validé, structuré, conservé et reprenable dans une application web en français. V1 permet de gérer plusieurs projets et de cadrer leurs versions successives, sans authentification ni gestion de plusieurs utilisateurs.

## Référence précédente

Première version du produit Aura Forge, sans référence précédente livrée. Les versions des projets gérés dans l’application sont distinctes des versions du produit Aura Forge.

Aucune fonctionnalité de cette V1 n’est déclarée implémentée ou livrée par le présent cadrage.

## Fonctionnalités incluses

- [FEAT-001 — Créer et consulter plusieurs projets](../../modules/project-management/create-and-view-projects.md).
- [FEAT-002 — Modifier la description d’un projet](../../modules/project-management/edit-project-description.md).
- [FEAT-003 — Archiver et restaurer un projet](../../modules/project-management/archive-and-restore-project.md).
- [FEAT-004 — Préparer les versions successives d’un projet](../../modules/version-management/prepare-project-versions.md).
- [FEAT-005 — Déclarer la livraison d’une version](../../modules/version-management/declare-version-delivery.md).
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](../../modules/version-management/reopen-approved-scoping.md).
- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](../../modules/functional-scoping/conduct-scoping-interview.md).
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](../../modules/functional-scoping/manage-proposals-and-backlog.md).
- [FEAT-009 — Structurer et modifier le catalogue fonctionnel](../../modules/functional-scoping/structure-feature-catalogue.md).
- [FEAT-010 — Valider les trois étapes du cadrage](../../modules/functional-scoping/approve-scoping-stages.md).
- [FEAT-011 — Sauvegarder et reprendre un cadrage](../../modules/continuity/save-and-resume-scoping.md).
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../../modules/continuity/view-functional-history.md).

## Évolutions des fonctionnalités existantes

Aucune : les douze fonctionnalités sont nouvelles pour le produit. Leurs fiches canoniques conservent chacune une section V1, qui pourra servir de référence lors de cadrages ultérieurs.

## Limites et fonctionnalités reportées

- Usage personnel : plusieurs utilisateurs, authentification, partage et collaboration sont reportés.
- Entrées textuelles uniquement : pièces jointes et import de documents sont reportés.
- Le cadrage n’inclut pas les phases UX/UI, architecture technique ou planification du développement.
- Les intégrations GitHub et le développement délégué à des agents sont reportés.
- L’archivage est réversible ; la suppression définitive est reportée.
- La fonction dédiée de reformulation ou d’enrichissement par IA de la description initiale est reportée. L’assistant d’entretien est inclus.
- L’export Markdown est refusé pour V1, sans report futur présumé.
- La synchronisation externe est un sujet évoqué mais non tranché, absent du périmètre.

Ces décisions sont figées pour ce cadrage V1. Le [backlog vivant](../../FUTURE-FEATURES.md) conserve les capacités hors V1 pour de futurs arbitrages, sans modifier le présent périmètre.

## Dépendances et décisions ouvertes

- Tout cadrage se rapporte à un projet et à une version identifiés.
- Le catalogue est préparé à partir d’une synthèse validée ; la validation finale suit celle du catalogue.
- Une seule version par projet est active en cadrage. Les projets distincts conservent leurs propres cadrages.
- Une version suivante peut être préparée avant livraison de la précédente ; le prévu et le confirmé livré restent distingués.
- La reprise du dernier cadrage approuvé et des éléments reportés n’inclut automatiquement aucun élément dans une nouvelle version.
- Une règle indispensable non clarifiée pour une fonctionnalité retenue bloque la validation finale. Une question non bloquante peut rester visible.

Aucune question fonctionnelle bloquante n’est consignée pour V1. Le fournisseur IA, sa configuration et ses coûts, l’adaptation technique des skills, les choix UX/UI, l’architecture et l’exploitation restent à étudier ultérieurement. Aucune disponibilité de service externe n’est présumée vérifiée.

## Traçabilité des décisions de l’entretien

Chaque décision D correspond à la question Q portant le même numéro. La source est la réponse explicite de l’utilisateur dans cette conversation, reprise dans la synthèse.

| Décision | Arbitrage retenu |
| --- | --- |
| D01 / Q1 | Usage personnel ; plusieurs projets ; pas d’authentification ni de gestion de plusieurs utilisateurs en V1 |
| D02 / Q2 | MVP centré sur le cadrage validé ; phases ultérieures et intégrations GitHub reportées |
| D03 / Q3 | Cadrages successifs par projet dès le MVP ; approbation distincte de la livraison |
| D04 / Q4 | Nom, description modifiable, archivage réversible ; suppression définitive reportée ; absence de réécriture automatique des cadrages validés |
| D05 / Q5 | Un cadrage actif par projet ; préparation de la version suivante avant livraison possible ; livraison déclarée par l’utilisateur |
| D06 / Q6 | Synthèse, catalogue puis cadrage final explicitement validés ; critères d’acceptation ; arbitrage des propositions |
| D07 / Q7 | Réouverture avant livraison avec conservation de l’état approuvé et nouvelle validation ; évolutions après livraison dans une nouvelle version |
| D08 / Q8 | Export Markdown refusé pour V1, sans report futur présumé |
| D09 / Q9 | Sauvegarde automatique, reprise après fermeture ou erreur IA, suspension avec questions ouvertes visibles et sans approbation implicite |
| D10 / Q10 | Textes saisis ou collés ; pièces jointes et import reportés ; amélioration dédiée par IA à préciser puis précisée par D14 |
| D11 / Q11 | Modification manuelle des modules, fonctionnalités, critères et décisions avec les mêmes règles de traçabilité et de nouvelle validation |
| D12 / Q12 | Dernier cadrage approuvé et éléments reportés comme contexte ; distinction prévu/livré ; aucune inclusion automatique |
| D13 / Q13 | Questions non bloquantes conservables ; règle indispensable indéterminée bloquant la validation finale jusqu’à clarification ou report |
| D14 / Q14 | Reformulation ou enrichissement dédié de la description par IA reporté ; assistant d’entretien inclus |
| D15 / Q15 | Retour explicite à la version précédente non livrée en suspendant la suivante ; revue des éléments affectés sans réécriture automatique |
| D16 / Q16 | Archive consultable ; restauration avant modification ou poursuite du cadrage ; validations et livraison inchangées |

## Approbations et revue documentaire

- **Synthèse approuvée** : l’utilisateur a répondu « j’approuve » à la demande de validation de la synthèse comme référence pour préparer le catalogue V1.
- **Catalogue et manifeste approuvés** : l’utilisateur a répondu « j’approuve » à la demande de validation des quatre modules, des douze fonctionnalités et des vingt fichiers proposés.
- **Documentation finale approuvée** : l’utilisateur a répondu « j’approuve » à la demande de validation de la documentation générée, glossaire compris, après présentation du rapport d’audit et du diff complet. Le statut de cette fiche est `approved`.
- **Livraison de V1** : aucune livraison confirmée.
- **Commit et push** : ces opérations requièrent des autorisations distinctes de l’approbation documentaire.

La synthèse source a été rédigée avant son approbation. Ses mentions `approval_status: pending` et « cette synthèse n’est pas encore approuvée » sont conservées comme état historique de rédaction, conformément à la copie à l’identique approuvée dans le manifeste. Les approbations postérieures sont attestées ci-dessus ; elles ne réécrivent pas la source.

Empreinte SHA-256 de la copie approuvée : `0DB939D99E851477B5D8586019248F90029C503B5AD895E348DFAE89ECEB00BC`.

## Source de cadrage

[Synthèse approuvée pour V1, conservée à l’identique](SCOPING-SUMMARY.md).
