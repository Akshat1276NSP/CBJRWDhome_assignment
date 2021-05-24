import random

def game(comp, b):
    if comp == "s":
        if b == "w":
            print("SORRY, U LOSE")
        elif b == "g":
            print("YAY! YOU WIN")
        elif b == "s":
            print("OH! IT IS A TIE")

    elif comp == "w":
        if b == "w":
            print("OH! IT IS A TIE")
        elif b == "g":
            print("SORRY, U LOSE")
        elif b == "s":
            print("YAY! YOU WIN")

    elif comp == "g":
        if b == "w":
            print("YAY! YOU WIN")
        elif b == "g":
            print("OH! IT IS A TIE")
        elif b == "s":
            print("SORRY, U LOSE")


print("computer turn :  Snake(s) Water(w) Gun(g)")

randNo = random.randint(1, 3)

if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"


b = input("player's turn :  Snake(s) Water(w) Gun(g)")

game(comp, b)
