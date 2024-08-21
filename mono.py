
def additive_cipher(plaintext,key):
    if (plaintext + key) % 26 == 0:
        return 26
    return (plaintext + key) % 26

def multiplicative_cipher(plaintext,key):
    if (plaintext * key) % 26 == 0:
        return 26
    return (plaintext * key) % 26

def affine_cipher(plaintext,key1,key2):
    if (plaintext * key1 + key2) % 26 == 0:
        return 26
    return (plaintext * key1 + key2) % 26

def additive_cipher_inverse(ciphertext,key):
    if (ciphertext - key) % 26 == 0:
        return 26
    return (ciphertext - key) % 26

def multiplicative_cipher_inverse(ciphertext,key):
    return (ciphertext * 23) % 26

def affine_cipher_inverse(ciphertext,key2):
    return ((ciphertext - key2) * 23) % 26
conversion_table_char_to_int = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26 
}

conversion_table_int_to_char = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
    
}

# plaintext = "PLS GIVE ME A ONE HUNDRED I TRYING HARD "  
# plaintext = plaintext.replace(" ", "")
# for c in plaintext:
#     if c == " ":
#         print(" ", end = "")
#     else:
#         print(c, end = " ")
# print()
# plain = []
# for c in plaintext:
#     if c == " ":
#         print(" ", end = "")
#     else:
#         arg = conversion_table_char_to_int[c]
#         print(arg, end = " ")
#         plain.append(affine_cipher(arg, 17,2))
# print()
# for num in plain:
#     print(num, end = " ")
# print()
# i = 0 
# for num in plain:
#     print(conversion_table_int_to_char[num], end = " ")
#     i+=1
#     if i % 3 == 0:
#         print()
        
# print()
# i = 0

# for num in plain:
#     print(conversion_table_int_to_char[affine_cipher_inverse(num, 2)], end = " ")
#     i+=1
#     if i % 3 == 0:
#         print()
# print()