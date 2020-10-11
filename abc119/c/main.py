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
def SLR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if args else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

def main():
    N, A, B, C = LI()
    L = IR(N)
    ans = INF

    for pattern in itertools.product([0, 1, 2, 3], repeat=N):
        x, y, z, rest = [], [], [], []
        for i in range(N):
            if pattern[i] == 0:
                x.append(L[i])
            elif pattern[i] == 1:
                y.append(L[i])
            elif pattern[i] == 2:
                z.append(L[i])
            else:
                rest.append(L[i])

        cost = max((len(x)-1)*10,0) + max((len(y)-1)*10, 0) + max((len(z)-1)*10, 0)

        al, bl, cl = sum(x) if x else INF, sum(y) if y else INF, sum(z) if z else INF
        block = [al, bl, cl] + rest

        for comb in itertools.combinations(block, r=3):
            c, b, a = sorted(comb)
            ans = min(ans, cost + abs(A-a) + abs(B-b) + abs(C-c))

    print(ans)





if __name__ == '__main__':
    main()