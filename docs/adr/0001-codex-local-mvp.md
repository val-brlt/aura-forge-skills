---
status: accepted
date: 2026-11-09
---

# Utiliser Codex local pour le MVP

Aura Forge V1 a besoin d’un assistant de cadrage et de sorties structurées, tout en conservant les validations sous le contrôle de l’utilisateur. Une API de modèle directe était initialement recommandée pour réduire la dépendance au runtime agent et faciliter le futur hébergement. L’utilisateur a choisi Codex local pour privilégier son accès existant et éviter une dépense supplémentaire : « enfaite je voudrais faire tous mais dans un premier temps faire avec codex en local pour ne pas payer en plus ».

Le MVP doit donc intégrer Codex sur le poste, en visant la connexion ChatGPT plutôt qu’une clé API. Ce choix ajoute la gestion d’un processus, de permissions et de sessions Codex. Il ne sélectionne pas de langage backend ni de SDK. Une décision séparée, [ADR-0002](0002-codex-app-server.md), retient ensuite la liaison app-server.

Les [modes d’authentification](https://learn.chatgpt.com/docs/auth) et les [conditions d’usage](https://learn.chatgpt.com/docs/pricing?codex-pricing-plans=individual), consultés le 9 novembre 2026, ne prouvent pas les droits ni le solde de l’utilisateur. Aucune gratuité ou capacité illimitée n’est garantie. L’application ne doit pas acheter de crédits ni basculer automatiquement vers une API payante ; la compatibilité du compte réel avec l’objectif sans surcoût reste à vérifier.

Une API directe et des modèles locaux restent souhaités ultérieurement, sans version attribuée. Le MVP ne comprend que le connecteur Codex ; les données et règles métier doivent permettre ces ajouts sans dépendre exclusivement de son historique de sessions. La migration vers un serveur privé réexaminera le mode d’accès autorisé. Un modèle local dès le MVP n’a pas été retenu : aucun besoin prioritaire d’inférence hors ligne, matériel ou niveau de qualité validé ne le justifie dans ce premier temps.

Portée : [conception technique V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Cette décision ne vaut pas approbation du dossier d’architecture complet ni livraison.
