num = int(input("ENTER THE NUMBER:  "))
prime = True
for i in range(2, num):
    if num%i == 0:  # "%" tells us the quotient and excludes the rem 
        prime = False
        break
if prime:
    print("THE ENTERED NUMBER IS A PRIME NUMBER..")
else:
    print("THE ENTERED NUMBER IS NOT A PRIME NUMBER..")

