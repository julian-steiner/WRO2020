from Gripper2 import Gripper2
from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from SandBagHandling import BagHandler
from time import sleep
from GameBoard import Gameboard

def log(x, name):
    print(name + ": >>>     " + str(x))

class DeichHandler:
    def __init__(self,Gripper,Gripper2,DriveTrain,time,BagHandler):
        self.Gripper = Gripper
        self.Gripper2 = Gripper2
        self.DriveTrain = DriveTrain
        self.rc = RobotContainer
        self.baghandler = BagHandler
        self.time = time
    
    def DeichPickUp(self,checkPoint):
        männli = Gameboard.humans
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**checkPoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-14)
        self.Gripper2.movemotor(100,True)
        self.time.sleep(1)
        color = self.Gripper2.RomerColorPU()
        if color[0] not in männli:
            self.Gripper2.movemotor(100,False)
        else:
            RobotContainer.setLoaded(0,color)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,14)
        self.DriveTrain.turnToLine((-1)**checkPoint*(self.rc.TURN_SPEED),"Black")
        return color
    
    def scanHumans(self,checkPoint, angle, scann):
        if checkPoint == 0 or checkPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90 - angle)
        else:
            angle = self.DriveTrain.optimizeAngle(-90 - angle)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.driveToLine(self.rc.SPEED, self.rc.LINE)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 11.5)
        if scann == True:
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 4)
            sleep(0.5)
            yellow = [34, 14, 8]
            red = [36, 10, 11]
            c_color = self.Gripper.RomerColor(red ,yellow, [0, 0, 1], "Red", "Yellow", "None")
            if(c_color == "None"):
                self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 1)
                c_color = self.Gripper.RomerColor(red, yellow, [0, 0, 1], "Red", "Yellow", "None")
            log(Motors.Gripper1.colorSensor.rgb, "RGB Value of the front sensor")
            log(c_color, "Color of the front sensor")
            Gameboard.setHuman(checkPoint, c_color)
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -4)

    def scanBlocks(self, checkPoint, scann):
        männli = Gameboard.humans
        if checkPoint == 0 or checkPoint == 2:
            angle = -90
        else:
            angle = 90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        sleep(1)
        self.DriveTrain.driveForward(self.rc.SPEED, 17)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-95)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        if scann == True:
            c_color = self.Gripper2.RomerColorPU()
            log(Motors.Gripper2.colorSensor.rgb, "RGB Value of the back sensor")
            log(c_color, "Color of the back sensor")
        else:
            c_color = Gameboard.bricks[checkPointz]
        Gameboard.setBrick(checkPointz, c_color)
        RobotContainer.setLoaded(0, c_color)
        if c_color in männli and c_color != "None":
            self.Gripper2.movemotor(100,True)
        elif c_color == "None":
            self.DriveTrain.driveForward(self.rc.SPEED, 9)
        sleep(0.2)
        return self.driveToPoint(checkPoint, checkPointz)

    def driveToPoint(self, checkPointz):
        sleep(0.5)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,9)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPointz))
        # self.DriveTrain.center("Black", direction='-1')
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,20)
        if checkPointz in [0, 2]:
            offset = -90
        else:
            offset = 90
        self.baghandler.pickUp(checkPointz, offset)
        return checkPointz
    
    def DeichPutDown(self, checkPoint, dislocated = 0):
        if dislocated != 0:
            pass
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)
        color = RobotContainer.getLoaded()[2]
        humans = Gameboard.humans
        print(color, humans)
        if color in humans:
            destination = humans.index(color)
            if checkPoint in [0, 2]:
                self.DriveTrain.driveCheckpoints(checkPoint, destination, -90, 0)
            else:
                self.DriveTrain.driveCheckpoints(checkPoint, destination, 90, 0)
            if destination in [0, 2]:
                angle = -90
            else:
                angle = 90
            self.DriveTrain.turnAngle(RobotContainer.TURN_SPEED, angle)
            self.DriveTrain.center("Black", direction='-1')
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-36)
            self.Gripper2.movemotor(50,False)
            self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 36)
            RobotContainer.setLoaded(0, None)
            Gameboard.setBlockDelivered(color)
        else:
            print("Color not in humans")
    
    def WorstCase(self,checkPoint):
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPoint + 1),"Black")
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,(-1)**checkPoint*9)
        sleep(0.2)
        self.DriveTrain.driveForward(self.rc.SPEED,-26.5)
        self.Gripper.moveMotor(100,-210)
        self.DriveTrain.turnAngle(self.rc.SLOW_TURN_SPEED,(-1)**(checkPoint + 1)*130)
        self.DriveTrain.turnAngle(self.rc.SLOW_TURN_SPEED,(-1)**(checkPoint)*40)
        sleep(0.2)
        self.Gripper.moveMotor(100,210)
        sleep(0.2)
# Scannen
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-23)
        c_color = self.Gripper2.RomerColorPU()
        Gameboard.setBrick(checkPoint,c_color)
# Drehen
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,23)
        self.DriveTrain.turnAngle(self.rc.SLOW_TURN_SPEED,(-1)**(checkPoint)*173.5)
# Seite wechslen
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-85)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        color = Gameboard.bricks[checkPointz]
        if color in Gameboard.humans:
            self.Gripper2.movemotor(100,True)
        self.driveToPoint(checkPointz)