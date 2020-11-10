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

    def scannhouse(self, checkpoint):
        if(len(Gameboard.deliveredOrders) <= 1):
            self.scannhouse1(checkpoint)
        else:
            self.scannhouse2(checkpoint)

    def scannhouse1(self,chekpoint):
        self.driveTrain.driveForward(37,2.1)
        time.sleep(0.1)
        c_color = Gripper.RomerColor(self,[13, 47, 72] ,[12, 7, 17], [1, 1, 0], "Blue", "Green", "None")
        print(c_color)
        time.sleep(0.1)
        Gameboard.setHouse(chekpoint,c_color)
        if c_color == "None":
            self.driveTrain.driveForward(RobotContainer.SLOW_SPEED,-4.1)
        else:
            self.driveTrain.driveForward(RobotContainer.SLOW_SPEED,-2.1)
        time.sleep(0.1)
    
    def scannhouse2(self,chekpoint):
        self.driveTrain.driveForward(50,2.5)
        time.sleep(0.1)
        c_color = Gripper.RomerColor(self,[13, 47, 72] ,[5, 33, 8], [1, 1, 0], "Blue", "Green", "None")
        print(c_color)
        time.sleep(0.1)
        Gameboard.setHouse(chekpoint,c_color)
        if c_color == "None":
            self.driveTrain.driveForward(RobotContainer.SLOW_SPEED,-6)
        else:
            self.driveTrain.driveForward(RobotContainer.SLOW_SPEED,-2.5)
        time.sleep(0.1)
    