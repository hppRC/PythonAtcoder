import math
from collections import defaultdict

def lcm(a, b):
    return a * b // math.gcd(a, b)

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a / b) * x
        return d, x, y
    else:
        return a, 1, 0

def factors(n):
    d = defaultdict(int)
    a = 2
    while n >= a ** 2:
        if n % a == 0:
            n //= a
            d[a] += 1
        else:
            a += 1
    d[n] += 1
    return d

def divisors(N):
    divs = set([1, N])
    i = 2
    while i ** 2 <= N:
        if N % i == 0:
            divs.add(i)
            divs.add(N//i)
        i += 1
    return sorted(list(divs))

# Σ_{i=0}^{N−1} floor((A×i+B)/M)
def floor_sum(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            res += n * (b // m)
            b %= m
        y_max = (a * n + b) // m
        if y_max == 0: break
        x_max = b - y_max * m
        res += (n + x_max // a) * y_max
        n, m, a, b = y_max, a, m, x_max % a
    return res