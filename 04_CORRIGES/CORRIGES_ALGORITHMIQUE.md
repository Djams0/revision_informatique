# Algorithmique et pseudo-code — corrigés (15 activités)

Chaque solution est originale et séparée de l’énoncé. Les fichiers correspondants sont sous `05_CODE_EXEMPLES` quand du code est utile. Commence par relire ton propre essai et compare les sorties, y compris la frontière ou le cas vide.

## A01 — Tracer une séquence

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La deuxième affectation lit l’ancienne valeur puis la remplace. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
x ← 3
AFFICHER x
x ← x + 2
AFFICHER x
Trace : 3, puis 5. Si x commence à 0 : 0, puis 2.
```

**Vérification.** Départ 3 → 3 puis 5 ; départ 0 à la place de 3 → 0 puis 2.

**À surveiller.** Écris une ligne par instruction.

## A02 — Texte ou nombre ?

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le texte affiché ressemble au nombre mais ne permet pas le même calcul. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
a ← "4"  // texte
b ← 4    // entier
AFFICHER a
AFFICHER b + 1
Sorties : 4 et 5. Il faut convertir a en entier avant un calcul numérique.
```

**Vérification.** a="4", b=4 → 4 puis 5 ; a="9", b=9 → 9 puis 10.

**À surveiller.** Les guillemets signalent du texte.

## A03 — Prédire une branche

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Le test choisit une branche exclusive ; 20 appartient à la première. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
SI prix >= 20 ALORS
    AFFICHER "remise"
SINON
    AFFICHER "normal"
FIN SI
Trace : 19 → normal, 20 → remise, 21 → remise.
```

**Vérification.** 19 → normal ; 20 → remise ; 21 → remise.

**À surveiller.** `>=` inclut la valeur 20.

## A04 — Prédire une boucle

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Notre pseudo-code inclut la borne finale : 1+2+3 vaut 6. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
total ← 0
POUR i DE 1 À 3 FAIRE
    total ← total + i
FIN POUR
AFFICHER total
Trace : (1,1), (2,3), (3,6). Sortie 6 ; borne 2 → 3.
```

**Vérification.** Borne 3 → 6 ; borne 2 → 3.

**À surveiller.** Après chaque tour, note `i` et `total`.

## A05 — Prédire les indices

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Une liste de deux éléments utilise les positions 0 et 1. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
noms ← ["Lia", "Noé"]
AFFICHER noms[0]
AFFICHER longueur(noms)
Sorties : Lia, puis 2 ; dernier indice : 1.
```

**Vérification.** Deux noms → Lia puis 2 ; `["Lia"]` → Lia puis 1.

**À surveiller.** Les indices commencent à zéro.

## A06 — Monnaie entière

**Démarche.** 1. Relever les entrées et la précondition : Prix et paiement entiers non négatifs. 2. Appliquer la règle : Le calcul de monnaie ne se fait que si paiement couvre le prix. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
LIRE prix
LIRE paiement
SI paiement < prix ALORS
    AFFICHER "insuffisant"
SINON
    AFFICHER paiement - prix
FIN SI
8,10 → 2 ; 12,10 → insuffisant.
```

**Vérification.** 8,10 → 2 ; 12,10 → insuffisant.

**À surveiller.** Teste la comparaison avant la soustraction.

## A07 — Recette doublée

**Démarche.** 1. Relever les entrées et la précondition : Portions entières positives. 2. Appliquer la règle : La multiplication transforme l’entrée en sortie ; vérifier 0 si autorisé. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
LIRE portions
oeufs ← 2 * portions
AFFICHER oeufs
1 → 2 ; 3 → 6.
```

**Vérification.** 1 → 2 ; 3 → 6.

**À surveiller.** Multiplier les œufs par les portions.

## A08 — Âge autorisé

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : Avec OU, presque tous les âges passeraient ; ET impose les deux limites. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
LIRE age
SI age >= 18 ET age <= 25 ALORS
    AFFICHER "accès"
SINON
    AFFICHER "refus"
FIN SI
```

