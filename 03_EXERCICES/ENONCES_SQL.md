# SQLite et données — énoncés (5 activités)

Travaille sur une copie dans `mes_exercices`. Les solutions sont dans `04_CORRIGES`, à ouvrir seulement après un essai. Les valeurs et identités sont fictives. Les niveaux 1/3, 2/3 et 3/3 sont des paliers, pas des notes. Pour chaque activité, prédis puis observe deux cas.

Si tu n'as jamais exécuté de SQL, commence par [la fiche de pratique sans terminal SQL](../02_FICHES/PRATIQUER_SQL_PAS_A_PAS.md). Elle utilise seulement Thonny et Python 3 ; chaque requête tourne en mémoire dans une base fictive neuve.

## Q01 — Créer une table avec clé

**Semaine :** 15 · **Difficulté :** 1/3 · **Prérequis :** M06 S15 · **Durée :** 20 min.

**Consigne.** Crée `livres(id INTEGER PRIMARY KEY, titre TEXT NOT NULL, annee INTEGER)` et insère deux lignes fictives. Liste tout.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Atlas/2020, Contes/2018 → 2 lignes ; après un troisième livre → 3 lignes.

**Indice (à lire seulement après un essai).** Une clé primaire distincte pour chaque ligne.

**Réussite.** Colonnes et lignes attendues, aucune clé répétée.

## Q02 — Lire une colonne

**Semaine :** 15 · **Difficulté :** 1/3 · **Prérequis :** M06 S15 · **Durée :** 15 min.

**Consigne.** Sur la table de livres fictifs, affiche seulement les titres triés alphabétiquement.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Atlas, Contes → Atlas puis Contes ; ajoute Jardin → Atlas, Contes, Jardin.

**Indice (à lire seulement après un essai).** `SELECT titre` puis `ORDER BY titre`.

**Réussite.** Une seule colonne triée.

## Q03 — Filtrer par année

**Semaine :** 15 · **Difficulté :** 2/3 · **Prérequis :** M06 S15 · **Durée :** 18 min.

**Consigne.** Sur trois livres fictifs, sélectionne les titres publiés à partir de 2020 inclus, triés par année.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 2018,2020,2023 → titres 2020 puis 2023 ; seuil 2023 → titre 2023 seul.

**Indice (à lire seulement après un essai).** `WHERE annee >= 2020`.

**Réussite.** La frontière 2020 est incluse.

## Q04 — Ajouter puis modifier

**Semaine :** 15 · **Difficulté :** 2/3 · **Prérequis :** M06 S15 · **Durée :** 20 min.

**Consigne.** Ajoute un livre fictif, corrige son année avec `UPDATE ... WHERE id=...`, puis relis la ligne. Explique le risque sans WHERE.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** id 3 année 2020 → 2021 ; autre ligne id 1 reste inchangée.

**Indice (à lire seulement après un essai).** Teste la clé avant `UPDATE`.

**Réussite.** Seule la ligne 3 change.

## Q05 — Relier deux tables

**Semaine :** 15 · **Difficulté :** 3/3 · **Prérequis :** M06 S15 · **Durée :** 25 min.

**Consigne.** Dessine `auteurs` et `livres` avec `auteur_id` ; crée les deux tables et affiche un titre avec le nom de son auteur grâce à une jointure simple.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Un auteur/1 livre → 1 paire ; un auteur/2 livres → 2 paires.

**Indice (à lire seulement après un essai).** `livres.auteur_id` renvoie vers `auteurs.id`.

**Réussite.** Clés cohérentes et résultat joint exact.
