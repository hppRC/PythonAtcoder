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
INF = float('inf')

def main():
    N = I()
    XYP = LIR(N)

    anss = [INF] * (N+1)

    preX, preY = [None for _ in range(1 << N)], [None for _ in range(1 << N)]
    for pattern in itertools.product([0, 1], repeat=N):
        X, Y = [0], [0]
        keyX, keyY = 0, 0
        tmpX, tmpY = [], []
        for i, bit in enumerate(pattern):
            keyX |= bit << i
            keyY |= bit << i
            if bit:
                X.append(XYP[i][0])
                Y.append(XYP[i][1])
        for x, y, p in XYP:
            min_distX = abs(y)
            min_distY = abs(x)
            for rx in X:
                if min_distX > abs(x - rx):
                    min_distX = abs(x - rx)
            for ry in Y:
                if min_distY > abs(y - ry):
                    min_distY = abs(y - ry)
            tmpX.append(min_distX * p)
            tmpY.append(min_distY * p)
        preX[keyX] = tmpX
        preY[keyY] = tmpY

    for pattern in itertools.product([0, 1, 2], repeat=N):
        keyX, keyY = 0, 0
        root = 0
        for i, which in enumerate(pattern):
            if which == 1:
                keyX |= which << i
                root += 1
            elif which == 2:
                keyY |= int(bool(which)) << i
                root += 1

        tmp = 0
        for vx, vy in zip(preX[keyX], preY[keyY]):
            tmp += min(vx, vy)

        if anss[root] > tmp:
            anss[root] = tmp

    for ans in anss:
        print(ans)

if __name__ == '__main__':
    main()