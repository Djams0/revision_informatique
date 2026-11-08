# Plan de production — étapes 1 à 4, dossier livré

## État de l'étape 1

Six fichiers administratifs existent à la racine `00_ADMIN/` : inventaire CSV, sélection, audit d'erreurs, parcours, ressources et présent plan. Les archives d'origine et les textes extraits ne sont pas placés ici. Les décisions et notes de l'inventaire sont sujettes à une ultime relecture humaine des données personnelles avant une diffusion externe.

## Arborescence finale attendue

```text
FORMATION_INFORMATIQUE_DEBUTANTE/
├── README_COMMENCER_ICI.md            # mode d'emploi, installation, rythme et secours
├── INDEX.md                           # navigation, schéma et tableau des 18 semaines
├── GUIDE_COMPLET.md                   # neuf cours réunis en un document Markdown
├── NOTE_POUR_L_ACCOMPAGNANT.md        # aide hebdomadaire de 15–30 min
├── 00_ADMIN/
│   ├── INVENTAIRE_SOURCES.csv
│   ├── SELECTION_SOURCES.md
│   ├── AUDIT_ERREURS.md
│   ├── PARCOURS_18_SEMAINES.md
│   ├── RESSOURCES_A_VERIFIER.md
│   └── PLAN_DE_PRODUCTION.md
├── 01_COURS/
│   └── M00.md … M08.md               # 9 modules couvrant 18 semaines
├── 02_FICHES/
│   ├── LEXIQUE_FR_EN.md
│   ├── MEMENTO_PSEUDOCODE_PYTHON.md
│   ├── MEMENTO_SYSTEME_WEB.md
│   ├── INSTALLATION_ET_DEPANNAGE.md
│   └── UTILISER_IA_POUR_APPRENDRE.md
├── SUIVI_18_SEMAINES.csv
├── 03_EXERCICES/                   # 5 feuilles par thème, 58 exercices, 4 quiz
├── 04_CORRIGES/                    # 5 feuilles de solutions distinctes, corrigés quiz
├── 05_CODE_EXEMPLES/               # 30 scripts Python, 8 sites locaux, 5 scripts SQLite
├── 06_PROJETS/                     # P1 calculatrice, P2 quiz, P3 tâches, P4 portfolio
│   └── IDEES_POUR_LA_SUITE.md     # 10 pistes de projets facultatives
├── 07_RESSOURCES/                  # 16 liens dont 4 vidéos, fiche IA autonome
└── 08_CONTROLES/                   # manifeste, résultats, checklist finale
```

## Responsabilités et livraisons par étape

| Étape | Production contrôlable | Validation avant la suivante |
|---|---|---|
| 1 — audit (présente) | Les six fichiers `00_ADMIN`, 365 lignes d'inventaire détaillées, choix de 18 semaines, liens vérifiés. | Confirmer adéquation du public, rythme et niveau ; relire les signalements de sécurité. |
| 2 — cours | `README_COMMENCER_ICI`, 9 modules couvrant 18 semaines, 5 fiches et un CSV de suivi ; exemples originaux. | Chaque semaine a objectif, prérequis, exemple expliqué, mini-défi, résumé et vérification ; la traduction pseudo-code/Python est explicite. |
| 3 — pratique (présente) | 58 exercices numérotés en cinq feuilles thématiques, six fichiers de corrigés séparés, quatre quiz, quatre projets guidés avec solutions, 43 jeux d'exemples de code et ressources contrôlées. | Vérifier identité des numéros, compilation et exécution des solutions Python, exécution SQLite, fichiers HTML/CSS locaux, liens et cohérence des projets. |
| 4 — livraison (terminée) | Relecture des cours, correction de l'exemple CSV, harmonisation du parcours, index, guide, note d'accompagnement, rapports de contrôles et archive ZIP. | Voir `08_CONTROLES/RESULTATS_TESTS.md` et `VALIDATION_FINALE.md` pour preuves et limites. |

## Règles éditoriales et techniques

- Viser des leçons lisibles en 15–25 min, avec une notion principale et une illustration originale seulement quand elle clarifie la tâche. Français simple pour adulte ; anglais comme ressource facultative.
- Les solutions sont physiquement séparées des énoncés. L'exercice « essentiel » est faisable en 3 h cumulées ; les paliers 2 et 3 servent de prolongement. Les contrôles distinguent « compris », « à revoir » et « besoin d'aide ».
- Python 3 est l'unique langage de programmation du tronc commun. HTML/CSS et SQL sont présentés comme technologies ciblées avec un résultat local ; Scratch est une courte option, jamais un embranchement obligatoire. Ne pas imposer PHP, framework, Docker, cloud payant, API complexe ni POO avancée.
- Écrire de nouveaux exemples anonymes et des jeux de données fictifs ; ne jamais inclure les ZIP reçus, corrections tierces, VPN, clés, chemins internes, noms, emails, projets personnels ou copies de diapositives. Les liens vers ressources publiques sont permis sans les incorporer.
- Pour un partage élargi, contrôler visuellement la page portfolio locale sur l'appareil de l'apprenante ; les données d'exemple sont fictives, les sources originales ne sont pas intégrées.
