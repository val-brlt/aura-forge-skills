---
id: FEAT-007
module: functional-scoping
decision_status: approved
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-007 — Mener l’entretien de cadrage avec l’IA

## Objectif utilisateur

Clarifier une idée ou de nouveaux besoins avec l’aide de l’IA pour préparer le périmètre fonctionnel d’une version.

## Comportement attendu

L’assistant mène un entretien interactif en français pour comprendre les objectifs, clarifier les besoins et les règles métier, puis proposer une synthèse. Pour la première version, il part de l’idée initiale ; pour les suivantes, il réutilise le contexte existant en distinguant le prévu du confirmé livré.

Les entrées sont des textes saisis ou collés. L’assistant peut questionner et proposer, mais aucune proposition n’est approuvée sans décision explicite. Le processus s’inspire de `project-scoping`, avec séparation entre cadrage fonctionnel et phases ultérieures.

## Historique fonctionnel par version

### V1

**Comportement validé :** entretien conversationnel de cadrage par version, à partir de textes et avec production d’une synthèse soumise à validation.

**Critères d’acceptation validés :**

- L’utilisateur peut fournir l’idée ou les nouveaux besoins et répondre à l’assistant par texte saisi ou collé.
- L’assistant questionne et propose en français pour clarifier les objectifs et les règles fonctionnelles de la version concernée.
- Pour une version suivante, il prend en compte le cadrage approuvé de référence et les éléments reportés sans présenter le prévu comme livré.
- Il produit une synthèse soumise à validation explicite avant la préparation du catalogue.
- Le cadrage n’impose ni parcours d’interface, ni technologies, ni modèles de données, ni tâches de développement.
- La fonction dédiée de reformulation ou d’enrichissement de la description initiale reste hors V1 ; cela ne retire pas l’assistant d’entretien du périmètre.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), description initiale et D02, D06, D10, D12, D14.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](../version-management/prepare-project-versions.md) : version et contexte de référence identifiés.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](manage-proposals-and-backlog.md) : décisions de l’utilisateur pendant l’entretien.
- [FEAT-011 — Sauvegarder et reprendre un cadrage](../continuity/save-and-resume-scoping.md) : entretien conservé et reprenable.

## Questions ouvertes

Aucune question fonctionnelle bloquante consignée. Le fournisseur IA, ses coûts, sa configuration et l’adaptation technique des skills seront étudiés ultérieurement.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de la description initiale et de D02, D06, D10, D14 ; D12 précise la référence pour les versions suivantes. Son découpage a été approuvé avec le catalogue.
