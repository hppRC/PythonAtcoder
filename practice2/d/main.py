# thanks: https://atcoder.jp/contests/practice2/submissions/16784996

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

class MaxFlowGraph:
    def __init__(self, N):
        self.N = N
        self.graph = [[] for _ in range(N)]
        self.capacities = [dict() for _ in range(N)]

    def add_edge(self, v, w, cap=1):
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.capacities[v][w] = cap
        self.capacities[w][v] = 0

    def bfs(self, s, t):
        self.level = [-1] * self.N
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for w, cap in self.capacities[v].items():
                if cap and self.level[w] == -1:
                    self.level[w] = self.level[v] + 1
                    if w == t: return True
                    q.append(w)
        return False

    def dfs(self, s, t, limit):
        st = [t]
        while st:
            v = st[-1]
            if v == s: break
            #vから行ける全ての頂点について
            while self.it[v] < len(self.graph[v]):
                # w -> v の cap
                w = self.graph[v][self.it[v]]
                cap = self.capacities[w][v]
                if cap and self.level[w] != -1 and self.level[v] > self.level[w]:
                    st.append(w)
                    break
                self.it[v] += 1
            else:
                st.pop()
                self.level[v] = self.N
        else: return 0

        flow = min(limit, min(self.capacities[st[i + 1]][st[i]] for i in range(len(st) - 2)))
        for i in range(len(st) - 1):
            self.capacities[st[i]][st[i+1]] += flow
            self.capacities[st[i+1]][st[i]] -= flow
        return flow

    def flow(self, s, t, flow_limit=18446744073709551615):
        flow = 0
        while flow < flow_limit and self.bfs(s, t):
            self.it = [0]*self.N
            while flow < flow_limit:
                f = self.dfs(s, t, flow_limit - flow)
                if not f: break
                flow += f
        return flow

    def min_cut(self, s):
        visited = [False]*self.N
        q = [s]
        while q:
            v = q.pop()
            visited[v] = True
            for w, cap in self.capacities[v].items():
                if cap and not visited[w]:
                    q.append(w)

def main():
    N, M = LI()
    S = SLR(N)
    g = MaxFlowGraph(N*M+2)

    s = N*M
    t = N*M+1

    # 偶数はblack, 奇数はwhiteとして市松模様に塗る、二部グラフの最大マッチング問題
    # s -> black -> white -> t の辺を張って最大流を求める
    for y in range(N):
        for x in range(M):
            # black
            if (y+x) % 2 == 0:
                g.add_edge(s, M*y+x)
                for dy, dx in [[1, 0], [0, 1]]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and S[y][x] == "." and S[ny][nx] == ".":
                        g.add_edge(M*y+x, M*ny+nx)
            # white
            else:
                g.add_edge(M*y+x, t)
                for dy, dx in [[1, 0], [0, 1]]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and S[y][x] == "." and S[ny][nx] == ".":
                        g.add_edge(M*ny+nx, M*y+x)

    print(g.flow(s, t))

    # blackから考える
    for u in range(N*M+2):
        uy, ux = divmod(u, M)
        if (uy + ux) % 2 == 1: continue

        for v, cap in g.capacities[u].items():
            if cap != 0: continue
            vy, vx = divmod(v, M)
            if u != s and u != t and v != s and v != t:
                if uy - 1 == vy:
                    S[uy][ux], S[vy][vx] = "^", "v"
                elif uy + 1 == vy:
                    S[uy][ux], S[vy][vx] = "v", "^"
                elif ux + 1 == vx:
                    S[uy][ux], S[vy][vx] = ">", "<"
                elif ux - 1 == vx:
                    S[uy][ux], S[vy][vx] = "<", ">"

    for p in S:
        print("".join(p))



if __name__ == '__main__':
    main()