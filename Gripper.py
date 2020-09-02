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
        speed *= -1
        self.motor.on(speed, block=False)
        self.motor.wait_until_not_moving(300)

    def moveMotor(self, speed, degrees):
        self.motor.on_for_degrees(speed, degrees)

    def getColors(self):
        values = []
        def getColor(color):
            if(color[1] < color[2]):
                return "Blue"
            else:
                return "Green"
            return "No color"
        values.append(getColor(self.color1.rgb))
        values.append(getColor(self.color2.rgb))
        return values
