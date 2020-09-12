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

class BIT:
    def __init__(self, li):
        self.n, self.data = len(li) + 1, [0] + li
        for i in range(1, self.n):
            if i + (i & -i) < self.n: self.data[i + (i & -i)] += self.data[i]

    def add(self, i, a):
        i += 1
        while i < self.n:
            self.data[i] += a
            i += i & -i

    # sum of [0, i)
    def acc(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    # sum of [l, r)
    def get(self, l, r = None):
        if r is None: r = l+1
        return self.acc(r) - self.acc(l)

class ExBIT:
    def __init__(self, li):
        self.p = Bit(li[:])
        self.q = Bit(li[:])

    # add x to [l, r] (not [l, r)])
    def add(self, x, l, r=None):
        if r is None: r = l
        r += 1
        self.p.add(l, -x * l)
        self.p.add(r, x * r)
        self.q.add(l, x)
        self.q.add(r, -x)

    def sum(self, l, r):
        r += 1
        return self.p.acc(r) + self.q.acc(r) * r - self.p.acc(l) - self.q.acc(l) * l

    def get(self, l, r=None):
        if r is None: r = l
        return self.sum(l, r)

def main():
    N = I()
    N, Q = LI()
    A = LI()
    query = LIR(Q)
    bit = ExBIT(A)

    for a, b, c, d, e in query:
        if a == 0:
            

if __name__ == '__main__':
    main()