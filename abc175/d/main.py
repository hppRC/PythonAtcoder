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
    N, K = LI()
    P = LI1()
    C = LI()

    visit = [False] * N
    where = [-1] * N

    group = []
    group_sum = []
    for i in range(N):
        if visit[i]: continue
        
        now = i
        tmp = []
        cum = 0
        while not visit[now]:
            tmp.append(now)
            visit[now] = True
            where[now] = len(group)
            cum += C[now]
            now = P[now]
        group.append(tmp)
        group_sum.append(cum)

    ans = -INF

    for i in range(N):
        g = group[where[i]]

        if len(g) <= K:
            loop_count = K // len(g) - 1
            rest = K - loop_count * len(g)
        else:
            loop_count = 0
            rest = K

        loop_score = group_sum[where[i]]

        tmp = C[P[i]]
        tmp_max = C[P[i]]
        now = P[i]
        for _ in range(rest-1):
            now = P[now]
            tmp += C[now]
            tmp_max = max(tmp, tmp_max)
        ans = max(ans, max(tmp_max, tmp_max + loop_count * loop_score))
    print(ans)






if __name__ == '__main__':
    main()