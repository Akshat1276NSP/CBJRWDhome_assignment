# n! = 1*2*3*4.....n
# n! = 1*2*3*4...*(n-1)*n
# n! = (n-1)! * n

def factorial_iter(n):
    product = 1
    for i in range(n):
        product *= (i+1)
    print(product)
factorial_iter(6)


def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(5))
