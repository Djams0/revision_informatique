# Python 3 — énoncés (25 activités)

Travaille sur une copie dans `mes_exercices`. Les solutions sont dans `04_CORRIGES`, à ouvrir seulement après un essai. Les valeurs et identités sont fictives. Les niveaux 1/3, 2/3 et 3/3 sont des paliers, pas des notes. Pour chaque activité, prédis puis observe deux cas.

## P01 — Premier affichage

**Semaine :** 7 · **Difficulté :** 1/3 · **Prérequis :** M03 S7 · **Durée :** 8 min.

**Consigne.** Affiche exactement deux lignes : « Bonjour » puis « Je découvre Python ».

**Préconditions.** Aucune entrée.

**Deux jeux de vérification.** Exécution 1 → deux lignes ; exécution 2 → les mêmes deux lignes.

**Indice (à lire seulement après un essai).** Une instruction `print` par ligne.

**Réussite.** Texte et ordre exacts.

## P02 — Salutation variable

**Semaine :** 7 · **Difficulté :** 1/3 · **Prérequis :** M03 S7 · **Durée :** 10 min.

**Consigne.** Demande un prénom fictif et affiche « Salut, <prénom> ! ».

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Lia → Salut, Lia ! ; Noé → Salut, Noé !

**Indice (à lire seulement après un essai).** Lis avec `input`, puis compose la phrase.

**Réussite.** La saisie apparaît au bon endroit.

## P03 — Addition de deux entiers

**Semaine :** 7 · **Difficulté :** 1/3 · **Prérequis :** M03 S7 · **Durée :** 12 min.

**Consigne.** Lis deux entiers et affiche leur somme.

**Préconditions.** Deux entiers valides.

**Deux jeux de vérification.** 2,3 → 5 ; -2,7 → 5.

**Indice (à lire seulement après un essai).** `input` renvoie du texte : convertir avec `int`.

**Réussite.** Addition numérique, pas concaténation.

## P04 — Prix total de plusieurs articles

**Semaine :** 7 · **Difficulté :** 2/3 · **Prérequis :** M03 S7 · **Durée :** 12 min.

**Consigne.** Lis un prix entier et une quantité positive, affiche le total en euros.

**Préconditions.** Prix entier >=0 et quantité >=1.

**Deux jeux de vérification.** 3,4 → 12 ; 5,2 → 10.

**Indice (à lire seulement après un essai).** Multiplie prix par quantité.

**Réussite.** Un seul total correct.

## P05 — Texte et longueur

**Semaine :** 8 · **Difficulté :** 1/3 · **Prérequis :** M03 S8 · **Durée :** 10 min.

**Consigne.** Lis un mot fictif et affiche son nombre de caractères ; un espace compte aussi si saisi.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** chat → 4 ; a b → 3.

**Indice (à lire seulement après un essai).** `len` mesure la chaîne.

**Réussite.** Deux longueurs justes.

## P06 — Pair ou impair

**Semaine :** 8 · **Difficulté :** 2/3 · **Prérequis :** M03 S8 · **Durée :** 15 min.

**Consigne.** Lis un entier et affiche « pair » ou « impair ».

**Préconditions.** Entier valide, y compris négatif.

**Deux jeux de vérification.** 4 → pair ; 7 → impair.

**Indice (à lire seulement après un essai).** Le reste `nombre % 2` vaut 0 pour un nombre pair.

**Réussite.** Cas pair, impair et zéro.

## P07 — Âge validé

**Semaine :** 8 · **Difficulté :** 2/3 · **Prérequis :** M03 S8 · **Durée :** 15 min.

**Consigne.** Refuse un âge négatif ; sinon affiche adulte à partir de 18 ans, mineur avant.

**Préconditions.** Entrée convertible en entier.

**Deux jeux de vérification.** -1 → âge invalide ; 17 → mineur ; 18 → adulte.

**Indice (à lire seulement après un essai).** Teste d’abord l’entrée invalide.

**Réussite.** Les trois branches donnent une seule réponse.

## P08 — Petite remise entière

**Semaine :** 8 · **Difficulté :** 2/3 · **Prérequis :** M03 S8 · **Durée :** 18 min.

**Consigne.** Pour un prix entier, retranche 2 € si le prix atteint 20 €, sinon conserve le prix. Refuse le négatif.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** 19 → 19 ; 20 → 18 ; -1 → invalide.

**Indice (à lire seulement après un essai).** Sépare d’abord l’entrée négative.

**Réussite.** Frontière 20 et négatif gérés.

## P09 — Compte à rebours

**Semaine :** 9 · **Difficulté :** 1/3 · **Prérequis :** M03 S9 · **Durée :** 15 min.

**Consigne.** Affiche de n jusqu’à 1 avec `for` ; n est un entier positif.

