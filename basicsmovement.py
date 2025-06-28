from djitellopy import Tello
import time
import math
from pathFinding import a_star

# Replace grid steps with actual coordinates or fixed movement
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

# Coordinates of buildings (as grid positions)
building_A = (0, 0)
building_B = (4, 3)

path = a_star(grid, building_A, building_B)

print("Path from A to B:")
for step in path:
    print(step)
tello = Tello()


# simulate 1 grid cell = 50 cm
step_size_cm = 10
z = 50  # fixed height in cm


try:
    tello.connect()
    print(f"Battery level: {tello.get_battery()}%")
    tello.takeoff()
    # tello.move_up(z)

    # Optional: Abort if battery too low
    # if tello.get_battery() < 20:
    #     raise Exception("Battery too low for safe flight")


    for i in range(1, len(path)):
        dx = (path[i][1] - path[i - 1][1]) * step_size_cm
        dy = (path[i - 1][0] - path[i][0]) * step_size_cm  # Invert Y

        # Calculate the angle to face the correct direction
        if dx > 0 and dy == 0:  # Moving right
            yaw_angle = 90
        elif dx < 0 and dy == 0:  # Moving left
            yaw_angle = -90
        elif dy > 0 and dx == 0:  # Moving up
            yaw_angle = 0
        elif dy < 0 and dx == 0:  # Moving down
            yaw_angle = 180
        else:
            yaw_angle = int(math.degrees(math.atan2(dy, dx)))  # Diagonal movement

        # Rotate to face the correct direction
        tello.rotate_clockwise(yaw_angle) if yaw_angle >= 0 else tello.rotate_counter_clockwise(abs(yaw_angle))

        # Calculate the distance to move forward
        distance = int((dx**2 + dy**2)**0.5)

        # Move forward
        tello.move_forward(distance)
        time.sleep(2)

    tello.land()

except KeyboardInterrupt:
    print("🔴 Manual abort! Landing now.")
    tello.land()

except Exception as e:
    print(f"⚠️ Emergency: {e}")
    tello.land()

finally:
    tello.end()