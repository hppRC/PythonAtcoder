class DAG:
    def __init__(self, n, AB):
        self.n = n
        self.G = [[] for _ in range(n)]
        self.revG = [[] for _ in range(n)]
        self.AB = AB
        for a, b in AB:
            self.G[a].append(b)
            self.revG[b].append(a)

    def scc(self):
        visited = [False] * self.n
        order = []
        for i in range(self.n):
            if visited[i]: continue

            q = deque([i])
            visited[i] = True
            while q:
                v = q[-1]
                for u in self.G[v]:
                    if not visited[u]:
                        q.append(u)
                        visited[u] = True
                        break
                else:
                    #全て訪問済みの時
                    q.pop()
                    order.append(v)

        visited = [False] * self.n
        scc = []
        for i in order[::-1]:
            if visited[i]: continue
            tmp = [i]
            visited[i] = True
            q = deque([i])

            while q:
                v = q.pop()
                for u in self.revG[v]:
                    if visited[u]: continue
                    visited[u] = True
                    tmp.append(u)
                    q.append(u)
            scc.append(tmp)

        return scc

