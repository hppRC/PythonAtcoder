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

    dp = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(4)]
    table = [[0 for _ in range(C)] for _ in range(R)]

    for r, c, v in rcv:
        table[r][c] = v + 1

    for i in range(1, 4):
        for r in range(R):
            for c in range(C):
                if r > 0 and c > 0:
                    dp[i][r][c] = max([dp[i][r][c-1], dp[i][r-1][c], dp[i-1][r][c-1] + table[r][c-1], dp[i-1][r-1][c] + table[r-1][c]])
                elif r == 0 and c == 0:
                    pass
                elif r == 0:
                    dp[i][r][c] = max([dp[i][r][c-1], dp[i-1][r][c-1] + table[r][c-1]])
                elif c == 0:
                    dp[i][r][c] = max([dp[i][r-1][c], dp[i-1][r-1][c] + table[r-1][c]])


    for p in dp:
        for q in p:
            print(q)
        print("-"*100)
    print(dp[1][R-1][C-1], dp[2][R-1][C-1], dp[3][R-1][C-1])



if __name__ == '__main__':
    main()