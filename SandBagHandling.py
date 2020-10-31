from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from time import sleep

class BagHandler:
    def __init__(self, DriveTrain, Gripper):
        self.DriveTrain = DriveTrain
        self.Gripper = Gripper
        self.rc = RobotContainer()

    def pickUp(self, startPoint, offset, houseColors):
        if startPoint == 0 or startPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90 - offset)
        else:
            angle = self.DriveTrain.optimizeAngle(-90 - offset)

        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.followToLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.LINE, ["Black", "Brown"])
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 9)
        color = self.Gripper.RomerColor([30, 35, 41] ,[20, 17, 40], [0, 0, 1], "Green", "Blue", "None")
        if(color in houseColors):
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -15)
            self.DriveTrain.center("Black")
            self.Gripper.lowerMotor(-40)
            self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 15)
            RobotContainer.setLoaded(color, 0)
            self.Gripper.moveMotor(10, 160)
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 1)
        
    def deliver(self, startPoint, offset, houseColors):
        self.Gripper.moveMotor(20, 1)
        color = RobotContainer.getLoaded()[1]
        self.DriveTrain.driveCheckpoints(startPoint, houseColors.index(color), offset, 0, 0)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 8)
        self.Gripper.lowerMotor(-30)
        self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, -2)
        self.Gripper.moveMotor(10, 160)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,  -5)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -18)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 5)
        self.Gripper.lowerMotor(-80)
        self.DriveTrain.driveForward(self.rc.SPEED, -10)
        self.DriveTrain.driveForward(self.rc.SPEED, 5)
        self.Gripper.lowerMotor(50)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 5)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -5)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 5)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 6)
        # self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 16)
        self.DriveTrain.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, ["Red", "Yellow", "Blue", "Green"], 16)

