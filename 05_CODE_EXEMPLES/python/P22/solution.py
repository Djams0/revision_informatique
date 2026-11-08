from pathlib import Path
chemin = Path(__file__).parent / "message.txt"
if chemin.exists():
    print(chemin.read_text(encoding="utf-8"), end="")
else:
    print("fichier absent")
