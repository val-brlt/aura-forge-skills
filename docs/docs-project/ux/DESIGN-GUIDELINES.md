# Principes de conception UX/UI

## Principes d'ergonomie

Donner le contexte du projet et de la version avant les actions. Distinguer une idée, une proposition acceptée, son inclusion dans une version, la validation d’un cadrage et une livraison déclarée. Présenter les résultats comme des documents relisibles, avec des actions explicites et des erreurs qui expliquent comment poursuivre.

L’assistant recommande et aide à préciser ; l’utilisateur décide. Une réponse libre passe par une interprétation relisible et corrigeable avant confirmation. Une discussion ne modifie pas automatiquement un résultat approuvé.

## Navigation partagée

« Mes projets » ouvre la liste, avec filtres actifs et archives. Dans un projet : vue d’ensemble, discussion IA, versions et historique. Le nom reste dans l’en-tête ; le menu ne le répète pas sous « Projet ouvert » ni sous un titre « Projet ».

La section « Étapes de travail » contient uniquement le cadrage fonctionnel en V1. Les questions, synthèse, catalogue, cadrage final et décisions/reportés appartiennent à sa navigation locale. Les discussions liées aux questions gardent leur sujet ; la discussion générale dispose d’un fil propre au projet et d’un contexte identifiable.

## Langage et messages

Français, phrases courtes et verbes d’action stables entre commande, confirmation et retour. Employer « cadrage », « version », « proposition », « éléments reportés » et « livraison » au sens du [glossaire](../../../GLOSSARY.md).

Un blocage cite la règle ou la validation manquante et indique une issue. Une archive explique la consultation seule et propose la restauration. Une erreur IA conserve le texte et offre un réessai ; une erreur de sauvegarde ne prétend pas que le travail est enregistré.

## Direction visuelle validée

Thème sombre par défaut : fond `#171820`, panneau `#20212c`, texte `#f0eff7`, accent `#baa7f5`. Thème clair : fond `#f7f8fc`, panneau blanc, texte `#252638`, accent `#5143ad`. Ces valeurs proviennent des fichiers approuvés, sans création d’un système visuel supplémentaire.

Police locale Segoe UI avec replis Tahoma et sans-serif. Titres alignés à gauche, hiérarchie par tailles et graisses. Les badges et couleurs renforcent des libellés, sans remplacer l’information textuelle. La bascule de thème reste accessible dans l’en-tête partagé.

## Composants et motifs d'interaction

Listes de projets et de versions, contexte partagé, documents avec panneau de décision, questions avec recommandation et réponse libre. Les confirmations de validation, archivage, réouverture et livraison emploient des dialogues nommés avec annulation possible.

Markdown sémantique dans les discussions, HTML brut échappé. Entrée envoie, Maj+Entrée ajoute une ligne ; l’éditeur respecte la composition du texte. Les fils et brouillons restent liés au bon contexte. Aucune saisie de fichier ni commande de publication n’est ajoutée au produit V1.

## Accessibilité et adaptation

Libellés associés, erreurs au champ, focus visible, accès clavier, lien d’évitement et statuts annoncés. Les chiffres servent aux étapes ou aux questions réelles. Les états sont nommés et ne dépendent pas de la seule couleur.

Sur mobile : colonnes empilées, contrôles dans la largeur, défilement horizontal limité aux sous-onglets et à la liste des questions, élément actif visible. La zone de validation suit le document ; le contexte de la discussion générale suit son fil. Préférence de réduction du mouvement respectée.

Contrôles et limites sont consignés dans [la synthèse UX V1](../versions/v1/ux/UX-SUMMARY.md). Aucun audit complet avec lecteur d’écran ni certification WCAG n’est revendiqué.

## Historique des décisions

V1 : direction et parcours de la galerie R3 explicitement validés par « ok je valide les maquettes », le 8 novembre 2026. Les maquettes sont [conservées avec leur version](../versions/v1/ux/mockups/index.html) ; le [contrat UX](../versions/v1/ux/UX-CONTRACT.json) décrit les interactions et états propres à cette version. Ces conventions partagées ne constituent pas du code de production.
