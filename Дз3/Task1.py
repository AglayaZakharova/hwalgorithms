def criticalConnections(n, connections):
        g = [[] for _ in range(n)]
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        visited = [-1] * n
        low = [float('inf')] * n # Самая глубокая вершина для данной
        disc = [float('inf')] * n
        parent = [-1] * n
        time = 0
        result = []

        def dfs(node):
            nonlocal time
            visited[node] = disc[node] = low[node] = time
            time += 1

            for neighbor in g[node]:
                if visited[neighbor] == -1:
                    parent[neighbor] = node
                    dfs(neighbor)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        result.append([node, neighbor])
                elif neighbor != parent[node]:
                    low[node] = min(low[node], disc[neighbor])

        for i in range(n): # Идем по всем вершинам в глубину
            if visited[i] == -1:
                dfs(i)

        return result


# Проверочка
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
critical_connections_result = criticalConnections(n, connections)
print(f"Critical Connections: {critical_connections_result}") # Должно быть: [[1, 3]]
