import Gripper
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

    def pickUp(self, startPoint, scann, driveBack = "1"):
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(startPoint), self.rc.LINE)
        sleep(0.2)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 2)
        self.DriveTrain.center("Black", direction = 1 * (-1) ** (startPoint+1))
        self.Gripper.lowerMotor(-45)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 20)
        sleep(0.2)
        if scann == True:
            Gameboard.setSand(startPoint, self.Gripper.getColor(scann))
        self.DriveTrain.tank_drive.on(-self.rc.APPROACH_SPEED/2, -self.rc.APPROACH_SPEED/2)
        self.Gripper.moveMotor(13, 160)
        self.DriveTrain.tank_drive.off()
        RobotContainer.setLoaded(Gameboard.sand[startPoint], 0)

        if driveBack == "1":
            self.DriveTrain.driveForward(self.rc.SPEED, -22)
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**startPoint)
        
    def deliver(self, startPoint, offset):
        self.Gripper.moveMotor(20, 1)
        if(not RobotContainer.LIVE_RUN):
            self.DriveTrain.followLine(self.rc.SPEED, RobotContainer.AGGRESSION, RobotContainer.BLUELINE + RobotContainer.REDLINE, 6)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -15)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 12)
        self.Gripper.lowerMotor(-40)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -8)
        self.Gripper.moveMotor(13, 160)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -16)
        self.Gripper.lowerMotor(-60)
        self.DriveTrain.driveForward(self.rc.SPEED, -6)
        self.Gripper.lowerMotor(70)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 14)
        Gameboard.setBagDelivered(RobotContainer.getLoaded()[1])
        RobotContainer.setLoaded(None, 0)
        self.DriveTrain.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, ["Red", "Yellow", "Blue", "Green"], 19)
        # self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-4)

