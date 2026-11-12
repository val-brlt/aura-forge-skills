---
version: v1
status: approved
---

# Conception technique — V1

## État et références

Le [cadrage V1](../VERSION.md), ses douze fonctionnalités et l’[UX approuvée](../ux/UX-SUMMARY.md) sont les entrées de cette conception. V1 est une identité de baseline documentaire, sans équivalent SemVer attribué ; le [MVP global](../../../MVP.md) peut être réalisé par plusieurs livraisons. La V1 n’est pas déclarée livrée. Le dossier technique a été approuvé le 10 novembre 2026 par « je valide », après présentation des contrats et contrôles du dossier intégré. La planification peut commencer ; aucune autorisation de commit ou push n’est donnée par cette validation.

L’[architecture globale](../../../architecture/ARCHITECTURE.md) consigne la cible acceptée. Aucun code produit, schéma de stockage ou contrat technique existant n’est à migrer dans ce dépôt.

## Placement accepté pour le MVP

Application web sur le poste personnel, utilisée par son navigateur, avec service applicatif accessible uniquement par boucle locale. L’utilisateur a choisi cette option le 9 novembre 2026 : « A pour le mVP et plus tard sur un serv privée ».

Le MVP conserve l’usage individuel sans authentification applicative. Son utilisation dépend du fonctionnement du poste et de l’application. Codex s’exécute sur le poste et utilise les services de modèles distants ; aucune inférence entièrement locale n’est incluse dans cette cible initiale.

Un serveur privé est souhaité ultérieurement, sans version ni fournisseur défini. Le choix de persistance et de configuration devra expliciter comment les données peuvent être déplacées et les accès reconfigurés. L’infrastructure distante et une éventuelle évolution du contrôle d’accès appartiendront à cette migration ultérieure.

## Moteur IA accepté

Codex local est le seul moteur à intégrer dans le MVP. Réponse explicite du 9 novembre 2026 : « enfaite je voudrais faire tous mais dans un premier temps faire avec codex en local pour ne pas payer en plus ». Voir [ADR-0001](../../../../adr/0001-codex-local-mvp.md).

L’accès visé est la connexion ChatGPT existante, sans clé API ni bascule payante automatique. L’application ne doit pas acheter de crédits ou déclencher une recharge. Les droits du compte, son allocation incluse, ses crédits et la possibilité de détecter les limites restent à vérifier ; un fonctionnement gratuit ou illimité n’est pas établi. Une limite ou erreur doit conserver le travail et laisser les validations métier inchangées.

Les API directes et modèles locaux sont souhaités ultérieurement, sans version attribuée. La conception doit permettre leur ajout sans faire des sessions Codex la source unique des décisions et références métier. Seul le connecteur Codex doit être réalisé pour le MVP ; l’adaptation des skills est acceptée et la politique de permissions approuvée figure dans ce dossier.

Vérification locale réalisée sans appel de modèle : `codex.cmd --version` indique `codex-cli 0.163.0` ; l’aide expose `app-server`, `exec --json`, `exec resume` et `--output-schema`. La commande app-server est encore marquée expérimentale dans cette version. Ces vérifications ne prouvent ni une authentification utilisable ni une réponse IA réussie.

## Liaison app-server acceptée

Réponse utilisateur du 9 novembre 2026 : « je partirai quand même sur codex app server ». Voir [ADR-0002](../../../../adr/0002-codex-app-server.md). Le backend lance et pilote app-server local via JSON-RPC sur stdio. Le navigateur communique avec Aura Forge ; aucun port Codex n’est exposé pour cette liaison. Les choix du langage et du framework backend restent indépendants.

La vérification demandée de la dernière version a confirmé `0.167.0` stable par le changelog officiel et le registre npm ; cette version sert de référence à l’analyse. Les risques de maturité et d’évolution app-server ont été présentés avant l’acceptation. Aucune mise à jour de l’installation locale n’est effectuée par cet arbitrage.

Les sections de contrats et de protection locale précisent le cycle du processus, l’association des threads, les sorties structurées, la reprise et les erreurs dans le dossier intégré approuvé. Les événements Codex doivent alimenter les états UX approuvés, sans accorder automatiquement une validation ou une livraison. Les données métier doivent rester conservées indépendamment de la disponibilité du processus et de ses sessions. `codex exec` n’est pas à implémenter comme deuxième mode pour ce MVP.

Avant d’utiliser l’intégration, vérifier une version fixée et son schéma, l’initialisation, la reprise, la gestion d’un arrêt de processus et les limites d’accès au compte. Ces vérifications ne sont pas déclarées exécutées. La forme des événements entre backend et navigateur est définie dans les contrats partagés approuvés de ce dossier.

## Backend Python et FastAPI acceptés

Python + FastAPI est accepté pour le backend à la suite de la réponse utilisateur du 9 novembre 2026 : « ok on part sur python alors ça sera mieux ». Voir [ADR-0003](../../../../adr/0003-python-fastapi-backend.md). Le backend gère les commandes métier et leur validation, la persistance SQLite et le processus Codex app-server. Ce choix ne sélectionne pas le frontend, la base ou le transport des événements navigateur.

Le SDK officiel `openai-codex` évite de réécrire le transport JSON-RPC et son routage. La lecture du paquet publié `0.167.0` et de ses modèles a confirmé la présence de `AsyncCodex`, création/reprise/historique des threads, flux d’événements, interruption/steering, `output_schema`, instructions, références aux skills et connexion ChatGPT. Le runtime `openai-codex-cli-bin==0.167.0` est épinglé dans cette distribution ; des wheels Windows amd64/arm64 existent. Le SDK requiert Python 3.10 ou plus, Pydantic et packaging selon ses métadonnées.

La couverture a été vérifiée par lecture du code distribué et documentation, sans installation ni import du SDK et sans inférence. L’état du compte et les limites réelles ne sont pas vérifiés. Le lancement Windows, la compatibilité du couple Python/SDK et les scénarios de reprise restent à exercer avant de déclarer l’intégration opérationnelle.

Les limites du compte sont accessibles via le client bas niveau. La façade principale n’injecte pas de callback personnalisé de permission ; le client synchrone bas niveau en propose un. Certaines demandes de commandes ou de fichiers peuvent être acceptées par le handler par défaut : la configuration de sandbox et d’approbation devra être explicite et cohérente avec les seules opérations utiles au produit. Cela ne remplace ni les validations fonctionnelles ni l’autorité de l’application sur ses données.

La séparation des discussions, l’unicité d’une tentative, les sauvegardes et la conservation des références approuvées restent des responsabilités d’Aura Forge ; le SDK ne les fournit pas pour les entités métier du produit.

## Frontend Vue et TypeScript acceptés

