# Algorithmique et pseudo-code — énoncés (15 activités)

Travaille sur une copie dans `mes_exercices`. Les solutions sont dans `04_CORRIGES`, à ouvrir seulement après un essai. Les valeurs et identités sont fictives. Les niveaux 1/3, 2/3 et 3/3 sont des paliers, pas des notes. Pour chaque activité, prédis puis observe deux cas.

## A01 — Tracer une séquence

**Semaine :** 4 · **Difficulté :** 1/3 · **Prérequis :** M02 S4 · **Durée :** 10 min.

**Consigne.** Sans ordinateur, prédis les deux affichages de `x ← 3 ; AFFICHER x ; x ← x + 2 ; AFFICHER x`. Note les valeurs avant de vérifier.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Départ 3 → 3 puis 5 ; départ 0 à la place de 3 → 0 puis 2.

**Indice (à lire seulement après un essai).** Écris une ligne par instruction.

**Réussite.** Deux sorties et trace dans l’ordre.

## A02 — Texte ou nombre ?

**Semaine :** 5 · **Difficulté :** 1/3 · **Prérequis :** M02 S5 · **Durée :** 10 min.

**Consigne.** Prédit le résultat et le type de `a ← "4" ; b ← 4 ; AFFICHER a ; AFFICHER b + 1`. Explique pourquoi additionner `a + 1` exige une conversion.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** a="4", b=4 → 4 puis 5 ; a="9", b=9 → 9 puis 10.

**Indice (à lire seulement après un essai).** Les guillemets signalent du texte.

**Réussite.** Deux types et sorties justifiés.

## A03 — Prédire une branche

**Semaine :** 5 · **Difficulté :** 1/3 · **Prérequis :** M02 S5 · **Durée :** 12 min.

**Consigne.** Avant de coder, trace `SI prix >= 20 ALORS AFFICHER "remise" SINON AFFICHER "normal" FIN SI` pour deux prix et la frontière.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 19 → normal ; 20 → remise ; 21 → remise.

**Indice (à lire seulement après un essai).** `>=` inclut la valeur 20.

**Réussite.** Trois sorties dont la frontière expliquées.

## A04 — Prédire une boucle

**Semaine :** 6 · **Difficulté :** 2/3 · **Prérequis :** M02 S6 · **Durée :** 15 min.

**Consigne.** Trace `total ← 0 ; POUR i DE 1 À 3 FAIRE total ← total + i FIN POUR ; AFFICHER total`. Prédis avant tout code ; note chaque tour.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Borne 3 → 6 ; borne 2 → 3.

**Indice (à lire seulement après un essai).** Après chaque tour, note `i` et `total`.

**Réussite.** Table de trace et résultat exact.

## A05 — Prédire les indices

**Semaine :** 6 · **Difficulté :** 2/3 · **Prérequis :** M02 S6 · **Durée :** 12 min.

**Consigne.** Prédis les affichages de `noms ← ["Lia", "Noé"] ; AFFICHER noms[0] ; AFFICHER longueur(noms)`. Identifie le dernier indice valide.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Deux noms → Lia puis 2 ; `["Lia"]` → Lia puis 1.

**Indice (à lire seulement après un essai).** Les indices commencent à zéro.

**Réussite.** Deux résultats et dernier indice valides.

## A06 — Monnaie entière

**Semaine :** 4 · **Difficulté :** 2/3 · **Prérequis :** M02 S4 · **Durée :** 20 min.

**Consigne.** Écris entrées, traitement et sortie en pseudo-code : prix et paiement entiers, refuser si paiement insuffisant.

**Préconditions.** Prix et paiement entiers non négatifs.

**Deux jeux de vérification.** 8,10 → 2 ; 12,10 → insuffisant.

**Indice (à lire seulement après un essai).** Teste la comparaison avant la soustraction.

**Réussite.** Les deux branches et le cas 10,10 fonctionnent.

## A07 — Recette doublée

**Semaine :** 4 · **Difficulté :** 1/3 · **Prérequis :** M02 S4 · **Durée :** 15 min.

**Consigne.** Une recette prend 2 œufs par portion. Écris le pseudo-code qui lit un nombre de portions et affiche le nombre d’œufs ; annonce les entrées/sorties.

**Préconditions.** Portions entières positives.

**Deux jeux de vérification.** 1 → 2 ; 3 → 6.

**Indice (à lire seulement après un essai).** Multiplier les œufs par les portions.

**Réussite.** Calcul correct pour les deux cas.

## A08 — Âge autorisé

**Semaine :** 5 · **Difficulté :** 2/3 · **Prérequis :** M02 S5 · **Durée :** 18 min.

