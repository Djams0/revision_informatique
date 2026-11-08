# Installer et dépanner sans se perdre

Vérification des pages officielles : 8 novembre 2026. Les versions et boutons peuvent changer. Le cours vise un ordinateur Windows, macOS ou Linux ; aucune commande d'installation copiée d'un site inconnu n'est nécessaire.

## Première installation : Thonny et Python 3 (semaine 7)

1. Depuis le navigateur, saisis toi-même [thonny.org](https://thonny.org/). Vérifie le nom du domaine avant de cliquer sur le téléchargement correspondant à **ton système et ton type de machine**. Thonny propose des installateurs Windows et macOS, et des instructions Linux. Sur plusieurs plateformes, Python est inclus ; vérifie dans Thonny quel interpréteur est sélectionné.
2. Windows : utilise l'installateur officiel adapté, ouvre Thonny depuis le menu Démarrer. macOS : prends le paquet officiel adapté au processeur, ouvre l'application et suis les consignes de sécurité du système. Linux : privilégie le gestionnaire de logiciels de la distribution ou les instructions officielles de Thonny ; demande de l'aide si l'installation exige une commande que tu ne comprends pas.
3. Dans Thonny, crée un fichier, écris `print("Bonjour")`, enregistre-le comme `bonjour.py` dans `mes_exercices/S07`, puis clique **Run/Exécuter**. La console doit afficher `Bonjour`. Garde les extensions visibles dans ton gestionnaire de fichiers.

Si Thonny n'est pas compatible avec l'ordinateur, [python.org/downloads](https://www.python.org/downloads/) fournit Python officiel, mais demande de choisir ensuite un éditeur ; sollicite une aide locale pour la configuration. Pour **observer** du code court sans installation, [Python Tutor](https://pythontutor.com/python-compiler.html) fonctionne dans le navigateur ; il ne remplace ni tes fichiers locaux ni l'installation et ne doit recevoir aucune donnée personnelle.

## Git (semaine 16)

Va sur [git-scm.com/install](https://git-scm.com/install/) et choisis Windows, macOS ou Linux. Sur Linux, utilise de préférence le gestionnaire de paquets officiel de la distribution. Après installation, ouvre un nouveau terminal et tape `git --version`. Si la commande n'existe pas, ferme et rouvre le terminal, puis vérifie que l'installation est terminée. GitHub n'est pas nécessaire pour créer un dépôt local.

## Trouver et lancer un fichier

| But | Manière simple |
|---|---|
| Exécuter Python | Ouvre le `.py` dans Thonny et clique Run ; lis la console. |
| Voir HTML | Ouvre `index.html` dans le navigateur et actualise après modification. |
| Voir CSV | Ouvre une **copie** dans un éditeur de texte ou un tableur ; vérifie le séparateur. |
| Lire ce cours | Ouvre le `.md` dans un éditeur de texte ou un lecteur Markdown. |

## Quelques commandes sûres pour apprendre le terminal

| Action | PowerShell (Windows) | macOS/Linux |
|---|---|---|
| Voir le dossier courant | `Get-Location` | `pwd` |
| Lister les fichiers | `Get-ChildItem` | `ls` |
| Monter au parent | `Set-Location ..` | `cd ..` |
| Créer un dossier dans le dossier courant | `New-Item -ItemType Directory -Name essai` | `mkdir essai` |

Avant une commande, confirme le dossier courant. Les commandes de création peuvent échouer si `essai` existe déjà ; c'est un message à lire, pas une raison de supprimer le dossier.

## Dépannage par symptôme

| Symptôme | Vérification et petit essai |
|---|---|
| `SyntaxError` | Regarde la ligne indiquée, les guillemets, parenthèses et `:`. Reviens à un exemple de deux lignes. |
| `IndentationError` | Vérifie quatre espaces par niveau de bloc et l'alignement des lignes du même bloc. |
| `ValueError` avec `int` | La saisie contient-elle seulement un entier comme `12` ? `12,5` n'est pas un entier. |
| `NameError` | Vérifie l'orthographe du nom et l'ordre de création des variables. |
| `FileNotFoundError` | Vérifie le nom exact, l'extension et le dossier recherché. |
| `ModuleNotFoundError` pour `csv`, `sqlite3` ou `pathlib` | Vérifie que Thonny utilise Python 3 et qu'aucun fichier personnel ne s'appelle `csv.py`, `sqlite3.py` ou `pathlib.py`. |
| La page ne prend pas le CSS | Vérifie `style.css`, la ligne `<link>` et le même dossier ; actualise le navigateur. |
| `git` non reconnu | Rouvre le terminal, puis vérifie l'installation officielle ; garde une copie du dossier même sans Git. |

**Méthode :** note attendu, observé, ligne d'erreur ; change une chose, relance. Évite les commandes destructrices proposées par des forums ou une IA. Aucun compte ni paiement n'est requis pour terminer le tronc commun.