L’utilisateur a approuvé A Vue + TypeScript le 9 novembre 2026 par « ok je valide A », après comparaison avec React/TypeScript et Jinja2/HTMX. Voir [ADR-0004](../../../../adr/0004-vue-typescript-frontend.md). Le frontend est compilé en fichiers statiques puis servi par FastAPI. Aucun serveur Node permanent n’est nécessaire pour cette variante d’exécution ; Node reste un outil de développement/construction.

L’interface doit reproduire les onze écrans et sept parcours de l’UX approuvée. Questions, interprétation corrigeable, trois validations, catalogue et discussions disposent d’états explicites. Les brouillons, sauvegardes et réponses tardives restent attachés à leur projet/discussion/question et au contexte de version adéquat ; le fil général du projet demeure commun aux versions consultées. Le réessai ne recrée pas le message utilisateur.

Le backend reste l’autorité sur les données et les validations. L’interface distingue une saisie locale, une sauvegarde en cours, un échec et une confirmation enregistrée. Les contrats d’échanges, la reprise des événements et la concurrence sont définis dans ce dossier approuvé. Aucun accès Codex n’est exposé directement au navigateur.

Cette décision ne sélectionne pas de bibliothèque visuelle, routeur ou store. Les styles et comportements des maquettes servent de référence UX ; leurs données en mémoire et simulations ne sont pas une implémentation de persistance. Markdown avec HTML brut échappé, clavier/IME, focus/dialogues, statuts annoncés, thèmes et adaptation mobile devront être vérifiés sur le frontend réel.

## Persistance SQLite acceptée

L’utilisateur a choisi A SQLite le 10 novembre 2026 : « je vais faire A », après comparaison avec PostgreSQL. Voir [ADR-0005](../../../../adr/0005-sqlite-local-storage.md). Le fichier métier réside sur le même hôte que FastAPI et reste accessible exclusivement par le backend. Ce placement n’oblige pas à changer de moteur lors d’un futur hébergement privé sur un hôte unique.

Les transactions et contraintes doivent protéger les liens, l’unicité d’une version active, les validations portant sur une révision précise, la préservation des références approuvées et les réessais sans duplication. Le modèle logique et les opérations atomiques sont définis dans ce dossier approuvé. Les appels Codex, flux progressifs et attentes utilisateur sont hors transaction ; le début et l’issue d’une tentative sont enregistrés séparément. Une écriture SQLite et un effet dans Codex ne constituent pas une transaction distribuée.

Une seule écriture simultanée impose des transactions courtes et une gestion explicite de la contention. Les clés étrangères doivent être activées et vérifiées sur chaque connexion avant les transactions. Le pilote, le modèle de connexion et le mode transactionnel restent à préciser, sans blocage de la boucle FastAPI par des opérations synchrones.

