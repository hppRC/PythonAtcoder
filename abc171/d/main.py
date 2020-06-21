#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)


def main():
    N = I()
    A = LI()
    Q = I()
    BC = [LI() for _ in range(Q)]

    d = defaultdict(int)

    for ai in A:
        d[ai] += 1

    ans = 0
    for (k, v) in d.items():
        ans += k * v

    for (b, c) in BC:
        tmp = d[b]
        d[b] = 0
        ans -= tmp * b
        d[c] += tmp
        ans += tmp * c
        print(ans)


main()
