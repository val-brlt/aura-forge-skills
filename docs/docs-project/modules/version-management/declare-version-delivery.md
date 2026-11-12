---
id: FEAT-005
module: version-management
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-005 — Déclarer la livraison d’une version

## Objectif utilisateur

Indiquer explicitement qu’une version d’un projet a été livrée afin que les cadrages suivants disposent d’un contexte fidèle.

## Comportement attendu

Les règles ci-dessous décrivent la référence V1 approuvée. Le [MVP global](../../MVP.md) est indépendant des releases ; l’adaptation de ces règles dans l’application est présentée dans les critères proposés et questions ouvertes, sans approbation implicite.

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

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Adaptation au MVP indépendant des releases — **proposition à valider**, sans modification des critères historiques approuvés :

- Rattacher une déclaration explicite à une release logicielle `MAJOR.MINOR.PATCH` et à son contenu identifié, sans assimiler cette déclaration à l’achèvement du MVP.
- Distinguer la tranche déclarée livrée du reste des critères d’une fonctionnalité ; une tranche seule laisse la fonctionnalité partiellement livrée. Le jalon MVP exige tous les critères indispensables satisfaits et toutes les fonctionnalités indispensables livrées.
- Conserver la déclaration manuelle comme comportement de base : aucun suivi de développement, vérificateur de déploiement ou écran de planification supplémentaire n’est approuvé par cette proposition.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](prepare-project-versions.md) : livraison rattachée à une version précise.
- [FEAT-012 — Consulter l’historique fonctionnel et les décisions](../continuity/view-functional-history.md) : information de livraison consultable avec son contexte.

## Questions ouvertes

À valider : granularité et présentation de la déclaration manuelle lorsqu’une release ne couvre qu’une partie du MVP ; provenance et preuve nécessaires avant d’affirmer un achèvement complet. Aucun mécanisme de vérification technique de livraison ni suivi du développement n’est ajouté au périmètre approuvé.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de D03 et D05, avec les règles transversales de D12 et D16. Son découpage a été approuvé avec le catalogue. Elle ne constitue pas une preuve que le produit Aura Forge est lui-même livré.
