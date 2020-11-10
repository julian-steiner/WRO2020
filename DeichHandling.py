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
    def __init__(self,Gripper,Gripper2,DriveTrain,BagHandler):
        self.Gripper = Gripper
        self.Gripper2 = Gripper2
        self.DriveTrain = DriveTrain
        self.rc = RobotContainer
        self.baghandler = BagHandler
    
    def DeichPickUp(self,checkPoint, e_offset = 180):
        angle = 90*(-1)**(checkPoint+1)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.driveForward(self.rc.SPEED, -24)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.driveForward(self.rc.SPEED, -14)
        self.Gripper2.movemotor(100, True)
        sleep(0.5)
        RobotContainer.setLoaded(0, Gameboard.bricks[checkPoint])
        self.DriveTrain.driveForward(self.rc.SPEED,13)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 18)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, e_offset - angle)
    
    def pickUpBoth(self, checkPoint):
        self.DeichPickUp(checkPoint, 0)
        self.baghandler.pickUp(checkPoint)
    
    def scanHumans(self,checkPoint, angle):
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPoint))
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE,8)
        # self.DriveTrain.driveForward(self.rc.SPEED, -48)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 25)
        
        yellow = [32, 11, 9]
        red = [51, 1, 1]
        c_color = self.Gripper.RomerColor(red ,yellow, [0, 0, 1], "Red", "Yellow", "None")
        if(c_color == "None"):
            self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 1)
            c_color = self.Gripper.RomerColor(red, yellow, [0, 0, 1], "Red", "Yellow", "None")
        # c_color = self.Gripper2.RomerColorPD()
        sleep(0.5)
        # self.DriveTrain.driveForward(self.rc.SPEED, 24)

        log(Motors.Gripper1.colorSensor.rgb, "RGB Value of the front sensor")
        log(c_color, "Color of the front sensor")
        Gameboard.setHuman(checkPoint, c_color)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -10)

    def scanBlocks(self, checkPoint):
        männli = Gameboard.humans
        if checkPoint == 0 or checkPoint == 2:
            angle = 90
        else:
            angle = -90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
        self.DriveTrain.driveForward(self.rc.SPEED, 17)
        sleep(0.5)
        self.DriveTrain.driveForward(self.rc.SPEED,-95)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        c_color = self.Gripper2.RomerColorPU()
        log(Motors.Gripper2.colorSensor.rgb, "RGB Value of the back sensor")
        log(c_color, "Color of the back sensor")
        Gameboard.setBrick(checkPointz, c_color)
        if c_color in männli and c_color != "None":
            print(c_color, männli)
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, c_color)
        elif c_color == "None":
            self.DriveTrain.driveForward(self.rc.SPEED, 9)
        sleep(0.2)

        checkpoint = self.driveToPoint(checkPointz)
        return checkpoint

    def driveToPoint(self, checkPointz):
        sleep(0.5)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,9)
        print(90*(-1)**(checkPointz))
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 60*(-1)**(checkPointz))
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPointz), self.rc.LINE)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,18)
        if checkPointz in [0, 2]:
            offset = -90
        else:
            offset = 90
        self.baghandler.scanBags(checkPointz, offset)
        if RobotContainer.getLoaded()[2] != None and RobotContainer.getLoaded()[2] in Gameboard.humans:
            if(Gameboard.getDistance(checkPointz, Gameboard.humans.index(RobotContainer.getLoaded()[2])) == 1):
                checkPointz = self.DeichPutDown(checkPointz, dislocated=0)
                return(checkPointz)

        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -22)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -90*(-1)**(checkPointz))
        return checkPointz

    def männliDriver(self, checkPoint):
        männli = Gameboard.humans

        #Drive to the turning point
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPoint), self.rc.LINE)
        self.DriveTrain.driveToLine(self.rc.SPEED, self.rc.LINE)
        self.DriveTrain.driveForward(self.rc.SPEED, 11)

        if checkPoint == 0 or checkPoint == 2:
            angle = -90
        else:
            angle = 90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        sleep(0.5)
