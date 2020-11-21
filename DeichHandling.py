from Gripper2 import Gripper2
from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from SandBagHandling import BagHandler
from time import sleep
from GameBoard import Gameboard

def log(x, name):
    print("[Deichhandler]   " + str(name) + ": >>>     " + str(x))

class DeichHandler:
    def __init__(self,Gripper,Gripper2,DriveTrain,BagHandler):
        self.Gripper = Gripper
        self.Gripper2 = Gripper2
        self.DriveTrain = DriveTrain
        self.baghandler = BagHandler
    
    def DeichPickUpold(self,checkPoint, e_offset = 180):
        angle = 90*(-1)**(checkPoint+1)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, angle)
        self.DriveTrain.driveForward(RobotContainer.SPEED, -24)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, angle)
        self.DriveTrain.driveForward(RobotContainer.SPEED, -14)
        self.Gripper2.movemotor(100, True)
        sleep(0.5)
        RobotContainer.setLoaded(0, Gameboard.bricks[checkPoint])
        self.DriveTrain.driveForward(RobotContainer.SPEED,13)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, -angle)
        self.DriveTrain.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 18)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, e_offset - angle)
    
    def DeichPickUp(self,checkPoint, e_offset = 180):
        angle = 90*(-1)**(checkPoint)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, angle)
        self.DriveTrain.driveForward(RobotContainer.SPEED, -15.5)
        self.Gripper2.movemotor(100, True)
        sleep(0.5)
        RobotContainer.setLoaded(0, Gameboard.bricks[checkPoint])
        self.DriveTrain.driveForward(RobotContainer.SPEED,13)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, angle)
        self.DriveTrain.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 24)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, e_offset + angle)
    
    def pickUpBoth(self, checkPoint):
        self.baghandler.pickUp(checkPoint, False, "0")
        self.DriveTrain.driveForward(RobotContainer.SLOW_SPEED,2)
        self.DeichPickUp(checkPoint)
    
    def scanHumans(self, checkPoint, scann):
        pass
        
    def scanBlocks(self, checkPoint, scann):
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, (-1)**(checkPoint + 1)*90)
        sleep(0.5)
        self.DriveTrain.driveForward(RobotContainer.SLOW_SPEED, 26)
        self.DriveTrain.driveForward(RobotContainer.FAST_SPEED,-95)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1

        # Farb bestimmung
        if scann == True:
            c_color = self.Gripper2.RomerColorPU()
            log(Motors.Gripper2.colorSensor.rgb, "RGB Value of the back sensor")
            log(c_color, "Color of the back sensor")
            Gameboard.setBrick(checkPointz, c_color)
        else:
            c_color = Gameboard.bricks[checkPointz]
            
        # Aufnehmen
        if c_color != "None":
            sleep(0.1)
            self.DriveTrain.driveForward(RobotContainer.SPEED,-3)
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, c_color)
        elif c_color == "None":
            self.DriveTrain.driveForward(RobotContainer.SPEED, 9)
        
        return checkPointz

    def männliDriver(self, checkPoint, scann):
        self.scanHumans(checkPoint,scann)
        
        # Drive To Point
        sleep(0.5)
        # old values 11, 18
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, 92*(-1)**(checkPoint+1))
        self.DriveTrain.driveForward(RobotContainer.FAST_SPEED, 20)
        self.DriveTrain.driveForward(RobotContainer.FAST_SPEED, -95)
        self.DriveTrain.driveForward(RobotContainer.SPEED, 1)
        self.Gripper2.movemotor(100, 1)
        sleep(0.5)
        self.DriveTrain.driveForward(RobotContainer.FAST_SPEED, 12)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, 90*(-1)**(checkPoint+1))
        


    def DeichPutDown(self, checkPoint):
        color = RobotContainer.getLoaded()[2]
        humans = Gameboard.humans
        self.Gripper2.movemotor(100, True)
        self.DriveTrain.driveForward(RobotContainer.SLOW_SPEED, -2)

        if color in humans:
            # self.DriveTrain.turnToLine(-RobotContainer.TURN_SPEED*(-1)**(checkPoint), RobotContainer.LINE)
            self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, -90*(-1)**checkPoint)
            self.DriveTrain.driveForward(RobotContainer.SPEED,-37)
            self.Gripper2.movemotor(50,False)
            self.DriveTrain.followLine(RobotContainer.SPEED,RobotContainer.AGGRESSION, RobotContainer.LINE, 32)
            RobotContainer.setLoaded(0, None)
            Gameboard.setBlockDelivered(color)
            self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, -90*(-1)**(checkPoint))

            return checkPoint
        else:
            print("Color not in humans")
    
    #TODO finish worst case
    def WorstCase(self,checkPoint):
        self.DriveTrain.driveForward(RobotContainer.SPEED,1.5)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED,90*(-1)**(checkPoint + 1))
        sleep(0.2)
        self.DriveTrain.driveForward(RobotContainer.SPEED,-28)
        self.Gripper.moveMotor(100,-210)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED,(-1)**(checkPoint + 1)*140)
        self.DriveTrain.turnToLine(RobotContainer.TURN_SPEED*(-1)**(checkPoint),"Black")
        sleep(0.2)
        self.Gripper.moveMotor(100,210)
        sleep(0.2)
        # Scannen
        self.DriveTrain.driveForward(RobotContainer.SPEED,-23)
        c_color = self.Gripper2.RomerColorPU()
        Gameboard.setBrick(checkPoint,c_color)
        # Drehen
        self.DriveTrain.driveForward(RobotContainer.SPEED,23)
        self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED,(-1)**(checkPoint)*179)
        # Seite wechslen
        self.DriveTrain.driveForward(RobotContainer.SPEED,-85)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        color = Gameboard.bricks[checkPointz]
        if color in Gameboard.humans:
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, color)
        # self.driveToPoint(checkPointz)

        return checkPointz
