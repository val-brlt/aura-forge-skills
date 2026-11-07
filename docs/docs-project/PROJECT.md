# Présentation du projet — Aura Forge Project AI

## Objectif et utilisateurs

Aura Forge Project AI est une application web en français qui permet à une personne de transformer une idée de logiciel en cadrage fonctionnel validé, structuré et reprenable. L’utilisateur conserve la maîtrise des décisions : l’IA questionne, clarifie et propose ; les validations importantes restent explicites.

La V1 est le MVP du produit. Elle vise un usage personnel, avec plusieurs projets, sans gestion de plusieurs utilisateurs ni authentification.

## Problèmes rencontrés et résultats attendus

Le produit transpose dans une application persistante des workflows de cadrage aujourd’hui expérimentés avec Codex. Il doit permettre de conserver le contexte entre sessions, de distinguer les propositions des décisions et de préparer les versions suivantes sans perdre les cadrages précédents.

Le résultat attendu est un cadrage consultable dans l’application : synthèse, catalogue des modules et fonctionnalités, critères d’acceptation, décisions, périmètre de version, éléments reportés et questions ouvertes.

## Périmètre fonctionnel

- Créer et consulter plusieurs projets, modifier leur description, les archiver et les restaurer.
- Cadrer les versions successives d’un projet, avec une seule version active en cadrage par projet.
- Mener l’entretien de cadrage avec l’IA à partir de textes saisis ou collés.
- Arbitrer les propositions et modifier manuellement les informations fonctionnelles.
- Valider successivement la synthèse, le catalogue puis le cadrage final.
- Sauvegarder automatiquement le travail, le reprendre et consulter son historique.

## Règles transversales

- Les contenus fonctionnels et l’interface destinés à l’utilisateur sont en français.
- Les informations métier sont structurées et persistantes ; leur représentation technique reste à concevoir.
- Une proposition, une inclusion dans une version, une validation de cadrage et une livraison sont des informations distinctes.
- Une fonctionnalité conserve son identité au fil de ses évolutions ; les règles et décisions de chaque version restent attribuables à cette version.
- Une version suivante peut être cadrée avant livraison de la précédente. Le prévu reste distingué du confirmé livré.
- Les modifications manuelles suivent les mêmes règles de traçabilité et de nouvelle validation que les propositions de l’IA.
- Les workflows `project-scoping` et `structure-project`, appuyés par les procédures d’entretien et de modélisation métier, servent de référence fonctionnelle. Leur adaptation technique à l’application appartient à une phase ultérieure.

Le vocabulaire de référence figure dans le [glossaire du projet](../../GLOSSARY.md).

## Modules

- [Gestion des projets](modules/project-management/MODULE.md) — identité, description, consultation et archivage des projets.
- [Gestion des versions](modules/version-management/MODULE.md) — cadrages successifs, déclaration de livraison et réouverture avant livraison.
- [Cadrage fonctionnel](modules/functional-scoping/MODULE.md) — entretien, propositions, catalogue et validations.
- [Continuité du travail](modules/continuity/MODULE.md) — sauvegarde, reprise et consultation de l’historique.

## Versions

- [V1 — MVP](versions/v1/VERSION.md) : première version du produit, centrée sur le cadrage fonctionnel. Cadrage et documentation approuvés, statut `approved`. Aucune livraison du produit n’est confirmée.

Les références aux versions suivantes des projets gérés décrivent une capacité de V1 ; elles n’engagent pas une future version du produit Aura Forge.

## Évolutions futures et points à clarifier

Le [backlog](FUTURE-FEATURES.md) distingue les capacités reportées, la proposition d’export Markdown refusée pour V1 et le sujet de synchronisation non tranché. Aucune capacité reportée n’a de version future attribuée.

## Décisions encore ouvertes

Aucune question fonctionnelle bloquante n’est consignée pour V1. Le fournisseur IA, les choix UX/UI, l’architecture, les coûts, l’exploitation et les adaptations techniques des skills restent à étudier dans leurs phases respectives.

## Sources et état du cadrage

La [synthèse de cadrage](versions/v1/SCOPING-SUMMARY.md) est conservée à l’identique. Les approbations de la synthèse, du catalogue et de la documentation sont attestées dans la [fiche V1](versions/v1/VERSION.md).