**Préconditions.** n entier >=1.

**Deux jeux de vérification.** 3 → 3,2,1 ; 1 → 1.

**Indice (à lire seulement après un essai).** Une plage descendante a un pas négatif.

**Réussite.** Pas de zéro ni de boucle infinie.

## P10 — Somme de 1 à n

**Semaine :** 9 · **Difficulté :** 2/3 · **Prérequis :** M03 S9 · **Durée :** 18 min.

**Consigne.** Calcule 1+2+…+n avec une boucle, sans utiliser `sum`.

**Préconditions.** n entier >=1.

**Deux jeux de vérification.** 3 → 6 ; 5 → 15.

**Indice (à lire seulement après un essai).** Initialise `total` à 0 avant la boucle.

**Réussite.** Somme exacte pour deux bornes.

## P11 — Saisie dans un intervalle

**Semaine :** 9 · **Difficulté :** 2/3 · **Prérequis :** M03 S9 · **Durée :** 18 min.

**Consigne.** Redemande une note entière tant qu’elle n’est pas entre 0 et 20 inclus.

**Préconditions.** Chaque saisie est un entier valide.

**Deux jeux de vérification.** 22 puis 12 → 12 ; 0 → 0.

**Indice (à lire seulement après un essai).** Utilise `while note < 0 or note > 20`.

**Réussite.** La boucle s’arrête sur 0 et 20.

## P12 — Deviner un nombre fixe

**Semaine :** 9 · **Difficulté :** 2/3 · **Prérequis :** M03 S9 · **Durée :** 20 min.

**Consigne.** Fais deviner le nombre fictif 7 ; indique trop petit/trop grand, puis « trouvé ».

**Préconditions.** Entrées entières valides.

**Deux jeux de vérification.** 5,9,7 → petit, grand, trouvé ; 7 → trouvé.

**Indice (à lire seulement après un essai).** Répète jusqu’à l’égalité.

**Réussite.** Arrêt correct avec les deux indices.

## P13 — Parcours d’une liste

**Semaine :** 10 · **Difficulté :** 1/3 · **Prérequis :** M03 S10 · **Durée :** 12 min.

**Consigne.** Affiche chacun des trois livres fictifs d’une liste, une ligne par livre. Change la liste pour un seul livre.

**Préconditions.** Liste de chaînes, éventuellement vide.

**Deux jeux de vérification.** 3 livres → 3 lignes ; 1 livre → 1 ligne.

**Indice (à lire seulement après un essai).** `for livre in livres` évite les indices.

**Réussite.** Chaque titre affiché une fois.

## P14 — Moyenne sans division par zéro

**Semaine :** 10 · **Difficulté :** 2/3 · **Prérequis :** M03 S10 · **Durée :** 18 min.

**Consigne.** Calcule la moyenne de trois nombres fictifs puis prévois le comportement d’une liste vide.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** [10,20] → 15.0 ; [] → aucune donnée.

**Indice (à lire seulement après un essai).** Teste la longueur avant la division.

**Réussite.** Deux cas, dont liste vide.

## P15 — Nettoyer une chaîne

**Semaine :** 10 · **Difficulté :** 2/3 · **Prérequis :** M03 S10 · **Durée :** 15 min.

**Consigne.** Lis un mot éventuellement entouré d’espaces ; affiche-le en minuscules et sa longueur après nettoyage.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.**   CHAT  → chat,4 ; Livre → livre,5.

**Indice (à lire seulement après un essai).** Combine `.strip()` et `.lower()`.

**Réussite.** Espaces extérieurs retirés, longueur exacte.

## P16 — Chercher un titre

**Semaine :** 10 · **Difficulté :** 2/3 · **Prérequis :** M03 S10 · **Durée :** 18 min.

**Consigne.** Dans une liste fixe, vérifie si un titre saisi existe, sans distinguer majuscules/minuscules.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** atlas → présent ; Roman → absent.

**Indice (à lire seulement après un essai).** Compare les deux côtés avec `.lower()`.

**Réussite.** Deux recherches correctes.

## P17 — Stock par dictionnaire

**Semaine :** 10 · **Difficulté :** 2/3 · **Prérequis :** M03 S10 · **Durée :** 16 min.

**Consigne.** Lis un titre et affiche son stock d’après `{"Atlas":2,"Contes":1}`, ou 0 si absent.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Atlas → 2 ; Autre → 0.

**Indice (à lire seulement après un essai).** `get(cle, 0)` donne une valeur par défaut.

**Réussite.** Titre connu et inconnu correctement traités.

## P18 — Fonction double

**Semaine :** 11 · **Difficulté :** 1/3 · **Prérequis :** M03 S11 · **Durée :** 15 min.

