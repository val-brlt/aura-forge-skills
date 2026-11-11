---
status: approved
active_version: v1
---

# Architecture d’Aura Forge Project AI

## État du système et du dossier

L’architecture de [V1 — MVP](../versions/v1/VERSION.md) est approuvée. Le 10 novembre 2026, l’utilisateur a répondu « je valide » à la revue du dossier intégré, contrats et contrôles compris. La planification peut commencer ; cette approbation ne constitue pas une livraison ou une autorisation Git.

Le dépôt contient le cadrage et les maquettes approuvés ; aucune application de production ni livraison n’est confirmée. Les simulations des maquettes ne définissent pas une stack de production.

## Contraintes fonctionnelles et UX

La [présentation du projet](../PROJECT.md) et le [contrat UX V1](../versions/v1/ux/UX-CONTRACT.json) font autorité : application web française, usage personnel, plusieurs projets et versions, sans authentification applicative ni gestion de plusieurs utilisateurs dans le MVP. Les propositions, inclusions dans un périmètre, validations et déclarations de livraison restent distinctes et explicites.

Les données doivent permettre la reprise du travail et préserver les références approuvées. Les discussions générales appartiennent au projet ; les discussions liées à une question restent distinctes. Une discussion ne modifie pas automatiquement les décisions métier.

## Exécution du MVP — décision acceptée

Le MVP s’exécute sur l’ordinateur personnel de l’utilisateur. L’interface s’utilise dans son navigateur ; le service applicatif est accessible uniquement par boucle locale. L’accès direct depuis un autre appareil n’est pas prévu dans cette cible initiale.

Ce placement évite d’exploiter un serveur distant pour le premier usage personnel. En contrepartie, le poste et l’application doivent fonctionner pendant l’utilisation ; installation, mises à jour et sauvegarde suivent la conception V1 approuvée et restent à réaliser. L’écoute locale ne dispense pas de contrôler les requêtes web et les origines autorisées.

L’utilisateur a accepté cette option le 9 novembre 2026 : « A pour le mVP et plus tard sur un serv privée ». Le serveur privé est une cible ultérieure, sans version ni hébergeur attribué. Le MVP n’inclut pas cette infrastructure. Les prochains choix doivent tenir compte du déplacement futur des données, de la configuration et des accès, sans promettre une migration sans coût.

Le moteur Codex est exécuté localement, mais ses requêtes aux modèles OpenAI restent distantes ; le placement local de l’application ne signifie pas une inférence hors ligne.

## Assistant IA du MVP — décision acceptée

Le MVP intègre Codex installé sur le poste, avec la connexion ChatGPT comme mode d’accès visé. L’utilisateur a retenu ce choix le 9 novembre 2026 : « enfaite je voudrais faire tous mais dans un premier temps faire avec codex en local pour ne pas payer en plus ». La priorité est d’utiliser son accès existant et d’éviter une facturation API supplémentaire. L’[ADR-0001](../../adr/0001-codex-local-mvp.md) conserve le compromis face à une API de modèle directe et à un modèle local.

