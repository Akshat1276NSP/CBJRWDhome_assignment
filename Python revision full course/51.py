a = int(input("ENTER THE REQUIRED NUMBER FOR MULTIPLICATION TABLE:  "))
b = []

for x in range(1, 11):
    c = x*a
    b.append(c)
print(b[::-1])
