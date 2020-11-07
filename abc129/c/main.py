#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1_000_000_007

def main():
    N, M = LI()
    A = set(IR(M))

    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1 if 1 not in A else 0

    for i in range(2, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
        if i in A:
            dp[i] = 0
    print(dp[-1])



if __name__ == '__main__':
    main()