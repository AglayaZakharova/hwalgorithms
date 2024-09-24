from collections import defaultdict

def find_strongly_connected_components(g):
    n = len(g)
    visited = [False] * n
    stack = []
    index = [0] * n
    lowlink = [0] * n
    index_counter = 0
    strongly_connected_components = []

    def dfs(node):
        nonlocal index_counter, strongly_connected_components
        index[node] = lowlink[node] = index_counter
        index_counter += 1
        stack.append(node)
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in stack:
                lowlink[node] = min(lowlink[node], index[neighbor])
        if index[node] == lowlink[node]:
            scc = []
            while stack[-1] != node:
                scc.append(stack.pop())
            scc.append(stack.pop())
            strongly_connected_components.append(scc)

    for node in range(n):
        if not visited[node]:
            dfs(node)
    return strongly_connected_components

def count_edges_to_make_strongly_connected(graph):
    sccs = find_strongly_connected_components(graph)
    # Компонент-граф
    comp_graph = defaultdict(list)
    for scc in sccs:
        for node in scc:
            for neighbor in graph[node]:
                if neighbor not in scc:
                    comp_graph[tuple(scc)].append(tuple([neighbor for neighbor in sccs if neighbor != scc and neighbor.intersection(graph[node])]))

    root_scc = None
    for scc in comp_graph:
        if not comp_graph[scc]:
            root_scc = scc
            break
    if root_scc is None:
        return -1 # Граф уже односвязный
    return len(comp_graph) - 1

# Проверочка
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [4],
    4: []
}
edges_needed = count_edges_to_make_strongly_connected(graph)
print("Нужно минимум", edges_needed)
