"""Rebuild GUIDE_COMPLET.md from M00–M08 (Markdown is the source of truth)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADER = """# Guide complet — informatique débutante, 18 semaines

Ce document réunit les **neuf cours originaux** du parcours dans l'ordre. Pour suivre les exercices et les projets, commence par [l'index](INDEX.md) et le [mode d'emploi](README_COMMENCER_ICI.md). Les fichiers autonomes sont dans `01_COURS/` ; ce guide est reconstruit depuis ces modules avec `python tools/construire_guide.py`.

**Repères :** M00 = semaine 1 ; M01 = 2–3 ; M02 = 4–6 ; M03 = 7–11 ; M04 = 12 ; M05 = 13–14 ; M06 = 15 ; M07 = 16 ; M08 = 17–18. Prévoir 3–5 heures par semaine.
"""
sections = []
for n in range(9):
    section = (ROOT / f"01_COURS/M{n:02d}.md").read_text(encoding="utf-8").strip()
    # The combined guide lives at root, one directory above the modules.
    for directory in ("02_FICHES", "03_EXERCICES", "04_CORRIGES", "06_PROJETS"):
        section = section.replace(f"](../{directory}/", f"]({directory}/")
    sections.append(section)
text = HEADER.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(sections) + "\n"
(ROOT / "GUIDE_COMPLET.md").write_text(text, encoding="utf-8")
print("GUIDE_COMPLET.md synchronisé avec M00–M08")
