# Validation finale — livraison initiale du 8 novembre 2026

> Ce document décrit la livraison initiale. Pour les correctifs ultérieurs et leurs résultats reproduits, lire [RAPPORT_CORRECTIFS.md](../RAPPORT_CORRECTIFS.md) et [RESULTATS_TESTS.md](RESULTATS_TESTS.md). Le manifeste actuel est régénéré depuis les fichiers présents ; les comptes historiques ci-dessous peuvent différer.

**Périmètre :** dossier `FORMATION_INFORMATIQUE_DEBUTANTE/` et archive du même nom suivie de `_18_SEMAINES.zip`. « Oui » signifie que le point demandé est établi par les fichiers ou par un contrôle indiqué ; les deux limites `NON_TESTE` sont détaillées dans `RESULTATS_TESTS.md`. Les ressources initiales sont des sources de réflexion seulement : aucun PDF, Word, ZIP ou script reçu n'a été redistribué.

| Point | Oui / non | Preuve ou chemin | État |
|---|---|---|---|
| V01 — 10 ZIP audités, doublons identifiés | Oui | `00_ADMIN/INVENTAIRE_SOURCES.csv` : 365 lignes, 10 archives ; `SELECTION_SOURCES.md` : synthèse et empreintes. | VALIDE |
| V02 — Sources triées, note /10, motifs | Oui | `00_ADMIN/SELECTION_SOURCES.md` et colonnes `note`, `category`, `details` du CSV. | VALIDE |
| V03 — Aucun contenu sensible ou distribué sans droit | Oui | Aucun original intégré ; chemins privés anonymisés dans l'inventaire ; contrôle des extensions interdites et recherche de coordonnées dans `RESULTATS_TESTS.md`. | VALIDE sur le paquet |
| V04 — 18 semaines, 3–5 h modulables | Oui | `00_ADMIN/PARCOURS_18_SEMAINES.md`, 18 lignes et section rythme. | VALIDE |
| V05 — Installation et départ de zéro | Oui | `README_COMMENCER_ICI.md`, M00 et `02_FICHES/INSTALLATION_ET_DEPANNAGE.md`. | VALIDE |
| V06 — Matériel, systèmes, réseaux, sécurité | Oui | M00–M01, `MEMENTO_SYSTEME_WEB.md`, T01–T03. | VALIDE |
| V07 — Logique, pseudo-code et organigrammes | Oui | M02, A01–A10, schéma de condition S5. | VALIDE |
| V08 — Transition vers Python 3 | Oui | Tableau M03 S7, traduction A11–A15, mémento. | VALIDE |
| V09 — Neuf cours homogènes | Oui | `01_COURS/M00.md` à `M08.md`, cinq rubriques et contrôles par module. | VALIDE |
| V10 — HTML/CSS et mini-site | Oui | M05, W01–W08, `06_PROJETS/P4_PORTFOLIO_LOCAL/SOLUTION/`. | VALIDE pour fichiers et liens ; rendu visuel NON_TESTE |
| V11 — SQL/SQLite local | Oui | M06, Q01–Q05 exécutés en mémoire, sans serveur. | VALIDE |
| V12 — Terminal et Git sans commande dangereuse | Oui | M07, T04–T05, essai de deux commits dans `RESULTATS_TESTS.md`. | VALIDE |
| V13 — 50 définitions au moins | Oui | `02_FICHES/LEXIQUE_FR_EN.md` : 80 numéros distincts. | VALIDE |
| V14 — 58 activités en 15/25/8/5/5 | Oui | `03_EXERCICES/` : analyse des identifiants dans `RESULTATS_TESTS.md`. | VALIDE |
| V15 — Correction séparée pour 100 % | Oui | `04_CORRIGES/` : mêmes 58 identifiants, une fois chacun. | VALIDE |
| V16 — Résultats de code vérifiables | Oui | Chaque fiche d'énoncé fournit deux jeux ; les fichiers exécutables et corrigés détaillent la sortie. | VALIDE |
| V17 — Quatre bilans corrigés | Oui | `03_EXERCICES/QUIZ_ET_BILANS.md` et `04_CORRIGES/CORRIGES_QUIZ.md`. | VALIDE |
| V18 — Quatre projets, critères, tests, solutions | Oui | `06_PROJETS/P1_CALCULATRICE/` à `P4_PORTFOLIO_LOCAL/`, quatre fichiers ou sous-dossiers requis chacun. | VALIDE |
| V19 — Douze ressources et quatre vidéos | Oui | `07_RESSOURCES/SITES_ET_VIDEOS_VERIFIES.md` : 16 entrées, quatre pages CS50 avec lecteur intégré. | VALIDE pour titre/page ; lecture intégrale NON_TESTE |
| V20 — Autoformation et IA | Oui | `07_RESSOURCES/METHODE_AUTOFORMATION_IA.md`, huit formulations, tests et confidentialité. | VALIDE |
| V21 — Python, SQL et HTML/CSS contrôlés | Oui | `08_CONTROLES/RESULTATS_TESTS.md` : 30 exemples Python, 11 blocs des cours, cinq SQL, neuf HTML, projets. | VALIDE pour exécution et structure ; rendu visuel NON_TESTE |
| V22 — Index et chemins internes | Oui | `INDEX.md`, `GUIDE_COMPLET.md`, analyse des liens locaux. | VALIDE |
| V23 — ZIP créé et rouvert | Oui | `RESULTATS_TESTS.md` : `ZipFile.testzip()` et comparaison entrée/manifeste après création. | VALIDE |
| V24 — ZIP final partagé | Oui | Lien direct de téléchargement donné avec la réponse finale : `FORMATION_INFORMATIQUE_DEBUTANTE_18_SEMAINES.zip`. | VALIDE après livraison |

**Exceptions documentées :** contrôle visuel automatisé et lecture audiovisuelle intégrale non testés dans cet environnement. Les pages HTML sont des fichiers locaux ouvrables, et toutes les notions obligatoires sont enseignées dans les cours écrits sans dépendre d'une vidéo. Les résultats négatifs auraient été marqués `NON_CONFORME` ; aucun n'a été constaté lors du dernier contrôle automatisé du dossier final.
