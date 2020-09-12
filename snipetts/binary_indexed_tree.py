class BIT:
    def __init__(self, li):
        self.n, self.data = len(li) + 1, [0] + li
        for i in range(1, self.n):
            if i + (i & -i) < self.n: self.data[i + (i & -i)] += self.data[i]

    def add(self, i, a):
        i += 1
        while i < self.n:
            self.data[i] += a
            i += i & -i

    # sum of [0, i)
    def acc(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    # sum of [l, r)
    def get(self, l, r = None):
        if r is None: r = l+1
        return self.acc(r) - self.acc(l)


# class ExBIT:
#     def __init__(self, n):
#         self.p = Bit(n + 1)
#         self.q = Bit(n + 1)

#     # add x to [l, r] (not [l, r)])
#     def add(self, x, l, r=None):
#         if r is None: r = l
#         r += 1
#         self.p.add(l, -x * l)
#         self.p.add(r, x * r)
#         self.q.add(l, x)
#         self.q.add(r, -x)

#     def sum(self, l, r):
#         r += 1
#         return self.p.sum(r) + self.q.sum(r) * r - self.p.sum(l) - self.q.sum(l) * l

#     def get(self, l, r=None):
#         if r is None: r = l
#         return self.sum(l, r)