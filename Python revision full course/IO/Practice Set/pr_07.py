content = True
i = 1
with open("log.txt") as f:
    
    while content:        
        content = f.readline()

        if "python" in content.lower():
            print(content)
            print("PYTHON IS PRESENT")
            print(f"YES, PYTHON IS PRESENT IN LINE {i}")
        i += 1
