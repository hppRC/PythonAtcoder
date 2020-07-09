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

    ans = 0
    for h in range(H):
        for w in range(W):
            if maze[h][w] == '#':
                continue

            visited = [[False] * W for _ in range(H)]
            visited[h][w] = True

            q = deque()
            q.append((0, h, w))

            while q:
                dist, y, x = q.popleft()

                for dy, dx in dire:
                    if y + dy >= 0 and y + dy < H and x + dx >= 0 and x + dx < W:
                        if maze[y + dy][x + dx] == '.' and not visited[y + dy][x + dx]:
                            q.append((dist + 1, y + dy, x + dx))
                            visited[y + dy][x + dx] = True

            ans = max(ans, dist)

    print(ans)

if __name__ == '__main__':
    main()