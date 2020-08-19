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

class LazySegmentTree:
    # N: 処理する区間の長さ
    # 0-indexed, if N == 10 => [0 ~ 9]
    # min version
    # seg = LazySegmentTree(N, f=min, default=float("inf"))
    def __init__(self, N, f=lambda x,y: x+y, default=0):
        self.N = N
        self.default = default
        self.f = f

        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [self.default]*(2*self.N0)
        self.lazy = [None]*(2*self.N0)

    # 伝搬対象の区間を求める
    def gindex(self, l, r):
        L = (l + self.N0) >> 1
        R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i: yield R
            if L < R and lc <= i: yield L
            L >>= 1
            R >>= 1

    # 遅延伝搬処理
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None: continue
            self.lazy[2*i-1] = self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None

    # 区間[l, r)をxで更新
    def update(self, x, l, r=None):
        if r is None: r = l + 1

        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L, R = self.N0 + l, self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.f(self.data[2*i-1], self.data[2*i])

    # 区間演算: [l, r)にxでfを作用させる
    def affect(self, x, l, r=None):
        if r is None: r = l + 1

        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L, R = self.N0 + l, self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.f(self.data[R-1], x)
                self.data[R-1] = self.f(self.data[R-1], x)
            if L & 1:
                self.lazy[L-1] = self.f(self.data[L-1], x)
                self.data[L-1] = self.f(self.data[L-1], x)
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.f(self.data[2*i-1], self.data[2*i])

    # 区間[l, r)内の最小値を求める
    def query(self, l, r=None):
        if r is None: r = l + 1
        self.propagates(*self.gindex(l, r))
        L, R = self.N0 + l, self.N0 + r

        s = self.default
        while L < R:
            if R & 1:
                R -= 1
                s = self.f(s, self.data[R-1])
            if L & 1:
                s = self.f(s, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

def main():
    N = 10

    seg = LazySegmentTree(N)
    seg.update(5, 0, 10)
    seg.affect(5, 0, 5)
    seg.affect(50, 0, 5)
    seg.affect(100, 6)
    seg.update(0, 2, 4)
    seg.affect(1, 0, 2)

    for i in range(N):
        print(seg.query(i), end=" ")
    print()

    print(seg.query(0, 3))
    print(seg.query(0, 6))
    print(seg.query(0, 10))
    print(seg.query(5, 10))

    seg.update(-10, 6)
    seg.affect(-200, 0, 3)

    for i in range(N):
        print(seg.query(i), end=" ")
    print()

    print(seg.query(0, 3))
    print(seg.query(0, 6))
    print(seg.query(0, 10))
    print(seg.query(5, 10))




if __name__ == '__main__':
    main()