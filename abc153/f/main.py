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
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_table(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007
INF = float("inf")

class Bit:
    def __init__(self, n, default=0):
        self.size = n
        self.tree = [default] * (n + 1)

    # get sum of [0, i]
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i = max(i, 1)
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # get sum of [l, r], or just l
    def get(self, l, r=None):
        if r is None: r = l
        return self.sum(r) - self.sum(l-1)

class ExBIT:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)

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
        return self.p.sum(r) + self.q.sum(r) * r - self.p.sum(l) - self.q.sum(l) * l

    def get(self, l, r=None):
        if r is None: r = l
        return self.sum(l, r)

def main():
    N, D, A = LI()
    XH = sorted(LIR(N), key=lambda x: x[0])
    X = [xi for xi, _ in XH]
    bit = ExBIT(N)

    for i in range(N):
        _, hi = XH[i]
        bit.add(math.ceil(hi / A), i)

    ans = 0

    for i, (xi, hi) in enumerate(XH):
        right = bisect_right(X, xi + 2 * D) - 1
        cnt = bit.get(i)
        if cnt > 0:
            bit.add(-cnt, i, right)
            ans += cnt

    print(ans)



if __name__ == '__main__':
    main()