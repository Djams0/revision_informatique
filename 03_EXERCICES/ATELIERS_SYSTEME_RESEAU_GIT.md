# Système, réseau, sécurité et Git — énoncés (5 activités)

Travaille sur une copie dans `mes_exercices`. Les solutions sont dans `04_CORRIGES`, à ouvrir seulement après un essai. Les valeurs et identités sont fictives. Les niveaux 1/3, 2/3 et 3/3 sont des paliers, pas des notes. Pour chaque activité, prédis puis observe deux cas.

## T01 — Ranger et retrouver

**Semaine :** 1 · **Difficulté :** 1/3 · **Prérequis :** M00 · **Durée :** 20 min.

**Consigne.** Dans Documents, crée `mes_exercices/S01`, un `note.txt`, ferme et retrouve-le. Fais une copie dans un sous-dossier `copies`.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Après fermeture → note retrouvée ; après copie → 2 fichiers dans 2 dossiers.

**Indice (à lire seulement après un essai).** Vérifie la fenêtre Enregistrer sous.

**Réussite.** Noms, extensions et emplacements vérifiables.

## T02 — Expliquer une URL et client/serveur

**Semaine :** 3 · **Difficulté :** 1/3 · **Prérequis :** M01 · **Durée :** 18 min.

**Consigne.** Sur l’URL fictive `https://exemple.org/livres`, indique protocole, domaine et chemin, puis trace navigateur → routeur/Internet → serveur → réponse.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** /livres → chemin livres ; /contact → chemin contact, domaine inchangé.

**Indice (à lire seulement après un essai).** DNS intervient pour trouver la destination du domaine.

**Réussite.** Composants identifiés et sens de la demande/réponse.

## T03 — Reconnaître un faux message

**Semaine :** 3 · **Difficulté :** 2/3 · **Prérequis :** M01 sécurité · **Durée :** 20 min.

**Consigne.** Analyse ce scénario inventé : « Compte bloqué dans 5 minutes ! Ouvre notre lien raccourci et donne ton mot de passe. » Note trois signaux et une action sûre.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Message urgent avec mot de passe → suspect ; notification dans l’application officielle sans lien → vérifier directement.

**Indice (à lire seulement après un essai).** Ne clique pas pour tester.

**Réussite.** Trois indices et vérification indépendante.

## T04 — Naviguer sans supprimer

**Semaine :** 16 · **Difficulté :** 1/3 · **Prérequis :** M07 et dossiers M00 · **Durée :** 20 min.

**Consigne.** Dans un dossier d’essai, affiche le dossier courant, liste le contenu, crée un dossier `atelier`, entre puis remonte. Fournis commandes Windows et macOS/Linux.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Dossier vide → `atelier` apparaît ; après retour → dossier courant initial.

**Indice (à lire seulement après un essai).** Vérifie `pwd`/`Get-Location` entre deux actions.

**Réussite.** Aucune suppression ni droits administrateur.

## T05 — Premier dépôt Git local

**Semaine :** 16 · **Difficulté :** 2/3 · **Prérequis :** M07 · **Durée :** 30 min.

**Consigne.** Dans un dossier d’essai avec `README.md`, initialise Git, crée deux commits après deux modifications et explique l’état intermédiaire ; aucun compte GitHub requis.

**Préconditions.** Données fictives ; respecter les entrées indiquées.

**Deux jeux de vérification.** Après premier commit → historique 1 ; après second → historique 2 et état propre.

**Indice (à lire seulement après un essai).** `status` avant `add`, après `add` et après `commit`.

**Réussite.** Deux commits lisibles, README présent.
