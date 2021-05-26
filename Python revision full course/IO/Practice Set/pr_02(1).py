def game():
    return 446

score = game()
with open("hiscore.txt") as f:
    hiscoreSTR = int(f.read())

if hiscoreSTR == '':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiscoreSTR) < score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
