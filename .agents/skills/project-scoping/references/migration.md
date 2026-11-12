# Migration du cadrage historique vers MVP et SemVer

Statut : **plan à valider pour les documents de projet**. Aucun renommage, déplacement, suppression ni conversion de contrat approuvé n'est effectué par cette intervention. Les nouveaux formats et leurs validateurs sont disponibles dès maintenant. Aucun numéro de release n'est attribué.

## État constaté dans ce dépôt

Le dépôt contient les trois skills, `structure-project`, leurs références et validateurs, ainsi que les conventions `docs/agents/`. Il ne contient ni `docs/docs-project/`, ni `docs/docs-projet/`, ni `versions/v1/VERSION.md`, ni contrat UX/architecture de projet ou maquette approuvée. Le glossaire racine est vide et aucun ADR de projet n'est présent. Il est donc impossible de dresser ici l'inventaire réel des FEAT/parcours/décisions déjà approuvés ou de certifier leur migration. Aucun entretien n'est relancé.

Le modèle hérité est constaté dans les instructions : cadrage V1/MVP puis V2+, `MVP.md` réduit à un pointeur dans `structure-project`, UX limitée aux dossiers `vN`, architecture par version. Les consommateurs locaux des champs de contrats sont les références et scripts des skills UX/architecture ; aucun autre consommateur de contrats n'a été trouvé dans les fichiers suivis. Des consommateurs dans un autre dépôt restent à inventorier.

## Options et recommandation

| Option | Conséquences | Risques et décision requise |
| --- | --- | --- |
| **Conserver les chemins approuvés `versions/v1/` et qualifier leur sens** — recommandée | `v1` reste une identité de périmètre historique. `MVP.md` décrit l'objectif global et pointe vers les mêmes FEAT/maquettes/contrats. Les versions logicielles restent dans les nouveaux champs de livraison. | Relecture humaine des liens et de la portée des anciennes approbations ; migration des contrats uniquement après revue. Aucun changement arbitraire de numéro. |
| Déplacer ensuite les références globales vers `ux/` et `architecture/` | Arborescence plus explicite ; mise à jour atomique de tous les liens, champs de chemins, scripts et consommateurs, avec table ancien → nouveau. | Risque de liens cassés, de doublons de sources canoniques ou de perte d'historique ; approbation distincte obligatoire avant déplacement/suppression. |
| Renommer `v1` en une version logicielle | N'a de sens que si une véritable livraison et son contenu sont établis. | **Aucune équivalence automatique** avec `0.1.0` ou `1.0.0` ; dépendances, compatibilité, stabilité et validation humaine sont préalables. Option déconseillée pour un simple cadrage approuvé. |

## Inventaire à produire dans le dépôt documentaire réel

Lire intégralement les documents approuvés et conserver un manifeste de contrôle avant toute mutation :

| Éléments | Références affectées et contrôles |
| --- | --- |
| `PROJECT.md`, `MVP.md`, `FUTURE-FEATURES.md`, synthèses approuvées | Liens de périmètre et d'origine, distinction MVP/futur, critères de réussite et approbations ; ne pas réécrire la synthèse historique. |
| `versions/v1/VERSION.md` et autres périmètres | Métadonnées `version`, `release_kind`, statut, listes FEAT, liens relatifs et éventuelles preuves de livraison ; `approved` ne prouve pas `delivered`. |
| `modules/**/MODULE.md` et cartes FEAT | IDs, `source`, anciens `release_bucket`, sections historiques, critères, liens interfonctionnels ; aucune renumérotation ni duplication. |
| `UX-SUMMARY.md`, `UX-CONTRACT.json`, HTML/CSS/JS/assets | `version`, `scope`, couverture, FLOW/SCREEN/ACT, ancres, `mockup`, liens interversions, assets et navigation hors ligne ; conserver les visuels exacts déjà approuvés. |
| `ARCHITECTURE.md`, `TECHNICAL-DESIGN.md`, contrat et ADR | `version.id`, `technical_design_path`, sources fonctionnelles/UX, chemins d'ADR/contrats, MOD/IFACE/DATA et traçabilité ; conserver les décisions et leurs preuves. |
| Scripts, schémas, CI, templates, outils et intégrations | Rechercher `versions/v1`, `vN`, expressions régulières de versions, `release_kind`, `release_bucket`, `schemaVersion`, `schema_version`, `scope`, `baseline_version`, `UX-CONTRACT`, `ARCHITECTURE-CONTRACT` et liens scratch. Tester chaque consommateur identifié. |

