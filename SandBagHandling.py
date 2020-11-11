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

    def scanBags(self, startPoint, offset):
        houseColors = Gameboard.houses

        self.DriveTrain.turnAngle(self.rc.TURN_SPEED * (-1) ** (startPoint), 150)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(startPoint), self.rc.LINE)
        sleep(0.2)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 8)
        self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 9)
        
        color = self.Gripper.RomerColor([0, 10, 3] ,[0, 7, 35], [200, 200, 200], "Green", "Blue", "None")
        print("[scanBags]   RGB value:  " + str(Motors.Gripper1.colorSensor.rgb))
        print("[scanBags]   Color of the bags is:    " + str(color))
        Gameboard.setSand(startPoint, color)
        if(color in houseColors and color != "None"):
            self.DriveTrain.driveForward(self.rc.SPEED, -15)
            self.DriveTrain.center("Black", direction=1 * (-1) ** startPoint)
            self.Gripper.lowerMotor(-40)
            self.DriveTrain.driveForward(self.rc.SPEED, 12)
            RobotContainer.setLoaded(color, 0)
            self.Gripper.moveMotor(10, 150)
        return 0

    def pickUp(self, startPoint, driveBack = "1"):
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(startPoint), self.rc.LINE)
        sleep(0.2)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 3)
        self.DriveTrain.center("Black", direction = 1 * (-1) ** startPoint)
        self.Gripper.lowerMotor(-40)
        self.DriveTrain.driveForward(self.rc.SPEED, 13)
        self.Gripper.moveMotor(10, 150)
        RobotContainer.setLoaded(Gameboard.sand[startPoint], 0)

        if driveBack == "1":
            self.DriveTrain.driveForward(self.rc.SPEED, -22)
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**startPoint)
        elif driveBack != "1":
            self.DriveTrain.driveForward(self.rc.SPEED, 2)
        
    def deliver(self, startPoint, offset):
        self.Gripper.moveMotor(20, 1)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -12)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 9)
        self.Gripper.lowerMotor(-30)
        self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, -2)
        self.Gripper.moveMotor(10, 160)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -12)
        self.Gripper.lowerMotor(-80)
        self.Gripper.lowerMotor(70)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 5)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 6)
        Gameboard.setBagDelivered(RobotContainer.getLoaded()[1])
        RobotContainer.setLoaded(None, 0)
        # self.DriveTrain.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, ["Red", "Yellow", "Blue", "Green"], 2)

