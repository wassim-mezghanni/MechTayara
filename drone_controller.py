from djitellopy import Tello
import time

MOVE_DIST = 30

def init_drone():
    tello = Tello()
    tello.connect()
    tello.streamon()
    tello.takeoff()
    time.sleep(2)
    return tello

def move_drone(tello, current, target):
    dx, dy = target[0] - current[0], target[1] - current[1]
    if dx == 1:
        tello.move_forward(MOVE_DIST)
    elif dx == -1:
        tello.move_back(MOVE_DIST)
    elif dy == 1:
        tello.move_right(MOVE_DIST)
    elif dy == -1:
        tello.move_left(MOVE_DIST)

def safe_land(tello):
    tello.land()
    tello.streamoff()