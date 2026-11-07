---
id: FEAT-002
module: project-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-002 — Modifier la description d’un projet

## Objectif utilisateur

Faire évoluer la description initiale du projet sans altérer silencieusement les cadrages déjà approuvés.

## Comportement attendu

L’utilisateur modifie le texte libre décrivant son projet. La modification ne réécrit pas automatiquement ses cadrages validés ni leurs décisions. L’enrichissement ou la reformulation dédiée de la description par IA est reporté ; l’assistant de cadrage reste disponible dans sa propre phase.

## Historique fonctionnel par version

### V1

**Comportement validé :** modification manuelle de la description initiale par texte saisi ou collé, sans réécriture automatique des cadrages validés.

**Critères d’acceptation validés :**

- La description libre d’un projet peut être modifiée manuellement.
- La nouvelle description est consultable pour le projet concerné.
- Un cadrage approuvé existant conserve son contenu après cette modification tant qu’il n’a pas fait l’objet d’une réouverture et d’une nouvelle validation explicites.
- La fonction dédiée d’amélioration de la description par IA ne fait pas partie de V1.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), D04, D10 et D14.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-001 — Créer et consulter plusieurs projets](create-and-view-projects.md) : la description appartient à un projet identifié.
- [FEAT-003 — Archiver et restaurer un projet](archive-and-restore-project.md) : un projet archivé doit être restauré avant modification.
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](../version-management/reopen-approved-scoping.md) si l’utilisateur souhaite aussi corriger le cadrage approuvé.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D04 et D10 ; D14 précise la capacité d’amélioration dédiée reportée. Son découpage a été approuvé avec le catalogue. Le [backlog](../../FUTURE-FEATURES.md) conserve cette amélioration sans version future attribuée.
