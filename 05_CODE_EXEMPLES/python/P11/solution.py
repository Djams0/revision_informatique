note = int(input("Note 0–20 ? "))
while note < 0 or note > 20:
    note = int(input("Réessaie : "))
print(note)
