class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        self._group_size = [1 for _ in range(n)]
        self.num_of_groups = n

    def find(self, x):
        vs = []
        while self._parent[x] != x:
            vs.append(x)
            x = self._parent[x]
        for v in vs: self._parent[v] = x
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self._rank[px] < self._rank[py]:
            self._parent[px] = py
            self._group_size[py] += self._group_size[px]
        else:
            self._parent[py] = px
            self._group_size[px] += self._group_size[py]
        if self._rank[px] == self._rank[py]: self._rank[py] += 1
        self.num_of_groups -= 1

    def is_same(self, x, y): return self.find(x) == self.find(y)
    def group_size(self, x): return self._group_size[self.find(x)]