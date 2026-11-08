# Sélection et notation des sources — 8 novembre 2026

L'inventaire de référence est `INVENTAIRE_SOURCES.csv` : 365 entrées y compris les contenus de ZIP imbriqués, 238 empreintes distinctes. Les doublons SHA-256 sont exclus ; une note recopiée indique la valeur du contenu, non une nouvelle sélection. Une équivalence proche sans égalité binaire n'est pas automatiquement un doublon. Échelle : 0 = inutile ou dangereux, 3 = notions isolées avec fortes corrections, 6 = matière utile après simplification, 10 = utilisable directement sans correction. Aucun support brut n'est redistribué.

## Synthèse par archive

| Archive | Entrées (imbriquées incluses) | Doublons exacts | À réécrire | Extraits | Plus tard | Exclus |
|---|---:|---:|---:|---:|---:|---:|
| cours Algorithme.zip | 70 | 8 | 1 | 9 | 37 | 23 |
| cours UML.zip | 13 | 0 | 0 | 1 | 7 | 5 |
| cours architecture materiel et reseau.zip | 8 | 0 | 0 | 3 | 4 | 1 |
| cours conception et exploitation d'une base de donnees environement web.zip | 219 | 64 | 3 | 0 | 13 | 203 |
| cours html css php.zip | 2 | 2 | 0 | 0 | 0 | 2 |
| e-commerce et obligation legale.zip | 11 | 11 | 0 | 0 | 0 | 11 |
| infrastructure systeme reseaux.zip | 8 | 8 | 0 | 0 | 0 | 8 |
| marketing.zip | 28 | 28 | 0 | 0 | 0 | 28 |
| mise en place de la communication digitale.zip | 4 | 4 | 0 | 0 | 0 | 4 |
| powershell.zip | 2 | 2 | 0 | 0 | 0 | 2 |

La grande archive reprend intégralement les ZIP HTML/CSS/PHP, commerce, marketing, communication, PowerShell et infrastructure ; le contenu identique n'a été extrait pour analyse qu'une fois. Les deux ZIP de VPN qu'elle contient sont identiques et ne sont pas ouverts. Dans les ZIP algorithmiques, les corrections et le dossier personnel ont été inventoriés jusqu'à trois niveaux ; les métadonnées macOS et images propriétaires ne sont pas destinées au cours.

## Ressources pédagogiques effectivement retenues ou différées

Une note s'applique à la ressource **pour cette débutante**, pas à sa valeur générale. Les pages PDF sont les pages physiques du fichier. Les mentions « après S18 » sont des options, jamais des prérequis. Les cas avec noms ou données internes servent uniquement à la réflexion ; les futurs exemples seront inventés.

