# Semaine 15 — essayer Q01 à Q05 dans SQLite, pas à pas

Cette fiche suppose que tu as installé **Thonny** en semaine 7. Tu n'as besoin ni de terminal SQL, ni de compte, ni de serveur : [le petit programme d'atelier](../tools/atelier_sql.py) utilise `sqlite3`, inclus avec Python, et crée une **base neuve en mémoire** à chaque lancement. Les noms et livres sont fictifs. N'ouvre aucune base personnelle.

## Préparer les deux dossiers

1. Dans ton gestionnaire de fichiers, repère le dossier de formation (il peut s'appeler `revision_informatique-main` ou `FORMATION_INFORMATIQUE_DEBUTANTE`). Son dossier parent doit aussi contenir `mes_exercices` : crée ce dossier s'il manque, puis crée `S15` dedans.
2. Ouvre Thonny. Clique sur **Fichier → Ouvrir** et choisis `tools/atelier_sql.py` dans le dossier de formation. Ne modifie pas le programme d'atelier.
3. Clique sur **Fichier → Nouveau**. Écris le SQL de ton essai, puis **Fichier → Enregistrer sous**. Sélectionne `mes_exercices/S15` et nomme le fichier **`essai.sql`**. Vérifie qu'il ne s'appelle pas `essai.sql.txt`.
4. Reviens sur l'onglet `atelier_sql.py` et clique sur **Exécuter** (triangle vert ou F5). Lis les lignes sous `Résultat` dans la console de Thonny. Tu peux écrire ou modifier `essai.sql`, l'enregistrer, puis relancer **l'onglet de l'atelier** pour chaque exercice.

Si tu lis `Fichier introuvable`, place `mes_exercices` **à côté** du dossier de formation, pas à l'intérieur. Si `no such table: livres` s'affiche, ton fichier doit créer et remplir sa table **à chaque exécution** : la base en mémoire repart de zéro. Si `syntax error` apparaît, regarde le numéro d'instruction indiqué, les virgules, les apostrophes et le point-virgule final. Le programme accepte seulement `CREATE TABLE`, `INSERT INTO`, `SELECT`, `UPDATE` et `PRAGMA foreign_keys = ON` ; il refuse les commandes de destruction ou d'accès à un fichier externe. Il sépare les instructions par `;` : n'emploie pas de point-virgule dans un titre de livre fictif.

## Les cinq essais

Lis d'abord [les énoncés](../03_EXERCICES/ENONCES_SQL.md) et écris ton `essai.sql`. Pour Q01, voici un démarrage complet à **recopier** afin de voir la chaîne de bout en bout :

```sql
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres (id, titre, annee) VALUES (1, 'Atlas', 2020), (2, 'Contes', 2018);
SELECT id, titre, annee FROM livres ORDER BY id;
```

Après F5 sur **`atelier_sql.py`**, tu dois lire deux lignes : `1 | Atlas | 2020` et `2 | Contes | 2018`. Ajoute un troisième livre et vérifie qu'il y a trois lignes. L'atelier affiche `Résultat 3 : 2 ligne(s)` pour le premier essai.

| Essai | Dans `essai.sql`, repars de `CREATE TABLE` et de lignes fictives puis… | Résultat attendu du premier jeu |
|---|---|---|
| Q02 | Termine par `SELECT titre FROM livres ORDER BY titre;`. | `Atlas` puis `Contes`, une colonne. |
| Q03 | Insère 2018, 2020, 2023 ; termine par `SELECT titre, annee FROM livres WHERE annee >= 2020 ORDER BY annee;`. | Deux lignes : le titre de 2020, puis celui de 2023. |
| Q04 | Insère au moins les identifiants 1 et 3 ; fais `UPDATE livres SET annee = 2021 WHERE id = 3;`, puis `SELECT id, titre, annee FROM livres ORDER BY id;`. | L'identifiant 3 porte 2021 ; l'identifiant 1 ne change pas. |
| Q05 | Crée `auteurs(id, nom)` et `livres(id, titre, auteur_id)` ; insère un auteur et deux livres, puis relie avec `JOIN`. | Deux paires « titre | auteur », le même auteur pour les deux livres. |

Pour Q05, lis la [fiche Auteur/Livre](AUTEUR_LIVRE.md) si la clé étrangère te bloque. Sur chaque essai, modifie ensuite les données comme le demande l'énoncé et **prédis** le résultat avant de faire F5. Si tu bloques après un vrai essai, compare ta copie avec les [cinq scripts de solution](../05_CODE_EXEMPLES/sql/) et les [corrigés](../04_CORRIGES/CORRIGES_SQL.md). Ne colle pas les cinq solutions l'une après l'autre dans le même fichier : elles créent chacune des tables du même nom.

**Vérification finale :** explique pourquoi une table existe pendant F5 et disparaît au prochain lancement, et montre la différence entre `SELECT` (lecture) et `UPDATE` (modification).
