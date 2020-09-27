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
def SLR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if args else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

class UnionFind:
    def __init__(self, N): self.N, self.group_count, self.root, self.rank = N, N, [-1] * N, [0] * N
    def __repr__(self): return str(self.all_groups())

    def find(self, x):
        while self.root[x] >= 0: x = self.root[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.rank[x] > self.rank[y]: x, y = y, x
        self.root[y] += self.root[x]
        self.root[x] = y
        if self.rank[x] == self.rank[y]: self.rank[y] += 1
        self.group_count -= 1

    def same(self, x, y): return self.find(x) == self.find(y)
    def count(self, x): return -self.root[self.find(x)]
    def members(self, x): return [i for i in range(self.N) if self.same(x, i)]
    def roots(self): return [i for i, x in enumerate(self.root) if x < 0]
    def all_groups(self):
        d = defaultdict(lambda: [])
        for i in range(self.N): d[self.find(i)].append(i)
        return dict(d)


def main():
    N, M = LI()
    ABCT = sorted(LIR(M), key=lambda x: x[2])

    left, right = 0, pow(10, 7)
    epsilon = pow(10, -6)
    while abs(right - left) > epsilon:
        mid = (right + left) / 2
        cost = 0
        uf = UnionFind(N)
        for a, b, c, t in sorted(ABCT, key=lambda x: x[2] - x[3]*mid):
            if c - t * mid <= 0 or not uf.same(a, b):
                uf.union(a, b)
                cost += c - t * mid
        if cost <= 0: right = mid
        else: left = mid


    print(right)


if __name__ == '__main__':
    main()