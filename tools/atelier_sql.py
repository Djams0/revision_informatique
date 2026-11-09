"""Execute a beginner's SQLite exercise only in a fresh in-memory database."""

from pathlib import Path
import re
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
EXERCICE = ROOT.parent / "mes_exercices" / "S15" / "essai.sql"
AUTORISE = re.compile(
    r"^(CREATE\s+TABLE|INSERT\s+INTO|SELECT\b|UPDATE\b|PRAGMA\s+foreign_keys\s*=\s*ON\s*$)",
    re.I,
)


def executer(chemin):
    texte = chemin.read_text(encoding="utf-8-sig")
    # Les cinq exercices ne mettent pas de point-virgule dans une chaîne SQL.
    lignes = [ligne for ligne in texte.splitlines() if not ligne.lstrip().startswith("--")]
    instructions = [partie.strip() for partie in "\n".join(lignes).split(";") if partie.strip()]
    if not instructions:
        raise ValueError("Le fichier SQL est vide.")
    with sqlite3.connect(":memory:") as base:
        base.execute("PRAGMA foreign_keys = ON")
        for numero, instruction in enumerate(instructions, 1):
            if not AUTORISE.match(instruction):
                raise ValueError(
                    f"Instruction {numero} non prévue dans cet atelier : {instruction[:70]!r}"
                )
            try:
                curseur = base.execute(instruction)
            except sqlite3.Error as erreur:
                raise ValueError(f"Instruction {numero} : {erreur}") from erreur
            if instruction.lstrip().upper().startswith("SELECT"):
                lignes = curseur.fetchall()
                print(f"Résultat {numero} : {len(lignes)} ligne(s)")
                for ligne in lignes:
                    print("  ", *ligne, sep=" | ")
    return len(instructions)


if __name__ == "__main__":
    chemin = Path(sys.argv[1]) if len(sys.argv) == 2 else EXERCICE
    if not chemin.is_file():
        print(f"Fichier introuvable : {chemin}")
        print("Crée mes_exercices/S15/essai.sql à côté du dossier de formation.")
        sys.exit(1)
    try:
        nombre = executer(chemin)
    except (OSError, UnicodeError, ValueError) as erreur:
        print(f"Erreur : {erreur}")
        sys.exit(1)
    print(f"Terminé : {nombre} instruction(s), base de test effacée à la fermeture.")
