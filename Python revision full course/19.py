a = {1, 2, 3, 4, 5, 4, 3, 2, 1, 0}
print(type(a))
print(a) #IT CAN BE OBSERVED THAT THE SECOND PAIR OF THE NUMBERS 4, 3, 2, 1 IS NOT PRINTED AS IT IS A PROPERTY OF SETS TO NOT REPEAT THE VALUES

# REMEMBER...... THE BELOW LINE WILL CREATE A EMPTY dictionary and not an empty set
a = {}
print(type(a))

# AN EMPTY SYNTAX CAN BE CREATED USING THE BELOW SYNTAX
b = set()
print(type(b))
b.add(4)
b.add(6)
