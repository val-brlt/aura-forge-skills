---
version: v1
status: approved
scope: versions/v1/VERSION.md
---

# Conception UX/UI — V1

## Objectifs et parcours principaux

Transformer une idée en cadrage fonctionnel conservé, compréhensible et explicitement validé. L’usage est personnel, en français, avec plusieurs projets et des entrées textuelles. Le [MVP global](../../../MVP.md) consolide les douze fonctionnalités indépendamment des releases. Le [périmètre historique V1](../VERSION.md) et ses fiches définissent les comportements approuvés de cette galerie ; le [contrat UX](UX-CONTRACT.json) relie les douze fonctionnalités aux sept parcours, onze écrans et interactions validés.

- Créer, retrouver, modifier, archiver et restaurer ses projets ; consulter les décisions et références antérieures (FLOW-001, FLOW-006).
- Préparer les versions, déclarer une livraison et rouvrir un cadrage approuvé non livré, avec conservation de la référence et revue des éléments affectés (FLOW-002).
- Analyser l’idée, répondre, reprendre le travail, arbitrer les propositions et corriger le catalogue (FLOW-003, FLOW-004).
- Valider successivement la synthèse, le catalogue et le cadrage final, après clarification ou report des règles indispensables (FLOW-005).
- Explorer le projet dans une discussion générale distincte des discussions de questions (FLOW-007).

## Navigation et décisions de conception

« Mes projets » rassemble les projets avec les filtres « En cours » et « Archivés ». Dans un projet, le menu donne accès à la vue d’ensemble, la discussion IA, les versions et l’historique. Le nom reste dans l’en-tête ; le menu ne répète ni « Projet ouvert », ni le nom, ni un titre « Projet ». La section « Étapes de travail » ne contient que le cadrage fonctionnel en V1 ; ses questions, synthèse, catalogue, cadrage final et décisions/reportés disposent d’une navigation locale.

Les questions structurées présentent le contexte, la recommandation et sa justification. L’utilisateur peut appliquer la recommandation ou relire et corriger l’interprétation de sa réponse libre avant confirmation. L’analyse prépare les questions ; elle n’ajoute aucune validation métier. Les propositions sont arbitrées dans le cadrage, avec acceptation et inclusion séparées. Les corrections sont tracées et imposent une nouvelle validation des résultats affectés.

Le fil général appartient au projet et reste conservé entre ses versions, avec le contexte des échanges identifiable. Messages et brouillons restent séparés entre projets et discussions de questions. Les échanges affichent le Markdown ; Entrée envoie, Maj+Entrée ajoute une ligne et la composition du texte est respectée. Un réessai ne duplique pas le message utilisateur. Discuter ne modifie automatiquement ni description, ni arbitrage, ni catalogue, ni validation, ni livraison ; l’exploration reste possible sur une version approuvée ou livrée. Une archive reste consultable et exige restauration avant saisie.

Un seul cadrage est actif par projet. Les reports ne sont jamais inclus automatiquement dans une nouvelle version. Réouverture, suspension et consultation historique préservent les références sans réécriture automatique. Les trois validations sont explicites ; silence, erreur et suspension n’approuvent rien. La livraison possède sa déclaration propre. Les identifiants V1/V2 de démonstration ne sont pas convertis en releases SemVer. La séparation applicative entre objectif MVP, cadrages et livraisons requiert une revue ciblée de FLOW-001/002/004/005/006/007, principalement SCREEN-003/004, et de leurs contextes SCREEN-002/005/006/007/008/009/010/011 ; elle reste proposée dans FEAT-004/005/006. Les onze écrans et interactions du présent contrat restent la référence approuvée.

Thème sombre par défaut, bascule claire dans l’en-tête, palette ardoise/lavande et police locale Segoe UI. Les [conventions partagées](../../../ux/DESIGN-GUIDELINES.md) précisent navigation, composants, messages et adaptation mobile. Les dialogues et panneaux sont des états des écrans concernés, sans nouveaux écrans autonomes. Tous les écrans de la référence approuvée correspondent à la première conception du produit. Les variantes de revue restent distinctes et ne remplacent pas cette galerie avant approbation.

## Maquettes validées

[Ouvrir les maquettes HTML approuvées](mockups/index.html).

La galerie R3 complète a été approuvée le 8 novembre 2026 par « ok je valide les maquettes ». Ses cinq fichiers HTML/CSS/JavaScript sont conservés à l’identique, autonomes et utilisables hors ligne. Les commandes d’exploration des états, identifiants d’écran et bandeau de proposition appartiennent au support de revue. Les versions Atelier et La Fabrique, ainsi que leurs propositions de réservation ou paiement, sont des exemples de projets gérés ; elles n’étendent pas le périmètre du produit Aura Forge.

## Anticipation des évolutions futures (hors périmètre)

La [vision du produit](../../../PROJECT.md) et le [backlog futur](../../../FUTURE-FEATURES.md) envisagent UX/UI, architecture, planification, GitHub et développement des projets gérés. La séparation entre contexte projet/version et étapes de travail permet une extension ultérieure de la navigation, sans phase future visible ni écran supplémentaire en V1 et sans attribution à une version future.

Authentification, collaboration, partage, fichiers, suppression définitive et enrichissement dédié de la description restent exclus. L’export Markdown est refusé pour V1 sans report présumé ; la synchronisation externe reste non tranchée et hors périmètre. Ces distinctions sont conservées dans `futureConsiderations`, sans couverture fonctionnelle V1 artificielle.

## Accessibilité, limites et questions ouvertes

Libellés associés, erreurs au champ, focus visible, lien d’évitement, dialogues nommés, statuts textuels et Markdown sémantique avec HTML brut échappé. Sur mobile, les colonnes s’empilent et les défilements horizontaux sont limités aux questions et sous-onglets ; l’élément actif reste visible. Les panneaux de validation et de contexte suivent leur document ou discussion. La préférence de réduction du mouvement est respectée.

Les contrôles antérieurs ont mesuré, en sombre/clair, des contrastes de 7,90:1 / 7,62:1 pour le bouton principal, 13,98:1 / 14,86:1 pour le texte principal, 7,63:1 / 5,67:1 pour le texte secondaire et 3,75:1 / 3,20:1 pour les contours de champs. Ils ne constituent pas un audit WCAG exhaustif ni une campagne complète avec lecteur d’écran.

Aucun point UX bloquant. La galerie utilise des données fictives en mémoire ; analyses, interprétations, réponses IA, sauvegardes, erreurs et reprises sont simulées. L’[architecture](../../../architecture/ARCHITECTURE.md) est approuvée : Python/FastAPI, Vue/TypeScript, SQLite, Codex app-server et HTTP JSON/SSE. Intégration, compte/coût, permissions effectives et restauration restent à vérifier ; aucune de ces capacités n’est démontrée par la galerie. L’approbation des documents et maquettes n’atteste ni implémentation ni livraison : la V1 reste `approved`, sans livraison confirmée. Le contrat UX utilise désormais l’enveloppe 2 avec avancement explicite, sans changer les données de parcours/écrans approuvées : baseline `v1`, scope historique, développement/livraison inconnus, aucune release ni affectation, jalon ouvert. Cette migration de format ne valide aucune nouvelle UX. La planification ultérieure devra croiser périmètre, UX et architecture validés, sans déduire un ticket par écran ni assimiler couverture de conception et livraison.
