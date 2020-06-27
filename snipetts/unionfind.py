class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        self._group_size = [1 for _ in range(n)]
        self.num_of_groups = n

    def find(self, x):
        if self._parent[x] == x:
            return x
        px = self._parent[x]
        root = self.find(px)
        self._parent[x] = root
        return root

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self._rank[px] < self._rank[py]:
            self._parent[px] = py
            self._group_size[py] += self._group_size[px]
        else:
            self._parent[py] = px
            self._group_size[px] += self._group_size[py]
        if self._rank[px] == self._rank[py]:
            self._rank[py] += 1
        self.num_of_groups -= 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        px = self.find(x)
        return self._group_size[px]
