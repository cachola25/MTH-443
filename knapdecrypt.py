
# SIC array
arr = [24038,29756,34172,34286,38334,1824,18255,19723,143,17146,35366,11204,32395,12958,6479]


# Ciphertext targets
targets = [152472,116116,68546,165420,168261]
 

# Prime to mod by
base = 47107

# a^-1
b = 30966

# Multiply SIC by b to get the original SIC
for i in range(len(arr)):
    arr[i] = (arr[i] * b) % base
print(arr[::-1])

# Multiply the targets by b to get the actual targets
for i in range(len(targets)):
    targets[i] = (targets[i] * b) % base
print(targets)