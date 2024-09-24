from collections import deque, defaultdict

def largestPathValue(colors, edges):
    n = len(colors)
    
    g = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        g[u].append(v)
        in_degree[v] += 1
    
    # Топологическая сортировка
    top_order = []
    queue = deque(i for i in range(n) if in_degree[i] == 0)
    
    while queue:
        node = queue.popleft()
        top_order.append(node)
        for neighbor in g[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(top_order) < n:
        return -1
    
    dp = [[0] * 26 for _ in range(n)]

    for i in range(n):
        dp[i][ord(colors[i]) - ord('a')] = 1
    
    for node in top_order:
        for neighbor in g[node]:
            for c in range(26):
                dp[neighbor][c] = max(dp[neighbor][c], dp[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))
    
    return max(max(row) for row in dp)
