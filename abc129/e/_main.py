#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

sys.setrecursionlimit(1000000)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

class ModInt:
    def __init__(self, x, MOD=1000000007):
        self.x = x % MOD
        self.MOD = MOD
    def __str__(self): return str(self.x)
    def __add__(self, other): return ModInt(self.x + other.x) if isinstance(other, ModInt) else ModInt(self.x + other)
    def __sub__(self, other): return ModInt(self.x - other.x) if isinstance(other, ModInt) else ModInt(self.x - other)
    def __mul__(self, other): return ModInt(self.x * other.x) if isinstance(other, ModInt) else ModInt(self.x * other)
    def __truediv__(self, other): return ModInt(self.x * other.inverse()) if isinstance(other, ModInt) else ModInt(self.x * pow(other, self.MOD - 2, self.MOD))
    def __pow__(self, other): return ModInt(pow(self.x, other.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(self.x, other, self.MOD))
    def __rsub__(self, other): return ModInt(other.x - self.x) if isinstance(other, ModInt) else ModInt(other - self.x)
    def __rtruediv__(self, other): return ModInt(other.x * other.inverse()) if isinstance(other, ModInt) else ModInt(other * pow(self.x, self.MOD - 2, self.MOD))
    def __rpow__(self, other): return ModInt(pow(other.x, self.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(other, self.x, self.MOD))

    __repr__ = __str__
    __radd__ = __add__
    __rmul__ = __mul__

    def inverse(self): return pow(self.x, self.MOD - 2, self.MOD)

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    L = S()

    ans = ModInt(0, MOD)
    bit_count = 0

    for i, bit in enumerate(L):
        if bit == '0':
            continue

        d = len(L) - (i + 1)
        ans += pow(2, bit_count, MOD) * pow(3, d, MOD)

        bit_count += 1


    ans += pow(2, bit_count, MOD)

    print(ans)


if __name__ == '__main__':
    main()