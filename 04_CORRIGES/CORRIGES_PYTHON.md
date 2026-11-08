# Python 3 — corrigés (25 activités)

Chaque solution est originale et séparée de l’énoncé. Les fichiers correspondants sont sous `05_CODE_EXEMPLES` quand du code est utile. Commence par relire ton propre essai et compare les sorties, y compris la frontière ou le cas vide.

## P01 — Premier affichage

**Démarche.** 1. Relever les entrées et la précondition : Aucune entrée. 2. Appliquer la règle : Chaque `print` ajoute une ligne dans la console. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
print("Bonjour")
print("Je découvre Python")
```

**Vérification.** Exécution 1 → deux lignes ; exécution 2 → les mêmes deux lignes.

**À surveiller.** Une instruction `print` par ligne.

## P02 — Salutation variable

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Une f-string intègre la chaîne dans le message. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
prenom = input("Prénom fictif ? ")
print(f"Salut, {prenom} !")
```

**Vérification.** Lia → Salut, Lia ! ; Noé → Salut, Noé !

**À surveiller.** Lis avec `input`, puis compose la phrase.

## P03 — Addition de deux entiers

**Démarche.** 1. Relever les entrées et la précondition : Deux entiers valides. 2. Appliquer la règle : Les deux conversions sont nécessaires avant `+`. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
a = int(input("Premier entier ? "))
b = int(input("Second entier ? "))
print(a + b)
```

**Vérification.** 2,3 → 5 ; -2,7 → 5.

**À surveiller.** `input` renvoie du texte : convertir avec `int`.

## P04 — Prix total de plusieurs articles

**Démarche.** 1. Relever les entrées et la précondition : Prix entier >=0 et quantité >=1. 2. Appliquer la règle : Les valeurs saisies sont converties avant multiplication. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
prix = int(input("Prix entier ? "))
quantite = int(input("Quantité ? "))
print(prix * quantite)
```

**Vérification.** 3,4 → 12 ; 5,2 → 10.

**À surveiller.** Multiplie prix par quantité.

## P05 — Texte et longueur

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La saisie est une chaîne, `len` compte ses caractères. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
texte = input("Texte ? ")
print(len(texte))
```

**Vérification.** chat → 4 ; a b → 3.

**À surveiller.** `len` mesure la chaîne.

## P06 — Pair ou impair

**Démarche.** 1. Relever les entrées et la précondition : Entier valide, y compris négatif. 2. Appliquer la règle : Le modulo donne le reste de la division par deux. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
nombre = int(input("Entier ? "))
if nombre % 2 == 0:
    print("pair")
else:
    print("impair")
```

**Vérification.** 4 → pair ; 7 → impair.

**À surveiller.** Le reste `nombre % 2` vaut 0 pour un nombre pair.

## P07 — Âge validé

**Démarche.** 1. Relever les entrées et la précondition : Entrée convertible en entier. 2. Appliquer la règle : L’ordre `if/elif/else` donne priorité au cas invalide. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
age = int(input("Âge fictif ? "))
if age < 0:
    print("âge invalide")
elif age >= 18:
    print("adulte")
else:
    print("mineur")
```

**Vérification.** -1 → âge invalide ; 17 → mineur ; 18 → adulte.

**À surveiller.** Teste d’abord l’entrée invalide.

## P08 — Petite remise entière

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La réduction fixe s’applique seulement après vérification du seuil. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
prix = int(input("Prix entier ? "))
if prix < 0:
    print("invalide")
elif prix >= 20:
    print(prix - 2)
else:
    print(prix)
```

**Vérification.** 19 → 19 ; 20 → 18 ; -1 → invalide.

**À surveiller.** Sépare d’abord l’entrée négative.

## P09 — Compte à rebours

**Démarche.** 1. Relever les entrées et la précondition : n entier >=1. 2. Appliquer la règle : `range(n, 0, -1)` s’arrête avant 0. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
n = int(input("Départ positif ? "))
for nombre in range(n, 0, -1):
    print(nombre)
```

**Vérification.** 3 → 3,2,1 ; 1 → 1.

**À surveiller.** Une plage descendante a un pas négatif.

## P10 — Somme de 1 à n

**Démarche.** 1. Relever les entrées et la précondition : n entier >=1. 2. Appliquer la règle : La valeur accumulée change à chaque tour, `n+1` inclut n. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
n = int(input("Dernier entier positif ? "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)
```

