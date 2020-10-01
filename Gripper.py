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
        self.motor.stop()

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

    def RomerColor(self):
        def convertColor(num):
            if num == 0:
                return "Blue"
            elif num == 1:
                return "Green"
            elif num == 2:
                return "None"

        for i in range(10):
            c1 = self.color1.rgb
            c2 = self.color2.rgb
            c = [[11, 35, 90], [8, 60, 20], [6, 3, 5]]
            # 0 = blue, 1 = green, 2 = no color
            diff1 = []
            diff2 = []
            for i in range(len(c)):
                v1 = 0
                v2 = 0
                for j in range(3):
                    v1 += (c[i][j] - c1[j])**2
                    v2 += (c[i][j] - c2[j])**2
                diff1.append(v1)
                diff2.append(v2)
            indeces = []
            indeces.append(convertColor(diff1.index(min(diff1))))
            indeces.append(convertColor(diff2.index(min(diff2))))
            return indeces
    
