with open("poems.txt") as f:
    content = f.read()

words = ["donkey", "kaddu", "mote"]

for word in words:
    content = content.replace(word, "&^%#$@")

with open("poems.txt", "w") as f:
    f.write(content)
