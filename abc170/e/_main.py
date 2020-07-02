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
def LI1R(n): return [LI1() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N, Q = LI()
    AB = LIR(N)
    CD = LIR(Q)

    num = 200_000 + 1
    enji = [0] * N
    kindergartens = [[] for _ in range(num)]
    for i, (a, b) in enumerate(AB):
        enji[i] = b
        heapq.heappush(kindergartens[b], (-a, i))

    def get_max_rate(where):
        while kindergartens[where]:
            minus_rate, x = kindergartens[where][0]
            if enji[x] == where:
                return -minus_rate
            else:
                heapq.heappop(kindergartens[where])
        return 0

    max_rates = []
    for i in range(num):
        x = get_max_rate(i)
        if x:
            max_rates.append((x, i))
    heapq.heapify(max_rates)

    def get_ans():
        while max_rates:
            rate, where = max_rates[0]
            if rate == get_max_rate(where):
                return rate
            heapq.heappop(max_rates)

    for c, d in CD:
        before = enji[c-1]
        enji[c-1] = d
        heapq.heappush(kindergartens[d], (-AB[c-1][0], c-1))
        for cls in (before, d):
            x = get_max_rate(cls)
            if x:
                heapq.heappush(max_rates, (x, cls))
        print(get_ans())

if __name__ == '__main__':
    main()