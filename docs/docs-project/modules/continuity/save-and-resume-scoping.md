---
id: FEAT-011
module: continuity
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-011 — Sauvegarder et reprendre un cadrage

## Objectif utilisateur

Reprendre le travail de cadrage entre sessions ou après une erreur de l’assistant, en retrouvant les informations et décisions conservées.

## Comportement attendu

L’entretien et les décisions sont sauvegardés automatiquement. Les informations du projet, de la version et du catalogue sont persistantes et exploitables dans l’application. Après fermeture ou erreur IA, l’utilisateur peut reprendre à partir du travail sauvegardé.

L’utilisateur peut suspendre un entretien incomplet ; sa couverture partielle et ses questions ouvertes restent visibles. Une interruption, une reprise ou une erreur ne transforme jamais une proposition en décision approuvée.

Les échanges et brouillons du fil général restent propres au projet, distincts des discussions liées aux questions. Changer de projet ne mélange ni messages ni saisies ; changer de version consultée d’un même projet conserve son fil général et le contexte de version des échanges. Après une erreur de réponse, le message utilisateur reste disponible et le réessai ne le duplique pas. Une erreur de sauvegarde signale que les changements restent dans la session et invite à réessayer avant fermeture.

L’archivage conserve les échanges en consultation seule ; la restauration précède toute nouvelle saisie.

## Historique fonctionnel par version

### V1

**Comportement validé :** sauvegarde automatique de l’entretien et des décisions, reprise entre sessions et après erreur, avec suspension explicite d’un travail partiel. Les échanges et brouillons généraux sont conservés par projet, avec le contexte de version identifiable.

**Critères d’acceptation validés :**

- L’entretien et les décisions sont sauvegardés automatiquement.
- Après fermeture de session, l’utilisateur peut retrouver l’entretien et les décisions sauvegardés pour le projet et la version concernés.
- Après une erreur de l’assistant, le travail sauvegardé reste reprenable.
- Les informations fonctionnelles conservées restent consultables et réutilisables dans l’application.
- L’utilisateur peut suspendre un entretien incomplet avec une couverture partielle indiquée et les questions ouvertes visibles.
- Une suspension, une erreur ou une reprise n’accorde aucune approbation implicite.
- Les échanges et les brouillons du fil général restent associés à leur projet ; la consultation d’un autre projet ne mélange pas ses messages ou sa saisie.
- Le changement de version consultée d’un même projet ne fait pas perdre son fil général ; les échanges restent attribuables à leur contexte de version.
- Après une erreur de réponse, le message utilisateur reste disponible et le réessai ne le duplique pas.
- L’archivage conserve la consultation du fil ; une nouvelle saisie exige la restauration du projet.
- Une erreur de sauvegarde indique que les changements restent dans la session et permet de réessayer sans prétendre qu’ils sont enregistrés.

**Source :** [Synthèse V1 — persistance, interruption et reprise](../../versions/v1/SCOPING-SUMMARY.md#5-persistance-interruption-et-reprise), description initiale et D09, D13.

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- Le cadrage sauvegardé se rapporte à un [projet](../project-management/create-and-view-projects.md) et à une [version](../version-management/prepare-project-versions.md) identifiés. Le fil général appartient au projet, avec le contexte de version des échanges conservé.
- Les conditions de validation finale restent celles de [FEAT-010 — Valider les trois étapes du cadrage](../functional-scoping/approve-scoping-stages.md), même après une reprise.
- Un [projet archivé](../project-management/archive-and-restore-project.md) doit être restauré avant de poursuivre son cadrage.

## Questions ouvertes

Aucune question fonctionnelle bloquante consignée. Les mécanismes cibles de sauvegarde, erreurs et stockage sont définis dans la [conception technique approuvée](../../versions/v1/architecture/TECHNICAL-DESIGN.md). Aucune sauvegarde/restauration applicative réelle n’est attestée. Toute opération IA, reprise de thread comprise, doit redemander explicitement `output_mode=structured` ; le backend garde contexte, révisions, provenance et idempotence, sans nouvelle promesse de disponibilité ou de délai.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de la description initiale et de D09 ; D13 distingue la suspension partielle de la validation finale. Son découpage a été approuvé avec le catalogue.
