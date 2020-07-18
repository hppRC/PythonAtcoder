#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    s = S()

    dp = [[0] * 13 for _ in range(len(s) + 1)]
    dp[0][0] = 1

    for i in range(len(s)):
        if s[i] == "?":
            for ch in range(10):
                for j in range(13):
                    dp[i+1][(j * 10 + ch) % 13] += dp[i][j]
        else:
            ch = int(s[i])
            for j in range(13):
                dp[i+1][(j * 10 + ch) % 13] += dp[i][j]

        for j in range(13):
            dp[i+1][j] %= MOD

    print(dp[len(s)][5])

if __name__ == '__main__':
    main()