**Consigne.** Définis une fonction qui retourne le double d’un entier et appelle-la sur une valeur saisie.

**Préconditions.** Entrée entière valide.

**Deux jeux de vérification.** 3 → 6 ; -2 → -4.

**Indice (à lire seulement après un essai).** `return` fournit la valeur, puis `print` l’affiche.

**Réussite.** Fonction réutilisable et sorties correctes.

## P19 — Fonction maximum

**Semaine :** 11 · **Difficulté :** 2/3 · **Prérequis :** M03 S11 · **Durée :** 20 min.

**Consigne.** Écris `maximum(a,b)` qui retourne le plus grand, avec égalité admise.

**Préconditions.** Deux entiers valides.

**Deux jeux de vérification.** 3,8 → 8 ; 5,5 → 5.

**Indice (à lire seulement après un essai).** Compare avec `>=`.

**Réussite.** Retour sans affichage dans la fonction.

## P20 — Compter les notes validées

**Semaine :** 11 · **Difficulté :** 2/3 · **Prérequis :** M03 S11 · **Durée :** 20 min.

**Consigne.** Écris une fonction qui compte les notes >=10 dans une liste fictive.

**Préconditions.** Liste de notes entières 0–20.

**Deux jeux de vérification.** [8,10,14] → 2 ; [] → 0.

**Indice (à lire seulement après un essai).** Compteur initial à 0 puis parcours.

**Réussite.** Fonction retourne le nombre sans afficher dedans.

## P21 — Corriger un bug de portée

**Semaine :** 11 · **Difficulté :** 3/3 · **Prérequis :** M03 S11 · **Durée :** 20 min.

**Consigne.** Répare le scénario : une fonction calcule un prix final mais le programme tente de lire sa variable locale `final` après l’appel. Fournis une version complète avec retour.

**Préconditions.** Entiers 0 <= remise <= prix.

**Deux jeux de vérification.** prix=10, remise=2 → 8 ; prix=5, remise=0 → 5.

**Indice (à lire seulement après un essai).** `return final` puis affecte le résultat de l’appel.

**Réussite.** Aucun `NameError`, deux résultats.

## P22 — Lire un fichier texte

**Semaine :** 12 · **Difficulté :** 2/3 · **Prérequis :** M04 S12 · **Durée :** 20 min.

**Consigne.** Crée un fichier local `message.txt` avec deux lignes fictives, puis écris un programme qui les lit et affiche sans doubler les sauts de ligne.

**Préconditions.** Créer `message.txt` dans le dossier du script pour les deux premiers cas.

**Deux jeux de vérification.** Fichier « A
B
 » → A puis B ; « Salut
 » → Salut.

**Indice (à lire seulement après un essai).** Utilise `Path(__file__).parent` et `.read_text`.

**Réussite.** Le programme fonctionne pour deux contenus et signale fichier absent.

## P23 — Écrire un journal local

**Semaine :** 12 · **Difficulté :** 2/3 · **Prérequis :** M04 S12 · **Durée :** 20 min.

**Consigne.** Demande une tâche fictive et ajoute-la dans `taches.txt`, une ligne par lancement ; ne supprime pas l’ancien contenu.

**Préconditions.** Saisir du texte fictif, sans saut de ligne.

**Deux jeux de vérification.** Premier « Lire » → une ligne ; puis « Marcher » → deux lignes.

**Indice (à lire seulement après un essai).** Mode `a` et saut `
`.

**Réussite.** Deux lancements conservent les deux tâches.

## P24 — CSV : total fictif

**Semaine :** 12 · **Difficulté :** 3/3 · **Prérequis :** M04 S12 · **Durée :** 25 min.

**Consigne.** Crée un CSV de deux dépenses fictives dans le dossier du script, puis calcule la somme de la colonne euros. Change les données pour un second test.

**Préconditions.** Entiers positifs fictifs ; le mode w remplace ce fichier d’exercice.

**Deux jeux de vérification.** 3+4 → 7 ; 2+5 → 7.

**Indice (à lire seulement après un essai).** `csv.DictReader` rend la colonne accessible par son nom.

**Réussite.** En-tête présent, conversion numérique et total juste.

## P25 — Déboguer une conversion

**Semaine :** 12 · **Difficulté :** 3/3 · **Prérequis :** M04 S12 · **Durée :** 25 min.

**Consigne.** Un utilisateur peut saisir des lettres au lieu d’un entier. Écris une boucle qui demande jusqu’à obtenir un entier, puis affiche son carré.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** abc puis 4 → erreur expliquée puis 16 ; -3 → 9.

**Indice (à lire seulement après un essai).** `try` autour de `int`, `except ValueError` ciblé.

**Réussite.** Pas de plantage sur texte, sortie numérique correcte.
