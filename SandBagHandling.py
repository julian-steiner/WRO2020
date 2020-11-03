from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from time import sleep
from GameBoard import Gameboard

class BagHandler:
    def __init__(self, DriveTrain, Gripper):
        self.DriveTrain = DriveTrain
        self.Gripper = Gripper
        self.rc = RobotContainer()

    def pickUp(self, startPoint, offset):
        houseColors = Gameboard.houses
        if startPoint == 0 or startPoint == 2:
            angle = 90 - offset
        else:
            angle = -90 - offset

        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.followToLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.LINE, ["Black", "Brown"])
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 9)
        color = self.Gripper.RomerColor([45, 49, 72] ,[8, 7, 13], [0, 0, 1], "Green", "Blue", "None")

        if(color in houseColors):
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -15)
            self.DriveTrain.center("Black")
            self.Gripper.lowerMotor(-40)
            self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 15)
            RobotContainer.setLoaded(color, 0)
            self.Gripper.moveMotor(10, 160)
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)

        print(color, Motors.Gripper1.colorSensor.rgb)
        
    def deliver(self, startPoint, offset):
        self.Gripper.moveMotor(20, 1)
        color = RobotContainer.getLoaded()[1]
        self.DriveTrain.driveCheckpoints(startPoint, Gameboard.houses.index(color), offset, 0, 0)
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

