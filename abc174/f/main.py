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

# 0-indexed BIT
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


def main():
    N, Q = LI()
    C = LI()
    lr = sorted(enumerate(LIR(Q)), key=lambda x: x[1][1])
    rightmostIndex = [-1]*(N+1)
    tree = BIT([0]*N)
    left, right = 0, 0
    ans = [None] * Q

    for i, (l, r) in lr:
        while right < r:
            if rightmostIndex[C[right]] < 0:
                rightmostIndex[C[right]] = right
            else:
                tree.add(rightmostIndex[C[right]], -1)
                rightmostIndex[C[right]] = right
            tree.add(right, 1)
            right += 1

        ans[i] = tree.get(l-1, r)


    print(*ans, sep="\n")


if __name__ == '__main__':
    main()