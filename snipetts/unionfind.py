class UnionFind:
    def __init__(self, N): self.N, self.group_count, self.root, self.rank = N, N, [-1] * N, [0] * N
    def __repr__(self): return str(self.all_groups())

    def find(self, x):
        while self.root[x] >= 0: x = self.root[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.rank[x] > self.rank[y]: x, y = y, x
        self.root[y] += self.root[x]
        self.root[x] = y
        if self.rank[x] == self.rank[y]: self.rank[y] += 1
        self.group_count -= 1

    def same(self, x, y): return self.find(x) == self.find(y)
    def count(self, x): return -self.root[self.find(x)]
    def members(self, x): return [i for i in range(self.N) if self.same(x, i)]
    def roots(self): return [i for i, x in enumerate(self.root) if x < 0]
    def all_groups(self):
        d = defaultdict(lambda: [])
        for i in range(self.N): d[self.find(i)].append(i)
        return dict(d)