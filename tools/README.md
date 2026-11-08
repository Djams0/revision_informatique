# Contrôles reproductibles

Depuis le dossier de formation, avec Python 3 installé, exécuter :

```text
python tools/construire_guide.py
python tools/generer_manifeste.py
python tools/valider_formation.py
python tools/creer_zip.py
```

Sur Windows, si `python` n'existe pas, essayer `py` ; dans Thonny, ouvrir le script et utiliser F5. `valider_formation.py` utilise la bibliothèque standard de Python et lance aussi un essai Git dans un dossier temporaire (Git doit être installé pour ce seul contrôle). Les scripts Python d'exemple sont exécutés **sur des copies temporaires** avec des données fictives ; les archives de cours originelles ne sont ni nécessaires ni exécutées. Le dossier `mes_exercices` personnel n'est pas touché par ces contrôles.

`atelier_sql.py` sert à l'apprenante en semaine 15, avec [la fiche pas à pas](../02_FICHES/PRATIQUER_SQL_PAS_A_PAS.md). Les tests automatiques exécutent les cinq scripts SQL dans SQLite en mémoire. Le manifeste donne **une ligne par autre fichier** : il s'exclut lui-même pour éviter qu'une taille auto-référente change à chaque écriture. Ses colonnes `PRESENT` indiquent l'existence, la taille et l'empreinte SHA-256, pas une garantie de qualité pédagogique ou de rendu visuel.

Le contrôle structurel HTML et la validité XML des SVG ne remplacent pas une inspection visuelle dans le navigateur. La lecture complète des vidéos et l'audit des archives originales ne sont pas reproduits par ces scripts.
