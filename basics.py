from djitellopy import Tello
import time
tello = Tello()
# tello.connect()
# print(f"Battery level: {tello.get_battery()}%")
# tello.takeoff()
# time.sleep(3)
# tello.move_up(50)  
# time.sleep(3)
# tello.move_forward(30)  
# time.sleep(3)
# tello.rotate_clockwise(90)
# time.sleep(3)
# tello.move_forward(30)
# time.sleep(3)
# tello.land()

# from djitellopy import Tello
# tello = Tello()

tello.connect()
tello.takeoff()
print(tello.get_battery())
tello.move_up(50)
tello.move_left(50)
tello.rotate_counter_clockwise(90)
tello.move_forward(50)
tello.land()