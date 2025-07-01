from djitellopy import Tello
import time
import heapq
import cv2

# Define the map grid (0 = free, 1 = obstacle)
map_grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 3)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
MOVE_DIST = 30
OBSTACLE_THRESHOLD = 300

# A* components
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                heapq.heappush(open_set, (cost + 1 + heuristic((nx, ny), goal), cost + 1, (nx, ny), path + [(nx, ny)]))
    return None

def confirm_obstacle(tello, retries=3):
    count = 0
    for _ in range(retries):
        frame = tello.get_frame_read().frame
        frame = cv2.resize(frame, (480, 360))
        if detect_obstacle(frame):
            count += 1
        time.sleep(0.1)  # Small delay
    return count >= retries - 1  # Confirm obstacle

# Visual detection placeholder
def detect_obstacle(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    h, w = edges.shape
    roi = edges[h//3:2*h//3, w//3:2*w//3]
    return cv2.countNonZero(roi) > OBSTACLE_THRESHOLD

# Initialize Tello
tello = Tello()
tello.connect()
tello.streamon()
tello.takeoff()
time.sleep(2)

current_position = start
path = a_star_search(map_grid, current_position, goal)

while path:
    print("Path:", path)
    for i in range(1, len(path)):
        next_position = path[i]
        frame = tello.get_frame_read().frame
        frame = cv2.resize(frame, (480, 360))

        if detect_obstacle(frame):
            print("Obstacle detected at:", next_position)
            map_grid[next_position[0]][next_position[1]] = 1
            path = a_star_search(map_grid, current_position, goal)
            break  # Break to restart with a new path

        x1, y1 = current_position
        x2, y2 = next_position
        dx, dy = x2 - x1, y2 - y1

        if dx == 1:
            tello.move_forward(MOVE_DIST)
        elif dx == -1:
            tello.move_back(MOVE_DIST)
        elif dy == 1:
            tello.move_right(MOVE_DIST)
        elif dy == -1:
            tello.move_left(MOVE_DIST)

        current_position = next_position
        cv2.imshow("Drone View", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break  # Exit while loop if we reached goal

print("Landing")
tello.land()
tello.streamoff()
cv2.destroyAllWindows()

