# Système, réseau, sécurité et Git — corrigés (5 activités)

Chaque solution est originale et séparée de l’énoncé. Les fichiers correspondants sont sous `05_CODE_EXEMPLES` quand du code est utile. Commence par relire ton propre essai et compare les sorties, y compris la frontière ou le cas vide.

## T01 — Ranger et retrouver

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Enregistrer dans le bon dossier puis rouvrir prouve la persistance. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
1. Créer mes_exercices puis S01 dans le gestionnaire.
2. Enregistrer note.txt dans S01 ; fermer et rouvrir.
3. Créer copies et y copier note.txt.
4. Constater deux emplacements distincts.
```

**Vérification.** Après fermeture → note retrouvée ; après copie → 2 fichiers dans 2 dossiers.

**À surveiller.** Vérifie la fenêtre Enregistrer sous.

## T02 — Expliquer une URL et client/serveur

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le navigateur client demande une ressource ; le serveur répond, HTTPS protège le transport. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
`https` est le protocole, `exemple.org` le nom de domaine, `/livres` le chemin.
Demande : navigateur → réseau → serveur ; réponse : serveur → réseau → navigateur.
Pour `/contact`, seul le chemin change.
```

**Vérification.** /livres → chemin livres ; /contact → chemin contact, domaine inchangé.

**À surveiller.** DNS intervient pour trouver la destination du domaine.

## T03 — Reconnaître un faux message

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Urgence, lien inattendu et demande de secret signalent un risque ; ouvrir soi-même le service. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
Indices : urgence artificielle, lien non vérifié, demande de mot de passe.
Action : ne pas cliquer ; ouvrir l’application ou l’adresse officielle connue et vérifier.
HTTPS seul ne garantit pas l’honnêteté.
```

**Vérification.** Message urgent avec mot de passe → suspect ; notification dans l’application officielle sans lien → vérifier directement.

**À surveiller.** Ne clique pas pour tester.

## T04 — Naviguer sans supprimer

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Les commandes portent sur le dossier courant ; le parent est `..`. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
PowerShell : Get-Location ; Get-ChildItem ; New-Item -ItemType Directory -Name atelier ; Set-Location atelier ; Set-Location ..
macOS/Linux : pwd ; ls ; mkdir atelier ; cd atelier ; cd ..
Vérifier le dossier courant avant chaque création.
```

**Vérification.** Dossier vide → `atelier` apparaît ; après retour → dossier courant initial.

**À surveiller.** Vérifie `pwd`/`Get-Location` entre deux actions.

## T05 — Premier dépôt Git local

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Git enregistre des versions locales ; `add` prépare, `commit` valide. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
Dans le dossier d’essai : git init ; git status ; git add README.md ; git commit -m "Première note".
Modifier README.md ; git status montre le fichier modifié ; git add README.md ; git commit -m "Précise le projet" ; git log --oneline montre deux commits.
Configurer une identité locale fictive si Git le demande.
```

**Vérification.** Après premier commit → historique 1 ; après second → historique 2 et état propre.

**À surveiller.** `status` avant `add`, après `add` et après `commit`.
