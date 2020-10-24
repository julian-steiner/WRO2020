from ev3dev2.motor import MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc
from Motors import Motors
import time

class Gripper2:
    def __init__(self):
        self.rc = rc.RobotContainer()
        # self.motor = MediumMotor(self.rc.GRIPPER_2)
        # self.color1 = ColorSensor(self.rc.COLOR_RECOGNITION)
        # self.color2 = ColorSensor(self.rc.COLOR_RECOGNITION2)
    
    def movemotor(self,speed,direction):
        if direction == True:
            direction=-1
        else:
            direction=1
        speed*=direction
        # self.motor.on(SpeedPercent(speed))
        Motors.Gripper2.gripperMotor.on(SpeedPercent(speed))
    
    def EvacuateOrder(self,speed):
        # self.motor.on_for_degrees(SpeedPercent(speed),-140)
        Motors.Gripper2.gripperMotor.on(SpeedPercent(speed), -140)
        time.sleep(0.5)
        Motors.Gripper2.gripperMotor.on_for_degrees(SpeedPercent(speed),140)
