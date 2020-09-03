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
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)


warp = [[dy, dx] for dy in range(-2, 3) for dx in range(-2, 3) if abs(dy) + abs(dx) > 1]

def main():
    H, W = LI()
    CH, CW = LI1()
    DH, DW = LI1()
    S = SR(H)
    dist = make_list(H, W, default=-1)

    q = deque()
    dist[CH][CW] = 0
    q.append((0, CH, CW))

    while q:
        d, y, x = q.popleft()

        for dy, dx in dire:
            newx, newy = x + dx, y + dy
            if 0 <= newx < W and 0 <= newy < H and S[newy][newx] == ".":
                if dist[newy][newx] == -1 or dist[newy][newx] > d:
                    dist[newy][newx] = d
                    q.appendleft((d, newy, newx))

        for dy, dx in warp:
            newx, newy = x + dx, y + dy
            if 0 <= newx < W and 0 <= newy < H and S[newy][newx] == ".":
                if dist[newy][newx] == -1 or dist[newy][newx] > d + 1:
                    dist[newy][newx] = d + 1
                    q.append((d + 1, newy, newx))

    print(dist[DH][DW])







if __name__ == '__main__':
    main()