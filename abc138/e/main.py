#!usr/bin/env python3
import collections, heapq, itertools, bisect
import math, fractions
import sys, copy

from collections import defaultdict, deque, Counter, OrderedDict
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

def L(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline().rstrip())
def S(): return list(sys.stdin.readline().rstrip())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]

alphabets = "abcdefghijklmnopqrstuvwxyz"

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    s = S()
    t = S()

    chars = {ch: [] for ch in alphabets}

    for i, ch in enumerate(s):
        chars[ch].append(i)

    ans = 0
    last = -1
    for ch in t:
        if len(chars[ch]) == 0:
            print(-1)
            return

        idx = bisect_right(chars[ch], last)
        idx = idx if idx < len(chars[ch]) else 0
        if chars[ch][idx] > last:
            ans += chars[ch][idx] - last
        else:
            ans += len(s) - last + chars[ch][idx]
        last = chars[ch][idx]

    print(ans)



if __name__ == '__main__':
    main()