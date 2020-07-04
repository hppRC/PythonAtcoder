#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    H, W = LI()
    maze = SR(H)
    # top, right, bottom, left
    info = [[0 for _ in range(W)] for _ in range(H)]

    # from top to bottom
    for w in range(W):
        current = 0
        for h in range(H):
            if maze[h][w] == "#":
                current = 0
            else:
                info[h][w] += current
                current += 1

    # from right to left
    for h in range(H):
        current = 0
        for w in range(W)[::-1]:
            if maze[h][w] == "#":
                current = 0
            else:
                info[h][w] += current
                current += 1

    # from bottom to top
    for w in range(W):
        current = 0
        for h in range(H)[::-1]:
            if maze[h][w] == "#":
                current = 0
            else:
                info[h][w] += current
                current += 1

    # from  left to right
    for h in range(H):
        current = 0
        for w in range(W):
            if maze[h][w] == "#":
                current = 0
            else:
                info[h][w] += current
                current += 1

    ans = 0
    for h in range(H):
        for w in range(W):
            if maze[h][w] == ".":
                ans = max(ans, info[h][w] + 1)
    print(ans)

if __name__ == '__main__':
    main()