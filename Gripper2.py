from ev3dev2.motor import MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc
from Motors import Motors
import time

class Gripper2:
    def __init__(self):
        self.rc = rc.RobotContainer()
    
    def movemotor(self,speed,direction):
        if direction == True:
            direction=-1
        else:
            direction=1
        speed*=direction
        Motors.Gripper2.gripperMotor.on(SpeedPercent(speed))

    def RomerColorPU(self):
        def convertColor(num):
            if num == 0:
                return "Red"
            elif num == 1:
                return "Yellow"
            elif num == 2:
                return "None"

        c2 = Motors.Gripper2.colorSensor.rgb
        c = [[51, 1, 4], [44, 9, 3], [40, 20, 25]]
        print(c2)
        diff2 = []
        for i in range(len(c)):
            v2 = 0
            for j in range(3):
                v2 += (c[i][j] - c2[j])**2
            diff2.append(v2)
        
        return convertColor(diff2.index(min(diff2)))

    def RomerColorPD(self):
        def convertColor(num):
            if num == 0:
                return "Red"
            elif num == 1:
                return "Yellow"

        for i in range(10):
            c2 = Motors.Gripper2.colorSensor.rgb
            print(c2)
            c = [[150, 15, 5], [175, 74, 10]]
            diff2 = []
            for i in range(len(c)):
                v2 = 0
                for j in range(3):
                    v2 += (c[i][j] - c2[j])**2
                diff2.append(v2)
            indeces = []
            indeces.append(convertColor(diff2.index(min(diff2))))
            return indeces[0]