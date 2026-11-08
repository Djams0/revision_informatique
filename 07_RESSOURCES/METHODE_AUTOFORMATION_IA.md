# Apprendre seule et utiliser une IA sans perdre la main

## Routine pour chaque exercice (20 à 40 minutes)

1. Lire la consigne et écrire à la main un exemple d'entrée et de sortie. Reformuler l'objectif en une phrase.
2. Essayer seule 10 minutes : pseudo-code ou quelques lignes Python, même incomplètes. Noter le blocage exact.
3. Consulter l'indice de l'exercice. Si besoin, demander **un indice ciblé** à une IA, sans solution complète.
4. Tester un cas normal, puis un cas limite. Lire la première ligne utile du message d'erreur et la ligne signalée. Changer une chose à la fois.
5. Comparer seulement ensuite avec le corrigé séparé. Expliquer pourquoi chaque condition ou boucle est là ; refaire sans regarder.
6. Un jour plus tard, résoudre une petite variante avec des valeurs et noms différents. Enregistrer ce que l'on sait faire dans le tableau de suivi.

Une réponse de l'IA est une hypothèse : **exécuter, vérifier contre la consigne et comparer au cours**. Elle peut proposer une syntaxe erronée, une dépendance absente ou une complexité excessive. Si elle introduit des classes, un framework ou une API pour un exercice de base, demander une solution plus simple avec les notions déjà vues.

## Huit formulations utiles

1. « Je suis en semaine 5. Reformule cet exercice en étapes sans écrire l'algorithme complet. Voici ma consigne : [texte]. »
2. « Mon pseudo-code donne [sortie] pour [entrée] ; j'attends [résultat]. Pose-moi deux questions pour trouver mon erreur sans donner la réponse. »
3. « Explique ce message d'erreur Python avec des mots de débutante, montre comment localiser la ligne, puis donne une seule piste : [erreur expurgée]. »
4. « Trace ces cinq lignes de Python sous forme de tableau : ligne, valeur de `x`, sortie. N'ajoute pas de nouveau concept : [petit code fictif]. »
5. « Propose trois tests utiles, dont un cas limite, pour cette fonction. N'écris pas la fonction : [objectif]. »
6. « Compare mon pseudo-code et ma traduction Python ; indique uniquement la première différence de logique : [deux petits extraits]. »
7. « Je viens de finir. Pose-moi trois questions ouvertes sur les conditions et les boucles, puis corrige mes réponses une par une. »
8. « Donne-moi une variante du même niveau à réaliser sans aide, avec un résultat attendu pour vérifier mon travail : [notion]. »

## Quand une réponse semble juste

- Vérifier que le résultat attendu concorde sur au moins deux exemples et un cas limite.
- Contrôler les noms exacts et la syntaxe dans la documentation de Python, MDN ou SQLite si la réponse prétend qu'une règle existe.
- Demander « pourquoi ? » puis expliquer à voix haute sans recopier le texte ; un résultat correct sans compréhension n'est pas acquis.
- Pour un site, ouvrir localement la page, tester les liens et l'affichage sur écran étroit.

## Ce qu'il faut préserver

Remplacer noms, e-mails, mots de passe, chemins personnels, données de travail et copies d'écran privées par des exemples inventés avant de coller une question. Ne jamais transmettre un fichier `.env`, une clé, une sauvegarde privée ni une archive de cours à un assistant en ligne pour un simple débogage. Les travaux de cours originaux peuvent avoir des droits de diffusion ; utiliser les énoncés réécrits de ce dossier.

## Si l'on bloque plus longtemps

Revenir à l'exemple du cours du module, exécuter une version de trois lignes, puis ajouter une seule étape. Repérer exactement la première entrée qui échoue. Un projet peut être terminé en plusieurs séances ; noter l'étape suivante dans `SUIVI_18_SEMAINES.csv` et reprendre plus tard.
