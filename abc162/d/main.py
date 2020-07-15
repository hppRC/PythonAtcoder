#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
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

def main():
    N = I()
    s = S()

    R = s.count("R")
    G = s.count("G")
    B = s.count("B")

    dup = 0
    for i in range(N):
        for k in range(i+1, N):
            if (i + k) % 2 == 0:
                j = (i + k) // 2
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    dup += 1

    print(R * G * B - dup)

main()
