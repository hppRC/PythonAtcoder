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
def SLR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if args else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 1000000007
INF = float("inf")

sys.setrecursionlimit(1000000)

def main():
    N = I()
    XY = LIR(N)

    right_angled, obtuse = 0, 0
    epsilon = pow(10, -10)

    total_acute, total_right_angled = 0, 0
    for x, y in XY:
        theta1 = sorted([math.atan2(yi - y, xi - x) for xi, yi in XY if (x != xi) or (y != yi)])
        theta2 = [x + 2*math.pi for x in theta1]
        theta = theta1 + theta2

        acute, right_angled = 0, 0
        left = 0
        for right in range(len(theta1), len(theta)):
            while theta[right] - theta[left] - math.pi / 2 > epsilon:
                left += 1
            acute += right - left
            if abs((theta[right] - theta[left]) - math.pi/2) < epsilon:
                right_angled += 1
        total_acute += acute
        total_right_angled += right_angled

    print(N*(N-1)*(N-2)//6 - (N*(N-1)*(N-2)//2 - total_acute) - total_right_angled, total_right_angled, N*(N-1)*(N-2)//2 - total_acute)

if __name__ == '__main__':
    main()