WAL et `synchronous=FULL` font partie du profil de persistance approuvé dans le dossier intégré. Si WAL est utilisé, la bibliothèque réellement distribuée doit inclure le correctif WAL-reset, présent en 3.51.3+ ou rétroport approprié. Le constat local SQLite 3.53.4 avec Python 3.15.1 couvre ce correctif ; il ne valide ni le futur empaquetage ni la compatibilité d’un pilote/ORM. Voir [SQLite — WAL](https://www.sqlite.org/wal.html).

Prévoir migrations de schéma versionnées et sauvegarde cohérente par l’API SQLite exposée en Python, puis restauration application arrêtée avec vérification de l’intégrité, des clés étrangères et du schéma. Aucun essai de sauvegarde/restauration n’a été exécuté et aucune base produit n’a été créée. Emplacement, fréquence, rétention et procédure opératoire restent ouverts. Cette protection opérationnelle n’ajoute ni export Markdown ni écran au périmètre fonctionnel.

## Organisation par métier acceptée

L’utilisateur a accepté A par « A » le 10 novembre 2026 : une seule application Python/FastAPI organisée par responsabilités métier, plutôt que par couches techniques globales. Voir [ADR-0006](../../../../adr/0006-organize-backend-by-business.md). La répartition sert les quatre modules fonctionnels existants :

| Fonctionnalités V1 | Responsabilité | Autorité |
| --- | --- | --- |
| FEAT-001 à FEAT-003 | Gestion des projets | Projet, description, archivage/restauration |
| FEAT-004 à FEAT-006 | Gestion des versions | Version, activité/suspension, livraison et liens de référence |
| FEAT-007 à FEAT-010 | Cadrage fonctionnel | Questions et interprétations, propositions, catalogue, arbitrages, validations et références approuvées |
| FEAT-011 et FEAT-012 | Continuité | Conversations, messages, brouillons, tentatives et reprise ; lecture de l’historique fourni par les autres propriétaires |

Une opération de sauvegarde ou de reprise ne contourne pas l’autorité métier. Les mutations de cadrage restent contrôlées par le cadrage ; celles de versions et de projets par leur propriétaire. La coordination applicative compose leurs opérations dans une transaction commune pour les invariants multi-objets, notamment FEAT-006. L’accès à la persistance reste derrière les opérations du propriétaire ; aucun package ne modifie directement les données d’un autre.

Le point d’entrée applicatif coordonne les packages, les opérations transactionnelles et les lectures de contexte. Les règles restent dans les responsabilités métier ; les packages ne s’appellent pas mutuellement par HTTP. Les dépendances et contrats d’opération sont définis dans le dossier intégré approuvé, sans cycle de coordination imposé entre packages.

L’intégration Codex porte processus, protocole, sessions et traduction des événements/erreurs. Le contexte lui est transmis par l’application ; les sorties sont des propositions validées techniquement puis traitées selon les commandes autorisées. Les appels IA restent hors transaction SQLite. Le frontend n’appelle que FastAPI. Une panne du processus Codex ne doit pas effacer le travail sauvegardé ou modifier une validation.

L’implémentation devra vérifier l’autorité d’écriture et les transactions via les opérations publiques, et contrôler les dépendances entre packages. Le choix ne fige pas les fichiers, classes, signatures privées, ORM ou transport d’événements ; aucun test de l’application réelle n’est déclaré réalisé.

## Transport HTTP JSON et SSE accepté

L’utilisateur a accepté A HTTP + SSE le 10 novembre 2026 par « A ». Voir [ADR-0007](../../../../adr/0007-http-json-and-sse.md). Les commandes et lectures sont HTTP JSON ; un flux SSE par page applicative mutualise les notifications, avec leur contexte de projet, version, discussion et tentative. La liaison SDK/Codex reste stdio ; elle n’est pas exposée au navigateur. Aucun transport WebSocket ou polling périodique de secours n’est à ajouter au MVP.

FLOW-003 et FLOW-007 conservent attente annoncée, erreur/réessai et réponse Markdown. Les fragments de texte sont une capacité, sans nouveau comportement d’affichage obligatoire. FLOW-005 reste contrôlé par des commandes explicites : ni événement terminé, ni réponse IA, ni acquittement technique ne valide un cadrage.

Les commandes doivent être dédupliquées par identifiant stable lors des retransmissions ; un réessai de génération reste lié au message utilisateur existant. Les révisions attendues protègent les sauvegardes et validations obsolètes. Les formes de requête, acquittement et erreur sont définies dans les contrats partagés approuvés ci-dessous et restent à implémenter. Un résultat durable n’est notifié qu’après commit ; une réponse HTTP peut seulement confirmer le début d’une tentative encore en cours.

Le navigateur établit l’abonnement puis relit l’état enregistré ; les événements reçus pendant la lecture doivent être réconciliés par révision. Cette reprise est requise à l’ouverture/reconnexion et devant un contexte ou curseur périmé. Last-Event-ID ne garantit pas de rejeu et repart vide pour un nouvel objet EventSource après rechargement. Aucun journal durable de chaque fragment n’est choisi ici.

Une déconnexion nettoie l’abonnement sans donner au générateur SSE la propriété de l’opération IA. La tentative déjà acceptée peut terminer et conserver son résultat ; une reconnexion ne la duplique pas. Après arrêt du backend/Codex, réconcilier les tentatives inachevées avant toute nouvelle inférence. Lecteurs lents, files bornées, heartbeats et limites de connexions doivent être vérifiés sur les versions navigateur/ASGI retenues. FastAPI expose ses primitives SSE natives depuis 0.135.0 ; compatibilité et versions exactes restent à vérifier, sans installation effectuée.

Les lectures ne déclenchent pas de mutation ; les commandes JSON et les accès au flux doivent respecter les contrôles de requêtes locales. Le détail Host/Origin et de protection contre requêtes web étrangères sera traité dans les modalités d’exploitation. Aucun secret dans une URL ou le frontend, aucune authentification produit ajoutée par ce transport.

## État courant, copies approuvées et journal acceptés

L’utilisateur a accepté A par « A » le 10 novembre 2026, après comparaison avec des révisions immuables généralisées. Voir [ADR-0008](../../../../adr/0008-current-state-approved-copies-and-audit.md). Le courant modifiable, les copies de validations et le journal avant/après sont distincts ; leur cohérence est transactionnelle. Le journal ne devient pas l’unique état à rejouer au démarrage.

Chaque validation de synthèse, catalogue ou cadrage final conserve les valeurs nécessaires à sa lecture, le contexte projet/version, la révision source et les validations amont dont elle dépend. Les liens vers les identités fonctionnelles servent la traçabilité, sans remplacer les valeurs historiques par celles du courant. Les copies et formats du journal portent une version de représentation permettant leur lecture après migration, sans modification rétroactive du sens approuvé.

Lors d’une réouverture, la copie approuvée demeure consultable et une nouvelle validation produit une nouvelle copie. La validité pour le courant et le fait historique d’une approbation restent distincts. La référence exacte utilisée par une version suivante est conservée pendant suspension et revue ; aucune correction ne réécrit automatiquement ses décisions. L’historique et les références restent consultables après archivage. La livraison explicitement déclarée reste distincte de ces validations.

### Modèle logique approuvé

Cette table précise la représentation retenue dans le dossier intégré approuvé ; elle ne fixe pas les colonnes SQL ou les classes privées.

| Ensemble logique | Autorité | Relations et invariants |
| --- | --- | --- |
| Project | Gestion des projets | Identité stable, description et archivage ; contexte de toutes les versions |
| ProjectVersion | Gestion des versions | Appartient au projet ; activité/suspension, référence de cadrage exacte et livraison explicite distinctes ; une seule active par projet |
| FeatureIdentity et VersionFeature | Cadrage fonctionnel | Identité de fonctionnalité au niveau du projet ; comportement/critères et inclusion explicite attribués à la version |
| Question, Interpretation, Proposal et Decision | Cadrage fonctionnel | Contexte projet/version et liens de provenance ; proposition, interprétation non confirmée et décision distinctes |
| WorkingScoping | Cadrage fonctionnel | Synthèse, catalogue et cadrage courant avec révisions et validité des validations ; changements soumis aux règles métier |
| Approval et ApprovedSnapshot | Cadrage fonctionnel | Validation explicite et copie immuable d’un contenu/révision ; dépendances amont identifiées ; aucune livraison implicite |
| ChangeRecord | Propriétaire de l’objet modifié | Contexte, opération et avant/après dans la transaction métier ; continuité fournit une vue de lecture et ne réécrit pas ces faits |
| Conversation et Message | Continuité | Fil général propre au projet et fils de questions distincts ; chaque échange garde son contexte de version |
| Draft | Continuité | Contexte précis de saisie, révision ; un changement de vue n’en change pas le propriétaire |
| GenerationAttempt | Continuité, avec intégration Codex | Liée à l’opération et au message existants ; état/résultat durables distincts du processus externe et du flux SSE |

Les copies approuvées n’embarquent pas une duplication de tous les brouillons ou messages. Les liens utiles de provenance pointent vers leurs identités conservées. L’historique des décisions manuelles suit les mêmes exigences que celui des changements issus d’une proposition IA autorisée. Aucun besoin de restauration arbitraire à chaque frappe ni d’export de cette représentation n’est ajouté au MVP.

### Compatibilité des périmètres et des livraisons

Le modèle logique ci-dessus est celui de la baseline approuvée : `ProjectVersion`, `VersionFeature`, `WorkingScoping`, `DeliveryFact` et les routes `/api/v1` gardent leurs identifiants et leur signification. Le [MVP](../../../MVP.md) et le backlog séparent désormais objectif fonctionnel et releases ; cela ne transforme pas automatiquement `ProjectVersion` en release SemVer.

La migration proposée doit dissocier identité du périmètre, appartenance MVP, affectations de tranches et faits de livraison, tout en conservant les copies approuvées et les liens de contexte existants. Les règles de réouverture après livraison partielle et d’activité unique demandent d’abord une décision fonctionnelle et UX dans FEAT-004/005/006. Aucun nouveau DATA-* ni route, schéma SQL ou migration exécutable n’est approuvé ici. Les contrats documentaires passent aux formats UX 2 / architecture 1.1 avec `delivery.scope.kind=legacy`, la source V1 intacte, les mêmes critères et un registre de releases vide. Les champs de schéma ne sont pas des versions de logiciel.

Pour les livraisons futures, la convention documentaire est `MAJOR.MINOR.PATCH` : rupture du contrat public → MAJOR, fonctionnalité compatible ou dépréciation publique → MINOR, correction compatible → PATCH, avec remise à zéro des composants inférieurs. En `0.x.y`, les conventions installées proposent PATCH pour une correction compatible, MINOR pour une fonctionnalité ou une incompatibilité ; leur application détaillée au produit et les critères de stabilité seront soumis à validation, sans inventer la première release. Toute incompatibilité requiert une migration documentée. Les contenus effectivement publiés restent immuables. Un PATCH compatible se traite par analyse d’impact ciblée et réutilisation des décisions/maquettes ; un risque réel de frontière, sécurité ou migration impose sa propre revue.

Les contrats listent indépendamment décision, affectations, développement et livraison. Les états sans preuve restent `unknown`, les affectations et releases vides, et le jalon MVP ouvert. La future planification proposera les `CHANGE-*`, leurs critères de tranche, dépendances et releases ; aucune capacité de planification ou suivi du développement n’est ajoutée à l’application MVP.

### Garanties de commande à préciser

Une mutation vérifie le contexte modifiable et la révision attendue, applique ses règles, puis enregistre ensemble son effet, le changement métier et le résultat associé à son identifiant de commande. Une retransmission réseau du même identifiant ne doit pas produire un nouvel effet ; le contrat est précisé dans « Commandes, acquittements et lectures » ci-dessous. Une sauvegarde obsolète ne doit pas écraser silencieusement une révision récente, même entre deux onglets du même utilisateur.

Pour FEAT-010, prérequis, révision concernée et questions bloquantes sont vérifiés dans la transaction d’approbation, puis validation et copie sont enregistrées ensemble. Pour FEAT-006, la coordination des propriétaires conserve la référence, modifie les états de versions et journalise l’opération atomiquement selon l’action autorisée. Les appels Codex restent hors transaction. Ce sont des garanties à vérifier sur l’implémentation, pas des essais déjà réalisés.

## Skills à deux modes acceptés

L’utilisateur a répondu « ça me parait ok » le 10 novembre 2026 à la proposition de conserver les mêmes skills avec `output_mode=files|structured`. Voir [ADR-0009](../../../../adr/0009-dual-output-skills-and-structured-proposals.md). A propositions structurées est retenue face au travail sur miroir documentaire interne ; un parent applicatif supplémentaire n’est pas imposé.

Le fonctionnement historique reste `files` par défaut. Aura Forge doit demander `structured` explicitement, y compris lors d’une reprise de thread, et propager ce mode aux instructions dépendantes adaptées. Le tronc commun conserve méthode d’entretien, recommandations justifiées, interprétations à confirmer, identités et provenance, références approuvées et distinction prévu/approuvé/livré. Les instructions de fichiers, scratch, diff et Git ne s’appliquent pas au mode structuré. Une erreur ne bascule pas vers le mode fichiers. Les skills tiers d’origine ne sont pas modifiés.

La tâche choisie par Python détermine le contexte et le schéma : préparation de questions, interprétation, synthèse, catalogue, consolidation ou discussion contextuelle, selon les actions UX existantes. Les résultats proposent du contenu ; ils n’approuvent pas le cadrage. Le backend valide les références, la révision de départ et les règles avant persistance. Il conserve dans la tentative les versions d’instructions et de schéma. Le `mode=preview|apply|audit` documentaire de structure-project reste un autre axe ; apply ne devient pas un droit d’écriture SQLite donné au modèle.

Le SDK audité expose instructions et output_schema ; la version de runtime et le schéma supportés devront être fixés ensemble. Les sorties structurées ne désactivent pas les outils. Les permissions ne doivent pas reprendre aveuglément les valeurs par défaut du SDK : deny_all est traduit en approvalPolicy=never, tandis que read_only autorise encore des lectures et certaines commandes. Un cwd dédié ne limite pas à lui seul toutes les lectures. La configuration effective des capacités (shell, web, MCP, apps/plugins et héritages) doit être contrôlée avant données réelles, sans modifier le profil global personnel. Les données propres au runtime/session restent distinctes des fichiers métier.

À vérifier lors de la réalisation : branche files préservée, structured propagé, absence d’écritures métier/Git déclenchées par ce mode, refus d’une sortie invalide ou d’un contexte obsolète, séparation des discussions et maintien des trois validations. L’inspection du 12 novembre 2026 constate l’absence de `output_mode` dans les quatre skills installés et leurs références. Le double mode est donc une cible approuvée, non une capacité attestée de ces fichiers. Aucun skill, code produit ou accès au compte n’est modifié dans cette mise à jour documentaire.

## Contrats partagés — conception approuvée

Les contrats ci-dessous déclinent les choix acceptés ; leurs noms et formats font partie du dossier approuvé le 10 novembre 2026. Ils définissent les faits nécessaires aux échanges entre frontend, coordination, propriétaires métier et intégration Codex. Ils ne décrivent pas les signatures privées ou toutes les colonnes SQL.

### Commandes, acquittements et lectures

Les opérations publiques sont regroupées sous `/api/v1`. Le chemin et le contexte identifient les ressources ; un désaccord entre les deux est rejeté. Les lectures sont sans effet de bord. La version de protocole reste distincte des versions des projets gérés.

| Famille de contrat | Opérations et données utiles | Propriétaire / parcours |
| --- | --- | --- |
| Projets | Créer et lire ; modifier description ; archiver/restaurer | Gestion des projets ; FLOW-001, SCREEN-001 à SCREEN-003 |
| Versions | Préparer, sélectionner/reprendre une version, rouvrir avant livraison, déclarer livraison ; référence exacte et état d’activité | Gestion des versions avec coordination ; FLOW-002, SCREEN-004 |
| Cadrage | Lancer analyse ; proposer/interpréter une réponse ; confirmer/corriger une décision ; arbitrer inclusion/report ; modifier catalogue ; demander synthèse/catalogue/consolidation dans l’ordre autorisé | Cadrage fonctionnel ; FLOW-003/004, SCREEN-005 à SCREEN-008 |
| Validations | Valider explicitement synthèse, catalogue ou final, avec révisions et dépendances amont identifiées | Cadrage fonctionnel avec coordination ; FLOW-005, SCREEN-006/008/009 |
| Continuité | Lire/enregistrer le brouillon de son contexte, envoyer un message, réessayer une tentative sur le même message, lire son état et son résultat | Continuité ; FLOW-003/007, SCREEN-005/011 |
| Références et historique | Lire une copie approuvée et les changements attribués à projet/version/fonctionnalité ; distinguer livraison et approbation | Lecture coordonnée auprès des propriétaires ; FLOW-006, SCREEN-004/010 |

Routes partagées retenues ; les alternatives séparées par `|` représentent des chemins distincts, pas une valeur à transmettre littéralement :

| Routes | Effet / contenu spécifique dans payload |
| --- | --- |
| `GET /api/v1/projects`, `GET /api/v1/projects/{project_id}` | Liste et contexte de projet, sans mutation |
| `POST /api/v1/projects`, `PATCH /api/v1/projects/{project_id}/description` | Création avec nom/description ; correction de description |
| `POST /api/v1/projects/{project_id}/archive|restore` | Archivage ou restauration selon règles métier |
| `GET /api/v1/projects/{project_id}/versions`, `POST /api/v1/projects/{project_id}/versions` | Lire/préparer une version ; référence et contexte identifiés |
| `POST /api/v1/versions/{version_id}/resume|suspend|reopen|delivery` | Action explicite de reprise, suspension, réouverture ou déclaration de livraison |
| `GET /api/v1/versions/{version_id}/state` | Lecture cohérente du cadrage courant, révisions et opérations pertinentes |
| `POST /api/v1/versions/{version_id}/analysis` | Analyse et préparation des questions ; reçu accepted avec tentative |
| `POST /api/v1/versions/{version_id}/questions/{question_id}/interpretations|confirmations` | Interpréter le texte libre, ou confirmer explicitement l’interprétation relue/corrigée ; ces opérations restent distinctes |
| `POST /api/v1/versions/{version_id}/proposals/{proposal_id}/decisions` | Arbitrage explicite et version ciblée ; pas d’inclusion par simple discussion |
| `PATCH /api/v1/versions/{version_id}/catalogue` | Modifications structurées des modules/fonctionnalités/critères selon révisions et provenance |
| `POST /api/v1/versions/{version_id}/summary|catalogue|final/generations` | Produire la proposition de l’étape autorisée ; aucune validation automatique |
| `PATCH /api/v1/versions/{version_id}/summary` | Correction de synthèse avec traçabilité et revalidation des éléments affectés |
| `POST /api/v1/versions/{version_id}/approvals` | `stage=summary|catalogue|final`, révisions et validations amont concernées ; commande distincte de génération |
| `GET /api/v1/conversations/{conversation_id}/state` | Messages, brouillon et tentatives avec contexte et révisions |
| `PUT /api/v1/conversations/{conversation_id}/draft`, `POST /api/v1/conversations/{conversation_id}/messages` | Sauvegarder une saisie ou envoyer son texte ; opérations distinctes |
| `POST /api/v1/attempts/{attempt_id}/retries`, `GET /api/v1/attempts/{attempt_id}` | Réessai explicitement demandé sur la source existante ; lecture d’état sans relance |
| `GET /api/v1/projects/{project_id}/history`, `GET /api/v1/snapshots/{snapshot_id}` | Historique attribué et valeurs d’une copie précise |
| `GET /api/v1/commands/{command_id}`, `GET /api/v1/events` | Retrouver le reçu d’une opération ; ouvrir le flux SSE |

La notation de génération désigne `/summary/generations`, `/catalogue/generations` et `/final/generations`. La création du fil général fait partie de l’initialisation du projet ; un fil de question est préparé avec sa question si nécessaire, sans mutation cachée par une lecture GET ni nouvel écran de création de fil.

Toute mutation porte `command_id`, `context`, `expected_revisions` et `payload`. `context` contient les identifiants applicables de projet, version, discussion et question ; les champs non applicables sont absents, pas remplacés par la vue actuellement ouverte. Les créations initiales n’ont pas de révision antérieure à fournir ; les corrections, sauvegardes et validations identifient celle de la ressource lue. Les révisions sont comparables pour un même objet, sans supposer un ordre global entre tous les objets.

Le backend conserve un reçu associant l’identifiant à l’opération, au contexte, au contenu exact de la commande et à son résultat. Même identifiant et même commande renvoient le résultat connu ; un autre contenu avec le même identifiant est un conflit. L’effet métier, son historique et le reçu sont enregistrés atomiquement. Le reçu est consulté avant de tenter une réexécution : une réponse perdue ne déclenche ni seconde validation ni second message. Aucune purge arbitraire de ces reçus n’est prévue dans ce MVP.

L’acquittement distingue `committed` (effet enregistré) et `accepted` (tentative IA enregistrée, résultat non encore obtenu). Il contient `command_id`, contexte, révisions acquittées et résultat ou `attempt_id`. Un échec de commit n’est jamais annoncé comme sauvegarde réussie. Une sauvegarde de brouillon acquitte la révision enregistrée ; si l’utilisateur a déjà saisi davantage, l’interface garde ce nouveau contenu comme non encore sauvegardé. Les révisions obsolètes sont refusées avec l’état courant utile à la réconciliation ; aucun écrasement automatique d’une saisie plus récente.

Une lecture cohérente de contexte renvoie les ressources pertinentes avec leur révision, les décisions et validations applicables, brouillon, messages et tentatives connus. Elle sert au chargement et à la reprise ; une copie approuvée est lue explicitement par son identité, jamais substituée silencieusement par le courant. Une navigation n’altère pas le contexte des commandes déjà acceptées.

### Erreurs communes

Les erreurs exposent `code`, `message` en français, `command_id` si applicable, `context` et détails de réconciliation non sensibles. Codes applicatifs retenus : `invalid_input`, `not_found`, `revision_conflict`, `command_conflict`, `operation_not_allowed`, `prerequisite_missing`, `blocking_question`, `storage_unavailable`, `ai_unavailable`, `ai_result_invalid` et `ai_state_uncertain`. Correspondance partagée : 422 pour invalid_input, 404 pour not_found, 409 pour conflits/prérequis/état interdit/questions bloquantes/état IA incertain, 503 pour indisponibilité stockage ou IA, 502 pour résultat IA invalide. Une commande committed répond 200, ou 201 à la création ; accepted répond 202 avec attempt_id. Le client s’appuie aussi sur le code applicatif et ne déduit pas la reprise en analysant le texte d’erreur.

Un conflit demande une relecture et une action appropriée dans l’UX existante. Une erreur de stockage conserve la saisie locale avec son état non enregistré. Une erreur IA conserve message et décisions, avec réessai dans le même contexte. Les règles archivage, version livrée, suspension et étapes préalables sont contrôlées côté serveur à l’opération puis avant tout effet métier après une attente IA. Les contrôles techniques ne créent aucune nouvelle validation humaine.

### Tentative IA et limites de reprise

Une commande d’envoi enregistre ensemble message utilisateur, tentative et reçu. Le réessai IA porte `source_message_id` et un nouvel identifiant de commande/tentative ; il ne recrée pas le message. Une retransmission réseau de ce réessai conserve son identifiant initial. Une analyse sans message de discussion référence sa commande et son contexte métier, sans inventer de message utilisateur.

La tentative conserve contexte, tâche, révisions sources, versions d’instructions/schéma, identifiants thread/turn connus et état. États techniques retenus : `queued`, `dispatching`, `running`, `succeeded`, `failed`, `uncertain`. Ils alimentent attente/erreur/résultat de l’UX ; ils ne créent pas de nouveaux écrans ou commandes utilisateur.

Une discussion applicative est associée à son propre thread Codex : fil général du projet distinct de chaque fil de question, avec le contexte de version fourni à chaque tour. Les tâches structurées hors discussion utilisent un thread de travail propre à la version, distinct du fil général. Un seul tour est lancé à la fois dans un même thread ; une seconde commande incompatible retrouve l’opération en cours ou reçoit une erreur, sans démarrer un doublon. Ces identités techniques ne deviennent pas l’identité des conversations métier.

Avant reprise, réconcilier le tour connu et recharger le contexte utile depuis l’application. Si le thread n’est plus disponible, la tâche suivante peut créer un thread avec le contexte et les échanges sauvegardés pertinents, sans transformer la disparition de session en perte de données ou relance du tour incertain. Les instructions et structured restent explicites, même lors d’une reprise. Ne pas utiliser la mémoire du thread comme autorité sur les versions, validations ou livraisons.

Avant l’envoi externe, enregistrer `dispatching` ; après identification du tour, conserver son identité. Un arrêt entre ces opérations laisse une incertitude : SQLite et l’envoi stdio ne sont pas atomiques. Au redémarrage, réconcilier l’état et l’historique connus de Codex avant de relancer quoi que ce soit. En cas d’incertitude non résolue, conserver le travail et afficher l’erreur/réessai existant ; ne pas promettre une exécution exactement une fois du côté modèle ni relancer silencieusement une inférence. Les références approuvées restent utilisables sans session Codex disponible.

La finalisation d’un résultat vérifie identité, contexte et révisions, puis enregistre atomiquement réponse/proposition et état terminal. Un contenu invalide, obsolète ou interdit par l’état métier n’est pas appliqué. Une réponse tardive reste rattachée à son origine et ne modifie pas un autre projet ou une autre version à cause d’un changement de vue. Les événements de résultats durables suivent le commit.

### Événements et resynchronisation

Chaque connexion SSE reçoit un événement initial `ready` après établissement de son abonnement. Le frontend met les notifications suivantes en attente, lit son contexte cohérent puis applique celles plus récentes que les révisions retournées. Cette séquence est répétée à chaque reconnexion, y compris après redémarrage ; elle ferme la course entre lecture et abonnement. L’identifiant de session du flux permet de reconnaître un redémarrage ; Last-Event-ID seul n’est pas un journal durable.

Enveloppe retenue : `schema_version`, `event_id`, `stream_session_id`, `type`, `context`, `command_id`/`attempt_id` si applicables, `resource_revisions`, `payload`. Types utiles : `resource_changed`, `attempt_changed`, `result_available`, `resync_required`, et fragments transitoires éventuels. Un changement peut inviter à relire les données ; la notification n’est pas une seconde source d’autorité. Doublons et événements anciens sont ignorés selon identité/révision. Une notification inconnue ou une perte détectée déclenche la resynchronisation, pas une approbation.

Les files de notifications sont bornées ; un lecteur trop lent reçoit une demande de resynchronisation ou une fermeture entraînant relecture. Ne pas garder une transaction SQLite ouverte pour alimenter le flux. Une fermeture de connexion nettoie l’abonnement ; la tentative appartient au backend et peut enregistrer son résultat. Les heartbeats sont techniques, sans contenu sensible. Les valeurs de bornage et délais restent des réglages à vérifier, sans seuil de performance inventé.

### Résultats structurés des skills

L’appel applicatif fournit explicitement `output_mode=structured`, `task`, `context`, `source_revisions`, données utiles et versions d’instructions/schéma. Le contexte contient le courant et, si nécessaire, les valeurs de référence approuvées avec leur identité et les faits de livraison distincts. Les saisies utilisateur sont des données, pas des instructions autorisant une action technique.

Enveloppe de sortie retenue : `schema_version`, `task`, `context`, `source_revisions` et `result`. Le schéma de tâche précise les champs partagés suivants ; les schémas d’implémentation ne peuvent ajouter un effet métier ou remplacer une validation explicite :

| task | Contenu de result |
| --- | --- |
| `prepare_questions` | `questions[]` : `local_key` ou `existing_question_id`, `title`, `context`, `recommendation`, `rationale` ; `open_points[]` pour informations manquantes |
| `interpret_answer` | `question_id`, `proposed_text`, `rationale`, `clarification_needed` et éventuelle `clarification_question` ; jamais une réponse déclarée confirmée |
| `prepare_summary` | `summary` : `goal`, `users`, `scope`, `decision_refs`, `excluded`, `deferred`, `open_question_ids` ; `coverage` déclarée comme proposition à contrôler |
| `prepare_catalogue` | `modules[]` avec `local_key`/identité existante et `title` ; `features[]` avec `existing_feature_id` ou `local_key`, `module_ref`, `title`, `behavior`, `acceptance_criteria`, `decision_refs` ; éventuel `proposed_scope` à arbitrer |
| `prepare_final` | `sections`, `source_approval_ids`, `blocking_question_ids` proposés ; dépendances/prérequis et questions bloquantes sont aussi contrôlés par le backend |
| `discuss` | `text` en Markdown et éventuels `mentioned_resource_ids` ; aucune mutation de cadrage/description/catalogue/validation/livraison |

Le backend attribue les nouvelles identités persistantes et contrôle celles des objets déjà existants ; une identité annoncée par le modèle ne permet pas de changer de portée. Les champs prétendant accorder une validation, une livraison ou une autorisation technique ne sont pas des effets métier acceptables. Le schéma technique est fourni via output_schema et versionné avec les instructions ; les modèles partagés doivent reprendre ces noms et préserver les contraintes de portée/provenance. Les détails de type locaux sont fixés dans ce contrat partagé avant branchement des producteurs et consommateurs.

Le backend conserve la provenance de chaque proposition, la tâche, les révisions sources et les versions d’instructions/schéma dans la tentative et ses liens vers le résultat. Un échec de schéma, de référence, de révision ou de règle métier suit l’erreur existante `ai_result_invalid` ou le conflit applicable : aucune écriture métier non autorisée, aucune validation/livraison et aucune bascule automatique en `files`. Une reprise redemande explicitement `structured` et les instructions dépendantes adaptées.

Les sorties correspondent à la tâche autorisée et à ses prérequis. Elles peuvent produire une proposition, une interprétation ou une réponse selon l’action UX ; les validations humaines et arbitrages restent des commandes distinctes. Les formats exacts par tâche seront versionnés dans l’implémentation et vérifiés contre le SDK/runtime fixé avant utilisation. Un schéma valide ne remplace ni la vérification des références ni la relecture fonctionnelle.

## Parcours et preuves attendues — conception approuvée

Ces contrôles portent sur les invariants utiles, pas sur un miroir des fonctions privées. Ils restent à réaliser sur l’application ; les vérifications documentaires ne les remplacent pas.

| Parcours | Risque à couvrir | Preuve attendue lors de la réalisation |
| --- | --- | --- |
| FLOW-001 / SCREEN-001..003 | Projet archivé modifié ou données perdues après restauration | Consultation conservée, mutations interdites avant restauration, validations/livraison inchangées |
| FLOW-002 / SCREEN-004 | Deux versions actives, référence écrasée ou livraison confondue | Contrainte d’unicité, réouverture atomique avec référence intacte/suivante suspendue, déclaration de livraison distincte |
| FLOW-003 / SCREEN-005 | Interprétation approuvée implicitement, saisie écrasée, état IA perdu | Confirmation explicite, révision obsolète refusée, sauvegarde échouée signalée, reprise après coupure/processus arrêté |
| FLOW-004 / SCREEN-007/008 | Proposition incluse automatiquement ou identité fonctionnelle perdue | Arbitrage explicite, identité stable et contenu par version, traçabilité identique des modifications manuelles |
| FLOW-005 / SCREEN-006/008/009 | Validation d’un état ancien, validation partielle ou mauvais ordre | Contrôle des révisions/prérequis/questions bloquantes et atomicité validation/copie/journal/reçu |
| FLOW-006 / SCREEN-010 | Historique ou copie relisant le contenu courant à tort | Anciennes valeurs consultables après corrections et migrations ; approbation et livraison distinctes |
| FLOW-007 / SCREEN-011 | Mélange des projets, duplication d’un message ou effet métier d’un chat | Contextes persistants, réponse HTTP perdue puis réémission dédupliquée, réessai lié au message existant, aucune mutation automatique du cadrage |

Vérifier aussi Markdown avec HTML brut échappé, clavier/IME, focus/dialogues, thèmes et adaptation mobile sur les écrans réels. Tester spécifiquement la branche files historique des skills et structured avec contexte applicatif, ainsi que l’état effectif des outils et permissions. Compte/quotas, appel authentifié et absence de bascule payante doivent être exercés seulement dans une étape dédiée dont le coût est maîtrisé ; aucun essai réel n’est attesté ici.

## Livraison locale acceptée

Le 10 novembre 2026, après explication de l’application Windows autonome, l’utilisateur a choisi « ouais A pour le moment ». Le MVP se lance depuis le projet dans un environnement Python isolé ; le frontend compilé est servi par FastAPI. Un lanceur peut appeler directement l’interpréteur sans activation PowerShell. L’environnement se recrée depuis les dépendances fixées ; il n’est ni copié entre machines ni versionné dans Git.

Fixer ensemble Python, les dépendances directes/transitives, le SDK, son runtime et le build frontend. La référence auditée reste SDK/runtime 0.167.0 ; le CLI global 0.163.0 n’a pas été mis à jour. Le runtime effectivement lancé est déterminé explicitement, pas pris au hasard dans PATH. Les versions observées du poste ne prouvent pas la compatibilité d’ensemble. B paquet Windows autonome n’est pas dans cette livraison et n’a pas de version attribuée. La future cible privée reste distincte.

## Dépendances autorisées — conception approuvée

Le navigateur dépend uniquement de l’interface HTTP/SSE de coordination. Le point d’entrée applicatif appelle gestion des projets, versions, cadrage, continuité et intégration Codex ; il compose leurs opérations mais ne remplace pas leurs règles métier. Les packages métier reçoivent le contexte requis et utilisent leur accès SQL via une transaction fournie ; ils ne se coordonnent pas par appels mutuels cycliques et ne modifient pas les données d’un autre propriétaire. La continuité reçoit les faits nécessaires à ses vues depuis la coordination, sans devenir une seconde autorité sur les décisions.

Les utilitaires de persistance portent connexion, transactions, migrations et sauvegarde, pas un CRUD générique contournant les règles. L’intégration Codex reçoit des données préparées et ne lit pas directement SQLite. Ses résultats reviennent à la coordination puis au propriétaire compétent. Le mode files des skills reste un usage documentaire séparé ; il n’est pas exécuté par l’API applicative. Les classes, signatures privées et découpages de fichiers restent locaux à la réalisation.

Les références `MOD-*`, `IFACE-*` et `DATA-*` du [contrat de transmission](ARCHITECTURE-CONTRACT.json) sont les identifiants techniques définis par ce dossier pour la planification. Elles ne renomment pas les modules fonctionnels ni les FEAT/FLOW/SCREEN approuvés. Le contrat indique les consommateurs, l’autorité de données et les sources réelles ; tous les éléments V1 sont nouveaux, sans code livré à migrer.

## Protection locale et intégration Codex — conception approuvée

### Processus et permissions

L’usage réel cible une seule instance par répertoire de données et un worker applicatif sans rechargement automatique. Au démarrage, vérifier configuration, schéma, accès aux données et écoute loopback ; ne pas lancer une seconde instance concurrente sur le même répertoire. Un port occupé n’autorise pas un changement vers une interface réseau publique. Le gestionnaire de cycle de vie crée et ferme le client SDK et son processus enfant, draine ses sorties et nettoie les abonnements. L’API de travail n’expose ni shell, ni fichiers locaux, ni commande SQL au navigateur.

Le profil effectif de l’intégration demande read_only et refus d’escalade, désactive les capacités non nécessaires (shell, web, MCP, apps/plugins et automatismes étrangers au workflow), et fournit les instructions adaptées avec structured explicite. Le chargement des règles communes et de la branche applicable se fait de façon contrôlée ; une dépendance documentaire ne réactive pas un workflow d’écriture. Les réglages personnels/administrés et capacités réellement chargées doivent être vérifiés, pas déduits du seul cwd ou preset.

Le handler SDK par défaut peut accepter certaines demandes : il n’est pas autorisé à décider pour Aura Forge. L’adaptateur doit installer un refus explicite des demandes de commandes/fichiers et arrêter l’intégration sur une requête serveur inconnue, sans accorder une permission par défaut. L’audit 0.167.0 expose ce callback sur CodexClient synchrone bas niveau, pas sur la façade AsyncCodex. Utiliser ce point de contrôle dans l’adaptateur, avec opérations bloquantes hors boucle FastAPI ; ne pas faire d’appel SDK bloquant réentrant depuis son thread lecteur. Les méthodes typées de thread/tour, flux et sorties structurées restent celles du SDK officiel ; aucune liaison exec ou couche RPC maison parallèle n’est ajoutée.

L’exactitude des refus et de la configuration doit être démontrée sur le runtime fixé sous Windows avant usage réel. Une capacité inattendue ou un confinement requis non établi désactive l’intégration IA ; les lectures et modifications applicatives autorisées restent disponibles. Ne pas présenter read_only/never comme une isolation OS ou un mode universel sans outils. Les écritures propres au runtime et ses credentials sont distincts des fichiers métier ; aucun secret ne passe au frontend, aux prompts métier ou aux journaux ordinaires.

### Accès ChatGPT et contrôle du coût

Avant génération, établir le compte actif, la connexion ChatGPT attendue et l’autorisation d’usage inclus à partir de l’état fournisseur actuel, pas d’une estimation de pourcentage ou date de remise à zéro. Le modèle SDK audité expose ordinary_usage_allowed optionnel, lié au compte actif : absence/null n’est pas une autorisation. La sémantique et le comportement réels doivent être vérifiés dans un contrôle d’intégration avant le premier appel dont le coût ne serait pas maîtrisé.

La politique retenue est le refus de lancer une génération si l’accès inclus est inconnu, indisponible ou épuisé. Aucun achat, recharge, consentement technique automatique à consommer des crédits ou secours API payant. Une lecture préalable ne garantit pas à elle seule le coût du tour suivant : vérifier aussi la politique côté fournisseur et ses courses possibles. Tant que cette garantie n’est pas établie pour le compte/runtime, laisser l’IA désactivée et conserver le travail. L’architecture n’atteste ni droits réels, ni gratuité, ni usage illimité ; une autre politique nécessiterait une décision explicite de l’utilisateur.

### Requêtes web et données

Servir statique/API/SSE sur la même origine en loopback, avec Host autorisés explicitement et validation des chemins. Les mutations sont JSON, via méthodes mutantes, avec contrôle de l’origine et du contexte de requête ; CORS n’est pas ouvert globalement. Prévoir le cas documenté des lectures same-origin sans Origin, sans accepter arbitrairement une origine étrangère. Ne pas faire dépendre la protection des mutations de la seule impossibilité pour une page étrangère de lire la réponse. Une requête Web ou locale reste soumise aux règles métier, au contexte et aux révisions.

Conserver données/configuration/sauvegardes dans un répertoire utilisateur persistant distinct du checkout, des dépendances et du statique distribué, avec les accès utilisateur nécessaires. Aucun chemin fourni par le modèle n’est utilisé pour écrire dans la base ou le système de fichiers. Échapper le HTML brut dans Markdown et valider les URL/actions affichées ; ne pas injecter les sorties IA en HTML actif. Ces protections ne sont pas une authentification contre un autre processus du même utilisateur. La cible serveur privée ultérieure doit revoir accès, TLS et authentification du fournisseur avant exposition.

## Migrations, sauvegarde et diagnostic — conception approuvée

Utiliser des migrations de schéma versionnées, vérifiées sur la bibliothèque distribuée. Le démarrage refuse un schéma inconnu/trop récent plutôt que de le modifier implicitement. Avant migration, arrêter les opérations applicatives, produire une sauvegarde cohérente et vérifier son achèvement ; appliquer la migration avec les garanties transactionnelles adaptées puis contrôler intégrité, clés étrangères et compatibilité des formats historiques. L’échec laisse l’application arrêtée sur un état connu et une procédure de restauration, sans démarrer sur un schéma partiellement migré.

Le profil de persistance retenu fixe WAL avec synchronous=FULL, clés étrangères activées/vérifiées par connexion, mode transactionnel explicite, transactions courtes et attente de verrou bornée. Le runtime doit inclure le correctif WAL-reset ; le constat local ne remplace pas la vérification de la distribution. Les opérations SQLite synchrones ne bloquent pas la boucle serveur et ne restent pas ouvertes pendant IA/SSE. Ces réglages font partie du dossier approuvé ; aucun benchmark ou seuil chiffré n’est revendiqué.

La sauvegarde opérationnelle est une procédure locale à la demande, et obligatoire avant migration ; elle utilise l’API de backup cohérent SQLite exposée en Python. Ce n’est ni un écran d’export ni une copie à chaud du seul fichier principal. Stocker les sauvegardes hors chemin remplaçable et documenter leur sensibilité. Fréquence régulière, rétention et emplacement de copie séparée du poste sont des réglages d’exploitation à choisir lors de la mise en service, sans promesse de protection contre la perte du disque si tout reste sur ce même disque. Aucune synchronisation cloud n’est incluse.

Restaurer application arrêtée et connexions fermées, sans mélanger la copie avec d’anciens WAL/SHM. Contrôler ouverture, intégrité, clés étrangères, schéma et consultation des références après restauration. Un essai de restauration réussi est requis avant utilisation de données réelles et après modification du mécanisme. Aucun RPO/RTO ou test réalisé n’est inventé. Un retour arrière de code n’implique pas une rétrocompatibilité de schéma ; restaurer un ensemble code/données compatible selon la procédure documentée.

Les diagnostics techniques identifient commande, contexte non sensible, tentative et révisions, état du processus et codes d’erreur, sans texte de conversation, prompt complet ou credentials par défaut. Le journal métier avant/après reste dans le stockage protégé et sert l’historique, pas les logs techniques. Les messages visibles gardent l’état sauvegardé/non sauvegardé honnête. L’accès aux données persistées est indépendant d’un service de télémétrie externe ; aucun service supplémentaire de suivi n’est requis pour ce MVP.

## Revue, risques et passage à la planification

Le [contrat structuré](ARCHITECTURE-CONTRACT.json), les onze choix individuels et les contrats, dépendances et contrôles de ce dossier ont été approuvés le 10 novembre 2026 par « je valide », en réponse à la demande de validation finale du dossier d’architecture V1. Aucun arbitrage bloquant pour planifier le dossier historique approuvé n’est ouvert : planning_ready est true. Les adaptations produit de FEAT-004/005/006 ne sont pas comprises dans cette approbation et restent à valider avant leur planification comme exigences approuvées. Les conditions de réalisation ci-dessous restent à vérifier ; aucune application n’est déclarée implémentée ou livrée.

| Point restant | Classification | Condition concrète |
| --- | --- | --- |
| Approbation du dossier intégré et de ses contrats/contrôles | Obtenue le 10 novembre 2026 | « je valide » ; preuve conservée dans le contrat, planning_ready true |
| Compatibilité Python/FastAPI/Pydantic/SDK/runtime et capacités effectives Windows | Non bloquant pour organiser la réalisation ; préalable à l’intégration réelle | Fixer les versions, vérifier lancement/refus/configuration ; intégration IA désactivée en cas d’échec ; réexaminer l’architecture si aucun confinement adéquat n’est réalisable |
| Accès inclus et politique effective du compte | Non bloquant pour planifier ; bloquant pour activer les générations | Vérifier compte/runtime sans supposer les droits ; ne pas générer quand la possibilité d’usage sans surcoût n’est pas établie |
| Paramètres locaux de connexion, dépendances, bibliothèque de rendu et schémas détaillés par tâche | Choix d’implémentation dans les contrats approuvés | Fixer et vérifier sans changer les invariants, le périmètre UX ou les validations |
| Fréquence/rétention et emplacement séparé des sauvegardes | Réglages de mise en service, sans SLA défini | Documenter le choix utilisateur/opérateur ; sauvegarde avant migration et essai de restauration obligatoires |

L’objectif de coût, la maturité expérimentale app-server et les limites de confinement ne sont pas effacés par ce classement. Les gardes de désactivation et les vérifications sont des contraintes de réalisation ; un résultat incompatible doit revenir en arbitrage plutôt qu’être contourné. Le passage au serveur privé ou à d’autres moteurs reste hors V1. Aucun test applicatif, connexion utilisateur, génération, sauvegarde/restauration réelle ou mise à jour du CLI n’a été réalisé pendant cette conception.
