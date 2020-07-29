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
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N, K = LI()
    A = LI()

    P = sorted([ai for ai in A if ai > 0])
    Pm = sorted([-ai for ai in A if ai > 0])
    M = sorted([ai for ai in A if ai < 0])
    Mp = sorted([- ai for ai in A if ai < 0])
    zero = [ai for ai in A if ai == 0]

    zero_len = len(P) * len(zero) + len(M) * len(zero) + len(zero) * (len(zero) - 1) // 2

    if K <= len(P) * len(M):
        left = - 10 ** 18 - 1
        right = 0
        ans = right
        while right - left != 1:
            tmp = 0
            mid = (left + right) // 2
            for mi in M:
                tmp += bisect_right(Pm, - mid // mi)

            if tmp >= K:
                ans = min(ans, mid)
                right = mid
            else:
                left = mid
        print(ans)
    elif K <= len(P) * len(M) + zero_len:
        print(0)
    else:
        diff = len(P) * len(M) + zero_len
        left = 0
        right = 10 ** 18 + 1
        ans = right
        while right - left != 1:
            tmp = 0
            mid = (left + right) // 2
            for pi in P:
                tmp += bisect_right(P, mid // pi)
                tmp -= 1 if mid // pi >= pi else 0
            for mpi in Mp:
                tmp += bisect_right(Mp, mid // mpi)
                tmp -= 1 if mid // mpi >= mpi else 0
            tmp //= 2
            if tmp + diff >= K:
                ans = min(ans, mid)
                right = mid
            else:
                left = mid
        print(ans)

if __name__ == '__main__':
    main()