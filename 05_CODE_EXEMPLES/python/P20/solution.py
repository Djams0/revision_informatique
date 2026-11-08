def compter_reussites(notes):
    total = 0
    for note in notes:
        if note >= 10:
            total += 1
    return total

notes = [8, 10, 14]
print(compter_reussites(notes))
# Test 2 : remplace notes par [].
