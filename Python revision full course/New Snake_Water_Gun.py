import random


def game(comp, b):
    print(f"COMPUTER CHOSE {comp}")
    print(f"YOU CHOSE {b}")

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


randNo1 = random.randint(1, 2)
if randNo1 == 1:
    print("YOU LOST THE TOSS! COMPUTER'S TURN.. ")
elif randNo1 == 2:
    print("YAY! YOU WON THE TOSS")
b = input("YOUR turn [Snake(s) Water(w) Gun(g)] :  ")


randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"


game(comp, b)
