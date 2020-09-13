#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools, bisect
import math, fractions
import sys, copy

def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def S(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007


class FactInv:
    def __init__(self, N, MOD=1000000007):
        fact = [1]*(N+1)
        for i in range(1, N+1):
            fact[i] = fact[i - 1] * i % MOD

        inv = [None]*(N+1)
        inv[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N)[::-1]:
            inv[i] = inv[i + 1] * (i + 1) % MOD

        self.N = N
        self.MOD = MOD
        self.fact = fact
        self.inv = inv

    def perm(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nPermutaion arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[a-b] % self.MOD

    def comb(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nCombination arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[b] * self.inv[a-b] % self.MOD


class ModInt:
    def __init__(self, x, MOD=1000000007): self.x, self.MOD = x % MOD, MOD
    def __str__(self): return str(self.x)
    def __add__(self, other): return ModInt(self.x + other.x) if isinstance(other, ModInt) else ModInt(self.x + other)
    def __sub__(self, other): return ModInt(self.x - other.x) if isinstance(other, ModInt) else ModInt(self.x - other)
    def __mul__(self, other): return ModInt(self.x * other.x) if isinstance(other, ModInt) else ModInt(self.x * other)
    def __truediv__(self, other): return ModInt(self.x * other.inverse()) if isinstance(other, ModInt) else ModInt(self.x * pow(other, self.MOD - 2, self.MOD))
    def __pow__(self, other): return ModInt(pow(self.x, other.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(self.x, other, self.MOD))
    def __rsub__(self, other): return ModInt(other.x - self.x) if isinstance(other, ModInt) else ModInt(other - self.x)
    def __rtruediv__(self, other): return ModInt(other.x * other.inverse()) if isinstance(other, ModInt) else ModInt(other * pow(self.x, self.MOD - 2, self.MOD))
    def __rpow__(self, other): return ModInt(pow(other.x, self.x, self.MOD)) if isinstance(other, ModInt) else ModInt(pow(other, self.x, self.MOD))
    __repr__, __radd__, __rmul__ = __str__, __add__, __mul__
    def inverse(self): return pow(self.x, self.MOD - 2, self.MOD)

def main():
    N, M = LI()
    factinv = FactInv(M)
    a = ModInt(factinv.perm(M, N))
    tmp = ModInt(0)

    for k in range(N + 1):
        tmp += factinv.comb(N, k) * factinv.perm(M - k, N - k) * pow(-1, k)

    print(a * tmp)





if __name__ == '__main__':
    main()