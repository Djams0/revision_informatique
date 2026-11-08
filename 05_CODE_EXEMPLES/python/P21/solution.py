def prix_apres_remise(prix, remise):
    final = prix - remise
    return final

prix = int(input("Prix ? "))
remise = int(input("Remise ? "))
resultat = prix_apres_remise(prix, remise)
print(resultat)
