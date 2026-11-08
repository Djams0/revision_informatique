age = int(input("Âge fictif ? "))
if age < 0:
    print("âge invalide")
elif age >= 18:
    print("adulte")
else:
    print("mineur")
