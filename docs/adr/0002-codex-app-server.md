---
status: accepted
date: 2026-11-09
---

# Intégrer Codex par app-server local

Après le choix de [Codex local pour le MVP](0001-codex-local-mvp.md), deux liaisons ont été comparées : commandes `codex exec` avec événements JSONL et reprise de session, ou app-server avec protocole bidirectionnel et conversations. `exec` avait été recommandé pour sa maturité et les échanges par tours. L’utilisateur a demandé de vérifier la dernière version, puis une explication des différences, et a retenu app-server : « je partirai quand même sur codex app server ».

Le backend local pilotera donc app-server sur stdio. Le navigateur restera client d’Aura Forge ; la liaison ne nécessite pas de port réseau Codex. App-server offre une intégration interactive des conversations et des événements, au prix de la gestion d’un processus durable et de son protocole. Ce choix n’ajoute pas de comportement UX non approuvé ni une seconde liaison exec à réaliser.

Le statut expérimental et les réserves de support ont été présentés avant l’acceptation. La [référence des commandes](https://learn.chatgpt.com/docs/developer-commands) classe app-server Experimental ; sa [documentation dédiée](https://learn.chatgpt.com/docs/app-server) le recommande pour les clients riches. Sources consultées le 9 novembre 2026, avec Codex stable `0.167.0` comme référence publiée. La version et le schéma effectivement supportés devront être fixés et vérifiés ensemble, sans supposer une compatibilité permanente.

Les décisions et références métier resteront sous l’autorité de l’application, indépendamment des sessions Codex. Une interruption du processus ne doit pas accorder d’approbation implicite. Le contrôle des permissions, l’accès ChatGPT sans facturation supplémentaire présumée et la reprise restent à préciser dans la [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Cette décision ne vaut pas validation du dossier complet, choix de backend ou autorisation de mise à jour globale.
