prix = int(input("Prix ? "))
paiement = int(input("Paiement ? "))
if paiement < prix:
    print("Insuffisant")
else:
    monnaie = paiement - prix
    print(monnaie)
