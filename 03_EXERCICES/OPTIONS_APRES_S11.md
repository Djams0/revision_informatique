# Quatre activités facultatives après S11

Ces activités portent les identifiants **OA01, OA02, OW01, OW02**. Elles s'ajoutent aux 58 exercices du tronc commun ; elles ne sont nécessaires ni pour le quiz final ni pour le projet Python. Essaie d'abord, puis ouvre les [corrigés séparés](../04_CORRIGES/OPTIONS_APRES_S11.md). Utilise seulement des données fictives.

## OA01 — Rechercher dans une liste (10–15 min)

Après les listes de S10–S11, imagine `titres ← ["Atlas", "Contes", "Jardin"]`. En pseudo-code, parcours les titres un par un et affiche `Trouvé` si le titre demandé est présent, ou `Absent` **une seule fois après le parcours** si aucun titre ne correspond. Trace les cas `"Contes"`, `"Mer"` et liste vide. Quel est le danger d'afficher `Absent` à chaque élément différent ?

## OA02 — Voir un tri à bulles (15–20 min)

Sur des cartes en papier marquées `[4, 2, 3]`, compare des voisins ; échange-les si le premier est plus grand. Recommence un passage jusqu'à ce qu'aucun échange ne soit nécessaire. Écris la liste après **chaque échange** et précise combien de passages sont nécessaires. Ce tri est seulement une manière visuelle de comprendre les comparaisons ; pour les projets Python, `sorted(...)` suffit.

## OW01 — Tableau HTML sémantique (15–20 min)

Après S13, crée un `tableau.html` local affichant deux livres fictifs avec `table`, `caption`, `thead`, `tbody`, `tr`, `th` et `td`. Mets `scope="col"` sur les en-têtes « Titre » et « Année ». Ouvre-le dans le navigateur et vérifie deux lignes de données. Ce tableau présente des données ; il ne sert pas à disposer toute la page.

## OW02 — Formulaire local sans envoi (15–20 min)

Crée `formulaire.html` avec un `label` lié par `for` à l'`id` d'un `input`, et un `button type="button"`. Ajoute une phrase expliquant que le bouton **n'envoie rien** : aucun serveur, script ou stockage n'est configuré. Ouvre la page, tape un texte fictif, clique et observe qu'aucun message n'est transmis. Ne saisis jamais de donnée personnelle.
