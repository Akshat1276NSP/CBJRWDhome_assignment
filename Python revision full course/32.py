a = int(input("ENTER UR MARKS AND RECEIVE YOUR GRADE:  "))

if 90 < a <= 100:
    print("A")
elif 80 < a <= 90:
    print("B")
elif 70 < a <= 80:
    print("C")
elif 60 < a <= 70:
    print("D")
elif 50 < a <= 60:
    print("E")
elif 0 <= a < 50:
    print("F")
else:
    print("Please enter correct marks")
