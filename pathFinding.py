import heapq

# Define directions (up, down, left, right)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        est_total, cost, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for dx, dy in DIRS:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost + 1
                heapq.heappush(open_set, (
                    new_cost + heuristic((nx, ny), goal),
                    new_cost,
                    (nx, ny),
                    path + [(nx, ny)]
                ))
    return None  # No path found
