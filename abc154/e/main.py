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

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = input()
    K = I()

    dp1 = [[0] * len(N) for _ in range(K + 2)] #未確定
    dp2 = [[0] * len(N) for _ in range(K + 2)] #確定

    dp1[1][0] = 1
    dp2[0][0] = 1
    dp2[1][0] = int(N[0]) - 1

    for i in range(1, len(N)):
        num = int(N[i])
        for k in range(K+1):
            if num == 0:
                dp1[k][i] += dp1[k][i - 1]
                dp2[k][i] += dp2[k][i - 1]
                dp2[k+1][i] = dp2[k][i - 1] * 9
            else:
                dp1[k + 1][i] += dp1[k][i - 1]
                dp2[k][i] += dp2[k][i - 1] + dp1[k][i - 1]
                dp2[k + 1][i] = dp2[k][i - 1] * 9 + dp1[k][i - 1] * (num - 1)

    print(dp1[K][-1] + dp2[K][-1])

if __name__ == '__main__':
    main()