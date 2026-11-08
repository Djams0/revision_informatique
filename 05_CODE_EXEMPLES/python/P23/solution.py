from pathlib import Path
chemin = Path(__file__).parent / "taches.txt"
tache = input("Tâche fictive ? ").strip()
if tache:
    with chemin.open("a", encoding="utf-8") as fichier:
        fichier.write(tache + "\n")
    print("ajoutée")
else:
    print("vide refusé")
