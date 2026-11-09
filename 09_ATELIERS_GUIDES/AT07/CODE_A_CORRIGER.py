def compter_notes_valides(notes):
    total = 0
    for note in notes:
        if note > 10:  # BUG : la consigne inclut 10
            total += 1
    return total

print(compter_notes_valides([9, 10, 12]))
