# Initialize a 6x6 2D array
array_2d = [[0 for _ in range(6)] for _ in range(6)]

for i in range(0, 6):
    for j in range(0, 6):
        array_2d[i][j] = (i * j) % 6

for i in range(0, 6):
    print(array_2d[i][0:7])