Commandes de recherche locales possibles : `rg --files --hidden`, puis `rg -n --hidden 'versions/v1|release_kind|release_bucket|UX-CONTRACT|ARCHITECTURE-CONTRACT|schemaVersion|schema_version' <racines-inventoriées>` en excluant Git et dépendances. L'inventaire décrit ce qui existe réellement ; ne pas extrapoler à partir des exemples.

## Séquence après validation de l'option

1. Capturer chemins, IDs, liens, empreintes des fichiers approuvés, versions de schéma, statuts et références d'approbation ; distinguer baseline fonctionnelle et livraison vérifiée. Sauvegarder les originaux hors des emplacements canoniques, sans écraser le travail utilisateur.
2. Présenter le diff proposé pour `MVP.md` et les index. Déduire ses FEAT indispensables et critères uniquement des décisions approuvées ; faire clarifier les ambiguïtés. Préserver la portée du cadrage historique et les fonctionnalités futures séparément.
3. Préparer en scratch des candidats de contrats : UX `1` → `2`, architecture `"1.0"` → `"1.1"`. **Conserver tous les champs et données antérieurs**, IDs et chemins. Ajouter `delivery.scope.kind: "legacy"` tant que le statut MVP n'est pas confirmé. Si MVP confirmé, utiliser `mvp` et ses FEAT canoniques. Les anciens `version`/`version.id` restent des identités documentaires ; les anciens `baseline_version` restent des liens historiques. Ne pas les copier dans les versions de livraison.
4. Ajouter les items FEAT/UX/techniques à partir des sources existantes. Importer leurs critères acceptés sans les inventer. Utiliser `development_status: "unknown"`, `delivery_status: "unknown"`, des listes de versions/preuves vides et un jalon ouvert tant qu'aucune preuve ne permet mieux. Garder les approbations de conception d'origine ; les nouveaux champs non approuvés restent candidats. Pas de nouvelle approbation globale d'un design inchangé.
5. Migrer les affectations de releases seulement si dépendances et validation humaine sont établies. Importer des preuves de livraison sans généraliser un slice livré à une fonctionnalité complète. Une réussite MVP et une stabilité `1.0.0` nécessitent chacune leurs propres critères et preuves.
6. Valider les candidats, comparer anciens/nouveaux IDs, critères, sources et galeries. Tester les consommateurs réels, ouverture hors ligne et liens. Présenter le diff et les risques **avant** remplacement des contrats approuvés. Si un déplacement est choisi, préparer et faire approuver séparément le manifeste exact ancien → nouveau, liens et consommateurs inclus.
7. Appliquer uniquement les changements approuvés. Relancer tous les contrôles ; rejouer en lecture seule pour vérifier qu'aucun doublon ni nouveau diff n'est produit. En cas d'échec, restaurer les originaux à partir de la sauvegarde revue ; ne pas utiliser de reset destructif ni supprimer les sources approuvées.

## Compatibilité des outils dans cette intervention

