from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_source(self, source_node):
        self.add_node(source_node)

    def add_sink(self, sink_node):
        self.add_node(sink_node)


    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))


    def edmonds_karp(graph, source, sink):
        flow = 0
        residual_graph = {node: {neighbor: capacity for neighbor, capacity in adj.items()}
                        for node, adj in graph.items()}

        while True:
            queue = deque([source])
            parent = {source: None}
            path_found = False

            while queue:
                current_node = queue.popleft()
                if current_node == sink:
                    path_found = True
                    break

                for neighbor, capacity in residual_graph[current_node].items():
                    if capacity > 0 and neighbor not in parent:
                        parent[neighbor] = current_node
                        queue.append(neighbor)

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


def min_cells_to_paint(field, minotaur_positions):
    rows, cols = len(field), len(field[0])
    graph = nx.DiGraph()

    graph.add_node("source")
    graph.add_node("sink")

    unpainted_cells = []
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 0:
                unpainted_cells.append((r, c))
                graph.add_node((r, c))


    for r, c in unpainted_cells:
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            graph.add_edge("source", (r, c), capacity=1)

    for r1, c1 in unpainted_cells:
        for r2, c2 in unpainted_cells:
            if abs(r1 - r2) + abs(c1 - c2) == 1:
                graph.add_edge((r1, c1), (r2, c2), capacity=1)

    for r, c in minotaur_positions:
        graph.add_edge((r, c), "sink", capacity=1)


    max_flow_value = nx.maximum_flow_value(graph, "source", "sink", capacity='capacity')

    return max_flow_value


# Example usage:
field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
minotaur_positions = [(1, 1)] # Minotaur in the center


min_paint = min_cells_to_paint(field, minotaur_positions)
print(f"Minimum number of cells to paint: {min_paint}")


field2 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
minotaur_positions2 = [(0,0), (3,3)]

min_paint2 = min_cells_to_paint(field2, minotaur_positions2)
print(f"Minimum number of cells to paint: {min_paint2}")

