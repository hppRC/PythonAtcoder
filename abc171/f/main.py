#!usr/bin/env pypy3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect


def LI(): return [int(x) for x in sys.stdin.readline().split()]


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
MOD = 1000000007


class FactInv:
    def __init__(self, N, MOD=1000000007):
        fact = [1]*(N+1)
        for i in range(1, N+1):
            fact[i] = fact[i - 1] * i % MOD

        inv = [None]*(N+1)
        inv[N] = pow(fact[N], MOD - 2, MOD)

        for i in range(N)[::-1]:
            inv[i] = inv[i + 1] * (i + 1) % MOD

        self.N = N
        self.MOD = MOD
        self.fact = fact
        self.inv = inv

    def perm(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nPermutaion arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[a-b] % self.MOD

    def comb(self, a, b):
        if a > self.N or b > self.N:
            raise ValueError(
                "\nCombination arguments are bigger than N\n N = {}, a = {}, b = {}".format(self.N, a, b))
        return self.fact[a] * self.inv[b] * self.inv[a-b] % self.MOD


def main():
    K = I()
    l = len(S())

    fi = FactInv(K + l + 1)

    ans = 0

    for x in range(K+1):
        ans += fi.comb(l + K - x - 1, l - 1) * \
            pow(25, K - x, MOD) * pow(26, x, MOD) % MOD
        ans %= MOD

    print(ans)


main()