- Le validateur UX accepte les contrats historiques et `--version v1`, ainsi que les nouveaux contrats globaux via `--contract`. Les chemins existants de maquettes restent valides.
- Le validateur architecture accepte `"1.0"` et `"1.1"`. Le schéma et les invariants partagés sont contrôlés avec Python standard, sans dépendance facultative.
- Les trois skills partagent `project-scoping/references/versioning.md`, `delivery.schema.json` et `scripts/validate_delivery.py` ; conserver ces fichiers ensemble lors de la distribution. Ce sont des références/utilitaires, pas un nouveau skill de planification.
- Un audit fonctionnel `project-scoping/scripts/validate_scope.py` contrôle les nouveaux périmètres globaux sans exiger de dossier `versions/`. Les anciens arbres inchangés conservent leur audit hérité.
- `structure-project` n'est pas modifié ici. Son entrée indépendante et son validateur restent hérités (version obligatoire, MVP-pointeur). **Le cadrage emploie l'adaptateur explicite de `functional-documents.md`**, avec les mêmes procédures preview/apply/audit et validations humaines, sans appliquer ces règles héritées. Une évolution indépendante de `structure-project` et des consommateurs externes doit être préparée si leur utilisation directe est souhaitée.

## Approbations encore nécessaires

Choix de l'organisation documentaire réelle, modification des périmètres/synthèses approuvés, remplacement des contrats approuvés, tout déplacement/renommage/suppression et toute affectation de release. Recommandation : commencer par **conserver les chemins `v1`**, puis examiner un diff de migration sur les documents réels. Le présent plan n'autorise aucune de ces mutations. Commit et push exigent toujours deux autorisations explicites et séparées.

## Fichiers de cette intervention

Chemins relatifs à `.agents/skills/` :

| Fichiers | Modification |
| --- | --- |
| `project-scoping/SKILL.md`, `project-scoping/agents/openai.yaml` | Cadrage du MVP global ou d'une évolution, reprise des décisions et gates préservés. |
| `project-scoping/references/versioning.md` | Nouvelle référence commune : SemVer, contrats publics, stabilité, progression indépendante, dépendances et idempotence. |
| `project-scoping/references/functional-documents.md` | Formats fonctionnels globaux et adaptation des procédures preview/apply/audit de la dépendance héritée. |
| `project-scoping/references/delivery.schema.json`, `project-scoping/scripts/validate_delivery.py` | Schéma et contrôle partagés des intentions et preuves de livraison ; contrôles structurels des schémas locaux. |
| `project-scoping/scripts/validate_scope.py` | Audit structurel du MVP global, sans version imposée. |
| `project-scoping/references/migration.md` | Présent inventaire, options, risques et approbations restantes. |
| `project-scoping/tests/test_contracts.py` | Régressions anciens/nouveaux formats, MVP sans release, livraison partielle, gates et répétition des audits sans mutation. |
| `project-ux/SKILL.md`, `project-ux/agents/openai.yaml`, `project-ux/references/document-formats.md` | UX globale, subsets livrables, exemple JSON v2 et conservation des maquettes approuvées. |
| `project-ux/references/ux-contract.schema.json`, `project-ux/scripts/validate_ux_docs.py` | Schéma d'enveloppe et contrôles UX/delivery ; contrats globaux, SemVer et compatibilité legacy. |
| `project-architecture/SKILL.md`, `project-architecture/agents/openai.yaml` | Fondations globales, deltas proportionnés et parcours PATCH ; comparatifs et validations préservés. |
| `project-architecture/references/deliverables.md`, `project-architecture/references/technical-comparisons.md` | Livrables adaptés et indépendance explicite des choix vis-à-vis des outils installés. |
| `project-architecture/references/architecture-contract.schema.json`, `project-architecture/scripts/validate_contract.py` | Format 1.1, lecture 1.0 conservée et contrôle des références/gates avec Python standard. |
| `project-architecture/references/architecture-contract.example.json` | Exemple valide sans release artificielle, explicitement en conception avec un blocage réel dans l'exemple. |

Vérification reproductible : `python -B .agents/skills/project-scoping/tests/test_contracts.py`. Les tests rejouent les audits et comparent les fichiers avant/après ; ils ne constituent pas une simulation exhaustive de deux conversations d'agent. Les approbations réelles, les preuves et les comportements JavaScript restent à vérifier dans le dépôt documentaire cible.
