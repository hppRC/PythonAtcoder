#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools
import math, fractions
import sys, copy


def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def SL(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)
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
    N, X, M = LI()
    tmp = X
    s = set()
    while True:
        if tmp in s: break
        s.add(tmp)
        tmp = (tmp * tmp) % M

    f = len(s)
    s = set()

    while True:
        if tmp in s: break
        s.add(tmp)
        tmp = (tmp * tmp) % M

    mid = len(s)
    summid = sum(s)
    rest = (N - f + mid) % mid
    cnt = (N - f + mid) // mid

    first = f - mid
    tmp = X
    s = set()
    for _ in range(first):
        s.add(tmp)
        tmp = (tmp * tmp) % M
    first_res = sum(s)

    s = set()
    for _ in range(rest):
        s.add(tmp)
        tmp = (tmp * tmp) % M
    last_res = sum(s)

    print(first_res+ summid*cnt+ last_res)




if __name__ == '__main__':
    main()