from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

class RobotContainer:
    DRIVE_LEFT = OUTPUT_C
    DRIVE_RIGHT = OUTPUT_B
    GRIPPER = OUTPUT_A
    GRIPPER_2 = OUTPUT_C
    DRIVE_COLOR_LEFT = INPUT_4
    DRIVE_COLOR_RIGHT = INPUT_3
    COLOR_RECOGNITION = INPUT_1
    COLOR_RECOGNITION2 = INPUT_2
    WHEEL_DIAMETER = 5.5
    WHEEL_DISTANCE = 13
    def __init__(self):
        pass


    
