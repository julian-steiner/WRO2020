from RobotContainer import RobotContainer
from GameBoard import Gameboard

class OrderHandling:
    def __init__(self, driveTrain, gripper):
        self.driveTrain = driveTrain
        self.gripper = gripper
    
    def deliverOrder(self, checkpoint):
        self.driveTrain.driveForward(100, -10)
        self.driveTrain.driveForward(100, 14)
        self.driveTrain.driveForward(RobotContainer.SLOW_SPEED, -2)
        Gameboard.setOrderDelivered(checkpoint)
