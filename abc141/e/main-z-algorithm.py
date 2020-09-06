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

class ZAlgo:
    def __init__(self, seq):
        self.n = len(seq)
        # seq 自身と seq[i:] とが、先頭から最大で何文字一致しているか
        self.lcp = [0] * self.n
        self.lcp[0] = self.n
        i, j = 1, 0
        while i < self.n:
            while i + j < self.n and seq[j] == seq[i+j]:
                j += 1
            self.lcp[i] = j
            if j == 0:
                i += 1
                continue

            k = 1
            while i + k < self.n and k + self.lcp[k] < j:
                self.lcp[i + k] = self.lcp[k]
                k += 1
            i += k
            j -= k

    # seq[0:]とseq[i:]のLCP
    def getLCP(self, i): return self.lcp[i]

def main():
    N = I()
    S = SL()

    ans = 0

    for i in range(N):
        z = ZAlgo(S[i:])
        for j in range(N-i):
            ans = max(ans, min(z.getLCP(j), j))

    print(ans)


if __name__ == '__main__':
    main()