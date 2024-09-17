# список ребер в список смежности
def to_adj_list_from_edge_list(pg, n):
    g = [[] for i in range(n)]
    for v, u in pg:
        g[v].append(u)
    return g

# список смежности в список ребер
def to_edge_list_from_adj_list(g, n):
    pg = []
    for v in range(n):
        pg.append((v, g[v]))
    return pg


# список ребер в матрицу смежности
def to_adj_matr_from_edge_list(pg):
    matr_size = len(set([n for i in pg for n in i]))
    matr = [[0] * matr_size for _ in range(matr_size)]
    for v, u in g:
        matr[v][u] = 1
    return matr


# матрица смежности в список ребер
def to_edge_list_from_adj_matr(matr):
    pg = [[i, j] for i, l in enumerate(matr) for j, x in enumerate(l) if x]
    return pg


# список смежности в матрицу смежности
def to_adj_matr_from_adj_list(g, n):
    matr = [[0 for j in range(n)] 
            for i in range(n)]
    for i in range(n):
        for j in g[i]:
            matr[i][j] = 1
    return matr


# матрица смежности в список смежности
def to_adj_list_from_adj_matr(matr):
    g = []
    for i in range(len(matr)):
        for j in range(len(matr[i])):
                       if matr[i][j] != 0:
                           g[i].append(j)
    return g
