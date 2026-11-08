# Corrigés des quatre jalons

Barème par question : 3 points pour la réponse, 2 pour la justification/démonstration. Accepter une formulation équivalente correcte.

## J03

1. La RAM contient le travail en cours ; le stockage garde un fichier **enregistré** après extinction. La saisie non enregistrée n'a pas forcément été écrite sur le stockage.
2. Navigateur client → routeur/Internet → serveur ; le serveur renvoie une réponse que le navigateur affiche. Internet relie des réseaux ; le Web est un service qui fournit notamment des pages dessus.
3. `https` est le protocole, `exemple.org` le domaine, `/livres` le chemin. DNS aide à résoudre le nom en adresse du service ; ce n'est pas un moteur de recherche.
4. Urgence artificielle, lien imprévu et demande de secret sont suspects. Ne pas cliquer ; ouvrir soi-même l'application ou l'adresse connue et vérifier. HTTPS ne suffit pas pour garantir l'honnêteté.

## J06

1. `x` vaut 2, puis 5 après l'affectation ; on affiche 5. `←` donne une nouvelle valeur, ce n'est pas une équation simultanée.
2. `age >= 18 ET age <= 25`. 17 : faux ; 18 : vrai ; 25 : vrai ; 26 : faux. `ET` impose les deux limites et `>=`/`<=` incluent les bords.
3. Après les tours i=1,2,3, `total` vaut 1, 3, 6. La borne 3 est incluse dans **notre pseudo-code**.
4. Longueur 2, premier indice 0, dernier 1. Pour `TANT QUE`, une variable ou entrée doit changer afin que la condition devienne fausse ; tester le cas déjà valide.

## J12

1. `int("4") + 2` vaut 6, tandis que `"4" + "2"` vaut `"42"` ; le premier convertit en entier, le second assemble des chaînes.
2. Exemple complet :

```python
nombre = int(input("Entier ? "))
if nombre % 2 == 0:
    print("pair")
else:
    print("impair")
```

   Pour 4 : pair ; pour 7 : impair ; zéro est pair. L'entrée est un entier valide.
3. `range(1,4)` produit 1, 2, 3 : la borne 4 est exclue. `for i in range(1,4):` suivi de quatre espaces puis `print(i)` affiche ces trois nombres, chacun sur une ligne. L'indentation délimite le corps de la boucle.
4. Une liste vide provoquerait une division par zéro si l'on calcule `sum(notes)/len(notes)` ; tester `if not notes` avant. `return` remet une valeur à l'appelant, `print` l'affiche. `w` remplace le contenu du fichier : utiliser une copie d'essai avant d'écrire.

## J18

1. Accepter un projet exécutable dont les entrées/sorties sont nommées et un cas limite attendu/observé est montré, par exemple choix inconnu → message sans plantage.
2. `<h1>` structure le titre ; `h1 { color: ...; }` cible ce titre et change son apparence. La page doit rester lisible si CSS manque.
3. `SELECT titre FROM livres ORDER BY titre;` lit et trie. SQL est le langage de requêtes ; SQLite est le moteur local qui interprète ce SQL et conserve la base.
4. `git status` montre les modifications, `git add README.md` prépare, `git commit -m "Décrit le projet"` enregistre une version. Accepter une démonstration locale ou une explication correcte. La prochaine étape doit être petite et vérifiable, par exemple tester un choix vide avant d'ajouter une fonction.
