# still buggy
# https://tjkendev.github.io/procon-library/python/range_query/rmq_ruq_segment_tree_lp.html
class LazySegmentTree:
    # N: 処理する区間の長さ
    # 0-indexed, if N == 10 => [0 ~ 9]
    # min version
    # seg = LazySegmentTree(N, f=min, default=float("inf"))
    def __init__(self, N, f=lambda x,y: x+y, default=0):
        self.N = N
        self.default = default
        self.f = f

        self.LV = (N-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [self.default]*(2*self.N0)
        self.lazy = [None]*(2*self.N0)

    # 伝搬対象の区間を求める
    def gindex(self, l, r):
        L = (l + self.N0) >> 1
        R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i: yield R
            if L < R and lc <= i: yield L
            L >>= 1
            R >>= 1

    # 遅延伝搬処理
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None: continue
            self.lazy[2*i-1] = self.data[2*i-1] = self.lazy[2*i] = self.data[2*i] = v
            self.lazy[i-1] = None

    # 区間[l, r)をxで更新
    def update(self, x, l, r=None):
        if r is None: r = l + 1

        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L, R = self.N0 + l, self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.data[R-1] = x
            if L & 1:
                self.lazy[L-1] = self.data[L-1] = x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.f(self.data[2*i-1], self.data[2*i])

    # 区間演算: [l, r)にxでfを作用させる
    def affect(self, x, l, r=None):
        if r is None: r = l + 1

        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L, R = self.N0 + l, self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.f(self.data[R-1], x)
                self.data[R-1] = self.f(self.data[R-1], x)
            if L & 1:
                self.lazy[L-1] = self.f(self.data[L-1], x)
                self.data[L-1] = self.f(self.data[L-1], x)
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.f(self.data[2*i-1], self.data[2*i])

    # 区間[l, r)内の最小値を求める
    def query(self, l, r=None):
        if r is None: r = l + 1
        self.propagates(*self.gindex(l, r))
        L, R = self.N0 + l, self.N0 + r

        s = self.default
        while L < R:
            if R & 1:
                R -= 1
                s = self.f(s, self.data[R-1])
            if L & 1:
                s = self.f(s, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s
