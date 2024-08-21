
from math import sqrt


def factorial(n):
    if n == 0:
        return 1

    ret = 1
    while n > 0:
        ret *= n
        n -= 1
    return ret
def permutation(n,r):
    return factorial(n) // factorial(n-r)

def combination(n,r):
    return permutation(n,r) // factorial(r)

if __name__ == "__main__":
    
    product = (2**5) * (3**5) * (5**2)
    print(f"Product: {product}")

    # Find factors of product
    factors = []
    for i in range(1, product+1):
        if product % i == 0:
            factors.append(i)
    print(f"Factors: {factors}")
    
    squares = []
    for factor in factors:
        if sqrt(factor) == int(sqrt(factor)):
            print(f"Factor: {factor} is a perfect square.")
            squares.append(factor)
    print("Squares: ", len(squares))