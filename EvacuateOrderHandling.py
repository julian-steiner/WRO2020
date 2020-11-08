from RobotContainer import RobotContainer
from GameBoard import Gameboard
from Gripper import Gripper
from Motors import Motors
import time

class OrderHandling:
    def __init__(self, driveTrain, gripper):
        self.driveTrain = driveTrain
    
    def deliverOrder(self, checkpoint):
        self.driveTrain.driveForward(100, 5)
        self.driveTrain.driveForward(100, -5)
        self.driveTrain.driveForward(100, 5)
        self.driveTrain.driveForward(RobotContainer.SLOW_SPEED, -4)
        Gameboard.setOrderDelivered(checkpoint)

    def scannhouse(self,chekpoint):
        self.driveTrain.driveForward(RobotContainer.SPEED,1)
        time.sleep(0.1)
        print(Motors.Gripper1.colorSensor.rgb)
        c_color = Gripper.RomerColor(self,[13, 47, 72] ,[5, 33, 8], [1, 1, 0], "Blue", "Green", "None")
        print(c_color)
        time.sleep(0.1)
        Gameboard.setHouse(chekpoint,c_color)
        self.driveTrain.driveForward(RobotContainer.SPEED,-1)
        time.sleep(0.1)