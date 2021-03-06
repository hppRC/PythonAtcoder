#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
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
    N, M, K = LI()
    A = LI()
    B = LI()

    a = [0]+list(accumulate(A))
    b = [0]+list(accumulate(B))

    ans = 0

    for i in range(N + 1):
        if a[i] > K:
            continue
        rest = K - a[i]
        j = bisect.bisect_right(b, rest)
        ans = max(ans, i + j - 1)

    print(ans)

main()
