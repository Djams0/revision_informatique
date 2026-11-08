# Rapport des correctifs ciblés — 8 novembre 2026

Branche `correctifs-parcours-debutant`, à comparer avec `main` au commit `0df536d72f8052ae9ff89037267e5c51fa3fe0df`. Les 10 archives originales n'étaient pas jointes à cette passe : le recoupement s'appuie uniquement sur `00_ADMIN/SELECTION_SOURCES.md` et `AUDIT_ERREURS.md`. Aucun support brut n'a été ajouté.

| Avant | Après | Pourquoi | Fichiers touchés | Contrôle |
|---|---|---|---|---|
| S11 et S12 : suivi = moyenne et carnet ; calendrier = P1 et P3. | P1 et P3 sont les livrables communs ; moyenne et carnet restent des variantes facultatives. | Suivre la même progression dans toutes les entrées. | `SUIVI_18_SEMAINES.csv`, calendrier, `INDEX.md`, M03, M04, guide. | Alignement S11/S12 et 18 lignes dans `tools/valider_formation.py`. |
| Le mode d'emploi supposait un nom de dossier unique. | Il reconnaît `revision_informatique-main`, `revision_informatique` et `FORMATION_INFORMATIQUE_DEBUTANTE`. | Reprendre le dossier quel que soit le mode de téléchargement. | `README_COMMENCER_ICI.md`. | Liens locaux et lecture manuelle. |
| Q01–Q05 supposaient de savoir lancer du SQL. | Fiche Thonny et `tools/atelier_sql.py` : un `essai.sql` dans `mes_exercices/S15`, base SQLite en mémoire à chaque F5. | Donner un premier essai praticable sans terminal ni base réelle. | Fiche SQL, M06, énoncés SQL, index, calendrier, suivi, guide, outils. | 5 scripts SQL exécutés et commande de destruction refusée. |
| Les explications reposaient sur le texte et un petit diagramme Mermaid. | Six schémas SVG originaux avec descriptions textuelles dans les cours. | Voir les flux et les relations, même hors ligne. | M01, M02, M06, fiche Auteur/Livre, `02_FICHES/SCHEMAS/`, guide. | 6 SVG parsés et rendus en planche ; inspection visuelle humaine de la planche. |
| Les scripts de validation étaient hors du dossier ; manifeste ancien. | Outils de construction et de validation dans `tools/` ; manifeste régénéré sans auto-référence, avec SHA-256 et tailles. | Reproduire les tests depuis le dépôt et repérer les changements. | `tools/`, `08_CONTROLES/`, README, ce rapport. | Contrôle de l'inventaire exact, 58 exercices et corrigés, Python, SQL, projets, liens. |
| Pas d'activité courte sur tableau, formulaire, recherche/tri, relation. | 4 activités facultatives et corrigés séparés ; fiche Auteur/Livre. | Réemployer des notions utiles des sources sans gonfler le tronc commun. | `03_EXERCICES/OPTIONS_APRES_S11.md`, `04_CORRIGES/OPTIONS_APRES_S11.md`, fiche, index. | 4 identifiants supplémentaires distincts, 58 inchangés. |

## Portes P1

| Point obligatoire | État | Preuve / limite |
|---|---|---|
| Cohérence des renvois S11–S12 | **VALIDÉ** | Suivi, index, calendrier, M03/M04 et guide alignés ; 18 semaines conservées. |
| Nom du dossier téléchargé | **VALIDÉ** | Le mode d'emploi décrit le ZIP GitHub, Git et le nom initial. |
| Pratique des cinq Q sans terminal SQL | **VALIDÉ** pour les scripts | Fiche clic par clic ; cinq SQL exécutés avec l'atelier en mémoire. L'interface Thonny doit encore être essayée sur l'ordinateur de l'apprenante. |
| Six schémas originaux et texte | **VALIDÉ** | Six SVG valides, convertis et inspectés ; descriptions dans les modules. |
| Script reproductible et états honnêtes | **VALIDÉ** | `tools/valider_formation.py`, 44 contrôles ; limites `NON_TESTÉ` détaillées dans les résultats. |
| Manifeste exact | **VALIDÉ** | 129 chemins, tailles et SHA-256 pour 130 fichiers, lui-même exclu. |
| Publicabilité et droits | **VALIDÉ** pour les fichiers présents | Recherche d'adresses et d'éléments sensibles ; aucun ZIP source ni support brut. Les archives originales ne sont pas réauditées ici. |

## Choix non retenus

| Idée | Décision et motif |
|---|---|
| Vidéos françaises supplémentaires | **NON RETENU** : aucune page, durée et lecture n'ont été revérifiées pour cette passe ; ne pas ajouter de liens supposés valides. Les ressources antérieures restent accompagnées de leurs limites. |
| HTML/PDF de tous les cours | **NON RETENU** : le Markdown et le guide complet synchronisé couvrent le besoin immédiat ; un export supplémentaire exigerait une vérification visuelle complète. |
| PHP, JavaScript obligatoire, UML exhaustif, cloud, supports bruts | **NON RETENU** : hors du tronc commun ou sans droit de redistribution établi. |

## Résultats et limites

Les résultats exécutés et les états `VALIDÉ`, `ÉCHEC` et `NON_TESTÉ` sont consignés dans [RESULTATS_TESTS.md](08_CONTROLES/RESULTATS_TESTS.md). Les exemples exécutables ont été lancés sur des copies temporaires ; les fichiers et identités d'exemple sont fictifs. Le rendu des pages Web locales et la lecture complète des vidéos restent à vérifier manuellement par l'apprenante. Le ZIP mis à jour est un artefact de distribution externe au dépôt Git : les sources brutes n'y figurent pas.

Au dernier passage : **44 contrôles VALIDÉ, 0 ÉCHEC**, 129 lignes dans le manifeste pour 130 fichiers partagés (manifeste inclus). L'archive `FORMATION_INFORMATIQUE_DEBUTANTE_18_SEMAINES_CORRIGEE.zip` a été rouverte : `testzip()` sans erreur, mêmes 130 chemins, tailles et empreintes SHA-256 de chaque fichier hors manifeste conformes. Le SHA-256 de l'archive dépend des métadonnées ZIP et peut changer lors d'une régénération, même si son contenu est identique.
