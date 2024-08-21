def elliptic_curve_multiplication(k, P):
    Q = None
    for i in range(k.bit_length()):
        if k & (1 << i):
            Q = point_addition(Q, P)
        P = point_doubling(P)
    return Q

def point_addition(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    if P[0] == Q[0] and P[1] == -Q[1]:
        return None
    if P[0] == Q[0]:
        m = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p)
    else:
        m = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p)
    x = (m * m - P[0] - Q[0]) % p
    y = (m * (P[0] - x) - P[1]) % p
    return (x, y)

def point_doubling(P):
    if P is None:
        return None
    try:
        m = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p)
    except ValueError:
        return None
    x = (m * m - 2 * P[0]) % p
    y = (m * (P[0] - x) - P[1]) % p
    return (x, y)

# Constants for the elliptic curve
a = -1
b = 0
p = 5

# Point on the elliptic curve
P = (2, 1)

# Constant to multiply the point by
k = 1

while (elliptic_curve_multiplication(k, P) != (2,4)):
    k += 1
print(k)