| Chemin source anonymisé | Note | Classement | Sujet / justification | Préalable | Moment | Passage | Correction prévue |
|---|---:|---|---|---|---|---|---|
| `cours Algorithme/Cours d' Algorithme Notion de base.docx` | 6/10 | INCLURE_APRES_REECRITURE | Données, tests, boucles, fonctions; intérêt : base à reformuler | aucun | S4–S6 | sections « langage pseudo-code », « si », « pour », « tant que » | Revoir types, portée, nommage, exemples et incohérences d’index. |
| `cours Algorithme/Algorithmique-2012-SynthesePC.pdf` | 4/10 | EXTRAIT_A_ADAPTER | Pseudo-code : instruction et condition; intérêt : exemple ou notion ponctuelle | aucun | S4–S5 | p. 1 ; p. 2 uniquement en appoint | Notation universitaire compacte ; retravailler les exemples, aucun fac-similé. |
| `cours Algorithme/TP - ALGO/TP_FINAL.ipynb` | 4/10 | EXTRAIT_A_ADAPTER | Énoncés de logique et formulation de problèmes; intérêt : exemple ou notion ponctuelle | conditions et boucles | S6–S7 | cellules markdown, sélectionner 2 tâches | Cahier des charges et squelettes trop denses ; reconstruire sans notebook. |
| `cours Algorithme/CODE/exo/exercice0.py` | 5/10 | EXTRAIT_A_ADAPTER | Table de multiplication; intérêt : exemple ou notion ponctuelle | boucle simple | S9 | lignes 1–5 | Bornes de la boucle ; nommage ; validation de saisie. |
| `cours Algorithme/CODE/exo/exercice2.py` | 5/10 | EXTRAIT_A_ADAPTER | Saisie contrôlée; intérêt : exemple ou notion ponctuelle | conditions et tant que | S9 | script complet | Ajouter explication de `or` et gestion d’une entrée non numérique. |
| `cours Algorithme/CODE/exo/exercice3.py` | 3/10 | EXTRAIT_A_ADAPTER | Jeu de devinette; intérêt : exemple ou notion ponctuelle | boucle et conditions | S9–S11 | script complet | Reconcevoir le flux : essai, comparaison, sortie et erreurs de saisie. |
| `cours Algorithme/CODE/exo/exercice5.py` | 4/10 | EXTRAIT_A_ADAPTER | Collection de notes; intérêt : exemple ou notion ponctuelle | listes et boucles | S10–S11 | script complet | Éviter la réutilisation de variable ; valider les notes et calculer la moyenne. |
| `cours Algorithme/corrections.zip!/corrections/[ANONYMISE]-python-exercices/exercice0.py` | 6/10 | EXTRAIT_A_ADAPTER | Correction de table; intérêt : exemple ou notion ponctuelle | boucles Python | S9 | script complet | Conserver idée seulement ; source tierce, ne pas redistribuer. |
| `cours Algorithme/corrections.zip!/corrections/[ANONYMISE]-python-exercices/exercice2.py` | 6/10 | EXTRAIT_A_ADAPTER | Correction de saisie; intérêt : exemple ou notion ponctuelle | boucles Python | S9 | script complet | `int(input())` peut lever ValueError ; refaire le corrigé. |
| `cours Algorithme/corrections.zip!/corrections/[ANONYMISE]-python-exercices/exercice10.py` | 5/10 | EXTRAIT_A_ADAPTER | Nombre mystère; intérêt : exemple ou notion ponctuelle | boucles et aléatoire | S9–S11 | script complet | Rendre les erreurs et les bornes compréhensibles. |
| `cours architecture materiel et reseau/Architecture_materielle__reseaux_-_partie_1.pdf` | 6/10 | EXTRAIT_A_ADAPTER | CPU, RAM, stockage et périphériques; intérêt : exemple ou notion ponctuelle | fichiers et logiciels | S2 | p. 32–49, 57–65 (choix de notions) | Trop de détail matériel ; redessiner les schémas, vérifier terminologie. |
| `cours architecture materiel et reseau/Architecture_materielle__reseaux_-_partie_2.pdf` | 6/10 | EXTRAIT_A_ADAPTER | Réseau local, IP, DNS, client/serveur; intérêt : exemple ou notion ponctuelle | matériel et système | S3 | p. 4–6, 19–24 | Modèle OSI trop tôt ; clarifier Internet versus Web et analogies. |
| `cours architecture materiel et reseau/Architecture_materielle__reseaux_-_partie_3.pdf` | 4/10 | EXTRAIT_A_ADAPTER | Un serveur fournit un service; intérêt : exemple ou notion ponctuelle | réseau local | S3 | p. 2–7 | Écarter cloud payant, virtualisation et détails commerciaux. |
| `cours conception et exploitation d'une base de donnees environement web/Cours Base de Données.docx` | 3/10 | INCLURE_APRES_REECRITURE | Table, ligne, colonne, clé, SELECT; intérêt : base à reformuler | listes, fichiers | S15 | intro et « manipulation des tables/données » | Nombreuses fautes SQL ; enseigner SQLite hors serveur, avec jeu fictif. |
| `cours conception et exploitation d'une base de donnees environement web/db_Spot[ANONYMISE].sql` | 3/10 | FACULTATIF_PLUS_TARD | Exemple de schéma relationnel multi-tables; intérêt : exemple ou notion ponctuelle | SQL simple | après S18 | début CREATE TABLE | Trop de tables ; noms propres ; vérifier clés étrangères et dialecte. |
| `cours UML/MCD.pdf` | 4/10 | EXTRAIT_A_ADAPTER | Table et relation sur un exemple; intérêt : exemple ou notion ponctuelle | SQL simple | S15 | p. 1–5 ; 12–13 en option | Redessiner un cas inédit ; distinguer MCD et SQL, droit de réutilisation. |
| `cours html css php/cours HTML et CSS.docx` | 4/10 | INCLURE_APRES_REECRITURE | Balises, liens, listes, sélecteurs; intérêt : base à reformuler | navigateur et fichiers | S13–S14 | paragraphes HTML puis CSS | Corriger sémantique, syntaxe des attributs, tableaux et formulaires. |
| `cours html css php/definition des langages informatique.docx` | 3/10 | INCLURE_APRES_REECRITURE | Rôles HTML, CSS, Python, SQL, SGBD; intérêt : base à reformuler | Web élémentaire | S13–S15 | document entier | Corriger SQL/MySQL/phpMyAdmin, PHP « toujours caché », CSS. |
| `cours UML/Exercice_MCD.odt` | 3/10 | FACULTATIF_PLUS_TARD | Repérer des entités et relations; intérêt : exemple ou notion ponctuelle | SQL simple | après S18 | énoncé | Boutique complexe ; préférer livres et emprunts fictifs. |
| `powershell/[ANONYMISE] [ANONYMISE] [ANONYMISE].docx` | 3/10 | FACULTATIF_PLUS_TARD | Concept de terminal et variables PowerShell; intérêt : exemple ou notion ponctuelle | Python et terminal | après S18 | note et script, théorie seulement | Deuxième langage inutile ; script dépend d’un chemin local, ne pas lancer. |
| `infrastructure systeme reseaux/infrastructure systeme reseaux/Projet Transversal - Installation - Infrastructure Système Réseau - v2.docx` | 2/10 | FACULTATIF_PLUS_TARD | Vocabulaire réseau, schéma global; intérêt : exemple ou notion ponctuelle | réseau et OS | après S18 | préambule uniquement | Infrastructures avancées, adresses internes et identité du projet : exclure source brute. |

## Arbitrages

- **Exclus** : marketing, communication, e-commerce juridique, cours d'anglais/français, projets PHP, API, serveurs, VPN, Packet Tracer, polices et raccourcis. Certains fichiers parlent d'informatique, mais demandent déjà un environnement, une équipe ou une expertise ; les SQL issus de projets et les scripts restent des sources internes de vérification, pas des devoirs à donner.
- **À traiter plus tard** : UML complet, MCD approfondi, PowerShell, infrastructure avancée, PHP. La base relationnelle est abordée avec SQLite dans un scénario local, sans installation de serveur.
- **Besoins absents des sources** : prise en main des fichiers et logiciels, sécurité personnelle, installation accessible de Python, gestion d'erreurs, Git et méthode d'autonomie. Ces chapitres seront écrits de zéro avec ressources officielles.
- **Droits** : les PDF de cours externes, supports enseignants et corrections d'autres personnes ne sont pas présumés redistribuables. Seuls liens, concepts reformulés et nouveaux schémas/exemples seront dans le dossier final.
