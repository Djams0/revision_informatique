"""Create and reopen a distribution ZIP from this folder and its manifest."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import csv
import hashlib

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parent/'FORMATION_INFORMATIQUE_DEBUTANTE_18_SEMAINES_CORRIGEE.zip'
MANIFEST=ROOT/'08_CONTROLES/MANIFESTE_FINAL.csv'
with MANIFEST.open(encoding='utf-8-sig',newline='') as stream:
    rows=list(csv.DictReader(stream))
def partageable(path):
    """Exclut les métadonnées Git, caches et environnements locaux."""
    rel = path.relative_to(ROOT)
    exclus = {'.git', '__pycache__', '.pytest_cache', '.mypy_cache',
              '.ruff_cache', '.venv', 'venv', 'node_modules'}
    return not any(part in exclus for part in rel.parts) and path.name not in {'.DS_Store', 'Thumbs.db'}

files=sorted(p for p in ROOT.rglob('*') if p.is_file() and partageable(p))
listed={row['fichier'] for row in rows}
actual={p.relative_to(ROOT).as_posix() for p in files}
assert listed==actual-{'08_CONTROLES/MANIFESTE_FINAL.csv'}
assert not any(p.is_symlink() for p in files)
assert all(p.suffix.lower() not in {'.zip','.ovpn','.lnk','.pem','.key','.pyc'} for p in files)
with ZipFile(DEST,'w',ZIP_DEFLATED,compresslevel=8) as archive:
    for file in files:
        archive.write(file,Path('FORMATION_INFORMATIQUE_DEBUTANTE')/file.relative_to(ROOT))
with ZipFile(DEST,'r') as archive:
    assert archive.testzip() is None
    assert len(archive.namelist())==len(files)
    assert {Path(name).as_posix().split('/',1)[1] for name in archive.namelist()}==actual
    for row in rows:
        data=archive.read('FORMATION_INFORMATIQUE_DEBUTANTE/'+row['fichier'])
        assert len(data)==int(row['taille_octets'])
        assert hashlib.sha256(data).hexdigest()==row['sha256']
    assert archive.read('FORMATION_INFORMATIQUE_DEBUTANTE/08_CONTROLES/MANIFESTE_FINAL.csv')==MANIFEST.read_bytes()
print(f'{DEST.name} : {len(files)} fichiers, {DEST.stat().st_size} octets, testzip OK')
print('SHA-256 : '+hashlib.sha256(DEST.read_bytes()).hexdigest())
