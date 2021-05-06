#conditionals expressions
a = int(input("ENTER THE FIRST NUMBER: "))

if(a<0):
    print("The val is negative")

elif(a>5):
    print("The  number is greater than 5")

elif(a>3):
    print("the number is greater than 3")
#REMEMBER, THE ELIF LADDER IS CASE SENSITIVE I.E. IF MORE THAN ONE STATEMENT IS TRUE THEN THE FIRST STATEMENT WILL BE COONSODERED AS TRUE

else:
    print("The value is lesser than 3")
