#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def LS(): return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


sys.setrecursionlimit(1000000)


class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        self._group_size = [1 for _ in range(n)]
        self.num_of_groups = n

    def find(self, x):
        if self._parent[x] == x:
            return x
        px = self._parent[x]
        root = self.find(px)
        self._parent[x] = root
        return root

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self._rank[px] < self._rank[py]:
            self._parent[px] = py
            self._group_size[py] += self._group_size[px]
        else:
            self._parent[py] = px
            self._group_size[px] += self._group_size[py]
        if self._rank[px] == self._rank[py]:
            self._rank[py] += 1
        self.num_of_groups -= 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        px = self.find(x)
        return self._group_size[px]


def main():
    N, M, K = LI()
    AB = [LI1() for _ in range(M)]
    CD = [LI1() for _ in range(K)]

    uf = UnionFind(N)

    friend = [[] for _ in range(N)]
    block = [[] for _ in range(N)]

    for (a, b) in AB:
        friend[a].append(b)
        friend[b].append(a)
        uf.union(a, b)
    for (c, d) in CD:
        block[c].append(d)
        block[d].append(c)

    for i in range(N):
        gs = uf.group_size(i)
        bc = 0
        for bi in block[i]:
            bc += int(uf.is_same(i, bi))
        # print(i, gs, fc, bc)
        print(gs - len(friend[i]) - bc - 1, end=" ")


main()
