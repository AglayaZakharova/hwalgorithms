# Я во Флойда загнала матрицу предшественников, и с помощью нее потом в get_shortest_path нахожу путь
def floyd_warshall_with_paths(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[-1] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                pred[i][j] = i


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


def get_shortest_path(pred, start, end):
    path = []
    if pred[start][end] == -1 and start != end:
        return None

    curr = end
    while curr != start:
        path.insert(0, curr)
        curr = pred[start][curr]
    path.insert(0, start)
    return path


# Проверочка
graph = [
    [0, 4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf')],
    [4, 0, 8, float('inf'), float('inf'), float('inf'), float('inf'), 11, float('inf')],
    [float('inf'), 8, 0, 7, float('inf'), 4, float('inf'), float('inf'), 2],
    [float('inf'), float('inf'), 7, 0, 9, 14, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), 9, 0, 10, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 4, 14, 10, 0, 2, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 0, 1, 6],
    [8, 11, float('inf'), float('inf'), float('inf'), float('inf'), 1, 0, 7],
    [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), 6, 7, 0]
]

dist, pred = floyd_warshall_with_paths(graph)

start_node = 0
end_node = 4

shortest_path = get_shortest_path(pred, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path exists between {start_node} and {end_node}")