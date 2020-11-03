#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

from itertools import *
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
def SLR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if args else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

def main():
    N, K = LI()
    S = SL()

    tmp = []
    cnt = 1
    for i in range(1, N):
        if S[i-1] == S[i]:
            cnt += 1
        else:
            tmp.append((cnt, abs(int(S[i-1]) - 1)))
            cnt = 1
    tmp.append((cnt, abs(int(S[-1]) - 1)))

    ans = 0
    left = 0
    now = 0
    k = 0
    for right in range(len(tmp)):
        now += tmp[right][0]
        k += tmp[right][1]
        while k > K:
            now -= tmp[left][0]
            k -= tmp[left][1]
            left += 1
        ans = max(ans, now)
    print(ans)



if __name__ == '__main__':
    main()