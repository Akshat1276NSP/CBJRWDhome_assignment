def remove_and_split(string, word):
    newSTR = string.replace(word, " ")
    print(newSTR.strip())

# this = "      boom      "
# print(this)
# print(this.strip())

remove_and_split("BOOM AND ROLL", "BOOM")
