#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = I()
    X = S()
    original_popcount = X.count("1")

    upper_popcount = original_popcount + 1
    lower_popcount = original_popcount - 1

    if original_popcount == 0:
        for i in range(N):
            print(1)
        return

    if original_popcount == 1:
        for i in range(N):
            if X[-1] == "1":
                if i != N-1:
                    print(2)
                else:
                    print(0)
            else:
                if X[i] == "1":
                    print(0)
                elif i == N-1:
                    print(2)
                else:
                    print(1)
        return

    # Xが0の可能性
    upper = [0] * N
    lower = [0] * N
    upper[-1] = 1 % upper_popcount
    lower[-1] = 1 % lower_popcount

    for i in range(1, N)[::-1]:
        upper[i-1] = (2 * upper[i]) % upper_popcount
        lower[i-1] = (2 * lower[i]) % lower_popcount

    mu = 0
    ml = 0
    for i in range(N):
        if X[i] == "1":
            mu = (mu + upper[i]) % upper_popcount
            ml = (ml + lower[i]) % lower_popcount

    for i in range(N):
        if X[i] == "0":
            m = (mu + upper[i]) % upper_popcount
        else:
            m = (ml - lower[i]) % lower_popcount

        ans = 1
        while m:
            tmp = m
            ones = 0
            while tmp:
                if tmp & 1 == 1:
                    ones += 1
                tmp //= 2
            m %= ones
            ans += 1

        print(ans)



if __name__ == '__main__':
    main()