**Vérification.** 3 → 6 ; 5 → 15.

**À surveiller.** Initialise `total` à 0 avant la boucle.

## P11 — Saisie dans un intervalle

**Démarche.** 1. Relever les entrées et la précondition : Chaque saisie est un entier valide. 2. Appliquer la règle : Le nouveau `input` dans la boucle permet de changer la condition. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
note = int(input("Note 0–20 ? "))
while note < 0 or note > 20:
    note = int(input("Réessaie : "))
print(note)
```

**Vérification.** 22 puis 12 → 12 ; 0 → 0.

**À surveiller.** Utilise `while note < 0 or note > 20`.

## P12 — Deviner un nombre fixe

**Démarche.** 1. Relever les entrées et la précondition : Entrées entières valides. 2. Appliquer la règle : Le nombre secret reste constant ; chaque nouvelle proposition remplace l’ancienne. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
secret = 7
while True:
    proposition = int(input("Proposition ? "))
    if proposition == secret:
        print("trouvé")
        break
    if proposition < secret:
        print("trop petit")
    else:
        print("trop grand")
```

**Vérification.** 5,9,7 → petit, grand, trouvé ; 7 → trouvé.

**À surveiller.** Répète jusqu’à l’égalité.

## P13 — Parcours d’une liste

**Démarche.** 1. Relever les entrées et la précondition : Liste de chaînes, éventuellement vide. 2. Appliquer la règle : Le parcours reçoit les éléments de la liste dans l’ordre. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
livres = ["Atlas", "Contes", "Poèmes"]
for livre in livres:
    print(livre)
# Test 2 : remplace livres par ["Atlas"].
```

**Vérification.** 3 livres → 3 lignes ; 1 livre → 1 ligne.

**À surveiller.** `for livre in livres` évite les indices.

## P14 — Moyenne sans division par zéro

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La branche vide évite `ZeroDivisionError`. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
notes = [10, 20]
if notes:
    print(sum(notes) / len(notes))
else:
    print("aucune donnée")
# Test 2 : remplace notes par [].
```

**Vérification.** [10,20] → 15.0 ; [] → aucune donnée.

**À surveiller.** Teste la longueur avant la division.

## P15 — Nettoyer une chaîne

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : `strip` retire aux extrémités, puis `lower` crée une nouvelle chaîne. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
mot = input("Mot ? ").strip().lower()
print(mot)
print(len(mot))
```

**Vérification.**   CHAT  → chat,4 ; Livre → livre,5.

**À surveiller.** Combine `.strip()` et `.lower()`.

## P16 — Chercher un titre

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : On parcourt les titres et compare leurs versions en minuscules ; un booléen garde le résultat. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
livres = ["Atlas", "Contes"]
recherche = input("Titre ? ").strip().lower()
trouve = False
for titre in livres:
    if titre.lower() == recherche:
        trouve = True
if trouve:
    print("présent")
else:
    print("absent")
```

**Vérification.** atlas → présent ; Roman → absent.

**À surveiller.** Compare les deux côtés avec `.lower()`.

## P17 — Stock par dictionnaire

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le dictionnaire associe chaque clé à un nombre ; l’absence ne plante pas. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
stock = {"Atlas": 2, "Contes": 1}
titre = input("Titre exact ? ")
print(stock.get(titre, 0))
```

**Vérification.** Atlas → 2 ; Autre → 0.

**À surveiller.** `get(cle, 0)` donne une valeur par défaut.

## P18 — Fonction double

**Démarche.** 1. Relever les entrées et la précondition : Entrée entière valide. 2. Appliquer la règle : Le paramètre local prend l’argument fourni. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
def double(nombre):
    return nombre * 2

valeur = int(input("Entier ? "))
print(double(valeur))
```

**Vérification.** 3 → 6 ; -2 → -4.

**À surveiller.** `return` fournit la valeur, puis `print` l’affiche.

## P19 — Fonction maximum

