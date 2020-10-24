from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain

class BagHandler:
    def __init__(self, DriveTrain, Gripper):
        self.DriveTrain = DriveTrain
        self.Gripper = Gripper
        self.rc = RobotContainer()

    def pickUp(self, startPoint, offset, houseColors):
        if startPoint == 0 or startPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90 - offset)
            # speed = self.rc.TURN_SPEED
        else:
            angle = self.DriveTrain.optimizeAngle(-90 - offset)
            # speed = -self.rc.TURN_SPEED
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        # self.DriveTrain.turnToLine(speed, self.rc.LINE)
        self.DriveTrain.followToLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.LINE, self.rc.LINE)
        self.Gripper.lowerMotor(-40)
        self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 11)
        color = self.Gripper.RomerColor([21, 25, 30] ,[20, 17, 40], [0, 0, 1], "Green", "Blue", "None")
        if(color in houseColors):
            print("colorMatch")
            self.Gripper.moveMotor(20, 120)
        print(color)
        print(Motors.Gripper1.colorSensor.rgb)



