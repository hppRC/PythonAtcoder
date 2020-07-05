#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
import collections, heapq, itertools, bisect
import math, fractions
from functools import reduce, lru_cache
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

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )

    def inverse(self):
        return pow(self.x, MOD - 2, MOD)

sys.setrecursionlimit(1000000)
dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
MOD = 1000000007

def main():
    N, K = LI()
    A = LI()

    if K == N:
        print(reduce(lambda x, y: x * y, A, ModInt(1)))
        exit()

    plus = sorted([ai for ai in A if ai >= 0], reverse=True)
    minus = sorted([ai for ai in A if ai < 0])

    if len(plus) == 0:
        if K % 2 == 1:
            print(reduce(lambda x, y: x * y, minus[-K:], ModInt(1)))
        else:
            print(reduce(lambda x, y: x * y, minus[:K], ModInt(1)))
        exit()

    ip, im = 0, 0
    ans = ModInt(1)

    j = 0

    while True:
        if j == K:
            break
        if j == K - 1:
            ans *= plus[ip]
            break

        # K - j >= 2
        if len(plus) - ip >= 2 and len(minus) - im >= 2:
            p = plus[ip] * plus[ip+1]
            m = minus[im] * minus[im+1]
            if p > m:
                ans *= plus[ip]
                ip += 1
                j += 1
            else:
                ans *= m
                im += 2
                j += 2
        elif len(plus) - ip >= 2:
            ans *= plus[ip]
            ip += 1
            j += 1
        elif len(minus) - im >= 2:
            ans *= minus[im] * minus[im+1]
            im += 2
            j += 2

    print(ans)



if __name__ == '__main__':
    main()