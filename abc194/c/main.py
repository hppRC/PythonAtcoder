#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

from itertools import *
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
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SLR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]


def perm(n, r): return math.factorial(n) // math.factorial(r)


def comb(n, r): return math.factorial(
    n) // (math.factorial(r) * math.factorial(n-r))


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def make_list(n, *args, default=0): return [make_list(*args, default=default)
                                            for _ in range(n)] if args else [default for _ in range(n)]


dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)


def main():
    N = I()
    A = LI()

    cnt = [0] * 401
    for a in A:
        cnt[a+200] += 1

    ans = 0
    for i, c1 in enumerate(cnt):
        for j, c2 in enumerate(cnt):
            ans += c1*c2*(((i-200) - (j-200))**2)
    print(ans//2)


if __name__ == '__main__':
    main()
