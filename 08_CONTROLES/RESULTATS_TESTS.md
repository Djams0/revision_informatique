# Résultats des contrôles — 8 novembre 2026

Les contrôles portent **uniquement sur les fichiers réécrits du dossier final**. Aucun script d'archive d'origine n'a été lancé. Environnement : Python 3.12, module standard `sqlite3`, Git local et analyseur HTML standard de Python. Le programme de contrôle `final_quality.py` reste hors du dossier destiné à l'apprenante ; ses résultats sont résumés ici. Les programmes écrivant un fichier ont été lancés dans des copies temporaires.

| Contrôle | Méthode et preuve observable | Résultat |
|---|---|---|
| Structure | Vérification de 26 fichiers principaux non vides ; 9 modules M00–M08, cinq fiches, programme et suivi. | **VALIDE** |
| Sources | Lecture CSV de `00_ADMIN/INVENTAIRE_SOURCES.csv` : 365 entrées, 10 noms d'archives, empreintes et doublons renseignés. | **VALIDE** |
| Progression | Lecture du calendrier : 18 lignes S1–S18 ; chacun des neuf modules contient objectif, explication, exemple, essai et vérification. | **VALIDE** |
| Lexique | 80 lignes numérotées distinctes dans `02_FICHES/LEXIQUE_FR_EN.md`. | **VALIDE** |
| Énoncés et corrigés | Extraction des identifiants `## A/P/W/Q/Tnn —` : 58 uniques dans les énoncés, mêmes 58 une fois chacun dans les corrigés ; 15 A, 25 P, 8 W, 5 Q, 5 T. Aucune solution de référence dans les énoncés. | **VALIDE** |
| Jalons | J03, J06, J12 et J18 présents dans `QUIZ_ET_BILANS.md` et `CORRIGES_QUIZ.md`. | **VALIDE** |
| Python de `05_CODE_EXEMPLES` | Compilation en mémoire de 30 fichiers ; exécution des 30 copies avec entrées de test et sortie attendue ; P23 exécuté deux fois et deux lignes conservées. | **VALIDE** |
| Code des cours | Extraction et exécution isolée des 11 blocs Python de M03, M04, M06 et M08 ; contrôle de la sortie de chacun. Variante CSV `"abc"` : `ValueError` attendu. | **VALIDE** |
| Projets | P1–P4 ont énoncé, indices, critères et solution distincte ; neuf scénarios pour P1–P3 : opérations, erreurs, score, texte vide et persistance au deuxième lancement. | **VALIDE** |
| SQL | `sqlite3.connect(':memory:')`, exécution des cinq `.sql` et comparaison exacte des résultats `SELECT` avec les jeux de référence. | **VALIDE** |
| Git | `git init`, identité fictive locale, deux `git add`/`git commit`, `git log --oneline` : deux lignes. | **VALIDE** |
| HTML/CSS | Analyse des neuf pages locales : doctype, `lang=fr`, ancres `#id`, images avec `alt`, liens relatifs vers CSS/SVG existants. P4 lié à son CSS local. | **VALIDE** pour la structure |
| Liens internes Markdown | Analyse des destinations locales de tous les `.md`, avec `INDEX.md` et `GUIDE_COMPLET.md` ; toutes les destinations existent. | **VALIDE** |
| Ressources Web | Ouverture des 12 pages de référence et des quatre pages officielles CS50 ; contrôle dans le navigateur du lecteur intégré pour Scratch, Python, HTML/CSS et SQL. Titres et sujets revus le 8 novembre 2026. | **VALIDE** pour les pages et les lecteurs intégrés |
| Nettoyage | Aucun fichier source brut, archive ZIP d'origine, `.ovpn`, `.lnk`, clé, certificat, cache ou `.pyc` dans le paquet. Le CSV d'inventaire et les renvois ont des chemins anonymisés. | **VALIDE** |
| ZIP final | Ouverture avec `zipfile.ZipFile`, `testzip()`, présence de la racine et concordance de tous les fichiers du manifeste. | **VALIDE** après contrôle de l'archive finale |

## Limites observées et contrôle alternatif

- **NON_TESTE — rendu visuel des fichiers locaux :** le lancement automatisé de Chromium s'arrête sur `socket() failed: Operation not permitted` ; le navigateur graphique de cet environnement bloque aussi l'ouverture des URL `file://` par sa politique d'organisation. Les neuf HTML, chemins CSS/SVG et ancres ont été inspectés statiquement. Sur son propre ordinateur, l'apprenante peut double-cliquer sur `05_CODE_EXEMPLES/web/W08/index.html` et `06_PROJETS/P4_PORTFOLIO_LOCAL/SOLUTION/index.html`, vérifier les styles et réduire la fenêtre à environ 375 px ; `CRITERES.md` du projet P4 décrit trois contrôles visibles. Aucun résultat de capture d'écran du site n'est revendiqué.
- **NON_TESTE — lecture audio/vidéo intégrale :** les quatre pages de cours CS50 et leurs lecteurs intégrés ont été observés dans un navigateur ; les lecteurs directs ont répondu de façon intermittente au contrôle automatique (un sur quatre a répondu à la dernière ouverture). Les sous-titres, la durée totale et la lecture complète dépendent du navigateur. Le fichier `07_RESSOURCES/SITES_ET_VIDEOS_VERIFIES.md` privilégie donc les pages officielles accessibles et indique cette limite. Les vidéos ne sont pas nécessaires pour réussir le parcours.
- La disponibilité des ressources externes et leurs conditions d'accès peuvent changer après le 8 novembre 2026. Les exercices, fichiers de code et projets de base fonctionnent localement.

## Reproduction rapide

Depuis un terminal équipé de Python 3, la commande `python final_quality.py` a été exécutée avant l'emballage depuis l'espace de contrôle ; elle ne fait pas partie des cours. Sans ce script : ouvrir les exemples dans Thonny, exécuter chaque `.sql` dans une base SQLite **vide**, ouvrir les `.html` en local et vérifier les résultats attendus écrits dans les énoncés et critères. Le manifeste `MANIFESTE_FINAL.csv` donne la liste exhaustive des fichiers partageables et leur taille.
