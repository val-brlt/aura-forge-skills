---
status: accepted
date: 2026-11-09
---

# Utiliser Python et FastAPI pour le backend

Le MVP doit piloter [Codex app-server local](0002-codex-app-server.md), conserver les données de cadrage et contrôler des validations explicites. Trois backends ont été comparés : TypeScript/Node.js avec Fastify, Python avec FastAPI, et C#/ASP.NET Core. TypeScript était initialement recommandé pour le contrôle direct du protocole et ses types générés. L’utilisateur a demandé de vérifier la couverture Python ; l’examen du SDK officiel publié `openai-codex 0.167.0` a confirmé les flux, reprises, sorties structurées et commandes de contrôle nécessaires.

La recommandation a été révisée en faveur de Python + FastAPI pour réduire le raccordement protocolaire. L’utilisateur a accepté : « ok on part sur python alors ça sera mieux », en réponse à cette proposition explicite le 9 novembre 2026. Le backend utilisera le SDK Python officiel pour app-server ; le frontend et la persistance restent à décider séparément.

Le SDK fournit transport, routage, modèles générés et façade asynchrone, avec runtime Codex épinglé. TypeScript garderait l’intérêt d’un contrôle direct ; C# reste viable, sans préférence ni besoin établi justifiant son raccordement spécifique. Le choix de Python n’établit aucun gain chiffré de performance ou de coût.

Le compromis est une dépendance au SDK et à sa version de runtime. Les limites du compte et les permissions fines demandent des accès de plus bas niveau ; les valeurs de permissions par défaut doivent être configurées explicitement. L’audit du code n’est pas un test en fonctionnement : Windows, session ChatGPT, quotas et reprise restent à vérifier. Les règles métier, la persistance et les validations restent sous l’autorité d’Aura Forge.

Références consultées le 9 novembre 2026 : [SDK officiel](https://learn.chatgpt.com/docs/codex-sdk#python-library), [FastAPI](https://fastapi.tiangolo.com/tutorial/body/), paquet publié `openai-codex 0.167.0` dont les métadonnées épinglent `openai-codex-cli-bin==0.167.0`. Portée : [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Cette décision ne vaut pas approbation du dossier d’architecture complet ou livraison.
