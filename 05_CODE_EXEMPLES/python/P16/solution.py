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
