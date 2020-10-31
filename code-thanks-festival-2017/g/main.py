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
    N, M = LI()
    AB = LIR1(M)
    s = [(1<<N - N//2)-1]*(1 << N//2)

    ok1 = [True]*(1<<N//2)
    ok2 = [True]*(1<<N-N//2)
    for a, b in AB:
        if a < N//2 and b < N//2:
            ok1[(1 << a) | (1 << b)] = False

        elif a >= N//2 and b >= N//2:
            ok2[(1 << a-N//2) | (1 << b-N//2)] = False

        else:
            a, b = min(a, b), max(a, b)
            s[1 << a] ^= 1 << b - N//2


    for i in range(1 << N//2):
        if not ok1[i]:
            for w in range(N//2):
                ok1[i | (1 << w)] = False
    for i in range(1 << N-N//2):
        if not ok2[i]:
            for w in range(N-N//2):
                ok2[i | (1 << w)] = False


    for i in range(1<<N//2):
        for w in range(N//2):
            s[i | (1 << w)] = s[i] & s[1 << w]


    dp = [None]*(1 << N - N//2)
    for i in range(1 << N - N//2):
        dp[i] = bin(i).count("1") if ok2[i] else 0
    for i in range(1 << N - N//2):
        for w in range(N - N//2):
            dp[i | (1 << w)] = max(dp[i | (1 << w)], dp[i])

    ans = 0
    for i in range(1 << N//2):
        if ok1[i]:
            ans = max(bin(i).count("1") + dp[s[i]], ans)
    print(ans)

if __name__ == '__main__':
    main()