---
status: accepted
date: 2026-11-10
---

# Utiliser HTTP JSON et SSE entre Vue et FastAPI

Aura Forge V1 combine des actions utilisateur ponctuelles, des sauvegardes et des états de réponse IA produits par le serveur. L’interface Vue et FastAPI sont servis sur la même origine ; Codex reste une dépendance du backend via stdio. HTTP JSON avec SSE, WebSocket bidirectionnel et HTTP avec interrogations périodiques ont été comparés. L’utilisateur a accepté A HTTP + SSE par « A » le 10 novembre 2026.

Les commandes et lectures utilisent HTTP JSON. Un flux SSE par page applicative transmet les notifications en identifiant leur projet, version, discussion et tentative. Mutualiser le transport ne fusionne pas les conversations. L’UX conserve ses états attente, erreur et réponse Markdown ; le choix ne rend pas obligatoire un affichage token par token et ne crée pas de contrôle d’annulation ou de steering.

SSE correspond au sens principal des notifications, serveur vers navigateur, tout en conservant les réponses et erreurs HTTP pour les commandes. WebSocket aurait apporté un canal permanent dans les deux sens avec un protocole applicatif de corrélation/reprise à définir. Les interrogations périodiques auraient évité le flux permanent, avec requêtes répétées et délai jusqu’à la lecture suivante. Les trois options sont viables ; aucun benchmark n’est revendiqué.

Le compromis accepté est la gestion de deux types d’échanges et du cycle de l’abonnement : reconnexion, nettoyage, bornage pour lecteurs lents et relecture de l’état durable. EventSource ne garantit ni rejeu durable ni exécution exactement une fois. SQLite fait autorité ; une notification de résultat durable suit son commit. Une coupure navigateur ne relance ni n’annule automatiquement la tentative IA et ne duplique pas le message utilisateur.

Les versions et contrats précis restent à fixer dans la [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Les contrôles locaux Host/Origin et des mutations restent nécessaires. Sources primaires : [WHATWG — EventSource](https://html.spec.whatwg.org/multipage/server-sent-events.html), [FastAPI — SSE](https://fastapi.tiangolo.com/tutorial/server-sent-events/), [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/), consultées le 10 novembre 2026. Aucun test applicatif ou échange IA authentifié n’est déclaré exécuté.
