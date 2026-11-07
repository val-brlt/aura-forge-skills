---
project: aura-forge-project-ai
version: v1
release_kind: mvp
cycle_kind: initial_version
approval_status: pending
coverage: complete
---

# Synthèse de cadrage — Aura Forge Project AI — V1 / MVP

## Statut et référence de départ

Synthèse soumise à approbation explicite, préparée le 7 novembre 2026. Les décisions de l’entretien sont actées individuellement ; cette synthèse n’est pas encore approuvée.

Il s’agit du cadrage de la première version d’Aura Forge Project AI, désignée MVP. Aucune version précédente du produit ne constitue une référence livrée. Les versions successives des projets gérés dans Aura Forge sont distinctes des versions du produit Aura Forge lui-même.

Source initiale : description « Aura Forge Project AI », fournie dans `C:/Users/Valentin/.codex/attachments/bcfcf771-5458-4b85-93a8-6e2fe88d6e32/Pasted text.txt`.

Source des arbitrages : réponses explicites de l’utilisateur aux questions Q1 à Q16 de cette conversation, consignées sous D01 à D16 dans le fichier de suivi du cycle.

## Objectif et résultat attendu

Permettre à une personne de transformer une idée en cadrage fonctionnel validé, structuré, conservé et reprenable dans une application web en français. Cette personne peut gérer plusieurs projets et cadrer leurs versions successives.

Le résultat du MVP est un cadrage consultable dans l’application : synthèse, modules, fonctionnalités et critères d’acceptation, décisions, périmètre de version, éléments reportés et questions ouvertes. Le développement des projets gérés appartient à des phases ultérieures. [Description initiale ; D01–D03, D06, D09]

## Périmètre retenu et règles métier

### 1. Usage personnel et projets

- L’application est destinée à un usage personnel, sans gestion de plusieurs utilisateurs ni authentification en V1. [D01]
- La personne peut créer et gérer plusieurs projets, chacun avec un nom et une description initiale en texte libre. [D01, D04, D10]
- La description est modifiable ; sa modification ne réécrit pas automatiquement les cadrages déjà validés. [D04]
- Un projet peut être archivé puis restauré. Il reste consultable avec son historique pendant l’archivage ; toute modification ou poursuite du cadrage exige sa restauration. [D04, D16]
- L’archivage ne modifie ni les validations ni les déclarations de livraison. [D16]

### 2. Entretien fonctionnel assisté par IA

- Les entrées se limitent aux textes saisis ou collés : idée initiale, nouveaux besoins et réponses à l’assistant. [D10]
- L’assistant questionne, clarifie les objectifs et règles métier, puis propose une synthèse et une organisation en modules et fonctionnalités selon le processus de référence `project-scoping`. [Description initiale ; D02, D06]
- L’utilisateur peut discuter, modifier, accepter, refuser ou reporter les propositions. Une proposition ne devient jamais approuvée sans décision explicite. [Description initiale ; D06, D09]
- Le cadrage reste fonctionnel : il ne décide pas des écrans, technologies, modèles de données, API ou tâches de développement. [Description initiale ; D02]

### 3. Catalogue, décisions et validations

- Les modules regroupent les fonctionnalités de façon fonctionnelle. Chaque fonctionnalité retenue possède des critères d’acceptation. [Description initiale ; D06]
- Le cadrage distingue les nouvelles fonctionnalités, les évolutions de fonctionnalités existantes, les éléments retenus pour la version, les propositions reportées ou refusées et les questions ouvertes. [Description initiale ; D03, D06, D12]
- L’utilisateur peut modifier manuellement les modules, fonctionnalités, critères d’acceptation et décisions, en complément du dialogue avec l’assistant. [D11]
- Les modifications manuelles suivent les mêmes règles de traçabilité et de nouvelle validation que les modifications proposées par l’IA. [D11]
- Trois validations explicites se succèdent : synthèse de l’entretien, catalogue de modules et fonctionnalités, puis cadrage final consolidé. [D06]
- Des questions non bloquantes peuvent rester ouvertes dans un cadrage final. Une règle indispensable indéterminée sur une fonctionnalité retenue empêche la validation finale ; l’utilisateur doit clarifier la règle ou reporter la fonctionnalité. [D13]

