from ev3dev2.motor import OUTPUT_A, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc
from Motors import Motors

class Gripper:
    def __init__(self):
        self.rc = rc.RobotContainer()
    
    def lowerMotor(self, speed):
        Motors.Gripper1.gripperMotor.on(speed, block=False)
        Motors.Gripper1.gripperMotor.wait_until_not_moving(300)
        Motors.Gripper1.gripperMotor.stop()

    def moveMotor(self, speed, degrees):
        Motors.Gripper1.gripperMotor.on_for_degrees(speed, degrees)

    def getColors(self):
        values = []
        def getColor(color):
            if(color[1] < color[2]):
                return "Blue"
            else:
                return "Green"
            return "No color"
        values.append(getColor(Motors.Gripper1.colorSensor.rgb))
        values.append(getColor(Motors.Gripper2.colorSensor.rgb))
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
            c1 = Motors.Gripper1.colorSensor.rgb
            c2 = Motors.Gripper2.colorSensor.rgb
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
    
