from RobotContainer import RobotContainer
from GameBoard import Gameboard
from Gripper import Gripper
from Motors import Motors
import time

class OrderHandling:
    def __init__(self, driveTrain, gripper):
        self.driveTrain = driveTrain
    
    def scannhouse(self, chekpoint):
        self.driveTrain.followLine(43, RobotContainer.AGGRESSION, RobotContainer.BLUELINE + RobotContainer.REDLINE, 4)
        time.sleep(0.1)
        c_color = Gripper.RomerColor(self,[13, 47, 72] ,[12, 7, 17], [13, 6, 16], "Blue", "Green", "None")
        print("[ScanHouse] color:   " + str(c_color))
        print("[ScanHouse] rgb:     " + str(Motors.Gripper1.colorSensor.rgb))
        time.sleep(0.1)
        Gameboard.setHouse(chekpoint,c_color)
        if c_color == "None":
            self.driveTrain.driveForward(37, -4.2)
        else:
            self.driveTrain.driveForward(37, -2.1)
            Gameboard.setOrderDelivered(chekpoint)
        time.sleep(0.1)
