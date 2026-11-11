---
status: accepted
date: 2026-11-10
---

# Adapter les mêmes skills avec une sortie structurée pour Aura Forge

Les skills locaux de cadrage pilotent actuellement fichiers, scratch et revues documentaires. Aura Forge conserve ses données dans SQLite et expose trois validations explicites dans son interface. Deux adaptations ont été comparées : instructions et propositions structurées pour le backend, ou travail documentaire dans un workspace interne puis import. Après discussion d’un parent dédié, l’utilisateur a proposé les mêmes skills à deux modes et répondu « ça me parait ok » à leur définition le 10 novembre 2026.

Les skills locaux concernés auront un tronc de règles fonctionnelles commun et un paramètre `output_mode` séparant `files` et `structured`. Le mode `files`, par défaut pour les usages documentaires historiques, conserve leur comportement. Aura Forge demande explicitement `structured` à chaque opération et propage ce mode aux instructions dépendantes. Aucun parent supplémentaire n’est nécessaire. Les skills tiers d’origine n’ont pas besoin d’être modifiés.

En mode `structured`, Python fournit tâche, contexte et schéma attendu, puis contrôle et enregistre les propositions renvoyées par Codex. Le modèle ne produit pas de SQL à exécuter et n’écrit ni base, ni fichiers métier ou Git. Questions, interprétation, synthèse et catalogue ont des formats adaptés ; une simple liste ne suffit pas à toutes les tâches. Une erreur de format ne bascule pas vers `files`. Le `mode=preview|apply|audit` existant de structure-project reste distinct du mode de sortie et n’accorde pas de droit SQLite au modèle.

Le backend contrôle les transitions, les références et révisions, l’idempotence et les validations humaines. Les consignes documentaires d’écriture, scratch et Git ne deviennent pas des actions du produit. L’autre adaptation aurait conservé un miroir de fichiers à produire, analyser et synchroniser avec SQLite. Le parent dédié aurait isolé les instructions applicatives, avec une autre organisation à maintenir. La solution acceptée réutilise un même ensemble de règles avec deux branches dont il faudra vérifier la cohérence.

Les permissions techniques doivent être configurées et vérifiées : `deny_all` correspond à `approvalPolicy=never`, sans désactiver tous les outils ; read_only et cwd ne démontrent pas un confinement des lectures. Les instructions ne constituent pas une barrière d’accès. L’intégration doit limiter les capacités non nécessaires et établir leur état effectif avant usage des données réelles. Aucun test de confinement, inférence ou modification de skill n’est réalisé par cette décision.

Sources : [project-scoping](../../.agents/skills/project-scoping/SKILL.md), [structure-project](../../.agents/skills/structure-project/SKILL.md), [SDK Python](https://learn.chatgpt.com/docs/codex-sdk), [permissions](https://learn.chatgpt.com/docs/agent-approvals-security), [configuration](https://learn.chatgpt.com/docs/config-file/config-reference). Portée : [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Le dossier intégré reste à approuver.
