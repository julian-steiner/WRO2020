from ev3dev2.motor import MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc
import time

class Gripper2:
    def __init__(self):
        self.rc = rc.RobotContainer()
        self.motor = MediumMotor(self.rc.GRIPPER_2)
        self.color1 = ColorSensor(self.rc.COLOR_RECOGNITION)
        self.color2 = ColorSensor(self.rc.COLOR_RECOGNITION2)
    
    def movemotor(self,speed,direction):
        if direction == True:
            direction=-1
        else:
            direction=1
        speed*=direction
        self.motor.on(SpeedPercent(speed))
    
    def EvacuateOrder(self,speed):
        self.motor.on_for_degrees(SpeedPercent(speed),-140)
        time.sleep(0.5)
        self.motor.on_for_degrees(SpeedPercent(speed),140)
