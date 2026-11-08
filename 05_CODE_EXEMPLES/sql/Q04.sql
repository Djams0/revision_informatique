CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER);
INSERT INTO livres VALUES (1, 'Atlas', 2019), (3, 'Jardin', 2020);
UPDATE livres SET annee = 2021 WHERE id = 3;
SELECT id, titre, annee FROM livres ORDER BY id;
