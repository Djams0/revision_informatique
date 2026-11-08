prix = int(input("Prix entier ? "))
if prix < 0:
    print("invalide")
elif prix >= 20:
    print(prix - 2)
else:
    print(prix)
