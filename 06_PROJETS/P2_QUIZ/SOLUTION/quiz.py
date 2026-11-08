def jouer(questions):
    score = 0
    for texte, bonne_reponse in questions:
        reponse = input(texte + " (a/b) ? ").strip().lower()
        if reponse == bonne_reponse:
            print("Correct.")
            score += 1
        else:
            print("Réponse attendue :", bonne_reponse)
    return score

questions = [
    ("1. 2 + 2 = a:4 ou b:5", "a"),
    ("2. HTML structure a:non ou b:oui", "b"),
    ("3. Une liste Python commence à l'indice a:0 ou b:1", "a"),
]
score = jouer(questions)
print("Score :", score, "/", len(questions))