**Vérification.** 17 → refus ; 18 → accès ; 25 → accès ; 26 → refus.

**À surveiller.** Combine deux comparaisons avec ET.

## A09 — Maximum de deux horaires

**Démarche.** 1. Relever les entrées et la précondition : Heures entières entre 0 et 23. 2. Appliquer la règle : Comparer avant d’afficher évite de produire deux réponses à l’égalité. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
LIRE heure1, heure2
SI heure1 >= heure2 ALORS
    AFFICHER heure1
SINON
    AFFICHER heure2
FIN SI
```

**Vérification.** 9,14 → 14 ; 11,11 → 11.

**À surveiller.** Une branche `>=` suffit.

## A10 — Compter jusqu’à zéro

**Démarche.** 1. Relever les entrées et la précondition : Compteur entier positif. 2. Appliquer la règle : Le compteur décroît, donc la condition devient fausse après 1. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```text
LIRE compteur
TANT QUE compteur > 0 FAIRE
    AFFICHER compteur
    compteur ← compteur - 1
FIN TANT QUE
```

**Vérification.** 3 → 3,2,1 ; 1 → 1.

**À surveiller.** Soustrais 1 à chaque tour.

## A11 — Traduire une affectation

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : L’entrée est déjà une chaîne, aucune conversion n’est nécessaire. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
prenom = input("Prénom fictif ? ")
print("Bonjour", prenom)
```

**Vérification.** Lia → Bonjour Lia ; Noé → Bonjour Noé.

**À surveiller.** `input` lit du texte ; `print` l’affiche.

## A12 — Traduire le calcul de monnaie

**Démarche.** 1. Relever les entrées et la précondition : Deux entiers non négatifs saisis dans l’ordre. 2. Appliquer la règle : On convertit les deux saisies puis on teste avant de soustraire. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
prix = int(input("Prix ? "))
paiement = int(input("Paiement ? "))
if paiement < prix:
    print("insuffisant")
else:
    print(paiement - prix)
```

**Vérification.** 8,10 → 2 ; 12,10 → insuffisant.

**À surveiller.** `←` devient `=`, `SI` devient `if`, indentation obligatoire.

## A13 — Traduire les âges

**Démarche.** 1. Relever les entrées et la précondition : Données fictives ; respecter les entrées indiquées. 2. Appliquer la règle : La conjonction `and` impose les deux bornes. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
age = int(input("Âge fictif ? "))
if age >= 18 and age <= 25:
    print("accès")
else:
    print("refus")
```

**Vérification.** 17 → refus ; 18 → accès ; 25 → accès ; 26 → refus.

**À surveiller.** `ET` devient `and`.

## A14 — Traduire la répétition

**Démarche.** 1. Relever les entrées et la précondition : Fin entière >= 1. 2. Appliquer la règle : Python exclut la deuxième borne de `range`, contrairement à notre pseudo-code. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
fin = int(input("Dernier entier positif ? "))
for i in range(1, fin + 1):
    print(i)
```

**Vérification.** Fin 3 → 1,2,3 ; fin 5 → 1,2,3,4,5.

**À surveiller.** `range(1, 4)` exclut 4.

## A15 — Traduire une liste

**Démarche.** 1. Relever les entrées et la précondition : Liste d’entiers ; la liste vide donne 0. 2. Appliquer la règle : `len` donne la borne exclue, donc les indices 0 à `len-1` sont visités. 3. Parcourir les deux cas indiqués et comparer à la sortie attendue.

**Solution de référence.**

```python
notes = [4, 7]
total = 0
for i in range(len(notes)):
    total = total + notes[i]
print(total)
# Pour le second test, remplace notes par [4, 7, 2].
```

**Vérification.** [4,7] → 11 ; [4,7,2] → 13.

**À surveiller.** Utilise `range(len(notes))` pour parcourir tous les indices.
