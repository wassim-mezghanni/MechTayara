from map_config import map_grid, start, goal
from path_planning import a_star_search
from drone_controller import init_drone, move_drone, safe_land
from obstacle_detection import detect_obstacle

tello = init_drone()
current_position = start
path = a_star_search(map_grid, current_position, goal)

while path:
    for i in range(1, len(path)):
        next_position = path[i]
        frame = tello.get_frame_read().frame
        # Resize frame for processing
        frame = cv2.resize(frame, (480, 360))

        if detect_obstacle(frame):
            print("Obstacle detected at:", next_position)
            map_grid[next_position[0]][next_position[1]] = 1
            path = a_star_search(map_grid, current_position, goal)
            break

        move_drone(tello, current_position, next_position)
        current_position = next_position

safe_land(tello)