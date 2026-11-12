# Présentation du projet — Aura Forge Project AI

## Objectif et utilisateurs

Aura Forge Project AI est une application web en français qui permet à une personne de transformer une idée de logiciel en cadrage fonctionnel validé, structuré et reprenable. L’utilisateur conserve la maîtrise des décisions : l’IA questionne, clarifie et propose ; les validations importantes restent explicites.

Le [MVP](MVP.md) est l’objectif fonctionnel global : usage personnel, plusieurs projets, sans gestion de plusieurs utilisateurs ni authentification. Il peut être réalisé par plusieurs livraisons. La référence historique V1 conserve le périmètre approuvé, sans équivalent SemVer attribué.

## Problèmes rencontrés et résultats attendus

Le produit transpose dans une application persistante des workflows de cadrage aujourd’hui expérimentés avec Codex. Il doit permettre de conserver le contexte entre sessions, de distinguer les propositions des décisions et de préparer les versions suivantes sans perdre les cadrages précédents.

Le résultat attendu est un cadrage consultable dans l’application : synthèse, catalogue des modules et fonctionnalités, critères d’acceptation, décisions, périmètre de version, éléments reportés et questions ouvertes.

## Périmètre fonctionnel

- Créer et consulter plusieurs projets, modifier leur description, les archiver et les restaurer.
- Cadrer les versions successives d’un projet, avec une seule version active en cadrage par projet.
- Mener le cadrage avec l’IA à partir de textes saisis ou collés : questions structurées, recommandations et réponses libres à confirmer.
- Explorer les besoins dans une discussion générale propre au projet, distincte des discussions liées aux questions et conservée entre les versions consultées.
- Arbitrer les propositions et modifier manuellement les informations fonctionnelles.
- Valider successivement la synthèse, le catalogue puis le cadrage final.
- Sauvegarder automatiquement le travail, le reprendre et consulter son historique.

## Règles transversales

- Les contenus fonctionnels et l’interface destinés à l’utilisateur sont en français.
- Les informations métier sont structurées et persistantes. Leur représentation cible est définie dans la [conception technique approuvée](versions/v1/architecture/TECHNICAL-DESIGN.md) ; aucune base produit ni intégration opérationnelle n’est attestée.
- Le MVP est indépendant des versions logicielles `MAJOR.MINOR.PATCH`. Approbation, planification, développement et livraison restent distincts ; une livraison partielle ne termine pas automatiquement une fonctionnalité ou le MVP.
- Le découpage du MVP et le premier numéro de release restent à la future planification, après analyse des dépendances et validation humaine. La première version stable exige ses propres critères, distincts de l’achèvement du MVP.
- Une proposition, une inclusion dans une version, une validation de cadrage et une livraison sont des informations distinctes.
- Une fonctionnalité conserve son identité au fil de ses évolutions ; les règles et décisions de chaque version restent attribuables à cette version.
- Une discussion ne modifie automatiquement ni description, ni arbitrage, ni catalogue, ni validation, ni livraison. Les échanges généraux et leurs brouillons restent propres au projet ; le contexte de version des messages reste identifiable.
- Un projet archivé reste consultable, échanges compris ; sa restauration précède toute modification ou nouvelle saisie.
- Une version suivante peut être cadrée avant livraison de la précédente. Le prévu reste distingué du confirmé livré.
- Les modifications manuelles suivent les mêmes règles de traçabilité et de nouvelle validation que les propositions de l’IA.
- Les workflows `project-scoping` et `structure-project` servent de référence fonctionnelle. Leur adaptation est approuvée par l’[ADR-0009](../adr/0009-dual-output-skills-and-structured-proposals.md) : mode documentaire `files`, propositions applicatives `structured`, avec validation et persistance sous l’autorité du backend Python. Les skills installés ne décrivent pas encore `output_mode` ; leur adaptation et leur intégration restent à réaliser et à vérifier.

Le vocabulaire de référence figure dans le [glossaire du projet](../../GLOSSARY.md).

## Modules

- [Gestion des projets](modules/project-management/MODULE.md) — identité, description, consultation et archivage des projets.
- [Gestion des versions](modules/version-management/MODULE.md) — cadrages successifs, déclaration de livraison et réouverture avant livraison.
- [Cadrage fonctionnel](modules/functional-scoping/MODULE.md) — entretien, propositions, catalogue et validations.
- [Continuité du travail](modules/continuity/MODULE.md) — sauvegarde, reprise et consultation de l’historique.

## Versions

- [Objectif MVP](MVP.md) : consolidation des mêmes douze fonctionnalités approuvées, sans attribution de release.
- [V1 — référence historique approuvée](versions/v1/VERSION.md) : cadrage, décisions et preuves conservés à leur emplacement, statut `approved`. L’ancien intitulé « V1 — MVP » et `release_kind: mvp` restent historiques ; aucune conversion en `1.0.0` ou `0.1.0`.

Aucune release logicielle du produit n’est attribuée ou confirmée livrée. Les identifiants de baseline `v1` des contrats UX/architecture ne sont pas des numéros de logiciel.

Les références aux versions suivantes des projets gérés décrivent une capacité de V1 ; elles n’engagent pas une future version du produit Aura Forge.

## Évolutions futures et points à clarifier

Le [backlog](FUTURE-FEATURES.md) distingue les capacités reportées, la proposition d’export Markdown refusée pour V1 et le sujet de synchronisation non tranché. Aucune capacité reportée n’a de version future attribuée.

## Décisions encore ouvertes

La référence V1 approuvée ne comporte pas de question fonctionnelle bloquante. La séparation documentaire MVP/releases est retenue ; les modalités produit de cadrage autonome, activité unique, livraison partielle et réouverture du reliquat restent proposées dans [FEAT-004](modules/version-management/prepare-project-versions.md), [FEAT-005](modules/version-management/declare-version-delivery.md) et [FEAT-006](modules/version-management/reopen-approved-scoping.md). Les règles historiques par version restent la baseline tant que cette adaptation fonctionnelle et UX n’est pas validée.

L’[architecture](architecture/ARCHITECTURE.md) est approuvée : exécution locale, Codex app-server, Python/FastAPI, Vue/TypeScript, SQLite et HTTP JSON/SSE. Compte/coût, compatibilité, permissions effectives et restauration restent à vérifier lors de la réalisation ; aucun fonctionnement réel n’est garanti par ces décisions.

La [synthèse UX](versions/v1/ux/UX-SUMMARY.md), le [contrat UX](versions/v1/ux/UX-CONTRACT.json) et les [maquettes HTML approuvées](versions/v1/ux/mockups/index.html) décrivent l’expérience validée de V1. Cette approbation ne confirme aucune livraison.

## Sources et état du cadrage

La [synthèse de cadrage](versions/v1/SCOPING-SUMMARY.md) est conservée à l’identique. Les approbations de la synthèse, du catalogue et de la documentation sont attestées dans la [fiche V1](versions/v1/VERSION.md). Les mentions historiques de choix techniques encore ouverts décrivent l’état de cette phase ; les décisions techniques courantes figurent dans l’architecture approuvée, sans réécrire ces preuves.
