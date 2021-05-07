a = int(input("ENTER UR FIRST MARKS:  "))
b = int(input("ENTER UR SECOND MARKS:  "))
c = int(input("ENTER UR THIRD MARKS:  "))
total_marks = a + b + c

if a > 33 and b > 33 and c > 33 and total_marks > 120:
    print("YAY!! U HAVE PASSED THE EXAM....")
else:
    print("HARD LUCK MAN...U HAVE FAILED...TRY AGAIN LATER...")