### 4. Versions et continuité fonctionnelle

- Dès le MVP d’Aura Forge, chaque projet peut faire l’objet d’un premier cadrage puis de cadrages pour ses versions suivantes. [D03]
- Une fonctionnalité conserve son identité lorsqu’elle évolue ; son comportement prévu pour chaque version et les décisions antérieures restent identifiables. [Description initiale ; D03]
- Une seule version par projet peut être active en cadrage. Une version suivante peut être préparée avant la livraison de la précédente. [D05]
- Pour une version suivante, l’assistant s’appuie sur le dernier cadrage approuvé et les éléments reportés, en distinguant le prévu du confirmé livré. Aucun élément reporté n’est automatiquement sélectionné. [D12]
- Un cadrage approuvé ne constitue pas une preuve de livraison. L’utilisateur déclare explicitement qu’une version est livrée. [D03, D05]
- Avant livraison, un cadrage approuvé peut être rouvert ; son état approuvé précédent est conservé, et les éléments affectés doivent être revalidés. [D07]
- Après livraison, les évolutions fonctionnelles sont portées par une nouvelle version. [D07]
- Si une version suivante est déjà en cadrage au moment de rouvrir la précédente non livrée, l’utilisateur revient explicitement sur la précédente et suspend la suivante. Après modification de la référence, les éléments affectés de la version suivante doivent être revus, sans réécriture automatique de ses décisions. [D15]

### 5. Persistance, interruption et reprise

- Les informations métier sont structurées et persistantes pour être consultées, modifiées et reliées dans l’application. Le choix de leur représentation technique est réservé à une phase ultérieure. [Description initiale ; D02, D09, D11]
- L’entretien et les décisions sont sauvegardés automatiquement. L’utilisateur peut reprendre après fermeture ou erreur de l’assistant. [D09]
- L’entretien peut être suspendu avec une couverture partielle explicitement indiquée et ses questions ouvertes visibles. Cette suspension ne vaut pas approbation. [D09, D13]
- Les décisions et cadrages précédemment approuvés restent consultables, avec leur attribution au projet et à la version concernés. [Description initiale ; D03, D07, D15]

## Vérifications fonctionnelles issues des décisions

Ces vérifications explicitent les décisions déjà prises ; elles n’ajoutent pas de capacités au périmètre.

| Cas | Résultat attendu | Origine |
| --- | --- | --- |
| Créer deux projets | Chaque projet conserve son nom, sa description et ses propres cadrages | D01, D04 |
| Modifier la description d’un projet déjà cadré | Le cadrage approuvé existant n’est pas réécrit automatiquement | D04 |
| Archiver un projet | Il reste consultable ; modification et poursuite du cadrage nécessitent une restauration | D04, D16 |
| Soumettre une proposition de l’assistant | Elle attend une décision explicite ; absence de réponse et interruption ne valent pas approbation | D06, D09 |
| Modifier manuellement une fonctionnalité approuvée avant livraison | L’état approuvé précédent reste consultable et les éléments affectés nécessitent une nouvelle validation | D07, D11 |
| Fermer une session ou subir une erreur IA | L’entretien et les décisions sauvegardés peuvent être repris sans approbation implicite | D09 |
| Valider un cadrage contenant une règle indispensable encore indéterminée | La validation finale est bloquée jusqu’à clarification ou report de la fonctionnalité | D13 |
| Préparer une version suivante avant livraison | Le contexte distingue les capacités prévues des capacités confirmées livrées | D05, D12 |
| Consulter les éléments reportés pendant le cadrage suivant | Ils restent candidats jusqu’à sélection explicite | D12 |
| Rouvrir la version précédente pendant le cadrage de la suivante | La suivante est suspendue ; les effets du changement de référence doivent être revus | D15 |
| Approuver un cadrage | La version n’est pas déclarée livrée par cette approbation | D03, D05 |

