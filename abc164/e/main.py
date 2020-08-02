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
INF = float("inf")

def main():
    N, M, S = LI()
    UVAB = LIR(M)
    CD = LIR(N)

    edge = [[] for _ in range(N)]
    for u, v, a, b in UVAB:
        edge[u - 1].append((v - 1, a, b))
        edge[v - 1].append((u - 1, a, b))

    dist = [[INF] * 2500 for _ in range(N)]
    heap = [(0, 0, min(2500, S))]

    while heap:
        cost, u, s = heappop(heap)
        c, d = CD[u]

        if s + c < 2500 and dist[u][s + c] > cost + d:
            dist[u][s + c] = cost + d
            heappush(heap, (cost + d, u, s + c))
        for v, a, b in edge[u]:
            if s - a >= 0 and dist[v][s - a] > cost + b:
                dist[v][s - a] = cost + b
                heappush(heap, (cost + b, v, s - a))

        # print(heap)

    for i in range(1, N):
        print(min(dist[i]))

if __name__ == '__main__':
    main()