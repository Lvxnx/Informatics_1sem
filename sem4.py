def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]

    return True, (set1, set2)


def kuhn(graph):
    n = len(graph.keys())
    match = [-1] * n
    vis = [False] * n
    _, parts = bipartite(graph)
    L = parts[0]
    def dfs(v):
        for u in graph[v]:
            if not vis[u]:
                vis[u] = True
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False
    for v in L:
        vis = [False] * n
        dfs(v)
    return match


def orientation(graph):
    match = kuhn(graph)
    or_graph = {u: [] for u in graph.keys()}
    for u in graph:
        for v in graph[u]:
            if match[v] == u:
                or_graph[v].append(u)
            else:
                or_graph[u].append(v)
    return or_graph


def dfs0(graph, m, L):
    n = len(graph.keys())
    vis = [False] * n
    l_p = []
    l_m = []
    r_p = []
    r_m = []
    def dfs1(v):
        vis[v] = True
        if v in L:
            l_p.append(v)
        else:
            r_p.append(v)
        for u in graph[v]:
            if not vis[u]:
                dfs1(u)
    f = []
    for v in L:
        if m[v] == -1:
            f.append(v)
    for v in f:
        if not vis[v]:
            dfs1(v)
    for v in L:
        if v not in l_p:
            l_m.append(v)
    for v in range(n):
        if v not in L and v not in r_p:
            r_m.append(v)
    return l_p, l_m, r_p, r_m

def left(graph):
    is_bipartite, parts = bipartite(graph)
    if not is_bipartite:
        raise ValueError("Граф не является двудольным.")
    return parts[0]


G = {}
G[0] = [1, 3]
G[1] = [0, 2, 6]
G[2] = [1]
G[3] = [4]
G[4] = [3, 5, 7]
G[5] = [0, 4]
G[6] = [1]
G[7] = [4]

print(bipartite(G))
print(kuhn(G))
print(orientation(G))
l_p, l_m, r_p, r_m = dfs0(G, kuhn(G), left(G))
print ("Минимальное вершинное покрытиеЖ ", l_m + r_p)