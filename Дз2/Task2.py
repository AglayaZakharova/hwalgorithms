# список ребер в список смежности
def to_adj_list_from_edge_list(pg, n):
    g = dict()
    for v, u in pg:
        if v not in g.keys():
            g[v] = [u]
        else:
            g[v].append(u)
    return g

def topological_sort(g):
    visited = [0 for i in range(len(g))]
    order = []
    def dfs(v):
        for v in g.keys():
            visited[v] = True
            for u in g[v]:
                if not visited[v]:
                    dfs(u)
            order.append(v)
        for v in range(len(g)):
            if not visited[v]:
                dfs(v)

        return list(reversed(order))


pg = {("Галстук", "Пиджак"),("Носки", "Туфли"),("Рубашка", "Ремень"), ("Рубашка", "Галстук"),
("Ремень", "Пиджак"), ("Трусы", "Брюки"),("Трусы", "Туфли"),("Брюки", "Туфли"),
("Брюки", "Ремень")}
g = to_adj_list_from_edge_list(pg, 10)
print(topological_sort(g))