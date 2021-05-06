a = int(input("ENTER YOUR AGE:  "))
b = 18 - a

if a >= 18:
    print("Yes sir, You are eligible for driving in India")
elif a < 18 and a >= 16:
    print("Sorry, u are not eligigble to drive in India but you can drive in the United States Of America")
elif a < 16:
    print("you will have to study and wait for about", 18-b, "Years before sitting in front of the wheel")
else:
    print("YOU GOTTA BE KIDDING ME")

