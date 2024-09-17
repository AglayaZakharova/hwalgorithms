# Я в этой задаче в качестве списка смежности использую dict

def are_they_reachable(g, v, u):
    # рекурсивная функция поиска всех путей
    def find_all_paths(g, start, end):
        path = []
        path += [start]
        if start == end:
            return [path]
        if not g.has_key(start):
            return []
        paths = []
        for node in g[start]:
            if node not in path:
                newpaths = find_all_paths(g, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    if find_all_paths(g, v, u) and find_all_paths(g, u, v): # Если оба списка непустые, значит вершины взаимно достижимы
        return True
    else:
        return False