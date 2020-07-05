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
    N = I()
    A = sorted(LI(), reverse=True)
    q = []
    ans = A[0]
    q.append((-min(A[0], A[1]), A[0], A[1]))
    q.append((-min(A[0], A[1]), A[0], A[1]))


    for i in range(2, N):
        (minus_x, left, right) = heapq.heappop(q)
        ans += -minus_x
        heapq.heappush(q, (-min(left, A[i]), left, A[i]))
        heapq.heappush(q, (-min(right, A[i]), A[i], right))

    print(ans)


if __name__ == '__main__':
    main()