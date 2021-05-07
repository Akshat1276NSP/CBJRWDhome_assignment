a = input("ENTER THE PHRASE AND I WILL TELL YOU WHETHER IT IS A SPAM OR NOT:  ")

spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

if (a == spam1) or (a == spam1.capitalize()) or (a == spam1.upper()) or (a == spam2) or (a == spam2.capitalize()) or (a == spam2.upper()) or (a == spam3) or (a == spam3.capitalize()) or (a == spam3.upper()) or (a == spam4) or (a == spam4.capitalize()) or (a == spam4.upper()):
    print("YES...IT IS A SPAM")
else:
    print("HAVE FUN....IT ISN'T A SPAM..")
