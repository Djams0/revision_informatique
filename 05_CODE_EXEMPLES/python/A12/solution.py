prix = int(input("Prix ? "))
paiement = int(input("Paiement ? "))
if paiement < prix:
    print("insuffisant")
else:
    print(paiement - prix)
