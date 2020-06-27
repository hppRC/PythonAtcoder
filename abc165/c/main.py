from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations_with_replacement, compress
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
    N, M, Q = LI()
    abcd = [LI() for _ in range(Q)]
    ans = 0

    for A in combinations_with_replacement(range(1, M + 1), N):
        tmp = 0
        for (a, b, c, d) in abcd:
            tmp += d if (A[b-1] - A[a-1] == c) else 0
        ans = max(ans, tmp)
    print(ans)


main()
