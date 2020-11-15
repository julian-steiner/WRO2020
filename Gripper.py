from ev3dev2.motor import OUTPUT_A, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
import RobotContainer as rc
from Motors import Motors

class Gripper:
    def __init__(self):
        self.rc = rc.RobotContainer()
    
    def lowerMotor(self, speed):
        #Moves the motor until it stops (positive = up)
        Motors.Gripper1.gripperMotor.on(speed, block=False)
        Motors.Gripper1.gripperMotor.wait_until_not_moving(400)
        Motors.Gripper1.gripperMotor.stop()

    def moveMotor(self, speed, degrees):
        Motors.Gripper1.gripperMotor.on_for_degrees(speed, degrees)

    def getColor(self):
        #get the color
        corr_factor = 1.4
        def getColor(color):
            if(color[1]*corr_factor <= color[2]):
                return "Blue"
            else:
                return "Green"
            return "No color"

        return getColor(Motors.Gripper1.colorSensor.rgb)

    def getCardColor(self):
        #scan the card, distance is 2 cm near the line
        rgb = Motors.Gripper1.colorSensor.rgb
        if(rgb[1] > 4):
            return "Yellow"
        return "Red"

    def RomerColor(self, color1, color2, color3, colorname1, colorname2, colorname3):
        def convertColor(num):
            if num == 0:
                return colorname1
            elif num == 1:
                return colorname2
            elif num == 2:
                return colorname3
        differences = [0, 0, 0]
        for i in range(10):
            c1 = Motors.Gripper1.colorSensor.rgb
            c = [color1, color2, color3]
            # 0 = blue, 1 = green, 2 = no color
            diff1 = []
            for i in range(len(c)):
                v1 = 0
                for j in range(3):
                    v1 += (c[i][j] - c1[j])**2
                diff1.append(v1)
            for i in range(len(diff1)):
                differences[i] += diff1[i]
        return convertColor(differences.index(min(differences)))
    
