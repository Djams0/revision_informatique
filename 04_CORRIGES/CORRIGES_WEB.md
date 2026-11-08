# HTML/CSS — corrigés (8 activités)

Chaque solution est originale et séparée de l’énoncé. Les fichiers correspondants sont sous `05_CODE_EXEMPLES` quand du code est utile. Commence par relire ton propre essai et compare les sorties, y compris la frontière ou le cas vide.

## W01 — Squelette HTML

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le navigateur lit la métadonnée et le corps séparément. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Découverte</title></head>
<body><h1>Découverte</h1></body></html>
```

**Vérification.** Titre « Découverte » → onglet et page visibles ; titre remplacé par « Essai » → les deux changent.

**À surveiller.** `title` est dans `head`, `h1` dans `body`.

## W02 — Paragraphes et hiérarchie

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Les titres portent le sens de la page, pas une taille choisie. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Ma semaine</title></head>
<body><h1>Ma semaine</h1><h2>Lecture</h2><p>Un livre fictif.</p>
<h2>Marche</h2><p>Une promenade fictive.</p></body></html>
```

**Vérification.** Deux sections → 2 h2 et 2 p ; ajoute une troisième section → 3 h2 et 3 p.

**À surveiller.** Un `h1` décrit la page, les `h2` les sections.

## W03 — Liste de tâches

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Une liste traduit la structure ; `ol` serait adapté à des étapes numérotées. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Tâches</title></head>
<body><h1>Tâches fictives</h1><ul><li>Lire</li><li>Marcher</li><li>Écrire</li></ul></body></html>
```

**Vérification.** 3 tâches → 3 puces ; 1 tâche → 1 puce.

**À surveiller.** `ul` contient des `li`.

## W04 — Lien interne utilisable

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le navigateur recherche l’élément portant cet identifiant. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Liens</title></head>
<body><h1>Page locale</h1><a href="#livres">Aller aux livres</a>
<p>Introduction fictive.</p><section id="livres"><h2>Livres</h2><p>Atlas.</p></section>
</body></html>
```

**Vérification.** `#livres` et id livres → section atteinte ; id changé sans href → lien cassé, à réparer.

**À surveiller.** Le fragment `#` correspond à l’attribut `id`.

## W05 — Image locale accessible

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : L’image originale est placée à côté de `index.html`. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Badge</title></head>
<body><h1>Mon badge fictif</h1><img src="badge.svg" alt="Cercle bleu portant une étoile blanche" width="120" height="120"></body></html>
```

**Vérification.** Fichier présent → badge visible ; fichier renommé → texte alternatif disponible.

**À surveiller.** `src` est relatif au fichier HTML, `alt` décrit la fonction de l’image.

## W06 — Structure sémantique

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Les balises sémantiques rendent le rôle des zones explicite. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Atelier</title></head>
<body><header><h1>Atelier fictif</h1></header><main>
<section><h2>But</h2><p>Apprendre.</p></section>
<section><h2>Étapes</h2><p>Essayer puis vérifier.</p></section>
</main><footer><p>Exercice local.</p></footer></body></html>
```

**Vérification.** Deux sections → deux h2 ; ajoute une section → troisième h2 sous main.

**À surveiller.** La structure indique les grandes parties, sans style obligatoire.

## W07 — Classe et feuille CSS

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le HTML garde le sens, CSS change l’apparence. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

`index.html` :

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Style</title><link rel="stylesheet" href="style.css"></head>
<body><h1>Une note</h1><p class="important">À retenir</p></body></html>
```

`style.css` :

```css
.important { font-weight: bold; color: #184b73; }
```

**Vérification.** CSS lié → phrase en gras ; lien retiré → phrase normale.

**À surveiller.** `class="important"` correspond à `.important`.

## W08 — Mise en page lisible

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La largeur maximale limite la longueur des lignes ; le padding protège les bords. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

`index.html` :

```html
<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Portfolio fictif</title><link rel="stylesheet" href="style.css"></head>
<body><main><h1>Mes essais</h1><p>Un programme Python et une page Web locale.</p></main></body></html>
```

`style.css` :

```css
* { box-sizing: border-box; }
body { font-family: Arial, sans-serif; color: #222; background: #f7f7f7; line-height: 1.6; }
main { max-width: 42rem; margin: 2rem auto; padding: 1rem; background: white; }
h1 { color: #184b73; }
```

**Vérification.** Grand écran → colonne centrée ; fenêtre étroite → texte lisible sans défilement horizontal.

**À surveiller.** `max-width`, `margin: auto`, `padding` et `box-sizing`.
