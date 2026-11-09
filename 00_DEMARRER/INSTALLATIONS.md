# Installer ce qu'il faut — ni plus ni moins

**À ne PAS installer au début :** VS Code, PyCharm, Anaconda, Jupyter, Docker, MySQL, PHP, XAMPP et Git. Ces logiciels pourront servir plus tard, mais pas maintenant.

## Semaine 1 : préparer les dossiers, sans installer de langage
- Un ordinateur Windows / macOS / Linux, son navigateur et son éditeur de texte déjà présent suffisent.
- **Windows :** Explorateur, Bloc-notes, afficher les extensions dans l'Explorateur.
- **macOS :** Finder, TextEdit **en texte brut**.
- **Linux :** gestionnaire de fichiers et éditeur de texte existants.
- Crée **mes_exercices/S01**, puis **bonjour.txt**. Écris une phrase, enregistre, ferme et rouvre. Le fichier est-il encore là ?
- Télécharge les cours depuis https://github.com/Djams0/revision_informatique via **Code → Download ZIP** (pas besoin d'installer Git).

## Semaine 7 : Thonny + Python
**Site officiel :** https://thonny.org/ . Il propose des installateurs Windows, macOS Intel/Apple Silicon et des instructions Linux. Sur plusieurs plateformes Python est inclus ; ne réinstalle pas Python séparément sans nécessité.

1. Choisis l'installateur du site officiel adapté au système et à son architecture.
2. Ouvre Thonny, crée un nouveau script.
3. Recopie et enregistre dans **mes_exercices/S07/bonjour.py** :
   
   ~~~python
   print("Bonjour, je programme !")
   ~~~
4. Clique sur **Exécuter** (souvent F5) et constate : **Bonjour, je programme !**
5. Rouvre le fichier et exécute-le de nouveau.

**Vidéo d'installation FR (2020) :** https://www.youtube.com/watch?v=U9_z6qHYsa8 (Sébastien CLAUDIN, « Installation de Thonny - Python »). Les boutons peuvent différer de l'édition actuelle : le site officiel fait foi. La vidéo ne dispense pas de vérifier le résultat par toi-même.

**Si ça bloque :** [fiche dépannage](../02_FICHES/INSTALLATION_ET_DEPANNAGE.md). Aucun script inconnu ni désactivation d'antivirus.

## Semaines 13–14 : HTML/CSS
**Aucun nouveau logiciel obligatoire.** Crée index.html et style.css dans le même dossier, ouvre la page dans le navigateur puis actualise après enregistrement.

## Semaine 15 : SQLite
**Aucun serveur à installer.** Thonny suffit : suivre [la fiche SQL](../02_FICHES/PRATIQUER_SQL_PAS_A_PAS.md) et utiliser la base temporaire de l'atelier.

## Semaine 16 : Git seulement maintenant
Télécharger depuis https://git-scm.com/install ; vérifier dans un nouveau terminal **git --version**. **Vidéo installation Windows FR (2024)** : https://www.youtube.com/watch?v=72nOpz8dCHo ; **formation Git en français** : https://grafikart.fr/formations/git (introduction, installation, premiers commits uniquement). Les anciennes captures des vidéos peuvent ne pas correspondre à la version actuelle.

**GitHub est facultatif ; un dépôt Git local suffit.** Ne colle jamais de mot de passe ou de clé dans un exercice ou une IA.
