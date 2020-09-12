class Bit:
    def __init__(self, n, default=0): self.size, self.tree = n, [default] * (n + 1)
    # get sum of [0, i]
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i = max(i, 1)
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # get sum of [l, r], or just l
    def get(self, l, r=None):
        if r is None: r = l
        return self.sum(r) - self.sum(l-1)

class ExBIT:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)

    # add x to [l, r] (not [l, r)])
    def add(self, x, l, r=None):
        if r is None: r = l
        r += 1
        self.p.add(l, -x * l)
        self.p.add(r, x * r)
        self.q.add(l, x)
        self.q.add(r, -x)

    def sum(self, l, r):
        r += 1
        return self.p.sum(r) + self.q.sum(r) * r - self.p.sum(l) - self.q.sum(l) * l

    def get(self, l, r=None):
        if r is None: r = l
        return self.sum(l, r)