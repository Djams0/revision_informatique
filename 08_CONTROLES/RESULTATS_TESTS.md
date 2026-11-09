# Résultats des contrôles reproductibles — 8 novembre 2026

Commande lancée depuis la racine du dépôt : `python tools/valider_formation.py`, après `python tools/construire_guide.py` et `python tools/generer_manifeste.py`. Environnement observé : Python 3.12.14, SQLite du module standard `sqlite3` et Git 2.52.0. Les sorties détaillées sont produites en JSON sur la console ; le script quitte avec code 1 si au moins un contrôle échoue.

**Bilan de cette passe : 44 contrôles `VALIDÉ`, 0 `ÉCHEC`.** Les catégories ci-dessous résument les contrôles réellement exécutés. Le résultat est reproductible **sur les fichiers actuellement dans ce dépôt**, sans les archives d'origine.

| Contrôle exécuté | Preuve observable | État |
|---|---|---|
| Inventaire et structure | 365 entrées de 10 archives dans le CSV historique ; 18 lignes de calendrier ; 9 modules et 33 fichiers de référence présents. Les archives brutes ne sont pas relues. | **VALIDÉ** pour les documents présents |
| Exercices et corrigés | 58 identifiants uniques A15, P25, W8, Q5, T5 ; même ensemble une fois dans les corrigés ; 4 jalons J03/J06/J12/J18. Les 4 options OA01/OA02/OW01/OW02 restent distinctes et corrigées. | **VALIDÉ** |
| Semaines 11–12 et guide | Suivi à 18 lignes, P1 en S11, P3 en S12, variantes nommées facultatives ; les 9 cours figurent dans le guide avec liens adaptés. | **VALIDÉ** |
| Programmes Python | 30 solutions copiées dans des dossiers temporaires, exécutées avec saisies et sorties attendues ; 11 blocs des cours exécutés ; fichier P23 relu après deux lancements ; variante CSV `abc` : `ValueError` attendu. | **VALIDÉ** |
| Projets | 4 dossiers avec énoncé, indices, critères et solution ; 9 scénarios console exécutés pour P1–P3. P4 est contrôlé statiquement parmi les pages HTML. | **VALIDÉ** pour ces contrôles |
| SQL et guide débutant | Résultats exacts des 5 `.sql` dans SQLite en mémoire ; chacun relancé par `tools/atelier_sql.py`. `DROP TABLE` refusé par cet atelier. | **VALIDÉ** |
| Git local | Deux commits fictifs dans un dépôt temporaire ; deux lignes de journal. | **VALIDÉ** |
| Navigation et graphismes | Liens locaux de 64 Markdown résolus ; 9 pages HTML : doctype, `lang`, liens et `alt` contrôlés statiquement ; 6 SVG XML ont un titre et une description. Les SVG ont été convertis en PNG et inspectés en planche ; le schéma DNS a été corrigé après cette inspection. | **VALIDÉ** pour ces contrôles |
| Manifeste et nettoyage | 129 autres fichiers, tous listés avec chemin, taille et SHA-256 concordants ; aucun `.zip`, `.ovpn`, `.lnk`, clé ou cache interdit dans le dépôt. Recherche d'adresses : seulement `apprenante@example.invalid`, aucune adresse non fictive. | **VALIDÉ** après régénération finale du manifeste |

## Limites séparées des validations

| Point | État | Contrôle manuel restant |
|---|---|---|
| Mise en page des neuf pages HTML locales sur divers écrans | **NON_TESTÉ** | Ouvrir `05_CODE_EXEMPLES/web/W08/index.html` et la solution de P4 dans un navigateur, vérifier les styles et une fenêtre étroite. Les vérifications statiques ne prouvent pas le rendu. |
| Parcours SQL dans l'interface graphique Thonny sur Windows, macOS et Linux | **NON_TESTÉ** | Ouvrir la fiche, créer `mes_exercices/S15/essai.sql`, utiliser F5 et comparer avec Q01. Le même script a été exécuté en ligne de commande sur les cinq solutions. |
| Vidéos externes et disponibilité future des liens | **NON_TESTÉ** à cette passe | Ouvrir les pages officielles sur la machine de l'apprenante ; aucun titre, durée ni lecture complète supplémentaire n'est revendiqué ici. |
| Audit direct des 10 archives originales | **NON_TESTÉ** à cette passe | Archives non accessibles lors des correctifs ; le CSV et les rapports d'audit antérieurs restent la traçabilité disponible. |

Le manifeste s'exclut lui-même pour éviter une taille et une empreinte auto-référentes ; son nombre de lignes équivaut au nombre total de fichiers **moins un**. Si un fichier du dépôt est édité, régénérer le guide si nécessaire, puis le manifeste avant de relancer les contrôles.
