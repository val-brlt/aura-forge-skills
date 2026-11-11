---
status: accepted
date: 2026-11-10
---

# Conserver les données métier dans SQLite local

Le MVP d’Aura Forge est une application personnelle en boucle locale, avec backend Python/FastAPI. Il doit conserver projets, versions, cadrages, décisions, références approuvées, discussions et brouillons, indépendamment des sessions Codex. SQLite et PostgreSQL peuvent fournir les transactions et contraintes nécessaires. L’utilisateur a accepté A SQLite le 10 novembre 2026 : « je vais faire A ».

Le backend utilise donc une base SQLite sur le même hôte, sans service de base séparé. Ce choix réduit les composants à exploiter pour le placement actuel. Son compromis est une seule transaction d’écriture simultanée : transactions courtes, traitement de contention, contraintes et vérification des révisions restent nécessaires. Les échanges IA et attentes utilisateur sont hors transaction.

PostgreSQL aurait facilité une base commune à plusieurs hôtes et davantage d’écritures concurrentes, avec un service supplémentaire à configurer et maintenir. Aucun besoin établi ne l’impose au MVP. Un serveur privé monohôte peut conserver SQLite ; une évolution distribuée ou des besoins de concurrence/exploitation mesurés justifieraient un réexamen. Une migration ne serait pas transparente.

Le choix ne fixe pas pilote, ORM, schéma détaillé ou réglages WAL. Les migrations et sauvegardes cohérentes doivent être prévues ; une copie isolée du fichier principal en activité WAL ne suffit pas. La sauvegarde opérationnelle reste distincte de l’export produit refusé pour V1. Aucune base ni implémentation n’est créée par cette décision.

Sources primaires consultées pour le comparatif : [SQLite — usages adaptés](https://www.sqlite.org/whentouse.html), [transactions](https://www.sqlite.org/lang_transaction.html), [WAL et sauvegarde des fichiers](https://www.sqlite.org/wal.html), [Python — sqlite3 et backup](https://docs.python.org/3/library/sqlite3.html), [PostgreSQL — concurrence](https://www.postgresql.org/docs/current/mvcc-intro.html). Portée : [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). L’acceptation du moteur ne vaut pas validation du dossier d’architecture complet.
