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
    H, W, K = LI()
    maze = SR(H)
    ans = 0
    for h in range(H+1):
        for w in range(W+1):
            for painted_row in itertools.combinations(range(H), h):
                for painted_col in itertools.combinations(range(W), w):
                    black = 0
                    for i in range(H):
                        for j in range(W):
                            if (i not in painted_row) and (j not in painted_col) and maze[i][j] == "#":
                                black += 1
                    if black == K:
                        ans += 1

    print(ans)


if __name__ == '__main__':
    main()