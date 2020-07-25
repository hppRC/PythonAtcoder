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

def main():
    N = I()

    people_inX = [0] * (10000 * 2 + 1)
    people_inY = [0] * (10000 * 2 + 1)

    XYP = LIR(N)

    for xi, yi, pi in XYP:
        people_inX[xi + 10000] += pi
        people_inY[yi + 10000] += pi

    numX = sorted(list(enumerate(people_inX)), key=lambda x: -x[1])
    numY = sorted(list(enumerate(people_inY)), key=lambda x: -x[1])

    X = [0]
    Y = [0]

    for k in range(N+1):
        idx = 0
        idy = 0
        for i in range(k):
            if numX[idx] >= numY[idx]:
                X.append(numX[idx][0] - 10000)
                idx += 1
            else:
                Y.append(numX[idx][0] - 10000)
                idx += 1

        for xi, yi, pi in XYP:
            print(min(X, key=lambda a: abs(a - xi)), min(Y, key=lambda a: abs(a - yi)))

        break

if __name__ == '__main__':
    main()