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

MOD = 10**9+7


def main():
    K = I()
    l = len(S())
    ans = 1

    for _ in range(K):
        ans *= (25 * l + 26)
        print(ans)
        l += 1

    tmp = 1
    for i in range(1, l - 2 - 1):
        tmp *= i

    print(tmp)
    print((ans // tmp) % MOD)


main()