**Démarche.** 1. Relever les entrées et la précondition : Deux entiers valides. 2. Appliquer la règle : La fonction choisit une des deux valeurs, l’appelant affiche. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
def maximum(a, b):
    if a >= b:
        return a
    return b

a = int(input("A ? "))
b = int(input("B ? "))
print(maximum(a, b))
```

**Vérification.** 3,8 → 8 ; 5,5 → 5.

**À surveiller.** Compare avec `>=`.

## P20 — Compter les notes validées

**Démarche.** 1. Relever les entrées et la précondition : Liste de notes entières 0–20. 2. Appliquer la règle : Chaque note admissible incrémente le compteur une fois. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
def compter_reussites(notes):
    total = 0
    for note in notes:
        if note >= 10:
            total += 1
    return total

notes = [8, 10, 14]
print(compter_reussites(notes))
# Test 2 : remplace notes par [].
```

**Vérification.** [8,10,14] → 2 ; [] → 0.

**À surveiller.** Compteur initial à 0 puis parcours.

## P21 — Corriger un bug de portée

**Démarche.** 1. Relever les entrées et la précondition : Entiers 0 <= remise <= prix. 2. Appliquer la règle : Une variable locale n’existe pas dans l’appelant ; la valeur retournée la transmet. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
def prix_apres_remise(prix, remise):
    final = prix - remise
    return final

prix = int(input("Prix ? "))
remise = int(input("Remise ? "))
resultat = prix_apres_remise(prix, remise)
print(resultat)
```

**Vérification.** prix=10, remise=2 → 8 ; prix=5, remise=0 → 5.

**À surveiller.** `return final` puis affecte le résultat de l’appel.

## P22 — Lire un fichier texte

**Démarche.** 1. Relever les entrées et la précondition : Créer `message.txt` dans le dossier du script pour les deux premiers cas. 2. Appliquer la règle : Lire le texte complet puis `print(..., end="")` évite un saut supplémentaire. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
from pathlib import Path
chemin = Path(__file__).parent / "message.txt"
if chemin.exists():
    print(chemin.read_text(encoding="utf-8"), end="")
else:
    print("fichier absent")
```

**Vérification.** Fichier « A
B
 » → A puis B ; « Salut
 » → Salut.

**À surveiller.** Utilise `Path(__file__).parent` et `.read_text`.

## P23 — Écrire un journal local

**Démarche.** 1. Relever les entrées et la précondition : Saisir du texte fictif, sans saut de ligne. 2. Appliquer la règle : Le mode append conserve le fichier existant ; le chemin est celui du script. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
from pathlib import Path
chemin = Path(__file__).parent / "taches.txt"
tache = input("Tâche fictive ? ").strip()
if tache:
    with chemin.open("a", encoding="utf-8") as fichier:
        fichier.write(tache + "\n")
    print("ajoutée")
else:
    print("vide refusé")
```

**Vérification.** Premier « Lire » → une ligne ; puis « Marcher » → deux lignes.

**À surveiller.** Mode `a` et saut `
`.

## P24 — CSV : total fictif

**Démarche.** 1. Relever les entrées et la précondition : Entiers positifs fictifs ; le mode w remplace ce fichier d’exercice. 2. Appliquer la règle : Les champs du CSV sont des chaînes, converties avant addition. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
from pathlib import Path
import csv
chemin = Path(__file__).parent / "depenses.csv"
with chemin.open("w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["objet", "euros"])
    writer.writerows([("pain", 3), ("bus", 4)])
with chemin.open("r", newline="", encoding="utf-8") as fichier:
    total = sum(int(ligne["euros"]) for ligne in csv.DictReader(fichier))
print(total)
# Test 2 : remplace les valeurs par 2 et 5.
```

**Vérification.** 3+4 → 7 ; 2+5 → 7.

**À surveiller.** `csv.DictReader` rend la colonne accessible par son nom.

## P25 — Déboguer une conversion

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Seule la conversion est protégée ; `break` termine après réussite. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
while True:
    texte = input("Entier ? ")
    try:
        nombre = int(texte)
    except ValueError:
        print("Entre un entier.")
        continue
    break
print(nombre * nombre)
```

**Vérification.** abc puis 4 → erreur expliquée puis 16 ; -3 → 9.

**À surveiller.** `try` autour de `int`, `except ValueError` ciblé.
