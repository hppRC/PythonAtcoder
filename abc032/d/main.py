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
    N, W = LI()
    vw = LIR(N)
    maxw = max(w for v, w in vw)
    maxv = max(v for v, w in vw)

    if N <= 30:
        ans = 0

        first = vw[:N//2+1]
        d = defaultdict(int)
        for s in powerset(first):
            sv, sw = 0, 0
            for v, w in s:
                sv += v
                sw += w
            d[sw] = max(d[sw], sv)
        cand = sorted([(v, w) for w, v in d.items()], key=lambda x: x[1])
        l = [cand[0]]

        for v, w in cand:
            if v > l[-1][0]: l.append((v, w))

        second = vw[N//2+1:]
        for s in powerset(second):
            sv, sw = 0, 0
            for v, w in s:
                sw += w
                sv += v
            rest = W - sw
            if rest < 0: continue

            left, right = -1, len(l)
            while right - left > 1:
                mid = (left + right) // 2
                if l[mid][1] > rest: right = mid
                else: left = mid
            ans = max(ans, sv + l[left][0])
        print(ans)


    elif maxw <= 1000:
        dp = make_list(N+1, N*maxw+1)
        for i in range(N):
            v, w = vw[i]
            for j in range(N*maxw+1):
                if j - w >= 0:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)
                else:
                    dp[i+1][j] = dp[i][j]

        print(dp[N][min(W, N*maxw)])


    elif maxv <= 1000:
        dp = make_list(N+1, N*maxv+1, default=N*maxw+1)
        dp[0][0] = 0
        for i in range(N):
            v, w = vw[i]
            for j in range(N*maxv+1):
                if j-v >= 0:
                    dp[i+1][j] = min(dp[i][j], dp[i][j-v] + w)
                else:
                    dp[i+1][j] = dp[i][j]
        print(max([v for v, w in enumerate(dp[N]) if w <= W]))

if __name__ == '__main__':
    main()