#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

sys.setrecursionlimit(1000000)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def divisors(N):
    divs = set([1, N])
    i = 2
    while i ** 2 <= N:
        if N % i == 0:
            divs.add(i)
            divs.add(N//i)
        i += 1
    return sorted(list(divs))

def is_ok(N, K):
    if K <= 1:
        return False
    while N % K == 0:
        N //= K
    return N % K == 1

def main():
    N = I()
    ans = 0

    for divisor in divisors(N-1):
        if is_ok(N, divisor):
            ans += 1

    for divisor in divisors(N):
        if is_ok(N, divisor):
            ans += 1

    print(ans)



if __name__ == '__main__':
    main()