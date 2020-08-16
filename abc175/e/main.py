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
def comb(n, r): return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007
INF = float("inf")

def main():
    R, C, K = LI()
    rcv = LIR1(K)

    # dp = make_list(R+1, C+1, 4)
    dp = make_list(C+1, 4)
    table = make_list(R, C)

    for r, c, v in rcv: table[r][c] = v + 1

    for r in range(R):
        newdp = [[max(p), 0, 0, 0] for p in dp]
        for c in range(C):
            for i in range(1, 4)[::-1]:
                newdp[c][i] = max(newdp[c][i], newdp[c][i - 1] + table[r][c])
                newdp[c + 1][i] = max(newdp[c + 1][i], newdp[c][i])
            newdp[c + 1][0] = max(newdp[c + 1][0], newdp[c][0])
        dp = newdp

    print(max(dp[C-1]))


if __name__ == '__main__':
    main()