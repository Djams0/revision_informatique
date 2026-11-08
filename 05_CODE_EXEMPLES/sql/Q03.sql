CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Contes', 2018), (2, 'Atlas', 2020), (3, 'Jardin', 2023);
SELECT titre, annee FROM livres WHERE annee >= 2020 ORDER BY annee;
