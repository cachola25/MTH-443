from mappings import char_to_int_a0 as c2i
from mappings import int_to_char_a0 as i2c
arr = [i for i in range(26)]
units = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

for i in arr:
    if (i * 16) % 26 == 14:
        print(i)
# a = 22
# b = 19
# message = "OTG WRV RHU GXO XUQ UEK VYO TSE NYU NSI YSH MHB BUR ZTR CCD DAK MHC ALI OJZ UOT JYC KFN KIO THO GWK Z"
# message = message.replace(" ", "")
# for i in range(0, len(message), 2):
#     print(f"{message[i]}{message[i+1]}", end=" ")
# print()
# for i in range(0,len(message),2):
#     decrypted = (a * c2i[message[i]] + b * c2i[message[i+1]]) % 26
#     print(f"{i2c[decrypted]}", end=" ")
# print()