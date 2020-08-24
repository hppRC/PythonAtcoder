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
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

sys.setrecursionlimit(1000000)
dire, dire8 = [[1, 0], [0, 1], [-1, 0], [0, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets, ALPHABETS = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD, INF = 1000000007, float("inf")

def main():
    N, M = LI()
    SC = LIR(M)

    if N == 1:
        for i in range(0, 10):
            string = str(i)
            for s, c in SC:
                if int(string[s-1]) != c:
                    break
            else:
                print(i)
                break
        else:
            print(-1)
        return

    for i in range(10 ** (N-1), 10 ** N):
        string = str(i)
        for s, c in SC:
            if int(string[s-1]) != c:
                break
        else:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()