# Drive to the blocks
        self.DriveTrain.driveForward(50, 20)
        self.DriveTrain.driveForward(self.rc.SPEED,-95)

        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1     
    
        c_color = Gameboard.bricks[checkPointz]

        if c_color in männli and c_color != "None":
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, c_color)
        elif c_color == "None":
            self.DriveTrain.driveForward(self.rc.SPEED, 9)

        sleep(0.5)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,11)
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPointz))
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 60*(-1)**(checkPointz))
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPointz), self.rc.LINE)
        #self.DriveTrain.center("Black", direction='-1')
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,20)
        if checkPointz in [0, 2]:
            offset = 90
        else:
            offset = -90

        if Gameboard.sand[checkPointz] in Gameboard.houses:
            print("Pickupsand executed")
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, offset)
            self.baghandler.pickUp(checkPointz, driveBack="0") 

        if RobotContainer.getLoaded()[2] != None and RobotContainer.getLoaded()[2] in Gameboard.humans:
            print("deliverBlocks executed")
            
            if(Gameboard.getDistance(checkPointz, Gameboard.humans.index(RobotContainer.getLoaded()[2])) == 1):
                self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, -24)
                self.DeichPutDown(Gameboard.humans.index(RobotContainer.getLoaded()[2]), dislocated=0)
                return(checkPointz)

        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**checkPoint)

        return(checkPointz)

    
    
    def DeichPutDown(self, checkPoint, dislocated = 1):
        color = RobotContainer.getLoaded()[2]
        humans = Gameboard.humans
        self.Gripper2.movemotor(100, True)

        if color in humans:
            if dislocated == 0:
                if checkPoint in [0, 2]:
                    angle = 90
                else:
                    angle = -90
                    
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
                # self.DriveTrain.driveForward(self.rc.SPEED, 57)
                self.DriveTrain.driveForward(self.rc.SPEED, 20)
                self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 33)
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
                self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -12.5)
                self.Gripper2.movemotor(50, False)
                sleep(0.5)
                self.DriveTrain.driveForward(self.rc.SPEED, 2)
                self.DriveTrain.center("Black", direction='-1')
                self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 27)
                destination = Gameboard.humans.index(color)
                RobotContainer.setLoaded(0, None)
                Gameboard.setBlockDelivered(color)
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
                return destination

            else:
                self.DriveTrain.turnToLine(-self.rc.TURN_SPEED*(-1)**(checkPoint), self.rc.LINE)
                self.DriveTrain.driveForward(self.rc.SPEED,-33)
                self.Gripper2.movemotor(50,False)
                self.DriveTrain.driveForward(self.rc.SPEED, 31)
                RobotContainer.setLoaded(0, None)
                Gameboard.setBlockDelivered(color)
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -90*(-1)**(checkPoint))

                return checkPoint
        else:
            print("Color not in humans")
    
    def WorstCase(self,checkPoint):
        self.DriveTrain.driveForward(self.rc.SPEED,1.5)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPoint + 1))
        # self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPoint + 1),"Black")
        # self.DriveTrain.center("Black")
        sleep(0.2)
        self.DriveTrain.driveForward(self.rc.SPEED,-26.5)
        self.Gripper.moveMotor(100,-210)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,(-1)**(checkPoint + 1)*140)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPoint),"Black")
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED,(-1)**(checkPoint + 1)*130)
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED,(-1)**(checkPoint)*20)
        sleep(0.2)
        self.Gripper.moveMotor(100,210)
        sleep(0.2)
# Scannen
        self.DriveTrain.driveForward(self.rc.SPEED,-23)
        c_color = self.Gripper2.RomerColorPU()
        Gameboard.setBrick(checkPoint,c_color)
# Drehen
        self.DriveTrain.driveForward(self.rc.SPEED,23)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,(-1)**(checkPoint)*179)
        self.DriveTrain.center("Black",-1)
# Seite wechslen
        self.DriveTrain.driveForward(self.rc.SPEED,-85)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        color = Gameboard.bricks[checkPointz]
        if color in Gameboard.humans:
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, color)
        self.driveToPoint(checkPointz)

        return checkPointz
