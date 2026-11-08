PRAGMA foreign_keys = ON;
CREATE TABLE auteurs (id INTEGER PRIMARY KEY, nom TEXT NOT NULL);
CREATE TABLE livres (id INTEGER PRIMARY KEY, titre TEXT NOT NULL, auteur_id INTEGER NOT NULL REFERENCES auteurs(id));
INSERT INTO auteurs VALUES (1, 'Autrice fictive');
INSERT INTO livres VALUES (1, 'Atlas', 1), (2, 'Contes', 1);
SELECT livres.titre, auteurs.nom FROM livres JOIN auteurs ON livres.auteur_id = auteurs.id ORDER BY livres.id;
