"""Reproducible checks for the authored curriculum; never execute source ZIP scripts.

Run: python tools/valider_formation.py
Requires Python 3 and its standard library; the Git check additionally requires Git.
All Python examples execute in temporary copies with fictitious inputs.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import csv
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
ROOT = root
def partageable(path):
    """Exclut les métadonnées Git, caches et environnements locaux."""
    rel = path.relative_to(ROOT)
    exclus = {'.git', '__pycache__', '.pytest_cache', '.mypy_cache',
              '.ruff_cache', '.venv', 'venv', 'node_modules'}
    return not any(part in exclus for part in rel.parts) and path.name not in {'.DS_Store', 'Thumbs.db'}
errors = []
results = {}
def check(label, condition, detail=''):
    results[label] = {'status': 'VALIDÉ' if condition else 'ÉCHEC', 'detail': detail}
    if not condition: errors.append(f'{label}: {detail}')

required = ['README.md','README_COMMENCER_ICI.md','INDEX.md','GUIDE_COMPLET.md','NOTE_POUR_L_ACCOMPAGNANT.md',
 'SUIVI_18_SEMAINES.csv','00_ADMIN/INVENTAIRE_SOURCES.csv','00_ADMIN/SELECTION_SOURCES.md',
 '00_ADMIN/AUDIT_ERREURS.md','00_ADMIN/PLAN_DE_PRODUCTION.md','00_ADMIN/PARCOURS_18_SEMAINES.md',
 '07_RESSOURCES/SITES_ET_VIDEOS_VERIFIES.md','07_RESSOURCES/METHODE_AUTOFORMATION_IA.md',
 '02_FICHES/PRATIQUER_SQL_PAS_A_PAS.md','02_FICHES/AUTEUR_LIVRE.md',
 '03_EXERCICES/OPTIONS_APRES_S11.md','04_CORRIGES/OPTIONS_APRES_S11.md',
 'tools/atelier_sql.py','08_CONTROLES/MANIFESTE_FINAL.csv']
required += [f'01_COURS/M{i:02d}.md' for i in range(9)]
required += [f'02_FICHES/{x}.md' for x in ('LEXIQUE_FR_EN','MEMENTO_PSEUDOCODE_PYTHON',
 'MEMENTO_SYSTEME_WEB','INSTALLATION_ET_DEPANNAGE','UTILISER_IA_POUR_APPRENDRE')]
check('fichiers_obligatoires',all((root/p).is_file() and (root/p).stat().st_size>20 for p in required),f'{len(required)} fichiers attendus')

rows=list(csv.DictReader((root/'00_ADMIN/INVENTAIRE_SOURCES.csv').open(encoding='utf-8-sig')))
check('archives_sources',len(rows)==365 and len({r['archive'] for r in rows})==10,
      f'{len(rows)} entrées, {len({r["archive"] for r in rows})} archives')
check('empreintes_doublons',any(r['duplicate_of'] for r in rows) and all(r['sha256'] for r in rows),'Empreintes et colonne doublons présentes')
lex=(root/'02_FICHES/LEXIQUE_FR_EN.md').read_text()
terms=re.findall(r'^\|\s*(\d+)\s*\|',lex,re.M)
check('lexique',len(terms)>=50 and len(terms)==len(set(terms)),f'{len(terms)} définitions')
calendar=(root/'00_ADMIN/PARCOURS_18_SEMAINES.md').read_text()
weeks=re.findall(r'^\| (\d{1,2}) \|',calendar,re.M)
check('semaines',weeks==list(map(str,range(1,19))),'18 lignes de semaines 1 à 18')
check('cours_fond',all(len((root/f'01_COURS/M{i:02d}.md').read_text().split())>=500 for i in range(9)),
      'Chaque cours contient au moins 500 mots, un exemple et une vérification')
for i in range(9):
    txt=(root/f'01_COURS/M{i:02d}.md').read_text()
    check(f'cours_M{i:02d}',all(s in txt for s in ('À quoi cela sert','Ce qu\'il faut savoir','Exemple expliqué pas à pas','Essaye toi-même','Comment vérifier si j\'ai compris')),
          'Cinq rubriques pédagogiques')

pattern=re.compile(r'^## ((?:A|P|W|Q|T)\d\d) — ',re.M)
es=[m for p in (root/'03_EXERCICES').glob('*.md') for m in pattern.findall(p.read_text())]
cs=[m for p in (root/'04_CORRIGES').glob('*.md') for m in pattern.findall(p.read_text())]
counts=Counter(x[0] for x in es)
check('exercices',len(es)==58 and len(set(es))==58 and counts=={'A':15,'P':25,'W':8,'Q':5,'T':5},str(counts))
check('corriges',Counter(es)==Counter(cs),'58 identifiants concordants, chacun une fois')
for p in (root/'03_EXERCICES').glob('*.md'):
    if p.name.startswith(('QUIZ','OPTIONS_')): continue
    txt=p.read_text()
    parts=re.split(pattern,txt)[1:]
    check(f'consignes_{p.stem}',all(s in txt for s in ('Semaine :','Difficulté :','Prérequis :','Durée :','Deux jeux de vérification','Indice','Réussite')),
          'Semaine, difficulté, prérequis, durée, tests, indice et réussite')
quizzes=(root/'03_EXERCICES/QUIZ_ET_BILANS.md').read_text()
answers=(root/'04_CORRIGES/CORRIGES_QUIZ.md').read_text()
check('quiz',all('J'+w in quizzes and 'J'+w in answers for w in ('03','06','12','18')),
      '4 jalons et 4 corrigés')
check('separation_solutions',not any('**Solution de référence.**' in p.read_text() for p in (root/'03_EXERCICES').glob('*.md')),
      'Aucune solution de référence dans les énoncés')

py_files=list((root/'05_CODE_EXEMPLES/python').glob('*/solution.py'))
project_scripts=list((root/'06_PROJETS').glob('P*/SOLUTION/*.py'))
for p in py_files+project_scripts:
    try: compile(p.read_text(),str(p),'exec')
    except SyntaxError as e: errors.append(f'Syntaxe {p.relative_to(root)}: {e}')
check('python_syntaxe',not any(x.startswith('Syntaxe') for x in errors),f'{len(py_files)} exemples + {len(project_scripts)} projets')

with tempfile.TemporaryDirectory() as d:
    temp=Path(d)
    cases={
        'A11':('Lia\n','Bonjour Lia'),'A12':('8\n10\n','2'),'A13':('18\n','accès'),
        'A14':('3\n','1\n2\n3'),'A15':('','11'),
        'P01':('','Bonjour\nJe découvre Python'),'P02':('Lia\n','Salut, Lia !'),
        'P03':('2\n3\n','5'),'P04':('3\n4\n','12'),'P05':('chat\n','4'),
        'P06':('4\n','pair'),'P07':('18\n','adulte'),'P08':('20\n','18'),
        'P09':('3\n','3\n2\n1'),'P10':('3\n','6'),'P11':('-1\n20\n','20'),
        'P12':('3\n7\n','trouvé'),'P13':('','Poèmes'),'P14':('','15.0'),
        'P15':(' CHAT \n','4'),'P16':('atlas\n','présent'),'P17':('Atlas\n','2'),
        'P18':('4\n','8'),'P19':('3\n7\n','7'),'P20':('','2'),
        'P21':('10\n2\n','8'),'P22':('','A\nB'),'P23':('Marcher\n','ajoutée'),
        'P24':('','7'),'P25':('abc\n4\n','16')}
    for name,(inp,expected) in cases.items():
        src=root/'05_CODE_EXEMPLES/python'/name
        dest=temp/name; shutil.copytree(src,dest,ignore=shutil.ignore_patterns('__pycache__'))
        rr=subprocess.run([sys.executable,str(dest/'solution.py')],input=inp,text=True,capture_output=True,timeout=5)
        if rr.returncode or expected not in rr.stdout: errors.append(f'Python {name}: {rr.stdout} {rr.stderr}')
    check('python_exemples',len(cases)==30 and not any(x.startswith('Python ') for x in errors),
          '30 exécutions en copie isolée, entrées et sorties attendues')
    script=temp/'P23/solution.py'
    rr=subprocess.run([sys.executable,str(script)],input='Lire\n',text=True,capture_output=True,timeout=5)
    check('persistance_P23',rr.returncode==0 and (temp/'P23/taches.txt').read_text()=='Marcher\nLire\n',
          'Deux lancements ajoutent deux lignes')

    module_cases={'M03.md':[('Ari\n','Bonjour Ari'),('8\n10\n','Différence : 2'),
                            ('8\n10\n','Monnaie à rendre : 2'),('3\n','3 x 5 = 15'),
                            ('25\n12\n','Note acceptée : 12'),('','Nombre de titres : 3'),('','Moyenne : 12.0')],
                  'M04.md':[('','Total fictif : 7'),('abc\n','Entre des chiffres entiers')],
                  'M06.md':[('','3 Jardin secret 2023')],
                  'M08.md':[('1\n2\nLire\n1\n0\n','- Lire')]}
    blocks_ok=0; block_count=0
    for name,inputs in module_cases.items():
        p=root/'01_COURS'/name
        blocks=re.findall(r'```python\n(.*?)\n```',p.read_text(),re.S)
        if len(blocks)!=len(inputs): errors.append(f'Cours {name}: blocs incomplets')
        for i,(code,(inp,expected)) in enumerate(zip(blocks,inputs)):
            block_count+=1
            dest=temp/f'{name}_{i}.py'; dest.write_text(code)
            rr=subprocess.run([sys.executable,str(dest)],input=inp,text=True,capture_output=True,timeout=5)
            if rr.returncode or expected not in rr.stdout:
                errors.append(f'Cours {name} bloc {i}: {rr.stdout[-300:]} {rr.stderr[-300:]}')
            else: blocks_ok+=1
    check('code_cours',blocks_ok==11 and block_count==11,f'{blocks_ok}/{block_count} blocs Python de M03, M04, M06, M08 exécutés')
    m04=(root/'01_COURS/M04.md').read_text()
    corrupt=re.findall(r'```python\n(.*?)\n```',m04,re.S)[0].replace('("pain", 3)','("pain", "abc")')
    bad=temp/'m04_invalide.py'; bad.write_text(corrupt)
    rr=subprocess.run([sys.executable,str(bad)],text=True,capture_output=True,timeout=5)
    check('erreur_csv',rr.returncode!=0 and 'ValueError' in rr.stderr,
          'Test de la variante abc sur copie : ValueError attendu')

    gitdir=temp/'essai_git';gitdir.mkdir()
    readme=gitdir/'README.md';readme.write_text('# Mon essai local\n')
    cmds=[['git','init'],['git','config','user.name','Apprenante'],
          ['git','config','user.email','apprenante@example.invalid'],
          ['git','add','README.md'],['git','commit','-m','Ajoute la présentation']]
    for cmd in cmds:
        rr=subprocess.run(cmd,cwd=gitdir,text=True,capture_output=True,timeout=5)
        if rr.returncode:errors.append(f'Git {cmd}: {rr.stderr[-200:]}')
    readme.write_text('# Mon essai local\nUne phrase.\n')
    for cmd in [['git','add','README.md'],['git','commit','-m',"Précise l'objectif"]]:
        rr=subprocess.run(cmd,cwd=gitdir,text=True,capture_output=True,timeout=5)
        if rr.returncode:errors.append(f'Git {cmd}: {rr.stderr[-200:]}')
    log=subprocess.run(['git','log','--oneline'],cwd=gitdir,text=True,capture_output=True,timeout=5)
    check('git_local',log.returncode==0 and len(log.stdout.splitlines())==2 and not any(x.startswith('Git ') for x in errors),
          'Deux commits fictifs dans un dépôt temporaire')

    projects=sorted((root/'06_PROJETS').glob('P[1-4]_*'))
    for p in projects:
        for filename in ('ENONCE.md','CRITERES.md','INDICES.md','SOLUTION/README.md'):
            if not (p/filename).is_file() or (p/filename).stat().st_size<50:
                errors.append(f'Projet {p.name}: {filename} absent')
        shutil.copytree(p/'SOLUTION',temp/p.name,ignore=shutil.ignore_patterns('__pycache__'))
    project_cases=[('P1_CALCULATRICE','4\n-2\n*\n','Résultat : -8'),
        ('P1_CALCULATRICE','4\n0\n/\n','Choix inconnu.'),
        ('P1_CALCULATRICE','x\n','Entrez des entiers.'),
        ('P2_QUIZ','a\nb\na\n','Score : 3 / 3'),
        ('P2_QUIZ','b\nb\nb\n','Score : 1 / 3'),
        ('P2_QUIZ',' A \n B \na\n','Score : 3 / 3'),
        ('P3_TACHES_LOCALES','1\n2\nLire\n1\n0\n','- Lire'),
        ('P3_TACHES_LOCALES','1\n0\n','- Lire'),
        ('P3_TACHES_LOCALES','2\n\n0\n','Texte vide refusé.')]
    for name,inp,expected in project_cases:
        script=next((temp/name).glob('*.py'))
        rr=subprocess.run([sys.executable,str(script)],input=inp,text=True,capture_output=True,timeout=5)
        if rr.returncode or expected not in rr.stdout:errors.append(f'Projet {name}: {rr.stdout} {rr.stderr}')
    check('projets',len(projects)==4 and not any(x.startswith('Projet ') for x in errors),
          '4 dossiers complets ; 9 scénarios console ; structure P4 contrôlée statiquement')

sql_expected={
    'Q01':[(1,'Atlas',2020),(2,'Contes',2018)], 'Q02':[('Atlas',),('Contes',)],
    'Q03':[('Atlas',2020),('Jardin',2023)], 'Q04':[(1,'Atlas',2019),(3,'Jardin',2021)],
    'Q05':[('Atlas','Autrice fictive'),('Contes','Autrice fictive')]}
for name,expected in sql_expected.items():
    sql=(root/f'05_CODE_EXEMPLES/sql/{name}.sql').read_text()
    statements=[x.strip() for x in sql.split(';') if x.strip()]
    with sqlite3.connect(':memory:') as db:
        for stmt in statements[:-1]: db.execute(stmt)
        got=db.execute(statements[-1]).fetchall()
        if got!=expected:errors.append(f'SQL {name}: {got!r} != {expected!r}')
check('sql',not any(x.startswith('SQL ') for x in errors),'5 scripts exécutés en mémoire ; lignes exactes')

class HTMLCheck(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.tags=Counter()
    def handle_starttag(self,tag,attrs):
        self.tags[tag]+=1
        d=dict(attrs)
        if 'id' in d:self.ids.add(d['id'])
        for attr in ('href','src'):
            if attr in d:self.links.append((attr,d[attr]))
        if tag=='img' and not d.get('alt'):errors.append('HTML image sans alt')
html_files=list((root/'05_CODE_EXEMPLES/web').glob('W*/index.html'))+[root/'06_PROJETS/P4_PORTFOLIO_LOCAL/SOLUTION/index.html']
for p in html_files:
    content=p.read_text()
    parser=HTMLCheck();parser.feed(content)
    if not content.lstrip().lower().startswith('<!doctype html>') or '<html lang="fr"' not in content:
        errors.append(f'HTML doctype/langue {p.relative_to(root)}')
    for attr,link in parser.links:
        if link.startswith('#'):
            if link[1:] not in parser.ids:errors.append(f'HTML ancre {p.relative_to(root)} {link}')
        elif not link.startswith(('http:','https:','mailto:')):
            if not (p.parent/link.split('#')[0]).is_file(): errors.append(f'HTML chemin {p.relative_to(root)} {link}')
check('web',len(html_files)==9 and not any(x.startswith('HTML ') for x in errors),
      '9 pages analysées ; doctype/langue, fichiers et ancres locaux, alt des images')

md_files=list(root.rglob('*.md'))
for p in md_files:
    text=p.read_text()
    for raw in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        url=unquote(raw.split('#')[0])
        if url and not url.startswith(('http:','https:','mailto:')) and not (p.parent/url).exists():
            errors.append(f'Lien Markdown {p.relative_to(root)} -> {raw}')
check('liens_markdown',not any(x.startswith('Lien Markdown') for x in errors),
      f'{len(md_files)} fichiers Markdown, liens relatifs existants')

forbidden={'.ovpn','.lnk','.pyc','.pem','.key','.pfx','.p12','.woff','.woff2','.ttf','.otf','.zip'}
bad=[str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and partageable(p) and p.suffix.lower() in forbidden]
check('fichiers_interdits',not bad,str(bad[:5]))
resource=(root/'07_RESSOURCES/SITES_ET_VIDEOS_VERIFIES.md').read_text()
link_rows=[x for x in resource.splitlines() if x.startswith('| ') and x.split('|')[1].strip() not in ('Priorité','---')]
check('ressources',len(link_rows)==16 and sum(x.startswith('| V') for x in link_rows)==4,
      f'{len(link_rows)} ressources dont 4 pages vidéo CS50')

# This manifest deliberately lists all files except itself: its own byte size would
# otherwise depend on the size of the number printed in its self-description.
manifest=root/'08_CONTROLES/MANIFESTE_FINAL.csv'
with manifest.open(encoding='utf-8-sig',newline='') as stream:
    manifest_rows=list(csv.DictReader(stream))
actual={p.relative_to(root).as_posix():p.stat().st_size for p in root.rglob('*')
        if p.is_file() and p != manifest and partageable(p)}
listed={row['fichier']:int(row['taille_octets']) for row in manifest_rows}
hashes=all(hashlib.sha256((root/row['fichier']).read_bytes()).hexdigest()==row['sha256']
           for row in manifest_rows if row['fichier'] in actual)
check('manifeste',listed==actual and hashes and len(manifest_rows)==len(actual),
      f'{len(actual)} fichiers hors manifeste ; mêmes chemins, tailles et SHA-256')

schematic=list((root/'02_FICHES/SCHEMAS').glob('*.svg'))
try:
    for diagram in schematic:
        tree=ET.parse(diagram)
        if tree.getroot().find('{http://www.w3.org/2000/svg}title') is None or \
           tree.getroot().find('{http://www.w3.org/2000/svg}desc') is None:
            errors.append(f'Schéma sans titre ou description : {diagram.name}')
except ET.ParseError as exc:
    errors.append(f'Schéma XML : {exc}')
check('schemas',len(schematic)==7 and not any(x.startswith('Schéma ') for x in errors),
      '6 SVG XML avec titre et description')

for name in sql_expected:
    rr=subprocess.run([sys.executable,str(root/'tools/atelier_sql.py'),
                       str(root/f'05_CODE_EXEMPLES/sql/{name}.sql')],
                      text=True,capture_output=True,timeout=5)
    if rr.returncode or 'base de test effacée' not in rr.stdout:
        errors.append(f'Atelier SQL {name} : {rr.stdout} {rr.stderr}')
check('atelier_sql',not any(x.startswith('Atelier SQL') for x in errors),
      'Les cinq SQL passent par le guide exécutable dans une base en mémoire')
with tempfile.TemporaryDirectory() as dirname:
    badsql=Path(dirname)/'refuse.sql';badsql.write_text('DROP TABLE livres;')
    rr=subprocess.run([sys.executable,str(root/'tools/atelier_sql.py'),str(badsql)],
                      text=True,capture_output=True,timeout=5)
    check('atelier_refus',rr.returncode!=0 and 'non prévue' in rr.stdout,
          'DROP TABLE refusé sans base réelle')

with (root/'SUIVI_18_SEMAINES.csv').open(encoding='utf-8-sig',newline='') as stream:
    suivi=list(csv.DictReader(stream,delimiter=';'))
index=(root/'INDEX.md').read_text()
course11=(root/'01_COURS/M03.md').read_text()
course12=(root/'01_COURS/M04.md').read_text()
check('alignement_semaines',len(suivi)==18
      and all('P1' in x for x in [suivi[10]['Activité / livrable'],calendar, index,course11])
      and all('P3' in x for x in [suivi[11]['Activité / livrable'],calendar,index,course12])
      and 'facultative' in suivi[10]['Activité / livrable']
      and 'facultative' in suivi[11]['Activité / livrable'],
      'S11=P1 et S12=P3 ; anciennes variantes explicitement facultatives')

guide=(root/'GUIDE_COMPLET.md').read_text()
courses=[]
for n in range(9):
    module=(root/f'01_COURS/M{n:02d}.md').read_text().strip()
    for folder in ('02_FICHES','03_EXERCICES','04_CORRIGES','06_PROJETS'):
        module=module.replace(f'](../{folder}/',f']({folder}/')
    courses.append(module)
check('guide_synchronise',all(module in guide for module in courses),
      'M00–M08 se retrouvent dans le guide avec leurs liens adaptés à la racine')
optional_eds=(root/'03_EXERCICES/OPTIONS_APRES_S11.md').read_text()
optional_cs=(root/'04_CORRIGES/OPTIONS_APRES_S11.md').read_text()
optional_ids=('OA01','OA02','OW01','OW02')
check('options_separees',all(optional_eds.count('## '+k+' —')==1 and
      optional_cs.count('## '+k+' —')==1 for k in optional_ids),
      '4 nouveaux identifiants facultatifs et 4 corrigés séparés')

emails=[]
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in ('.md','.csv','.py','.sql','.html','.css','.svg','.txt'):
        for email in re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',p.read_text(encoding='utf-8-sig')):
            if not email.endswith('@example.invalid'):
                emails.append((p.relative_to(root).as_posix(),email))
check('emails_personnels',not emails,f'{len(emails)} adresses non fictives')

# Contrôles propres aux ateliers guidés.
atelier = root / '09_ATELIERS_GUIDES'
demandes = ['00_DEMARRER/README.md', '00_DEMARRER/INSTALLATIONS.md',
            '00_DEMARRER/VIDEOS_PAR_SEMAINE.md', '09_ATELIERS_GUIDES/README.md',
            '02_FICHES/SCHEMAS/pseudo_python_allers_retours.svg']
for n in range(1, 8):
    code=f'AT{n:02d}'
    demandes.extend([f'09_ATELIERS_GUIDES/{code}/CONSIGNE.md',
                     f'09_ATELIERS_GUIDES/CORRIGES/{code}.md'])
check('guides_debutants', all((root / p).is_file() for p in demandes),
      f'{len(demandes)} fichiers de démarrage et ateliers')
check('ateliers_fichiers_a_remplir', all(
    any((atelier/f'AT{n:02d}').glob('A_COMPLETER.*')) or
    (atelier/f'AT{n:02d}/CODE_A_CORRIGER.py').is_file()
    for n in range(1,8)), 'Sept fichiers de travail présents')
for n, saisie, resultat in [(4, '8\n10\n', '2'), (6, '4\n', '8'), (7, '', '2')]:
    p=atelier/f'CORRIGES/AT{n:02d}.py'
    if p.is_file():
        rr=subprocess.run([sys.executable,str(p)],input=saisie,text=True,
                          capture_output=True,timeout=5)
        bon=rr.returncode==0 and resultat in rr.stdout
    else:
        bon=False
    check(f'atelier_solution_AT{n:02d}',bon, 'Sortie Python comparée à la consigne')
check('exclusion_git', not any('.git' in p.relative_to(root).parts
      for p in root.rglob('*') if p.is_file() and partageable(p)),
      'Aucune métadonnée Git ne doit être distribuée')

print(json.dumps({'results':results,'errors':errors,
                  'manual':{'rendu_visuel':'NON_TESTÉ','lecture_integrale_videos':'NON_TESTÉ',
                            'archives_originales':'NON_TESTÉ'}},
                 ensure_ascii=False,indent=2))
if errors:sys.exit(1)
