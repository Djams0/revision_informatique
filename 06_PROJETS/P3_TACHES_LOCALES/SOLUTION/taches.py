from pathlib import Path

CHEMIN = Path(__file__).parent / "taches.txt"

def lire_taches():
    if not CHEMIN.exists():
        return []
    return CHEMIN.read_text(encoding="utf-8").splitlines()

def ajouter_tache(texte):
    with CHEMIN.open("a", encoding="utf-8") as fichier:
        fichier.write(texte + "\n")

while True:
    choix = input("1 Voir / 2 Ajouter / 0 Quitter : ").strip()
    if choix == "0":
        break
    if choix == "1":
        taches = lire_taches()
        if not taches:
            print("Aucune tâche.")
        else:
            for tache in taches:
                print("-", tache)
    elif choix == "2":
        texte = input("Tâche fictive : ").strip()
        if texte:
            ajouter_tache(texte)
            print("Ajoutée.")
        else:
            print("Texte vide refusé.")
    else:
        print("Choix inconnu.")