**Consigne.** Écris un test en pseudo-code pour indiquer « accès » seulement si un âge est entre 18 et 25 inclus. Dessine les deux branches.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 17 → refus ; 18 → accès ; 25 → accès ; 26 → refus.

**Indice (à lire seulement après un essai).** Combine deux comparaisons avec ET.

**Réussite.** Les deux frontières sont incluses.

## A09 — Maximum de deux horaires

**Semaine :** 5 · **Difficulté :** 2/3 · **Prérequis :** M02 S5 · **Durée :** 15 min.

**Consigne.** Lis deux heures entières et affiche la plus tardive ; en cas d’égalité, affiche l’heure commune une seule fois.

**Préconditions.** Heures entières entre 0 et 23.

**Deux jeux de vérification.** 9,14 → 14 ; 11,11 → 11.

**Indice (à lire seulement après un essai).** Une branche `>=` suffit.

**Réussite.** Une seule sortie correcte pour chaque cas.

## A10 — Compter jusqu’à zéro

**Semaine :** 6 · **Difficulté :** 2/3 · **Prérequis :** M02 S6 · **Durée :** 18 min.

**Consigne.** Écris une boucle TANT QUE qui affiche un compteur positif jusqu’à 1, puis s’arrête ; explique la mise à jour.

**Préconditions.** Compteur entier positif.

**Deux jeux de vérification.** 3 → 3,2,1 ; 1 → 1.

**Indice (à lire seulement après un essai).** Soustrais 1 à chaque tour.

**Réussite.** La boucle termine et n’affiche pas 0.

## A11 — Traduire une affectation

**Semaine :** 7 · **Difficulté :** 1/3 · **Prérequis :** M02 S5 puis M03 S7 · **Durée :** 15 min.

**Consigne.** Traduis `LIRE prénom ; AFFICHER "Bonjour", prénom` en un programme Python complet et teste deux prénoms fictifs.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Lia → Bonjour Lia ; Noé → Bonjour Noé.

**Indice (à lire seulement après un essai).** `input` lit du texte ; `print` l’affiche.

**Réussite.** Fichier `.py` autonome et deux sorties.

## A12 — Traduire le calcul de monnaie

**Semaine :** 8 · **Difficulté :** 2/3 · **Prérequis :** M02 S4 puis M03 S8 · **Durée :** 20 min.

**Consigne.** Traduis en Python le pseudo-code de A06, avec les deux branches. Utilise `int(input())`.

**Préconditions.** Deux entiers non négatifs saisis dans l’ordre.

**Deux jeux de vérification.** 8,10 → 2 ; 12,10 → insuffisant.

**Indice (à lire seulement après un essai).** `←` devient `=`, `SI` devient `if`, indentation obligatoire.

**Réussite.** Les deux branches et 10,10 sont corrects.

## A13 — Traduire les âges

**Semaine :** 8 · **Difficulté :** 2/3 · **Prérequis :** M02 S5 puis M03 S8 · **Durée :** 20 min.

**Consigne.** Traduis le test de A08 en Python ; prévois 17, 18, 25 et 26 avant de lancer.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 17 → refus ; 18 → accès ; 25 → accès ; 26 → refus.

**Indice (à lire seulement après un essai).** `ET` devient `and`.

**Réussite.** Frontières incluses, indentation correcte.

## A14 — Traduire la répétition

**Semaine :** 9 · **Difficulté :** 2/3 · **Prérequis :** M02 S6 puis M03 S9 · **Durée :** 20 min.

**Consigne.** Traduis `POUR i DE 1 À 3 FAIRE AFFICHER i FIN POUR` en Python. Puis adapte pour aller jusqu’à 5.

**Préconditions.** Fin entière >= 1.

**Deux jeux de vérification.** Fin 3 → 1,2,3 ; fin 5 → 1,2,3,4,5.

**Indice (à lire seulement après un essai).** `range(1, 4)` exclut 4.

**Réussite.** Nombre exact de lignes et borne comprise.

## A15 — Traduire une liste

**Semaine :** 10 · **Difficulté :** 3/3 · **Prérequis :** M02 S6 puis M03 S10 · **Durée :** 25 min.

**Consigne.** Traduis `notes ← [4,7] ; total ← 0 ; POUR i DE 0 À 1 FAIRE total ← total + notes[i] FIN POUR ; AFFICHER total`. Puis teste une liste de trois valeurs.

**Préconditions.** Liste d’entiers ; la liste vide donne 0.

**Deux jeux de vérification.** [4,7] → 11 ; [4,7,2] → 13.

**Indice (à lire seulement après un essai).** Utilise `range(len(notes))` pour parcourir tous les indices.

**Réussite.** Les deux listes donnent la somme sans indice manquant.
