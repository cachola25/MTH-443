units_of_z26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

for x in units_of_z26:
    for y in units_of_z26:
        print(f"{(x * y) % 26}",end=" ")
    print()
