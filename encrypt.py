from mappings import char_to_int_a0 as char_to_int
from mappings import int_to_char_a0  as int_to_char

message = "MYFEETAARECHEESY"
hills = [[5, 8], [17, 3]]

toFile = ""
for i in range(0,len(message),2):
    cipher_digraph = (char_to_int[message[i]], char_to_int[message[i+1]])
    a = hills[0][0]*cipher_digraph[0] + hills[0][1]*cipher_digraph[1]
    b = hills[1][0]*cipher_digraph[0] + hills[1][1]*cipher_digraph[1]
    decrypted_digraph = [a,b]
    toFile += f"{int_to_char[a%26]}{int_to_char[b%26]}"
with open("hill_system.txt", "w") as file:
    file.write(toFile)
    file.write("\n" + message)
print(f"Results written to hill_system.txt.")