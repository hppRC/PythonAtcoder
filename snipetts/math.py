import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a / b) * x
        return d, x, y
    else:
        return a, 1, 0