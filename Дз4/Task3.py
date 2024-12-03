from collections import deque

def parse_maze(maze_str):
    maze = [list(line) for line in maze_str.strip().split('\n')]
    return maze

def bfs(start, maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    queue = deque([start])
    distances[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                if distances[nx][ny] > distances[x][y] + 1:
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))
    return distances

def find_meeting_point(a_distances, b_distances, f_position, maze):
    min_cost = float('inf')
    best_meeting_point = None

    rows, cols = len(maze), len(maze[0])

    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == '.' or (x, y) == f_position:
                am = a_distances[x][y]
                bm = b_distances[x][y]
                mf = a_distances[f_position[0]][f_position[1]]
                
                cost = (am if am < float('inf') else 0) + (bm if bm < float('inf') else 0) + mf
                if cost < min_cost:
                    min_cost = cost
                    best_meeting_point = (x, y)

    return best_meeting_point

def mark_path(maze, start, end, distances):
    path = []
    x, y = end
    
    while (x, y) != start:
        path.append((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if distances[nx][ny] == distances[x][y] - 1:
                    x, y = nx, ny
                    break
    path.append(start)
    return path

def navigate_robots(maze_str):
    maze = parse_maze(maze_str)
    rows, cols = len(maze), len(maze[0])

    a_start = None
    b_start = None
    f_position = None

    # Ищем позиции A, B и F
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'A':
                a_start = (i, j)
            elif maze[i][j] == 'B':
                b_start = (i, j)
            elif maze[i][j] == 'F':
                f_position = (i, j)

    a_distances = bfs(a_start, maze)
    b_distances = bfs(b_start, maze)

    meeting_point = find_meeting_point(a_distances, b_distances, f_position, maze)

    # Обозначим путь для роботов
    if meeting_point:
        am_path = mark_path(maze, a_start, meeting_point, a_distances)
        bm_path = mark_path(maze, b_start, meeting_point, b_distances)

        # Маркируем путь
        for x, y in am_path:
            if maze[x][y] not in ('A', 'B', 'F'):
                maze[x][y] = 'o'
        for x, y in bm_path:
            if maze[x][y] not in ('A', 'B', 'F'):
                maze[x][y] = 'o'

        if meeting_point != f_position:
            mx, my = meeting_point
            maze[mx][my] = 'M'

    # Возвращаем результат в виде строки
    return '\n'.join(''.join(row) for row in maze)

# Тест
maze = """
######
#A...#
#....#
#..F.#
#B.#.#
######
"""

result = navigate_robots(maze)
print(result)
