
base = 5
arr = [i for i in range(0,base)]

for i in arr:
    print(f"f({i}) = {((i**3) - i) % base}")