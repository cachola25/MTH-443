def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

elem = [i for i in range(0,28)]
units = []

for i in elem:
    if gcd(i, 28) == 1:
        units.append(i)
print(units)
print(len(units))
        