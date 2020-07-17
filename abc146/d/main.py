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
def LIR1(n): return [LI1() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N = I()
    AB = LIR1(N-1)

    g = [[] for _ in range(N)]
    visited = [False] * N
    ins = [-1] * N

    for a, b in AB:
        g[a].append(b)
        g[b].append(a)

    q = deque()
    visited[0] = True
    q.append(0)

    while q:
        u = q.popleft()
        outs_num = 0
        visited[u] = True

        for v in g[u]:
            if not visited[v]:
                if outs_num == ins[u]:
                    outs_num += 1

                ins[v] = outs_num

                outs_num += 1
                q.append(v)

    print(max(ins) + 1)
    for a, b in AB:
        print(ins[b] + 1)
    


if __name__ == '__main__':
    main()