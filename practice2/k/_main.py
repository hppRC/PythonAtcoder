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
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def R(n): return [sys.stdin.readline().strip() for _ in range(n)]
def LR(n): return [L() for _ in range(n)]
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def LIR1(n): return [LI1() for _ in range(n)]
def SR(n): return [SL() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

def perm(n, r): return math.factorial(n) // math.factorial(r)
def comb(n, r): return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def make_list(n, *args, default=0): return [make_list(*args, default=default) for _ in range(n)] if len(args) > 0 else [default for _ in range(n)]

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
dire8 = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
alphabets = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MOD = 998244353
INF = float("inf")

sys.setrecursionlimit(1000000)


# モノイドに対して適用可能、Nが2冪でなくても良い
class LazySegTree():
    def __init__(self, initial_values, monoid_func, composition, operate, monoid_identity, operator_identity):
        self.N = len(initial_values)
        self.monoid_func = monoid_func
        self.composition = composition # composition(f, g) => g(f(x))の順であることに注意
        self.operate = operate #右作用 operate(a, f) => f(a), 雑に可換な処理を書こうとするとバグるので注意
        self.monoid_identity = monoid_identity
        self.operator_identity = operator_identity
        self.data = [self.monoid_identity]*(2*self.N)
        self.lazy = [self.operator_identity]*(2*self.N)
        self.size = [0]*(2*self.N)

        for i, ai in enumerate(initial_values):
            self.data[self.N+i] = ai
            self.size[self.N+i] = 1
        for i in range(self.N-1,0,-1):
            self.data[i] = self.monoid_func(self.data[i << 1], self.data[i << 1 | 1])
            self.size[i] = self.size[i << 1] + self.size[i << 1 | 1]

    def update(self,i,x):  # i番目(0-index)の値をxに変更
        i += self.N
        self.data[i] = x
        while i>1:
            i >>= 1
            self.data[i] = self.monoid_func(self.data[i << 1], self.data[i << 1 | 1])

    def eval_at(self,i):  # i番目で作用を施した値を返す
        return self.operate(self.data[i],self.lazy[i],self.size[i])

    def eval_above(self,i):  # i番目より上の値を再計算する
        while i > 1:
            i >>= 1
            self.data[i] = self.monoid_func(self.eval_at(i << 1),self.eval_at(i << 1 | 1))

    def propagate_at(self,i):  # i番目で作用を施し、1つ下に作用の情報を伝える
        self.data[i] = self.operate(self.data[i],self.lazy[i],self.size[i])
        self.lazy[i << 1] = self.composition(self.lazy[i << 1],self.lazy[i])
        self.lazy[i << 1 | 1] = self.composition(self.lazy[i << 1 | 1], self.lazy[i])
        self.lazy[i] = self.operator_identity

    def propagate_above(self,i):  # i番目より上で作用を施す
        H = i.bit_length()
        for h in range(H,0,-1):
            self.propagate_at(i >> h)

    def fold(self, L, R):  # [L,R)の区間取得
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        vL = self.monoid_identity
        vR = self.monoid_identity
        while L < R:
            if L & 1:
                vL = self.monoid_func(vL,self.eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.monoid_func(self.eval_at(R),vR)
            L >>= 1
            R >>= 1
        return self.monoid_func(vL,vR)

    #重たい
    def apply_range(self,L,R,x):  # [L,R)にxを作用
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self.propagate_above(L0)
        self.propagate_above(R0)
        while L < R:
            if L & 1:
                self.lazy[L] = self.composition(self.lazy[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.lazy[R] = self.composition(self.lazy[R], x)
            L >>= 1
            R >>= 1
        self.eval_above(L0)
        self.eval_above(R0)

# shift = 1 << 32
# mask = (1 << 32) - 1

def monoid_func(s, t):
    sv, sn = s >> 32, s % (1 << 32)
    tv, tn = t >> 32, t % (1 << 32)
    return (((sv + tv) % MOD) << 32) + sn + tn

# g(f(x))の順であることに注意
def composition(f, g):
    fb, fc = f >> 32, f % (1 << 32)
    gb, gc = g >> 32, g % (1 << 32)
    return ((fb * gb % MOD) << 32) + ((gb * fc + gc) % MOD)

#右作用
#雑に可換な処理を書こうとするとバグるので注意
def operate(a,f,_):
    fb, fc = f >> 32, f % (1 << 32)
    av, an = a >> 32, a % (1 << 32)
    return (((fb * av + fc * an) % MOD) << 32) + an

def main():
    monoid_identity = 0
    operator_identity = 1 << 32

    N, Q = LI()
    A = [(ai << 32) + 1 for ai in LI()]
    LST = LazySegTree(A, monoid_func, composition, operate, monoid_identity, operator_identity)

    for q in LIR(Q):
        if q[0] == 0:
            _, l, r, b, c = q
            LST.apply_range(l,r,(b<<32)+c)
        else:
            _, l, r = q
            print(LST.fold(l,r) >> 32)

if __name__ == '__main__':
    main()