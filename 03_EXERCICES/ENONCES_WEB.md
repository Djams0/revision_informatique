# HTML/CSS — énoncés (8 activités)

Travaille sur une copie dans `mes_exercices`. Les solutions sont dans `04_CORRIGES`, à ouvrir seulement après un essai. Les valeurs et identités sont fictives. Les niveaux 1/3, 2/3 et 3/3 sont des paliers, pas des notes. Pour chaque activité, prédis puis observe deux cas.

## W01 — Squelette HTML

**Semaine :** 13 · **Difficulté :** 1/3 · **Prérequis :** M05 S13 · **Durée :** 12 min.

**Consigne.** Crée un fichier `index.html` avec doctype, langue française, encodage UTF-8, titre d’onglet et un titre visible.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Titre « Découverte » → onglet et page visibles ; titre remplacé par « Essai » → les deux changent.

**Indice (à lire seulement après un essai).** `title` est dans `head`, `h1` dans `body`.

**Réussite.** Page ouverte hors ligne, balises fermées.

## W02 — Paragraphes et hiérarchie

**Semaine :** 13 · **Difficulté :** 1/3 · **Prérequis :** M05 S13 · **Durée :** 15 min.

**Consigne.** Ajoute à une page un titre principal, deux sous-titres de même niveau et un paragraphe sous chacun.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Deux sections → 2 h2 et 2 p ; ajoute une troisième section → 3 h2 et 3 p.

**Indice (à lire seulement après un essai).** Un `h1` décrit la page, les `h2` les sections.

**Réussite.** Hiérarchie logique et texte lisible sans CSS.

## W03 — Liste de tâches

**Semaine :** 13 · **Difficulté :** 1/3 · **Prérequis :** M05 S13 · **Durée :** 15 min.

**Consigne.** Affiche trois tâches fictives dans une liste non ordonnée ; compare avec une liste ordonnée si l’ordre compte.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 3 tâches → 3 puces ; 1 tâche → 1 puce.

**Indice (à lire seulement après un essai).** `ul` contient des `li`.

**Réussite.** Chaque tâche est un élément de liste.

## W04 — Lien interne utilisable

**Semaine :** 13 · **Difficulté :** 2/3 · **Prérequis :** M05 S13 · **Durée :** 18 min.

**Consigne.** Crée un lien « Aller aux livres » qui amène à une section de la même page ; teste aussi après avoir changé l’identifiant.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** `#livres` et id livres → section atteinte ; id changé sans href → lien cassé, à réparer.

**Indice (à lire seulement après un essai).** Le fragment `#` correspond à l’attribut `id`.

**Réussite.** Navigation interne fonctionnelle hors ligne.

## W05 — Image locale accessible

**Semaine :** 13 · **Difficulté :** 2/3 · **Prérequis :** M05 S13 · **Durée :** 20 min.

**Consigne.** Affiche l’image locale `badge.svg` fournie dans le dossier de correction, avec un texte alternatif pertinent. Explique ce qui reste si l’image manque.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Fichier présent → badge visible ; fichier renommé → texte alternatif disponible.

**Indice (à lire seulement après un essai).** `src` est relatif au fichier HTML, `alt` décrit la fonction de l’image.

**Réussite.** Image sans lien distant, alt non vide.

## W06 — Structure sémantique

**Semaine :** 13 · **Difficulté :** 2/3 · **Prérequis :** M05 S13 · **Durée :** 20 min.

**Consigne.** Organise une petite page avec `header`, `main`, deux `section` et `footer`. Un tableau n’est pas nécessaire.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Deux sections → deux h2 ; ajoute une section → troisième h2 sous main.

**Indice (à lire seulement après un essai).** La structure indique les grandes parties, sans style obligatoire.

**Réussite.** Un seul main, titres dans un ordre logique.

## W07 — Classe et feuille CSS

**Semaine :** 14 · **Difficulté :** 2/3 · **Prérequis :** M05 S14 · **Durée :** 22 min.

**Consigne.** Crée `style.css`, lie-le à la page, et utilise la classe `.important` pour mettre une phrase en gras. Change seulement le CSS pour tester.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** CSS lié → phrase en gras ; lien retiré → phrase normale.

**Indice (à lire seulement après un essai).** `class="important"` correspond à `.important`.

**Réussite.** Deux fichiers locaux, effet visuel vérifié.

## W08 — Mise en page lisible

**Semaine :** 14 · **Difficulté :** 3/3 · **Prérequis :** M05 S14 · **Durée :** 30 min.

**Consigne.** Améliore une page locale avec largeur maximale, marges, interligne et couleur contrastée. Vérifie une fenêtre étroite sans débordement horizontal.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Grand écran → colonne centrée ; fenêtre étroite → texte lisible sans défilement horizontal.

**Indice (à lire seulement après un essai).** `max-width`, `margin: auto`, `padding` et `box-sizing`.

**Réussite.** La page reste lisible à deux largeurs.
