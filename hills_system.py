from mappings import char_to_int_a0 as char_to_int
from mappings import int_to_char_a0  as int_to_char

def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


ints_mod_26 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
units = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

coeff1 = 6
coeff2 = 22

for a in ints_mod_26:
    for b in ints_mod_26:
        if (coeff1 * a) + (coeff2 * b) % 26 == 4:
            print(f"a: {a}, b: {b}")
coeff1 = 9
coeff2 = 24
for a in ints_mod_26:
    for b in ints_mod_26:
        if (coeff1 * a) + (coeff2 * b) % 26 == 4:
            print(f"a: {a}, b: {b}")
a = 0
b = 1
c_d = []
for c in ints_mod_26:
    for d in ints_mod_26:
        if (14 * c + 19 * d) % 26 == 7:
            c_d.append((c,d))
            
result = []
for c,d in c_d:
    if (a*d - b*c) % 26 in units:
        result.append([a,b,c,d])
            

# Check if each res in result is what decrypts the message
# message = "OHT XAE CUO HEI PGX TIQ HOF YZS TLV CTM JOF AZQ DQD RBF KSY AFA LCX BKK IBA YVC WPP WVP ZHT XWO KSH MZQ CPX TIG TML DTX AEL EBJ VGZ MFY ERX IXA CUQ FMQ ZQC PXY TKW LKK BFT UUM EQO HLT MSF AVI XLR VTB HHT KNN XAH UOL VGG IGH DHP WTK KSN NHV PWQ HPW XLA YJQ PRT LRR YCO HRR OHK SVC CUO ZMQ ZCV CQF ZDB F"
# message = "KFH YYG IGM CEJ SST EBO EUG RWJ TSD VYK ZOZ LIZ KFH XKU UIC WXF WJG AXQ PBQ AGV GXD VDG UEV GMI GYK QQP IPS CLL FYP MUL KFH XPM HGM EVD KAV YQC EGU EAL YYY ZSZ MPX ZOC TXT RIM DID VDG SXO ZFF TSM EDV MEI MDV MPK OUJ KOD UBO AXB OOR SLP ZCW IMD VYG JWM IFQ"
# message="VEA RGW MCN NDA KZM CEK YVH ZVE ARC GNN MMZ DJG CEJ BVE WSN NMM PRI COL JZG FZX JBR TCP ORP AMY YSC NSU RKW BVE QAP XVW PJL UUU AS"
message = "OTG WRV RHU GXO XUQ UEK VYO TSE NYU NSI YSH MHB BUR ZTR CCD DAK MHC ALI OJZ UOT JYC KFN KIO THO GWK Z"
message = message.replace(" ", "")

toFile = ""
for res in result:
    toFile += f"Key: {res}\n"
    for i in range(0,len(message),2):
        cipher_digraph = (char_to_int[message[i]], char_to_int[message[i+1]])
        a = res[0]*cipher_digraph[0] + res[1]*cipher_digraph[1]
        b = res[2]*cipher_digraph[0] + res[3]*cipher_digraph[1]
        decrypted_digraph = [a,b]
        toFile += f"{int_to_char[a%26]}{int_to_char[b%26]}"
    toFile += "\n\n\n"
with open("hill_system.txt", "w") as file:
    file.write(toFile)
print(f"Results written to hill_system.txt. {len(result)} results found.")


            
