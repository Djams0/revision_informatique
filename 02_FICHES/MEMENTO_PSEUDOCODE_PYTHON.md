# Mémo : du pseudo-code à Python 3

Notre pseudo-code est une **convention d'apprentissage**, pas un langage officiel exécutable. `←` affecte ; `=` compare ; `POUR ... À ...` inclut la borne finale. Python exécute du code avec une syntaxe précise : `=` affecte, `==` compare, les blocs sont indentés et `range` exclut la fin. Les entrées `input` sont toujours du texte à convertir si l'on veut calculer.

| Idée | Pseudo-code utilisé ici | Python 3 | Point à surveiller |
|---|---|---|---|
| Donner une valeur | `total ← 0` | `total = 0` | La variable peut changer. |
| Lire du texte | `LIRE nom` | `nom = input("Nom ? ")` | La saisie est une chaîne. |
| Lire un entier | `LIRE age` puis préciser entier | `age = int(input("Âge ? "))` | `ValueError` si texte non numérique. |
| Afficher | `AFFICHER total` | `print(total)` | Affiche, n'enregistre pas. |
| Tester une égalité | `SI x = 2 ALORS` | `if x == 2:` | `=` en Python affecte. |
| Tester deux conditions | `x > 0 ET x < 10` | `x > 0 and x < 10` | `or` signifie « ou ». |
| Choisir | `SI … ALORS … SINON … FIN SI` | `if …:\n    …\nelse:\n    …` | `:` et indentation. |
| Parcourir 0 à 2 | `POUR i DE 0 À 2 FAIRE … FIN POUR` | `for i in range(0, 3):\n    …` | Fin Python exclue. |
| Répéter | `TANT QUE x < 3 FAIRE … FIN TANT QUE` | `while x < 3:\n    …` | Faire évoluer `x`. |
| Liste | `nombres ← [2, 4]` | `nombres = [2, 4]` | Indices 0 et 1. |
| Fonction | `FONCTION double(x) RETOURNER x*2` | `def double(x):\n    return x * 2` | `return` n'affiche rien. |

## Cinq micro-exemples analysés

**1. Affectation.** Pseudo-code `prix ← 8 ; prix ← prix + 2 ; AFFICHER prix`. Python :

```python
prix = 8
prix = prix + 2
print(prix)
```

Sortie `10` : la deuxième ligne lit 8, ajoute 2, remplace la valeur.

**2. Saisie.** Pseudo-code `LIRE nom ; AFFICHER nom`. Python :

```python
nom = input("Nom fictif ? ")
print(nom)
```

Si l'entrée est `Ari`, sortie `Ari` ; le résultat de `input` est du texte.

**3. Condition.** Pseudo-code `SI age >= 18 ALORS AFFICHER "adulte" SINON AFFICHER "mineur" FIN SI`. Python :

```python
age = 18
if age >= 18:
    print("adulte")
else:
    print("mineur")
```

Sortie `adulte` : la borne 18 est comprise ; revenir à la marge ferme le bloc.

**4. Boucle.** Pseudo-code `POUR i DE 1 À 3 FAIRE AFFICHER i FIN POUR`. Python :

```python
for i in range(1, 4):
    print(i)
```

Sorties `1`, `2`, `3`, chacune sur une ligne. La fin 4 n'est pas imprimée.

**5. Liste et fonction.** Pseudo-code `notes ← [10, 20] ; AFFICHER notes[0] + notes[1]`. Version Python avec fonction pour réutiliser le calcul :

```python
def somme_deux(valeurs):
    return valeurs[0] + valeurs[1]

notes = [10, 20]
print(somme_deux(notes))
```

Sortie `30`. Il faut deux éléments ; avec une liste vide, le programme aurait `IndexError`. Teste les préconditions avant de réutiliser la fonction.

**Trace rapide :** note les colonnes « ligne / variables avant / variables après / sortie », puis avance sans sauter de ligne. Les erreurs fréquentes sont `=` au lieu de `==`, mauvaise indentation, borne finale de `range`, `input` non converti, et indice hors de la liste.
