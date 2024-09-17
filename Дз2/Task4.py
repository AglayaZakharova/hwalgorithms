def find_circle_num(isConnected):
    n = len(isConnected)
    provinces = 0
    visited = set()

    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    for city in range(n):
        if city not in visited:
            provinces += 1
            dfs(city)

    return provinces

# Проверочка:
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
total_provinces = find_circle_num(isConnected)
print("Total provinces:", total_provinces)
