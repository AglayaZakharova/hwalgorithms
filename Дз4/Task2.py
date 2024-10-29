from collections import deque

def find_exit(maze_str):
    maze = [list(line) for line in maze_str.strip().split('\n')]
    rows, cols = len(maze), len(maze[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start = None
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                queue.append((r, c, []))
                break
        if start:
            break

    if not start:
        print("Starting point 'S' not found.")
        return maze

    visited = set()
    visited.add(start)

    while queue:
        x, y, path = queue.popleft()

        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            for px, py in path:
                if maze[px][py] == '.':
                    maze[px][py] = 'o'
            maze[start[0]][start[1]] = 'S'
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if maze[nx][ny] in {'.', 'S'}:
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(x, y)]))

    for line in maze:
        print(''.join(line))

# Тест
maze = """
#####
#.S.#
###.#
#...#
#.###
"""
find_exit(maze)


