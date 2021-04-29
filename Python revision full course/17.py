myDict = {
    "Fast" : "in a quick manner",
    "Harry" : "Name of a sub human",
    "Marks" : [1, 2, 3, 4, 5],
    "bobby" : {"momo":"A tasty delicacy", "bubble":"a transparent material"}
}

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
myDict['Marks'] = [45, 67, 78]
print(myDict['bobby']['momo'])
print(myDict['bobby']['bubble'])
