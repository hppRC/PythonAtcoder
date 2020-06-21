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
    N, K = LI()
    A = LI()

    for _ in range(K):
        B = [0]*(N+1)
        for i in range(N):
            l = max(i - A[i], 0)
            r = min(A[i] + i + 1, N)
            B[l] += 1
            B[r] -= 1
        for i in range(N):
            B[i+1] += B[i]

        if A == B:
            break
        A = B
    print(*A[:-1], sep=" ")


main()
