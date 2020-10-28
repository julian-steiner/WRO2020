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
        print("Reached Line")
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 9)
        color = self.Gripper.RomerColor([30, 35, 41] ,[20, 17, 40], [0, 0, 1], "Green", "Blue", "None")
        print(color, "Color 1")
        print(Motors.Gripper1.colorSensor.rgb)
        if(color in houseColors):
            print("colorMatch")
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -15)
            self.DriveTrain.center("Black")
            self.Gripper.lowerMotor(-40)
            self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 15)
            RobotContainer.setLoaded(True, color, 0)
            self.Gripper.moveMotor(10, 160)
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 1)
        
    def deliver(self, startPoint, offset, houseColors):
        self.Gripper.moveMotor(20, 1)
        color = RobotContainer.getLoaded()[1]
        print(RobotContainer.getLoaded())
        print(color)
        self.DriveTrain.driveCheckpoints(startPoint, houseColors.index(color), offset, 0)
                



