---
status: accepted
date: 2026-11-10
---

# Séparer état courant, copies approuvées et changements métier

Aura Forge doit conserver le travail courant, les décisions et les états approuvés précédents, y compris après réouverture avant livraison. Les évolutions d’une fonctionnalité gardent leur identité et leur attribution par version. Deux représentations SQLite ont été comparées : état courant avec copies approuvées et journal, ou révisions immuables généralisées avec pointeurs courants. L’utilisateur a accepté A par « A » le 10 novembre 2026.

Les objets courants restent modifiables selon les règles métier. Chaque validation explicite de synthèse, catalogue ou cadrage final enregistre une copie immuable du contenu concerné, de sa révision source et de ses dépendances approuvées. La consultation d’une copie utilise les valeurs conservées, pas le contenu courant mutable. La référence finale et la livraison sont des faits distincts. Une nouvelle validation crée une nouvelle copie sans remplacer l’ancienne.

Les mutations métier conservent leur contexte, origine et changement avant/après dans la même transaction que l’état courant. Ce journal permet la consultation de l’historique ; son rejeu n’est pas nécessaire pour ouvrir l’application. Brouillons, messages et tentatives ont leur cycle de persistance propre, sans transformer chaque frappe ou fragment IA en décision. Une proposition IA seule ne constitue pas une validation.

L’alternative par révisions immuables aurait unifié l’adressage des contenus successifs et facilité leur comparaison, avec une gestion systématique des pointeurs et ensembles cohérents de révisions. Le besoin actuel privilégie travail courant, références approuvées et traçabilité, sans gestion générale des révisions exposée à l’utilisateur. Aucun gain de volume ou de performance n’est mesuré.

Le compromis accepté est la cohérence transactionnelle de trois représentations et la lecture de formats historiques versionnés. Réouverture et corrections doivent préserver l’ancienne référence, les états de validation historiques et les décisions de la version suivante soumise à revue. Les révisions attendues et identifiants de commandes évitent écrasements obsolètes et doubles effets lors des retransmissions. Schéma exact, classes et ORM restent à préciser dans la [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md).

Sources fonctionnelles : [FEAT-006](../docs-project/modules/version-management/reopen-approved-scoping.md), [FEAT-009](../docs-project/modules/functional-scoping/structure-feature-catalogue.md), [FEAT-010](../docs-project/modules/functional-scoping/approve-scoping-stages.md), [FEAT-012](../docs-project/modules/continuity/view-functional-history.md). Aucune base produit ni migration n’est créée par cette décision.
