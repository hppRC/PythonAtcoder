#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = I()
    A = []
    for _ in range(N):
        ni = I()
        A.append(LIR(ni))

    ans = 0
    for bit in range(1 << N):
        pattern = [bit >> i & 1 for i in range(N)]
        for (i, Ai) in enumerate(A):
            if not pattern[i]:
                continue
            # iが正直者の時
            for (x, y) in Ai:
                target = pattern[x-1]
                if target != y:
                    break
            else:
                continue
            break
        else:
            ans = max(ans, pattern.count(1))

    print(ans)


if __name__ == '__main__':
    main()