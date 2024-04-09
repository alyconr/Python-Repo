import random


def rockscissorspaper():
    print("piedra, papel, tijera")
    print("Enter piedra, papel, tijera, or salir")

    while True:
        user = input()
        if user == "salir":
            break
        computer = random.choice(["piedra", "papel", "tijera"])
        if user == computer:
            print("Empate")            
        elif user == "piedra":
            if computer == "tijera":
                print("User Gana")
                break
            else:
                print("PC Gana")
                break

        elif user == "tijera":
            if computer == "piedra":
                print("Pc Gana")
                break
            else:
                print("Usuario gana")
                break
        elif user == "paper":
            if computer == "piedra":
                print("Usuario gana")
                break
            else:
                print("Computer wins")
                break
        else:
            print("Opcion Invalida")
        print("Pc escogio", computer)
       


rockscissorspaper()
