---
scope_id: mvp
scope_kind: mvp
status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# Objectif MVP — Aura Forge Project AI

## Objectifs et critères de réussite

Permettre à une personne de transformer une idée de logiciel en cadrage fonctionnel validé, structuré, conservé et reprenable dans une application web en français. Cet objectif global peut être réalisé par plusieurs livraisons ; il ne désigne aucune version logicielle.

Ce document consolide les exigences déjà approuvées dans la référence historique V1 et les fiches canoniques, D01–D17 compris. `status: approved` reprend exclusivement ces approbations : les adaptations proposées dans FEAT-004/005/006, une nouvelle UX et une migration technique restent à valider.

- Plusieurs projets conservent leurs informations distinctes, avec description modifiable, archivage consultable et restauration avant modification : critères de FEAT-001 à FEAT-003.
- Cadrages successifs, références approuvées et informations de livraison restent distingués et consultables sans perte d’identité fonctionnelle : critères approuvés de FEAT-004 à FEAT-006 et FEAT-012. Les règles historiques par version restent la baseline de comportement tant que l’adaptation proposée n’est pas validée.
- L’entretien textuel en français propose des questions, recommandations et interprétations à confirmer ; les propositions sont arbitrées et le catalogue possède des critères vérifiables : FEAT-007 à FEAT-009.
- Synthèse, catalogue et cadrage final reçoivent trois validations explicites ; les règles indispensables indéterminées bloquent la validation jusqu’à clarification ou report : FEAT-010.
- Travail, discussions et brouillons sont reprenables dans leur contexte après fermeture ou erreur ; un réessai ne duplique pas le message utilisateur : FEAT-011.

Les critères détaillés restent dans les fiches liées ci-dessous ; aucun seuil supplémentaire n’est créé.

## Fonctionnalités incluses

- [FEAT-001 — Créer et consulter plusieurs projets](modules/project-management/create-and-view-projects.md).
- [FEAT-002 — Modifier la description d’un projet](modules/project-management/edit-project-description.md).
- [FEAT-003 — Archiver et restaurer un projet](modules/project-management/archive-and-restore-project.md).
- [FEAT-004 — Préparer les versions successives d’un projet](modules/version-management/prepare-project-versions.md).
- [FEAT-005 — Déclarer la livraison d’une version](modules/version-management/declare-version-delivery.md).
- [FEAT-006 — Rouvrir un cadrage approuvé avant livraison](modules/version-management/reopen-approved-scoping.md).
- [FEAT-007 — Mener l’entretien de cadrage avec l’IA](modules/functional-scoping/conduct-scoping-interview.md).
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](modules/functional-scoping/manage-proposals-and-backlog.md).
- [FEAT-009 — Structurer et modifier le catalogue fonctionnel](modules/functional-scoping/structure-feature-catalogue.md).
- [FEAT-010 — Valider les trois étapes du cadrage](modules/functional-scoping/approve-scoping-stages.md).
- [FEAT-011 — Sauvegarder et reprendre un cadrage](modules/continuity/save-and-resume-scoping.md).
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](modules/continuity/view-functional-history.md).

La discussion générale du projet appartient à FEAT-007 et FEAT-011 ; elle ne crée pas de treizième fonctionnalité.

## Dépendances et décisions ouvertes

Les dépendances fonctionnelles restent celles des fiches, sans ordre de livraison déduit de leur numérotation. Le catalogue dépend de la synthèse validée, puis le cadrage final du catalogue validé. Références, révisions, contextes et trois validations doivent rester cohérents dans la [conception UX](versions/v1/ux/UX-SUMMARY.md) et l’[architecture approuvée](architecture/ARCHITECTURE.md).

La séparation MVP/releases ne décide pas à elle seule la nouvelle règle d’activité du cadrage dans l’application, la déclaration d’une livraison partielle ou la réouverture du reliquat. Les propositions figurent dans les sections de critères proposés/questions ouvertes de FEAT-004/005/006, avec leurs effets sur catalogue, historique, UX et données. Aucune proposition n’est un critère approuvé de ce MVP.

La planification future proposera le découpage en tranches, analysera les dépendances fonctionnelles/UX/techniques et soumettra les affectations de releases à validation humaine. Aucune release, date ou tâche de développement n’est attribuée ici.

## Limites et exclusions

Usage personnel, textes saisis ou collés uniquement. Plusieurs utilisateurs, authentification, collaboration, partage, pièces jointes/import, suppression définitive et enrichissement dédié de description restent reportés. Les phases UX, architecture, planification, GitHub et développement des projets gérés restent hors MVP. L’export Markdown est refusé pour le périmètre historique ; la synchronisation externe reste non tranchée. Voir le [backlog unique](FUTURE-FEATURES.md).

Les livrables UX/architecture de cette documentation conçoivent Aura Forge lui-même ; ils n’activent pas ces phases pour les projets gérés. Seul Codex local est prévu au MVP ; API directe, modèles locaux, serveur privé et paquet Windows autonome restent ultérieurs, sans release attribuée.

## Avancement de l’objectif MVP

Jalon MVP **ouvert**. Cadrage, galerie et architecture sont approuvés pour la référence historique ; aucune application de production, réalisation complète ou livraison du produit n’est attestée. Les contrats déclarent l’avancement de développement/livraison `unknown`, des affectations et un registre de releases vides. Une approbation documentaire n’est pas une preuve d’avancement logiciel.

Une livraison partielle ne suffit pas à terminer une fonctionnalité. L’achèvement du MVP exigera les preuves de satisfaction de tous ses critères et la livraison de toutes ses fonctionnalités indispensables. Les critères de stabilité du contrat public et l’acceptation de la première version stable restent distincts et à définir ; aucun équivalent SemVer n’est inféré de `v1`.

## Source de cadrage

- [Synthèse historique approuvée, conservée à l’identique](versions/v1/SCOPING-SUMMARY.md).
- [Périmètre et preuves d’approbation V1](versions/v1/VERSION.md).
- [Provenance historique D17 — discussion générale](versions/v1/SCOPING-ADDENDUM.md).

Ces documents conservent leurs identités historiques, formulations et validations. La présente consolidation ne les remplace pas.
