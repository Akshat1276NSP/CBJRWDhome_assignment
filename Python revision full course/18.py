myDict = {
    "Fast" : "in a quick manner",
    "Harry" : "Name of a sub human",
    "Marks" : [1, 2, 3, 4, 5],
    "bobby" : {"momo":"A tasty delicacy", "bubble":"a transparent material"},
    "lolo" : "lol + o"
}
print(type(myDict.keys()))

print(list(myDict.values()))

print(type(list(myDict)))

print(myDict.items()) #print the key,values for all contents of dictionary

updatedictionary = {
    "lombardy":"french fries",
    "lombar":"french fries",
    "lom":"french fries",
    "lombardy":"bomb booom"
}
print(myDict.update(updatedictionary))
print(myDict)

#the difference between .get and [] syntax in dictionary
print(myDict.get("harry2")) #Returns none as harry2 is not present in the dictionary
print(myDict["harry2"]) #throws an error as harry2 is not present in dictionary
# Therefore it doesn't exit from the code by howing error so it is preferable to use .get instead pf print
