def adjacency_list(N, edges):
    g = make_list(N, 0)
    for a, b in edges: g[a].append(b), g[b].append(a)
    return g
def tree_utils(start, g):
    parent, children, depth, q = [-1]*len(g), make_list(len(g), 0), [-1]*len(g), deque([start]); depth[start] = 0
    while q:
        i = q.popleft()
        for j in g[i]:
            if depth[j] != -1: parent[i] = j
            else: depth[j] = depth[i] + 1; children[i].append(j), q.append(j)
    return parent, children, depth
def graph_distance(start, g):
    dist, q = [-1] * len(g), deque([start]); dist[start] = 0
    while q:
        i = q.popleft()
        for j in g[i]:
            if dist[j] == -1: dist[j] = dist[i] + 1; q.append(j)
    return dist