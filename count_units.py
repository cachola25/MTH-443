from mappings import char_to_int_a0 as c2i
from mappings import int_to_char_a0 as i2c
int_mod_26 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def additive_encrypt(message, b):
    if b == 0:
        return "no change"
    message = message.replace(" ", "")
    ret = ""
    for i in range(len(message)):
        ret += i2c[(c2i[message[i]] + b) % 26]
    print(ret)
    return ret
def multiplicative_encrypt(message, a):
    if a == 1:
        return "no chang"
    message = message.replace(" ", "")
    ret = ""
    for i in range(len(message)):
        ret += i2c[(c2i[message[i]] * a) % 26]
    print(ret)
    return ret
message = "MYFEETAARECHEESY"

for i in int_mod_26:
    for j in int_mod_26:
        if additive_encrypt(message,i) == multiplicative_encrypt(message, j):
            print(i, j)
            exit()
        
print("No solution found")

