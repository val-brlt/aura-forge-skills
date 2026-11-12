---
id: FEAT-007
module: functional-scoping
decision_status: approved
scope: mvp
source: versions/v1/SCOPING-SUMMARY.md
---

# FEAT-007 — Mener l’entretien de cadrage avec l’IA

## Objectif utilisateur

Clarifier une idée ou de nouveaux besoins avec l’aide de l’IA pour préparer le périmètre fonctionnel d’une version.

## Comportement attendu

L’assistant mène un entretien interactif en français pour comprendre les objectifs, clarifier les besoins et les règles métier, puis proposer une synthèse. Pour la première version, il part de l’idée initiale ; pour les suivantes, il réutilise le contexte existant en distinguant le prévu du confirmé livré.

Les entrées sont des textes saisis ou collés. L’assistant peut questionner et proposer, mais aucune proposition n’est approuvée sans décision explicite. Le processus s’inspire de `project-scoping`, avec séparation entre cadrage fonctionnel et phases ultérieures.

Une analyse préparatoire organise les questions sans constituer une validation métier. Chaque question présente son contexte, une recommandation et sa justification. L’utilisateur peut appliquer cette recommandation ou rédiger une réponse libre ; il relit et peut corriger l’interprétation proposée avant de la confirmer. Les réponses confirmées alimentent la synthèse, qui reste à valider. Une discussion propre à la question permet d’explorer le sujet avant de décider.

L’utilisateur dispose aussi d’un fil général pour explorer les besoins et le contexte du projet, distinct des discussions des questions. Ce fil suit le projet entre ses versions ; le contexte de version des échanges reste identifiable. L’assistant s’appuie sur la description, les versions et leurs décisions, en distinguant prévu, approuvé et livraison déclarée.

Les discussions acceptent du texte saisi ou collé et affichent les réponses en Markdown. Entrée envoie, Maj+Entrée ajoute une ligne ; la composition du texte ne déclenche pas d’envoi prématuré. Un échange général ne modifie automatiquement ni description, ni proposition, ni catalogue, ni validation, ni livraison. Les décisions restent explicites et rattachées à leur version. L’exploration peut se poursuivre même si la version consultée est approuvée ou livrée ; l’archivage impose la consultation seule jusqu’à restauration.

## Historique fonctionnel par version

### V1

**Comportement validé :** questions structurées de cadrage par version avec recommandations, réponses libres à confirmer et discussions contextuelles ; synthèse soumise à validation. Un fil général distinct permet d’explorer le projet entre ses versions sans modifier automatiquement ses décisions.

**Critères d’acceptation validés :**

- L’utilisateur peut fournir l’idée ou les nouveaux besoins et répondre à l’assistant par texte saisi ou collé.
- L’assistant questionne et propose en français pour clarifier les objectifs et les règles fonctionnelles de la version concernée.
- L’analyse prépare les questions sans approuver le périmètre ni ajouter une quatrième validation.
- Chaque question présente son contexte, une recommandation et sa justification ; l’utilisateur peut appliquer la recommandation ou confirmer sa réponse libre après relecture et correction éventuelle de l’interprétation.
- Une discussion liée à une question conserve son sujet ; ses échanges seuls ne confirment pas une réponse.
- Pour une version suivante, il prend en compte le cadrage approuvé de référence et les éléments reportés sans présenter le prévu comme livré.
- Il produit une synthèse soumise à validation explicite avant la préparation du catalogue.
- Le cadrage n’impose ni parcours d’interface, ni technologies, ni modèles de données, ni tâches de développement.
- La fonction dédiée de reformulation ou d’enrichissement de la description initiale reste hors V1 ; cela ne retire pas l’assistant d’entretien du périmètre.
- L’utilisateur peut discuter du contexte et des besoins d’un projet dans un fil général, distinct des discussions de ses questions de cadrage.
- Le fil appartient au projet et reste accessible lorsque l’utilisateur consulte ses versions successives. Le contexte de version d’un échange est identifiable.
- L’assistant utilise la description, les versions et leurs décisions sans confondre un cadrage approuvé et une livraison déclarée.
- Une discussion générale ne modifie pas automatiquement la description, les propositions, le catalogue, les validations ou la livraison. Les décisions de cadrage restent explicites et rattachées à leur version.
- L’exploration reste possible lorsque la version consultée est approuvée ou livrée. L’archivage impose la consultation seule jusqu’à restauration.
- Les discussions affichent le Markdown ; Entrée envoie, Maj+Entrée ajoute une ligne et une composition en cours ne provoque pas d’envoi.

**Source :** [Synthèse V1](../../versions/v1/SCOPING-SUMMARY.md), description initiale et D02, D06, D10, D12, D14.

## Critères d'acceptation validés

Les critères approuvés sont conservés dans la [section historique V1](#v1) ci-dessus. Ils fondent l’appartenance au [MVP global](../../MVP.md), sans attribuer de release ni attester de développement ou de livraison. Les critères proposés ci-dessous ne sont pas approuvés.

## Critères d’acceptation proposés

Aucun critère supplémentaire proposé.

## Dépendances fonctionnelles

- [FEAT-004 — Préparer les versions successives d’un projet](../version-management/prepare-project-versions.md) : version et contexte de référence identifiés.
- [FEAT-008 — Arbitrer les propositions et les éléments reportés](manage-proposals-and-backlog.md) : décisions de l’utilisateur pendant l’entretien.
- [FEAT-011 — Sauvegarder et reprendre un cadrage](../continuity/save-and-resume-scoping.md) : entretien conservé et reprenable.

## Questions ouvertes

Aucune question fonctionnelle bloquante pour la référence approuvée. L’[architecture](../../architecture/ARCHITECTURE.md) retient Codex local et l’adaptation structured de l’ADR-0009 ; compte/coût, permissions effectives et intégration restent à vérifier. L’entretien autonome sans release suivra la décision de FEAT-004 ; aucune nouvelle question d’entretien n’est requise pour un simple découpage de livraison.

## Traçabilité

Fonctionnalité nouvelle de V1, issue de la description initiale et de D02, D06, D10, D14 ; D12 précise la référence pour les versions suivantes. Son découpage a été approuvé avec le catalogue.
