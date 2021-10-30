# WORKS SUCCESSFULLY

# 1. Have a drone
# 2. App setup and Test Run
    #  App -> TELLO
    # settings -> More -> Firmware update

# 3. Basic Movement
    # install djitello
    # install opencv
from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
# print(me.get_battery())

me.takeoff()

# me.move_forward(30)
me.send_rc_control(0, 50, 0, 0) # left/right, front/back, up/down, rotation
sleep(2)
me.send_rc_control(30, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.land()