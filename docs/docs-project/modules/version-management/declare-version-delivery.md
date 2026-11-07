---
id: FEAT-005
module: version-management
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-005 — Déclarer la livraison d’une version

## Objectif utilisateur

Indiquer explicitement qu’une version d’un projet a été livrée afin que les cadrages suivants disposent d’un contexte fidèle.

## Comportement attendu

La livraison d’une version est renseignée par déclaration explicite de l’utilisateur. Elle reste distincte de l’approbation de son cadrage. L’IA n’infère pas une livraison à partir des validations du cadrage ou de la seule existence d’un périmètre approuvé.

La réalisation et le suivi du développement ne sont pas couverts par cette déclaration dans V1.

## Historique fonctionnel par version

### V1

**Comportement validé :** déclaration manuelle de livraison et distinction explicite entre prévu, approuvé et confirmé livré.

**Critères d’acceptation validés :**

- L’utilisateur peut déclarer explicitement qu’une version identifiée de son projet est livrée.
- La validation d’une synthèse, d’un catalogue ou d’un cadrage final ne déclare pas automatiquement la version livrée.
- Tant qu’aucune livraison n’est confirmée, le contexte des versions suivantes ne présente pas le seul périmètre approuvé comme un comportement livré.
- Archiver un projet ne change pas les déclarations de livraison de ses versions.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), D03, D05, D12 et D16.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](prepare-project-versions.md) : livraison rattachée à une version précise.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : information de livraison consultable avec son contexte.

## Questions ouvertes

Aucune question fonctionnelle consignée pour V1. Aucun mécanisme de vérification technique de la livraison n’est retenu dans ce cadrage.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D03 et D05, avec les règles transversales de D12 et D16. Son découpage a été approuvé avec le catalogue. Elle ne constitue pas une preuve que le produit Aura Forge est lui-même livré.
