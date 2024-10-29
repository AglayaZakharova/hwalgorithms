from collections import deque

def shortestPathAllKeys(grid):
    m, n = len(grid), len(grid[0])
    start_row, start_col = None, None
    keys = set()
    locks = set()
    for row in range(m):
        for col in range(n):
            if grid[row][col] == '@':
                start_row, start_col = row, col
            elif grid[row][col].islower():
                keys.add(grid[row][col])
            elif grid[row][col].isupper():
                locks.add(grid[row][col])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start_row, start_col, 0, set())])
    visited = set([(start_row, start_col, '')])

    while queue:
        row, col, moves, collected_keys = queue.popleft()

        if len(collected_keys) == len(keys):
            return moves

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != '#':
                new_keys = collected_keys.copy()
                if grid[new_row][new_col].islower():
                    new_keys.add(grid[new_row][new_col])
                if grid[new_row][new_col].isupper():
                    if grid[new_row][new_col].lower() not in new_keys:
                        continue 

                new_state = (new_row, new_col, ''.join(sorted(new_keys)))
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_row, new_col, moves + 1, new_keys))

    return -1
