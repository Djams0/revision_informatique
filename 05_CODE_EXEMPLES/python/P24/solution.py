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
