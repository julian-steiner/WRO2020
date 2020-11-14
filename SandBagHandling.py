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

    def scanBags(self, startPoint, driveBack = "1"):
        #drive to the blocks and pick them up
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(startPoint), self.rc.LINE)
        sleep(0.2)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 3)
        self.DriveTrain.center("Black", direction = 1 * (-1) ** startPoint)
        self.Gripper.lowerMotor(-40)
        self.DriveTrain.driveForward(self.rc.SPEED, 13)
        color = self.Gripper.RomerColor([0, 10, 3] ,[0, 0, 7], [200, 200, 200], "Green", "Blue", "None")
        print("[scanBags]   RGB value:  " + str(Motors.Gripper1.colorSensor.rgb))
        print("[scanBags]   Color of the bags is:    " + str(color))
        Gameboard.setSand(startPoint, color)
        self.Gripper.moveMotor(10, 150)
        RobotContainer.setLoaded(Gameboard.sand[startPoint], 0)

        #drive back
        if driveBack == "1":
            self.DriveTrain.driveForward(self.rc.SPEED, -24)
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**startPoint)
        elif driveBack != "1":
            self.DriveTrain.driveForward(self.rc.SPEED, 2)

    def pickUp(self, startPoint, driveBack = "1"):
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(startPoint), self.rc.LINE)
        sleep(0.2)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 3)
        self.DriveTrain.center("Black", direction = 1 * (-1) ** startPoint)
        self.Gripper.lowerMotor(-40)
        self.DriveTrain.driveForward(self.rc.SPEED, 11)
        self.Gripper.moveMotor(10, 150)
        RobotContainer.setLoaded(Gameboard.sand[startPoint], 0)

        if driveBack == "1":
            self.DriveTrain.driveForward(self.rc.SPEED, -21)
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**startPoint)
        elif driveBack != "1":
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 3)
        
    def deliver(self, startPoint, offset):
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE + self.rc.REDLINE, 10)
        self.DriveTrain.driveForward(self.rc.SPEED, -5)        
        self.Gripper.moveMotor(20, 1)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -12)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 9)
        self.Gripper.lowerMotor(-30)
        self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, -2)
        self.Gripper.moveMotor(10, 160)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -12)
        self.Gripper.lowerMotor(-80)
        self.Gripper.lowerMotor(100)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 5)
        Gameboard.setBagDelivered(RobotContainer.getLoaded()[1])
        RobotContainer.setLoaded(None, 0)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 180)
        self.DriveTrain.driveForward(self.rc.SPEED, -15)
       
        # self.DriveTrain.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, ["Red", "Yellow", "Blue", "Green"], 2)

