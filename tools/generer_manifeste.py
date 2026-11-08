"""List all repository files and their byte sizes, excluding the manifest itself."""
from pathlib import Path
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "08_CONTROLES/MANIFESTE_FINAL.csv"
ROLES = {
    "00_ADMIN": "audit et parcours",
    "01_COURS": "cours hebdomadaire",
    "02_FICHES": "aide et schéma",
    "03_EXERCICES": "énoncé et bilan",
    "04_CORRIGES": "corrigé séparé",
    "05_CODE_EXEMPLES": "exemple exécutable",
    "06_PROJETS": "projet guidé",
    "07_RESSOURCES": "ressource commentée",
    "08_CONTROLES": "contrôle documenté",
    "tools": "outil reproductible",
}
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p != DEST and
             '__pycache__' not in p.parts)
with DEST.open('w',encoding='utf-8',newline='') as stream:
    writer=csv.writer(stream,lineterminator='\n')
    writer.writerow(['fichier','role','taille_octets','sha256','etat'])
    for path in files:
        rel=path.relative_to(ROOT)
        role=ROLES.get(rel.parts[0],'guide et suivi')
        state='PRESENT_RENDU_NON_TESTE' if path.suffix.lower() in {'.html','.css','.svg'} else 'PRESENT'
        writer.writerow([rel.as_posix(),role,path.stat().st_size,
                         hashlib.sha256(path.read_bytes()).hexdigest(),state])
print(f'{len(files)} lignes ; manifeste lui-même exclu (pas de boucle auto-référente)')
