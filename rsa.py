
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return abs(a)
from tqdm import tqdm
def gcd(a, b):
    return (a % 2 == 0) or (a % 101 == 0) or (a % 1289 == 0)
def findValidRsaKeys(n):
    validKeys = []
    for i in range(1, n):
        if not gcd(i, n):
            validKeys.append(i)
    return validKeys

p = 2579
q = 809
n = p * q  # n should be the product of p and q
phi_n = (p - 1) * (q - 1)  # Euler's totient function
factors = [2,101,1289]

sum = 0
for factor in factors:
    sum += phi_n // factor

sub = (phi_n // 202) + (phi_n // 2578) + (phi_n // 130189) + (phi_n // 260378)
m = sum - sub
totalKeys = phi_n - m
print(totalKeys)
keys = findValidRsaKeys(phi_n)
print(len(keys) / phi_n)