with open("poems.txt") as f:
    content = f.read()

content = content.replace("donkey", "&^%#$@")

with open("poems.txt", "w") as f:
    f.write(content)
