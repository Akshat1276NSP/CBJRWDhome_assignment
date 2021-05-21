def greatest(a, b, c):
    if a > b or a > c:
        print("THE GREATEST VALUE IS", a)
    elif b > c or b > a:
        print("THE GREATEST VALUE IS", b)
    else:
        print("THE GREATEST VALUE IS", c)

greatest(18,15,16)
