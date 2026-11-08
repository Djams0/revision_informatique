CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Atlas', 2020), (2, 'Contes', 2018);
SELECT id, titre, annee FROM livres ORDER BY id;
