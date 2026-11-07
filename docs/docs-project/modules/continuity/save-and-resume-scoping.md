---
id: FEAT-011
module: continuity
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-011 — Sauvegarder et reprendre un cadrage

## Objectif utilisateur

Reprendre le travail de cadrage entre sessions ou après une erreur de l’assistant, en retrouvant les informations et décisions conservées.

## Comportement attendu

L’entretien et les décisions sont sauvegardés automatiquement. Les informations du projet, de la version et du catalogue sont persistantes et exploitables dans l’application. Après fermeture ou erreur IA, l’utilisateur peut reprendre à partir du travail sauvegardé.

L’utilisateur peut suspendre un entretien incomplet ; sa couverture partielle et ses questions ouvertes restent visibles. Une interruption, une reprise ou une erreur ne transforme jamais une proposition en décision approuvée.

## Historique fonctionnel par version

### V1

**Comportement validé :** sauvegarde automatique de l’entretien et des décisions, reprise entre sessions et après erreur, avec suspension explicite d’un travail partiel.

**Critères d’acceptation validés :**

- L’entretien et les décisions sont sauvegardés automatiquement.
- Après fermeture de session, l’utilisateur peut retrouver l’entretien et les décisions sauvegardés pour le projet et la version concernés.
- Après une erreur de l’assistant, le travail sauvegardé reste reprenable.
- Les informations fonctionnelles conservées restent consultables et réutilisables dans l’application.
- L’utilisateur peut suspendre un entretien incomplet avec une couverture partielle indiquée et les questions ouvertes visibles.
- Une suspension, une erreur ou une reprise n’accorde aucune approbation implicite.

**Source :** [Synthèse V1 — persistance, interruption et reprise](../../versions/v1/SCOPING-SUMMARY.md#5-persistance-interruption-et-reprise), description initiale et D09, D13.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- Le travail sauvegardé se rapporte à un [projet](../project-management/create-and-view-projects.md) et à une [version](../version-management/prepare-project-versions.md) identifiés.
- Les conditions de validation finale restent celles de [FEAT-010 — Valider les trois étapes du cadrage](../functional-scoping/approve-scoping-stages.md), même après une reprise.
- Un [projet archivé](../project-management/archive-and-restore-project.md) doit être restauré avant de poursuivre son cadrage.

## Questions ouvertes

Aucune question fonctionnelle bloquante consignée. Les mécanismes de sauvegarde, de gestion des erreurs et de stockage seront définis dans la phase technique, sans promesse supplémentaire de disponibilité ou de délai dans ce cadrage.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de la description initiale et de D09 ; D13 distingue la suspension partielle de la validation finale. Son découpage a été approuvé avec le catalogue.
