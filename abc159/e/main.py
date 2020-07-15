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

def bit_pattern(bits, length):
    return [(bits >> i) & 1 for i in range(length)]

def main():
    H, W, K = LI()
    s = SR(H)

    ans = float("inf")

    for i in range(1 << (H - 1)):
        pattern = bit_pattern(i, H-1)
        divided = []
        tmp = [s[0]]
        tmp_ans = 0

        for i, bit in enumerate(pattern):
            if bit:
                tmp_ans += 1
                divided.append(tmp)
                tmp = [s[i+1]]
            else:
                tmp.append(s[i+1])
        divided.append(tmp)

        whites = []

        for block in divided:
            white = [0] * W
            for row in block:
                for i, panel in enumerate(row):
                    if panel == "1":
                        white[i] += 1
            whites.append(white)

        curs = [0] * len(whites)
        outer = False
        for w in range(W):
            for i, white in enumerate(whites):
                if white[w] > K:
                    outer = True
                    break
                elif white[w] + curs[i] > K:
                    curs = [white[w] for white in whites]
                    tmp_ans += 1
                    break
                else:
                    curs[i] += white[w]
            else:
                continue
            if outer:
                break
        else:
            ans = min(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()