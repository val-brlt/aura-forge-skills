---
id: FEAT-001
module: project-management
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-001 — Créer et consulter plusieurs projets

## Objectif utilisateur

Conserver plusieurs idées de logiciels comme des projets distincts et retrouver les informations de chacun.

## Comportement attendu

L’utilisateur crée et consulte plusieurs projets, chacun identifié par un nom et une description initiale libre. Les informations et cadrages restent rattachés au projet concerné. V1 vise un usage personnel sans authentification ni gestion de plusieurs utilisateurs.

## Historique fonctionnel par version

### V1

**Comportement validé :** création et consultation de plusieurs projets à partir de textes saisis ou collés, avec un nom et une description pour chacun.

**Critères d’acceptation validés :**

- L’utilisateur peut créer au moins deux projets distincts, chacun avec son nom et sa description.
- Il peut consulter les informations de chaque projet et retrouver les cadrages qui lui sont associés.
- Les informations d’un projet restent distinctes de celles des autres projets.
- La création et la consultation ne nécessitent ni gestion de plusieurs utilisateurs ni authentification dans V1.

**Source :** [Synthèse V1 — usage personnel et projets](../../versions/v1/SCOPING-SUMMARY.md#1-usage-personnel-et-projets), D01, D04 et description initiale.

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-011 — Sauvegarder et reprendre un cadrage](../continuity/save-and-resume-scoping.md) pour la continuité des informations rattachées au projet.
- [FEAT-004 — Préparer les versions successives d’un projet](../version-management/prepare-project-versions.md) pour ses cadrages par version.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. Les écrans et la navigation sont décrits dans les [livrables UX approuvés](../../versions/v1/ux/UX-SUMMARY.md).

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D01 et D04. Le découpage FEAT-001 a été explicitement approuvé avec le catalogue. Sa présence dans V1 ne constitue pas une confirmation de livraison.
