---
status: accepted
date: 2026-11-10
---

# Organiser une application unique par responsabilité métier

Aura Forge V1 doit coordonner des règles liées : une seule version active, trois validations explicites, conservation des références approuvées et suspension d’une version suivante lors d’une réouverture. FastAPI et SQLite local sont déjà choisis. Une application organisée par métier et une application organisée par couches techniques globales sont toutes deux viables. L’utilisateur a accepté A, organisation par métier, par « A » le 10 novembre 2026.

Le backend forme une seule application déployable avec des packages consacrés à la gestion des projets, la gestion des versions, le cadrage fonctionnel et la continuité. Ce sont des responsabilités techniques au service des quatre modules fonctionnels approuvés, sans nouveau contexte métier. Les règles et l’autorité d’écriture restent chez leur propriétaire ; la coordination applicative compose les opérations nécessaires dans une transaction commune quand un invariant le demande. Aucun appel HTTP interne ne sépare ces responsabilités.

L’intégration Codex concentre la dépendance externe et ses erreurs ; elle ne possède pas les décisions ou validations métier. Les accès SQLite servent les opérations du propriétaire concerné. Ce choix ne prescrit pas une interface générique, une classe ou une couche de transmission pour chaque objet.

L’alternative par couches techniques globales aurait réduit les conventions initiales, tout en dispersant davantage une évolution métier entre routes, logique et persistance communes. Les services déployés séparément n’ont pas de bénéfice établi pour cet usage personnel et compliqueraient la coordination transactionnelle. Le processus Codex externe demeure une dépendance à gérer, sans justifier une distribution des métiers.

Le compromis accepté est le contrôle des dépendances, des accès aux données et de la coordination entre packages. Il devra être vérifié lors de l’implémentation. Aucun gain mesuré de performance ou de développement n’est revendiqué. Modèle logique, contrats partagés, transport navigateur et validation du dossier intégré restent à préciser dans la [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md).