Ce choix ne garantit pas un usage gratuit ou illimité. La [documentation d’authentification](https://learn.chatgpt.com/docs/auth) distingue connexion ChatGPT et clé API ; les [conditions d’usage du plan](https://learn.chatgpt.com/docs/pricing?codex-pricing-plans=individual) comprennent limites et crédits. Les droits, la session et les réglages de facturation du compte ne sont pas vérifiés. Le MVP ne doit ni acheter de crédits ni basculer automatiquement vers une API payante. L’épuisement de l’allocation doit conserver le travail et permettre une reprise, sans approbation métier implicite. La détection de cette situation et l’éventuel usage de crédits déjà disponibles restent à vérifier avant de garantir l’absence de surcoût.

Les échanges, les décisions et les références approuvées doivent rester exploitables indépendamment des fichiers de session de Codex. Une permission technique accordée au runtime ne constitue pas une validation fonctionnelle dans Aura Forge.

## Liaison Codex app-server — décision acceptée

Le backend local pilote un processus Codex app-server par son protocole JSON-RPC sur stdio. Le navigateur utilise l’application Aura Forge ; il ne se connecte pas directement au processus Codex. Ce transport ne nécessite pas d’exposer un port réseau Codex.

L’utilisateur a retenu app-server le 9 novembre 2026 : « je partirai quand même sur codex app server », après comparaison avec `codex exec`, vérification de la dernière version et présentation du statut expérimental. L’[ADR-0002](../../adr/0002-codex-app-server.md) consigne ce choix et ses conséquences. `exec` n’est pas une seconde liaison ou un secours automatique à réaliser dans le MVP.

App-server permet de suivre les conversations et les événements progressifs dans une intégration interactive. L’application doit gérer la vie du processus, les connexions et la reprise après erreur. Une réponse IA, une permission technique ou un événement de fin ne valent jamais validation métier. Les capacités du protocole ne créent pas de nouveaux contrôles UX au-delà des parcours approuvés.

Le risque d’évolution de l’interface expérimentale est accepté pour ce MVP personnel. La référence stable évaluée est Codex `0.167.0` ; le protocole et la version effectivement supportés devront être fixés et vérifiés ensemble. L’installation inspectée reste `0.163.0`, sans mise à jour effectuée. Aucun échange authentifié ni test de génération n’a encore été réalisé.

## Backend Python et FastAPI — décision acceptée

Le backend du MVP est écrit en Python avec FastAPI. Il porte les règles métier et la validation des commandes, les accès à SQLite et le pilotage de Codex app-server. L’utilisateur a accepté ce choix le 9 novembre 2026 : « ok on part sur python alors ça sera mieux », en réponse à la proposition Python + FastAPI après vérification du SDK. L’[ADR-0003](../../adr/0003-python-fastapi-backend.md) conserve la comparaison avec TypeScript/Fastify et C#/ASP.NET Core.

L’intégration utilise le SDK Python officiel `openai-codex` pour app-server. Le paquet `0.167.0` examiné fournit une façade asynchrone, les flux d’événements, les handles d’interruption et de steering, les sorties structurées et la reprise des conversations. Sa distribution dépend du runtime Codex `0.167.0` épinglé. Cette référence de conception ne constitue pas une installation ni une validation de fonctionnement sur le poste.

Les accès de plus bas niveau nécessaires, notamment les limites du compte, restent dans l’intégration Codex. Les valeurs par défaut de permissions du SDK ne doivent pas être reprises sans configuration explicite. La politique, le cycle de vie du processus et la reprise sont définis avec les contrats partagés approuvés. Le stockage métier ne repose pas exclusivement sur les sessions SDK.

SQLite a été choisi séparément pour la persistance, HTTP JSON et SSE pour les échanges avec le navigateur. Python ne les impose pas. Aucun avantage chiffré de performance ou de coût n’est présumé.

## Interface Vue et TypeScript — décision acceptée

L’interface est construite avec Vue et TypeScript, puis compilée en fichiers statiques servis par FastAPI. L’utilisateur a accepté l’option A le 9 novembre 2026 : « ok je valide A ». L’[ADR-0004](../../adr/0004-vue-typescript-frontend.md) conserve le compromis face à React/TypeScript et Jinja2/HTMX.

Vue porte les états d’interface nécessaires aux questions, interprétations, documents, brouillons et discussions. Les règles et validations métier restent contrôlées par Python ; un état local modifié ne prouve pas qu’une sauvegarde ou une validation est enregistrée. Le contexte des brouillons et échanges respecte la portée projet, version ou question définie par l’UX.

Node intervient pour le développement et la construction de cette interface ; l’exécution des fichiers compilés ne requiert pas de serveur Node permanent. Le navigateur communique avec Aura Forge en HTTP JSON et SSE et ne reçoit pas d’accès direct au SDK, au processus ou aux credentials Codex. Les contrats précis des commandes et notifications sont définis dans la conception V1 approuvée.

Les maquettes approuvées définissent le rendu et les comportements à reproduire. Routeur, store, bibliothèque visuelle et moteur Markdown ne sont pas choisis par cette décision. L’accessibilité, le focus, la composition du texte, les thèmes et le rendu Markdown devront être vérifiés dans l’interface réelle.

## Persistance SQLite — décision acceptée

Les données métier du MVP sont conservées dans une base SQLite sur le même poste que le backend. Seul le backend accède à cette base ; le navigateur passe par Aura Forge. L’utilisateur a accepté A SQLite le 10 novembre 2026 : « je vais faire A », après comparaison avec PostgreSQL. L’[ADR-0005](../../adr/0005-sqlite-local-storage.md) conserve le compromis.

SQLite évite un service de base séparé pour l’usage personnel initial. En contrepartie, une seule transaction peut écrire à la fois : les écritures doivent être courtes et la contention traitée. Aucune transaction ne reste ouverte pendant un échange IA ou une attente utilisateur. Contraintes, révisions et idempotence doivent préserver les règles métier ; le moteur ne les implémente pas seul. Les données et références approuvées restent indépendantes des sessions Codex.

Un futur serveur privé peut conserver SQLite avec le fichier et le backend sur le même hôte. Partager directement le fichier entre machines n’est pas la cible. PostgreSQL sera à réexaminer si plusieurs hôtes applicatifs ou des besoins de concurrence/exploitation le justifient ; une migration demandera du travail sur le schéma, les données et les requêtes.

Le choix du moteur ne fixe pas ORM, pilote ou réglages WAL. L’exploitation devra prévoir migrations versionnées, sauvegardes cohérentes et restauration vérifiée. La copie du seul fichier principal pendant une activité WAL n’est pas une sauvegarde garantie. La sauvegarde opérationnelle ne crée pas de fonction d’export produit dans le MVP.

## Organisation du backend — décision acceptée

Le backend reste une application unique, organisée par responsabilités métier. L’utilisateur a choisi A le 10 novembre 2026 par « A », face à une organisation par couches techniques globales. L’[ADR-0006](../../adr/0006-organize-backend-by-business.md) consigne le compromis : localiser les règles d’un métier, avec des dépendances et écritures à contrôler.

| Responsabilité technique | Autorité et rôle |
| --- | --- |
| Gestion des projets | Identité, description, archivage et restauration |
| Gestion des versions | Versions du projet, activité/suspension, livraison déclarée et liens de référence |
| Cadrage fonctionnel | Questions, interprétations, propositions, arbitrages, catalogue, validations et contenu des références approuvées |
| Continuité | Conversations, messages, brouillons, tentatives, reprise et consultation de l’historique |

Ces packages servent les quatre modules fonctionnels existants ; ils ne modifient pas le glossaire ou le périmètre produit. La consultation d’historique lit les faits conservés par leurs propriétaires et ne constitue pas une seconde autorité sur les validations ou livraisons. La continuité ne reçoit pas un droit générique d’écriture sur tous les objets.

La coordination applicative compose les opérations métier dans une même transaction SQLite si nécessaire, sans appels HTTP internes ni écritures directes dans les données d’un autre propriétaire. La réouverture doit ainsi conserver la référence approuvée, modifier l’état de travail et suspendre la version suivante de façon cohérente. Le modèle logique et le contrat transactionnel sont définis dans la conception V1 approuvée.

L’intégration Codex isole protocole, processus, sessions, événements et erreurs externes. Elle reçoit le contexte préparé par l’application et retourne des propositions ; elle ne valide jamais le cadrage. Le choix n’impose ni services métier séparés, bus externe, dépôts génériques ou couches de simple transmission. Leur absence est cohérente avec le MVP personnel et ses transactions communes.

## Échanges HTTP et SSE — décision acceptée

L’utilisateur a accepté A HTTP + SSE par « A » le 10 novembre 2026. Les actions et lectures passent par HTTP JSON ; le serveur publie les changements d’état utiles par un flux SSE mutualisé par page applicative. Voir [ADR-0007](../../adr/0007-http-json-and-sse.md), qui conserve les alternatives WebSocket et interrogations périodiques.

Chaque notification identifie son contexte de projet, version, discussion et tentative. Le navigateur traite les états attente, erreur et résultat selon l’UX approuvée, sans nouvel effet de texte ou contrôle imposé. Les réponses HTTP distinguent commande enregistrée et tentative IA encore en cours. Un acquittement de sauvegarde exige le commit réussi de la révision concernée ; la réception d’un événement ne vaut jamais validation métier.

EventSource peut reconnecter un flux, mais ne fournit ni journal durable ni rejeu automatique garanti. Au chargement et après reconnexion, l’interface relit l’état applicatif enregistré, avec une coordination entre abonnement et révisions pour ne pas perdre une mise à jour pendant cette lecture. SQLite reste l’autorité après une coupure ; les fragments éventuels sont transitoires jusqu’à l’enregistrement du résultat. Les contrats de réconciliation et de déduplication sont définis dans la conception V1 approuvée.

Une fermeture d’onglet libère l’abonnement sans annuler ni relancer automatiquement une tentative déjà acceptée par le backend. Connexions, files de notifications et lecteurs lents doivent être gérés. La même origine et la boucle locale ne remplacent pas les contrôles Host/Origin et des commandes. Aucun secret n’est placé dans l’URL du flux ou transmis au frontend.

## État courant et références approuvées — décision acceptée

L’utilisateur a accepté A le 10 novembre 2026 par « A » : état courant relationnel, copies immuables aux validations et journal des changements métier. Voir [ADR-0008](../../adr/0008-current-state-approved-copies-and-audit.md), qui conserve l’alternative de révisions immuables généralisées.

Le travail courant reste modifiable selon les règles métier. Les identités de projet, version et fonctionnalité restent stables ; le comportement et les critères d’une fonctionnalité sont attribués à leur version. Chaque validation explicite de synthèse, catalogue ou cadrage final conserve son contenu exact, sa révision source et ses dépendances approuvées. La copie ne dépend pas du contenu mutable pour être relue. Une nouvelle validation produit une nouvelle copie ; l’ancienne reste consultable.

La référence de cadrage finale et la livraison sont distinctes. Rouvrir une version non livrée conserve sa copie approuvée, permet de modifier le travail et exige de revalider les éléments affectés. La validité d’une validation pour l’état courant peut être perdue sans effacer son fait historique. La version suivante garde sa référence exacte et ses décisions pendant la suspension et la revue prévues.

Une mutation métier conserve son contexte, son origine et le changement avant/après dans la même transaction. Ce journal accompagne le courant ; son rejeu n’est pas nécessaire au démarrage. Les sauvegardes de brouillons, messages et tentatives suivent leur cycle propre, sans assimiler chaque frappe ou fragment à une décision. La conception V1 approuvée précise le modèle logique et la lecture des formats historiques versionnés.

## Adaptation des skills — décision acceptée

L’utilisateur a accepté le 10 novembre 2026, par « ça me parait ok », des skills locaux à deux modes de sortie. Voir [ADR-0009](../../adr/0009-dual-output-skills-and-structured-proposals.md). Les règles communes de cadrage restent partagées ; `output_mode=files` conserve le fonctionnement documentaire habituel, et `output_mode=structured` fournit des propositions structurées à l’application. Aucun parent supplémentaire n’est imposé.

Aura Forge transmet explicitement `structured`, la tâche, le contexte métier et le schéma attendu. Python valide le format, les références, les révisions et les règles métier, puis écrit SQLite. Codex ne reçoit pas de rôle d’écriture SQL ou de validation. Les questions, interprétations, synthèses et catalogues suivent des formats propres à leur tâche ; un résultat conforme au schéma n’est pas une décision humaine.

Le mode est propagé aux instructions dépendantes ; les procédures de fichiers, scratch, diff, Git et issue tracker appartiennent à `files`. Une erreur de format en mode applicatif ne déclenche pas de secours documentaire. Le mode de sortie reste distinct des opérations preview/apply/audit de structure-project. Les modifications des skills et leurs vérifications font partie de la réalisation à venir ; elles ne sont pas déjà effectuées.

Le backend garde les transitions et les validations, prépare le contexte de la bonne version et traite les sorties comme propositions. La discussion générale reste exploratoire. Codex app-server, son SDK et le mode d’accès visé restent ceux déjà choisis. Les permissions devront être explicites et vérifiées : refus d’escalade ne signifie pas désactivation de tous les outils ; read_only et cwd n’établissent pas un confinement des lectures. Aucun accès métier ne doit être confié sur la seule foi des instructions.

## Évolution des modes IA

L’utilisateur souhaite également des appels directs à des API de modèles et une inférence locale ultérieurement, sans version attribuée. La conception doit conserver les règles métier et les données indépendantes du moteur afin de permettre ces ajouts. Seul le connecteur Codex est dans le MVP ; les connecteurs et réglages des autres modes ne sont pas à construire maintenant.

Le futur serveur privé exigera une nouvelle vérification du mode d’accès autorisé à Codex ou au fournisseur choisi. L’authentification locale et ses credentials ne sont pas présumés transférables tels quels.

## Lancement depuis le projet — décision acceptée

Le 10 novembre 2026, l’utilisateur a choisi « ouais A pour le moment » : lancement depuis le projet avec un environnement Python isolé et reproductible pour le MVP. L’alternative d’une application Windows autonome est conservée comme possibilité ultérieure, sans date/version. Cette préparation facilite modification et diagnostic sur son poste, au prix d’une installation initiale et d’un environnement à recréer sur chaque cible. Un lanceur peut appeler directement le bon interpréteur ; aucune modification de la politique PowerShell n’est requise par cette conception.

L’interface est compilée puis servie par FastAPI. Les dépendances résolues et le runtime Codex doivent être fixés ensemble, sans utiliser arbitrairement le CLI global. Python est nécessaire à l’exécution du backend ; Node sert à la préparation et à la construction du frontend. Un serveur Node permanent ou un paquet Windows autonome ne font pas partie de cette livraison initiale.

## Exploitation locale — conception approuvée

Une instance applicative gère son processus Codex et ses abonnements SSE. La cible d’usage réel est un worker applicatif, sans rechargement automatique, avec données/configuration/sauvegardes hors checkout et environnement remplaçable. Le port est configurable en boucle locale ; un conflit produit un échec explicite, sans ouverture réseau élargie. Les credentials Codex restent hors données métier et ne sont pas fournis au navigateur.

Les requêtes doivent respecter une liste de Host locaux autorisés, la même origine et une politique explicite de contrôle des mutations ; GET ne modifie rien. Les origines étrangères, contenus inattendus et chemins vers fichiers métier sont refusés. La boucle locale n’authentifie pas un processus présent sur le poste. Un serveur privé futur nécessitera son propre contrôle d’accès et une vérification de l’authentification fournisseur.

La conception opérationnelle prévoit une sauvegarde cohérente avant migration, une procédure locale de sauvegarde à la demande et une restauration testée avant usage réel. Les délais/fréquence/rétention restent des réglages d’exploitation sans objectif chiffré présumé. Les copies approuvées sont l’historique métier ; les sauvegardes protègent le stockage et ne créent pas d’export produit.

L’intégration Codex doit refuser les permissions imprévues, contrôler ses capacités effectives et suspendre les générations quand l’accès inclus ne peut pas être établi. Elle n’achète aucun crédit et ne bascule pas vers une API payante. La compatibilité, les droits réels du compte et le comportement des limites sont des vérifications préalables à l’intégration sur données réelles, pas des tests déjà réalisés ou des garanties de gratuité.

## Revue du dossier intégré

Les choix individuels, les contrats détaillés, les contrôles opérationnels et la stratégie de vérification ont été approuvés ensemble le 10 novembre 2026 par « je valide ». La [conception V1](../versions/v1/architecture/TECHNICAL-DESIGN.md) et le [contrat de transmission](../versions/v1/architecture/ARCHITECTURE-CONTRACT.json) portent cette approbation ; planning_ready est true. Les prérequis avant usage réel restent à exercer pendant la réalisation.

Aucun modèle accessible, droit d’abonnement réel, coût chiffré, volumétrie ou objectif de disponibilité n’est présumé. Les vérifications de code, d’accès au compte, de génération et de restauration seront réalisées pendant la construction selon les prérequis du dossier ; cette architecture ne déclare aucune fonctionnalité implémentée ou livrée.
