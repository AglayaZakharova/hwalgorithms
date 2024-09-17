from collections import defaultdict

# У меня тут g - это словарь с зависимостями
def topological_sort(g):
    # Считаем смежные
    in_degree = defaultdict(int)
    for node in g:
        for dependent in g[node]:
            in_degree[dependent] += 1

    # Очередь со всеми вершинами без смежных
    queue = [node for node in g if in_degree[node] == 0]

    sorted_list = []

    # Идем по всем вершинам в очереди
    while queue:
        node = queue.pop(0)
        sorted_list.append(node)

        # Обрабатываем смежные
        for dependent in g[node]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # Проверка, все ли вершины обработаны
    if len(sorted_list) != len(g):
        return None # Существует цикл

    return sorted_list


# Проверочка:
g = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': ['G'],
  'E': ['H'],
  'F': [],
  'G': [],
  'H': []
}

sorted_order = topological_sort(g)

if sorted_order:
  print("Topological Sort:", sorted_order)
else:
  print("Cycle detected.")
