b = set()
print(type(b))

# adding values to set
b.add(4)
b.add(1)
b.add(1)
b.add(5)
b.add(5) #WON'T BE ADDED AS SET CONSISTS OF NON-REPEATITIVE ELEMENTS
b.add(5)
b.add([2, 3, 4]) # ERROR DISPLAYED AS LIST CANNOT BE ADDED
b.add((2, 3, 4)) # NO ERROR AD TUPLE CAN BE ADDED TO A SET
b.add({2:3}) # ERROR DISPLAYED AS DIICTIONARY CANNOT BE ADDED

print(len(b)) #Prints the length of this set

b.remove(5) #Removes 5 from the set
b.remove(15) #error showed as 15 is not in the set

print(b.pop()) #REMOVES ANY ONE ELEMENT FROM THE WHOLE SET

set.clear # EMPTIES THE WHOLE SET
print(b)

print(b.union({4, 2, 11})) #RETURN A NEW SET WHICH CONTAINS VALUES FROM BOTH THE SETS

print(b.intersection({4, 2, 11})) #RETURNS A NEW SET WHICH CONTAINS ONLY THE COMMON ITEMS IN BOTH THE SETS
