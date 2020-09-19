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
def SL(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

class Eratosthenes:
    # https://cp-algorithms.com/algebra/prime-sieve-linear.html
    def __init__(self, n):
        primes, lp = [], [0] * (n + 1)
        for i in range(2, n + 1):
            if lp[i] == 0:
                primes.append(i)
                lp[i] = i

            for pj in primes:
                if pj > lp[i] or i * pj > n: break
                lp[i * pj] = pj
        self.primes, self.lp = primes, lp

    def is_prime(self, x): return self.lp[x] == x

    def factors(self, x):
        ret = []
        while x > 1:
            ret.append(self.lp[x])
            x //= self.lp[x]
        return ret

    def factors_count(self, x):
        ret = defaultdict(int)
        while x > 1:
            ret[self.lp[x]] += 1
            x //= self.lp[x]
        return ret


def main():
    N = I()
    era = Eratosthenes(N)
    d = defaultdict(int)
    for i in range(1, N):
        cnt = era.factors_count(i)
        tmp = 1
        for v in cnt.values():
            tmp *= v+1
        d[i] = tmp

    ans = 0
    for c in range(1, N):
        ans+= d[N - c]

    print(ans)


if __name__ == '__main__':
    main()