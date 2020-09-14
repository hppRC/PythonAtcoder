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

def main():
    N = I()
    A = LI()
    B = LI()


# def solve(N, A, B):
    d = defaultdict(int)
    s = set()
    nums = []
    for bi in B:
        d[bi] += 1
        if not bi in s:
            s.add(bi)
            nums.append(bi)

    C = [None] * N
    now = 0
    print(d, nums)

    for i in range(N):
        if nums[now] == A[i]:
            now = (now + 1) % len(nums)
        while d[nums[now]] <= 0:
            now = (now + 1) % len(nums)

        C[i] = nums[now]
        d[nums[now]] -= 1

    print(d, nums)

    for ai, ci in zip(A, C):
        if ai == ci:
            print("No")
            break
    else:
        print("Yes")
        print(*C)


# def main():
#     for p in itertools.combinations_with_replacement(range(5), r=4):
#         for q in itertools.combinations_with_replacement(range(5), r=4):
#             print(p, q)
#             solve(4, p, q)
#             print("-"*100)




if __name__ == '__main__':
    main()