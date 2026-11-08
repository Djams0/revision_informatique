def calculer(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    return None

try:
    a = int(input("Premier entier ? "))
    b = int(input("Second entier ? "))
except ValueError:
    print("Entrez des entiers.")
else:
    operation = input("Opération (+, -, *) ? ").strip()
    resultat = calculer(a, b, operation)
    if resultat is None:
        print("Choix inconnu.")
    else:
        print("Résultat :", resultat)
