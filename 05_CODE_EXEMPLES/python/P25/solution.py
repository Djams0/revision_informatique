while True:
    texte = input("Entier ? ")
    try:
        nombre = int(texte)
    except ValueError:
        print("Entre un entier.")
        continue
    break
print(nombre * nombre)
