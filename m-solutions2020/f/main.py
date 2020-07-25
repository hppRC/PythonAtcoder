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

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = I()
    XYU = LR(N)
    d1 = {"U":set(), "R":set(), "D":set(), "L":set()}
    d2 = {"U":set(), "R":set(), "D":set(), "L":set()}
    d3 = {"U":set(), "R":set(), "D":set(), "L":set()}
    d4 = {"U":set(), "R":set(), "D":set(), "L":set()}

    ans = MOD

    for x, y, u in XYU:
        x = int(x)
        y = int(y)
        if u == "R" or u == "L":
            v = True
        else:
            v = False

        if v:
            if y - x in d1[u]:
                ans = min(abs(y - x), ans)
            else:
                d1[u].add(y - x)
                d1[u].add(-y + x)

            if x + y in d1[u]:
                ans = min(abs(x + y), ans)
            else:
                d2[u].add(x + y)
                d2[u].add(-(x + y))

    print(ans * 10)

if __name__ == '__main__':
    main()