# Corrigés des activités facultatives

Lis d'abord les [énoncés OA01–OW02](../03_EXERCICES/OPTIONS_APRES_S11.md). Ces exemples ne changent pas les 58 corrigés du tronc commun.

## OA01 — Recherche

```text
trouve ← FAUX
POUR chaque titre DE titres FAIRE
    SI titre = recherche ALORS
        trouve ← VRAI
    FIN SI
FIN POUR
SI trouve ALORS AFFICHER "Trouvé"
SINON AFFICHER "Absent"
FIN SI
```

`Contes` → Trouvé ; `Mer` → Absent ; liste vide → Absent. Dire « Absent » dans la boucle serait faux dès qu'un premier élément est différent, même si un suivant correspond.

## OA02 — Tri à bulles

`[4, 2, 3]` : échange 4 et 2 → `[2, 4, 3]` ; échange 4 et 3 → `[2, 3, 4]`. Un deuxième passage ne change rien et permet de constater l'arrêt. Une implémentation peut optimiser le nombre de comparaisons ; ce n'est pas un prérequis.

## OW01 — Tableau

Copie ceci dans un fichier `tableau.html` de ton dossier personnel :

```html
<!doctype html>
<html lang="fr">
<meta charset="utf-8">
<title>Livres fictifs</title>
<table>
  <caption>Deux livres inventés</caption>
  <thead><tr><th scope="col">Titre</th><th scope="col">Année</th></tr></thead>
  <tbody>
    <tr><td>Atlas</td><td>2020</td></tr>
    <tr><td>Contes</td><td>2018</td></tr>
  </tbody>
</table>
</html>
```

Le `caption` décrit le tableau ; `th` désigne des en-têtes, `td` des cellules de données. Vérifie les deux lignes dans le navigateur.

## OW02 — Formulaire local

```html
<!doctype html>
<html lang="fr">
<meta charset="utf-8">
<title>Essai de formulaire local</title>
<p>Essai local : le bouton ne transmet ni ne sauvegarde le texte.</p>
<label for="nom-fictif">Nom fictif</label>
<input id="nom-fictif" name="nom-fictif" type="text">
<button type="button">Tester (sans action)</button>
</html>
```

Le `for` du label et l'`id` de l'input ont la même valeur. `type="button"` et l'absence de script ou de traitement empêchent ici toute action lors du clic. Le texte saisi reste seulement dans le champ affiché tant que la page reste ouverte.
