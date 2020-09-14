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

# reffer to: https://qiita.com/dn6049949/items/afa12d5d079f518de368
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.data = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    # example:
    # tree = SegmentTree(N, f=max, default=-1).initialize(A)
    def initialize(self, A):
        for i, ai in enumerate(A): self.update(i, ai)
        return self

    def update(self, i, x):
        i += self.size
        self.data[i] = x
        while i > 0:
            i >>= 1
            self.data[i] = self.f(self.data[i*2], self.data[i*2+1])

    # [l, r)
    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                rres = self.f(self.data[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

    # You can use lower_bound only if f == max.
    # return min({i | x <= i and v <= a[i]}, self.num_leaf)
    def lower_bound(self, x, v):
        x += self.size
        while self.data[x] < v:
            if x & 1: # x % 2 == 1
                if len(bin(x)) == len(bin(x+1)):
                    x += 1
                else:
                    return self.size
            else:
                x >>= 1
        while x < self.size:
            if self.data[2*x] >= v:
                x = 2*x
            else:
                x = 2*x + 1
        return x - self.size


def main():
    N, Q = LI()
    A = LI()
    query = LIR(Q)
    tree = SegmentTree(N, f=max, default=-1).initialize(A)

    for t, a, b in query:
        if t == 1:
            tree.update(a-1, b)
        elif t == 2:
            print(tree.query(a-1, b))
        else:
            print(min(tree.lower_bound(a-1, b), N) + 1)



if __name__ == '__main__':
    main()