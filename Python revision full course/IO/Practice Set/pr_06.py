with open("log.txt") as f:
    content = f.read()

if "python" in content.lower():
    print("PYTHON IS PRESENT")
else:
    print("PYTHON IS ABSENT")
