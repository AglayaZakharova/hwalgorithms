from collections import deque


# класс со встроенным эдмондсом-карпом для задачки
class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, u, v, capacity):
        self.add_node(u)
        self.add_node(v)
        self.graph[u][v] = capacity

    def edmonds_karp(self, source, sink):
        flow = 0
        residual_graph = {node: {neighbor: cap for neighbor, cap in adj.items()}
                          for node, adj in self.graph.items()}
        while True:
            queue = deque([source])
            parent = {source: None}
            visited = {source}

            path_found = False
            while queue:
                u = queue.popleft()
                if u == sink:
                    path_found = True
                    break
                for v, capacity in residual_graph.get(u, {}).items():
                    if capacity > 0 and v not in visited:
                        parent[v] = u
                        visited.add(v)
                        queue.append(v)

            if not path_found:
                break

            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]

            flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] = residual_graph.get(v, {}).get(u, 0) + path_flow
                v = u

        return flow


def solve_alien(field, alien_positions):
    rows, cols = len(field), len(field[0])
    graph = DirectedGraph()
    graph.add_node("source")
    graph.add_node("sink")

    nodes = {}
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 0:
                node_id = (r, c)
                nodes[node_id] = node_id
                graph.add_node(node_id)
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    graph.add_edge("source", node_id, 10**9)
                if (r, c) in alien_positions:
                    graph.add_edge(node_id, "sink", 10**9)

    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 0:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and field[nr][nc] == 0:
                        graph.add_edge(nodes[(r,c)], nodes[(nr, nc)], 1)

    max_flow = graph.edmonds_karp("source", "sink")
    return max(0, max_flow) # максимальный поток и есть минимальное количество клеточек для закраски


# Тестики:
field = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
alien_positions = [(1, 1)]
print(f"Min blocks: {solve_alien(field, alien_positions)}") # Output: 4


field2 = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]
alien_positions2 = [(2, 2), (3, 3)]
print(f"Min blocks: {solve_alien(field2, alien_positions2)}") # Output: 3


field3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
alien_positions3 = [(1, 1)]
print(f"Min blocks: {solve_alien(field3, alien_positions3)}") # Output: 4
