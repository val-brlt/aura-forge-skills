---
status: accepted
date: 2026-11-09
---

# Construire l’interface avec Vue et TypeScript

Le frontend du MVP doit représenter les questions structurées, les brouillons, les sauvegardes, l’interprétation à confirmer, les discussions et les décisions dans l’UX approuvée. Vue/TypeScript, React/TypeScript et Jinja2/HTMX sur FastAPI ont été comparés. Les trois sont viables ; Vue a été proposé pour ses conventions cohérentes de templates, formulaires et état réactif. L’utilisateur a répondu « ok je valide A » à cette proposition le 9 novembre 2026.

L’interface sera donc construite avec Vue et TypeScript, compilée en fichiers statiques servis par le backend Python/FastAPI. Le compromis est une étape de construction JavaScript et des contrats entre frontend et backend. Node sert au développement et à la construction ; aucun serveur Node permanent n’est requis pour cette variante d’exécution.

React reste proche fonctionnellement, sans compétence ou dépendance spécifique établie qui le favoriserait ici. Jinja2/HTMX aurait privilégié le rendu Python et évité une construction Node obligatoire, mais aurait demandé une organisation précise des fragments autour des saisies, brouillons et focus. Aucun avantage de performance ou de coût de développement de Vue n’est mesuré.

Les validations métier restent sous l’autorité de FastAPI ; l’état Vue n’est pas une preuve de sauvegarde. Les contrats d’événements, la persistance, le routeur, le store et les bibliothèques visuelles ne sont pas sélectionnés par cette décision. Les maquettes approuvées restent la référence UX et ne constituent pas du code de production.

Sources consultées le 9 novembre 2026 : [Vue — formulaires](https://vuejs.org/guide/essentials/forms.html), [gestion d’état](https://vuejs.org/guide/scaling-up/state-management.html), [React — reducer/context](https://react.dev/learn/scaling-up-with-reducer-and-context), [HTMX](https://htmx.org/docs/), [construction statique](https://vite.dev/guide/static-deploy.html). Portée : [conception V1](../docs-project/versions/v1/architecture/TECHNICAL-DESIGN.md). Cette acceptation ne vaut ni validation du dossier complet ni livraison.
