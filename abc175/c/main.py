#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools
import bisect
import math
import fractions
import sys
import copy


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


def comb(n, r): return math.factorial(
    n) // (math.factorial(r) * math.factorial(n-r))


alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007
INF = float("inf")


def main():
    X, K, D = LI()

    if abs(X) >= K * D:
        if X < 0:
            print(abs(X + K * D))
        else:
            print(abs(X - K * D))
    else:
        t = abs(X) // D
        rest = K - t
        if rest % 2 == 0:
            print(abs(X) % D)
        else:
            print(abs(abs(X) % D - D))


if __name__ == '__main__':
    main()
