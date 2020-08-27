from ev3dev2.motor import OUTPUT_A, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc

class Gripper:
    def __init__(self):
        self.rc = rc.RobotContainer()
        self.motor = MediumMotor(self.rc.GRIPPER)
        self.color1 = ColorSensor(self.rc.COLOR_RECOGNITION)
        self.color2 = ColorSensor(self.rc.COLOR_RECOGNITION2)
    
    def lowerMotor(self, speed):
        self.motor.on(speed, block=False)
        self.motor.wait_until_not_moving(300)

    def getColors(self):
