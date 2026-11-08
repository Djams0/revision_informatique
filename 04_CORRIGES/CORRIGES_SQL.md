# SQLite et données — corrigés (5 activités)

Chaque solution est originale et séparée de l’énoncé. Les fichiers correspondants sont sous `05_CODE_EXEMPLES` quand du code est utile. Commence par relire ton propre essai et compare les sorties, y compris la frontière ou le cas vide.

## Q01 — Créer une table avec clé

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La table décrit la forme des données ; `INSERT` apporte les lignes. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```sql
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Atlas', 2020), (2, 'Contes', 2018);
SELECT id, titre, annee FROM livres ORDER BY id;
```

**Vérification.** Atlas/2020, Contes/2018 → 2 lignes ; après un troisième livre → 3 lignes.

**À surveiller.** Une clé primaire distincte pour chaque ligne.

## Q02 — Lire une colonne

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La projection choisit la colonne ; le tri ne change pas la table. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```sql
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Contes', 2018), (2, 'Atlas', 2020);
SELECT titre FROM livres ORDER BY titre;
```

**Vérification.** Atlas, Contes → Atlas puis Contes ; ajoute Jardin → Atlas, Contes, Jardin.

**À surveiller.** `SELECT titre` puis `ORDER BY titre`.

## Q03 — Filtrer par année

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : `WHERE` filtre avant l’affichage ; les lignes exclues restent stockées. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```sql
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Contes', 2018), (2, 'Atlas', 2020), (3, 'Jardin', 2023);
SELECT titre, annee FROM livres WHERE annee >= 2020 ORDER BY annee;
```

**Vérification.** 2018,2020,2023 → titres 2020 puis 2023 ; seuil 2023 → titre 2023 seul.

**À surveiller.** `WHERE annee >= 2020`.

## Q04 — Ajouter puis modifier

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La clé primaire vise une ligne ; sans filtre, toutes les années pourraient changer. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```sql
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Atlas', 2019), (3, 'Jardin', 2020);
UPDATE livres SET annee = 2021 WHERE id = 3;
SELECT id, titre, annee FROM livres ORDER BY id;
```

**Vérification.** id 3 année 2020 → 2021 ; autre ligne id 1 reste inchangée.

**À surveiller.** Teste la clé avant `UPDATE`.

## Q05 — Relier deux tables

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La clé étrangère identifie l’auteur sans répéter son nom dans chaque livre. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```sql
PRAGMA foreign_keys = ON;
CREATE TABLE auteurs (id INTEGER PRIMARY KEY, nom TEXT NOT NULL);
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, auteur_id INTEGER NOT NULL REFERENCES auteurs(id));
INSERT INTO auteurs VALUES (1, 'Autrice fictive');
INSERT INTO livres VALUES (1, 'Atlas', 1), (2, 'Contes', 1);
SELECT livres.titre, auteurs.nom FROM livres JOIN auteurs ON livres.auteur_id = auteurs.id ORDER BY livres.id;
```

**Vérification.** Un auteur/1 livre → 1 paire ; un auteur/2 livres → 2 paires.

**À surveiller.** `livres.auteur_id` renvoie vers `auteurs.id`.
