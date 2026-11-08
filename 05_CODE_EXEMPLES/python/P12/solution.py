secret = 7
while True:
    proposition = int(input("Proposition ? "))
    if proposition == secret:
        print("trouvé")
        break
    if proposition < secret:
        print("trop petit")
    else:
        print("trop grand")
