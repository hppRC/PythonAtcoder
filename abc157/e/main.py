#!usr/bin/env python3
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce, lru_cache
from heapq import heappush, heappop, heapify

import itertools, bisect
import math, fractions
import sys, copy

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

# nodeをリストに変換したらクソ遅かった

import pprint

class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def __str__(self):
        def debug_info(nd):
            return (nd.value - 1, nd.left.value - 1 if nd.left else None, nd.right.value - 1 if nd.right else None)

        def debug_node(nd):
            v = debug_info(nd) if nd.value else ()
            left = debug_node(nd.left) if nd.left else []
            right = debug_node(nd.right) if nd.right else []
            return [v, left, right]

        return pprint.PrettyPrinter(indent=4).pformat(debug_node(self.root))

    __repr__ = __str__

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            # v がすでに存在する場合に何か処理が必要ならここに書く
            if v == nd.value:
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        return self.leftmost(nd.left) if nd.left else nd

    def rightmost(self, nd):
        return self.rightmost(nd.right) if nd.right else nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = nd.value if nd.value < v else 0
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = nd.value if nd.value > v else 0
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def max(self):
        return self.find_l((1<<self.N)-1)

    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd:
            nd = self.root
        if not prev:
            prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return
        if (not nd.left) and (not nd.right):
            if nd.value < prev.value:
                prev.left = None
            else:
                prev.right = None
        elif not nd.left:
            if nd.value < prev.value:
                prev.left = nd.right
            else:
                prev.right = nd.right
        elif not nd.right:
            if nd.value < prev.value:
                prev.left = nd.left
            else:
                prev.right = nd.left
        else:
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)

    # v以下のものの中での最大値
    def upper_bound(self, v):
        upper = self.find_r(v)
        return self.find_l(upper)

    def lower_bound(self, v):
        lower = self.find_l(v)
        return self.find_r(lower)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

def main():
    N = I()
    s = S()
    Q = I()
    query = LR(Q)

    trees = {ch: BalancingTree(25) for ch in alphabets}

    for i, ch in enumerate(s):
        trees[ch].append(i)

    for q in query:
        if q[0] == "1":
            _, i, c = q
            i = int(i) - 1
            prev = s[i]
            trees[prev].delete(i)
            s[i] = c
            trees[c].append(i)
        else:
            _, l, r = q
            l, r = int(l) - 1, int(r) - 1
            count = 0
            for _, tree in trees.items():
                first = tree.lower_bound(l)
                if first != tree.root.value - 1 and first <= r:
                    count += 1
            print(count)



if __name__ == '__main__':
    main()

