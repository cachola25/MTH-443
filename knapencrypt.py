# Dictionary that maps a->0, b->1, ...,
from mappings import char_to_int_a0 as c2i

# SIC array
arr = [24038,29756,34172,34286,38334,1824,18255,19723,143,17146,35366,11204,32395,12958,6479]

message = "hello world!".upper()

# Convert the message to its binary representation
# The length depends on the alphabet so since we have 32 characters, we need 5 bits
pt = [bin(c2i[x])[2:].zfill(5) for x in message if x not in ["\n", "\t"]]

# For problem #4, we need to encrypt in groups of 3
count = 0
num_of_chunks = int(input("Enter the number of chunks: "))
while num_of_chunks <= 0:
    num_of_chunks = int(input("Enter the number of chunks: "))
    
# Concatenation of three characters
total = ""
for letter in pt:
    # Print the sum of the products of the SIC array and the binary representation of the message
    if count % num_of_chunks == 0 and count != 0:
        products = [arr[i] for i in range(len(total)) if total[i] == "1"]
        print(sum(products), end=" ")
        total = ""
    count += 1
    total += letter

# Make sure all characters are encrypted
if total != "":
    products = [arr[i] for i in range(len(total)) if total[i] == "1"]
    print(sum(products), end=" ")
print()
