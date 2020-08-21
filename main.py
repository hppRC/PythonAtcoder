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
def adjacency_list(N, edges):
    g = make_list(N, 0)
    for a, b in edges: g[a].append(b), g[b].append(a)
    return g
def tree_utils(start, g):
    parent, children, depth, q = [-1]*len(g), make_list(len(g), 0), [-1]*len(g), deque([start]); depth[start] = 0
    while q:
        i = q.popleft()
        for j in g[i]:
            if depth[j] != -1: parent[i] = j
            else: depth[j] = depth[i] + 1; children[i].append(j), q.append(j)
    return parent, children, depth
def graph_distance(start, g):
    dist, q = [-1] * len(g), deque([start]); dist[start] = 0
    while q:
        i = q.popleft()
        for j in g[i]:
            if dist[j] == -1: dist[j] = dist[i] + 1; q.append(j)
    return dist

sys.setrecursionlimit(1000000)
dire, dire8 = [[1, 0], [0, 1], [-1, 0], [0, -1]], [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets, ALPHABETS = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD, INF = 1000000007, float("inf")

def main():
    N = I()

if __name__ == '__main__':
    main()