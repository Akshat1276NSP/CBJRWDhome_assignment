a = int(input("ENTER THE FIRST NUMBER:  "))
b = int(input("ENTER THE SECOND NUMBER:  "))
oper = str(input("ENTER THE OPERATOR YOU WOULD USE( +, -, *, / ):  "))

def add(a, b):
    print("THE SUM IS ", a+b)
def sub(a, b):
    print("THE DIFFERENCE IS ", a-b)
def mult(a, b):
    print("THE PRODUCT IS ", a*b)
def div(a, b):
    print("THE QUOTIENT IS ", a/b)

if oper == "+":
    add(a, b)
elif oper == "-":
    sub(a,b)
elif oper == "*":
    mult(a,b)
elif oper == "/":
    div(a, b)
elif oper == "div":
    
