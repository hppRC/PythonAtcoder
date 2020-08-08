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


@lru_cache(maxsize=1024*1024)
def fact(n): return math.factorial(n)

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return fact(n) // (fact(r) * fact(n-r))

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007
INF = float("inf")


class FactInv:
    def __init__(self, N, MOD=1000000007):
        fact, inv = [1]*(N+1), [None]*(N+1)
        for i in range(1, N+1): fact[i] = fact[i - 1] * i % MOD
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N)[::-1]: inv[i] = inv[i + 1] * (i + 1) % MOD
        self.N, self.MOD, self.fact, self.inv = N, MOD, fact, inv

    def perm(self, a, b):
        if a > self.N or b > self.N: raise ValueError("\nPermutaion arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[a-b] % self.MOD

    def comb(self, a, b):
        if a > self.N or b > self.N: raise ValueError("\nCombination arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[b] * self.inv[a-b] % self.MOD



def main():
    N, K = LI()
    A = sorted(LI())
    factinv = FactInv(N + 1)

    ans = 0
    for i, x in enumerate(A):
        maxc = factinv.comb(i, K - 1) if i >= K - 1 else 0
        minc = factinv.comb(len(A) - i - 1, K - 1) if len(A) - i - 1 >= K - 1 else 0
        ans = (ans + x * (maxc - minc)) % MOD

    print(ans % MOD)

if __name__ == '__main__':
    main()