Les critères d’acceptation détaillés seront répartis dans les fiches du catalogue proposé après approbation de cette synthèse. Toute exigence supplémentaire éventuelle devra rester identifiée comme proposition.

## Exclusions et évolutions reportées

### Reportées, sans engagement de version future

- Gestion de plusieurs utilisateurs, authentification, partage et collaboration. [D01]
- Phases UX/UI, architecture technique et planification du développement des projets gérés. [D02]
- Intégrations GitHub : dépôts, Issues et Projects. [Description initiale ; D02]
- Développement délégué à des agents, suivi de leurs tests, commits et pull requests. [Description initiale ; D02]
- Suppression définitive des projets. [D04]
- Pièces jointes et import de documents. [D10]
- Fonction dédiée de reformulation ou d’enrichissement par IA de la description initiale. L’assistant d’entretien reste inclus. [D10, D14]

### Proposition refusée pour V1

- Export Markdown du cadrage approuvé. Aucun report vers une version future n’est approuvé par cette décision. [D08]

### Sujet évoqué mais non tranché

- Synchronisation de données avec un outil externe : évoquée dans la recommandation Q8, sans décision distincte de l’utilisateur. Elle ne fait pas partie du périmètre retenu et ne constitue pas une évolution future approuvée.

## Dépendances fonctionnelles et limites de la référence

- Le cadrage porte sur un projet et une version identifiés. Le catalogue découle d’une synthèse validée ; le cadrage final découle du catalogue validé. [D03, D06]
- Un cadrage ultérieur réutilise le dernier cadrage approuvé et ses informations de livraison explicitement déclarées ; il ne présume pas une livraison effective. [D05, D12]
- L’assistant IA doit pouvoir accompagner l’entretien et proposer les résultats attendus. Son fournisseur, sa configuration, ses coûts et les adaptations techniques des skills seront étudiés ultérieurement ; aucune dépendance à un service précis ni aucune disponibilité externe n’a été vérifiée ou approuvée pendant cet entretien.
- Les workflows existants servent de référence et sont à réutiliser autant que possible. Leur exécution et leur stockage dans l’application restent à concevoir ; le présent cadrage n’en confirme pas la faisabilité technique. [Description initiale]

## Hypothèses de livraison

- Hypothèse de travail : Aura Forge démarre comme un nouveau produit, sans comportement existant livré à préserver. Le dépôt inspecté contient les workflows et consignes, sans cadrage produit antérieur constaté.
- Aucune fonctionnalité du produit ni aucune livraison de V1 n’est présumée réalisée.
- Les exemples de versions suivantes décrivent une capacité du MVP ; ils n’approuvent ni une V2 du produit Aura Forge, ni son contenu.
- Aucun choix de déploiement ou de protection d’accès n’est déduit de l’absence d’authentification en V1.

## Couverture et décisions encore ouvertes

Couverture fonctionnelle évaluée **complète pour le périmètre convenu**, sous réserve de la revue de cette synthèse par l’utilisateur. Les questions Q1 à Q16 ont reçu une réponse ; aucune question fonctionnelle bloquante ne reste consignée.

La synchronisation externe reste un sujet non retenu et non tranché. Les choix UX/UI, architecture, fournisseur IA, exploitation et réalisation restent hors de cette phase, sans être présentés comme des décisions prises.

Aucune proposition fonctionnelle supplémentaire n’est candidate à une inclusion automatique dans V1. Le découpage en modules, l’attribution des identifiants de fonctionnalités et le manifeste documentaire relèvent de l’étape suivante, soumise à approbation distincte.

## Approbations distinctes à venir

1. Approbation explicite de cette synthèse.
2. Approbation du catalogue, du périmètre de version et du manifeste des fichiers proposés.
3. Approbation de la documentation générée après vérification de cohérence.
4. Autorisation de commit, puis autorisation de push demandées séparément.

L’approbation de la synthèse ne vaut ni validation d’une exigence encore proposée ou non résolue, ni autorisation de générer le catalogue final, d’implémenter, de publier des tickets, de committer ou de pousser.
