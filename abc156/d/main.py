#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

def lcm(a, b): return a * b // math.gcd(a, b)
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a%b)
        y -= (a/b)*x
        return d, x, y
    else:
        return a, 1, 0


sys.setrecursionlimit(1000000)
MOD = 1000000007



def main():
    n, a, b = LI()

    a1, a2 = 1, 1
    for i in range(1, a+1):
        a1 = a1 * (n - i + 1) % MOD
        a2 = a2 * i % MOD
    b1, b2 = 1, 1
    for i in range(1, b+1):
        b1 = b1 * (n - i + 1) % MOD
        b2 = b2 * i % MOD
    nca = a1 * pow(a2, MOD-2, MOD) % MOD
    ncb = b1 * pow(b2, MOD-2, MOD) % MOD

    print((pow(2, n, MOD) - 1 - nca - ncb) % MOD)

main()
