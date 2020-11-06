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
    
    def DeichPickUp(self,checkPoint):
        angle = 90*(-1)**(checkPoint+1)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -20)
        self.Gripper2.movemotor(100, True)
        sleep(0.5)
        RobotContainer.setLoaded(0, Gameboard.bricks[checkPoint])
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,15)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 20)
    
    def pickUpBoth(self, checkPoint):
        #pick up the 
        angle = 90*(-1)**(checkPoint+1)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -20)
        self.Gripper2.movemotor(100, True)
        sleep(0.5)
        RobotContainer.setLoaded(0, Gameboard.bricks[checkPoint])
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,15)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
        self.DriveTrain.followLine(self.rc.TURN_SPEED, self.rc.AGGRESSION, self.rc.LINE, 22)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, -angle)
        self.baghandler.pickUp(checkPoint)
    
    def scanHumans(self,checkPoint, angle):
        if checkPoint == 0 or checkPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90 - angle)
        else:
            angle = self.DriveTrain.optimizeAngle(-90 - angle)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.driveToLine(self.rc.SPEED, self.rc.LINE)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 15.5)
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

    def scanBlocks(self, checkPoint):
        männli = Gameboard.humans
# Drehen
        if checkPoint == 0 or checkPoint == 2:
            angle = -90
        else:
            angle = 90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        sleep(1)
# Zu Betonblöcke fahren
        self.DriveTrain.driveForward(self.rc.SPEED, 17)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-95)
        c_color = self.Gripper2.RomerColorPU()
        log(Motors.Gripper2.colorSensor.rgb, "RGB Value of the back sensor")
        log(c_color, "Color of the back sensor")
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1     

        Gameboard.setBrick(checkPointz, c_color)
        if c_color in männli and c_color != "None":
            self.Gripper2.movemotor(100,True)
            RobotContainer.setLoaded(0, c_color)
        elif c_color == "None":
            self.DriveTrain.driveForward(self.rc.SPEED, 9)
        sleep(0.2)

        self.driveToPoint(checkPointz)

# Zur mitte fahren

    def driveToPoint(self, checkPointz):
        sleep(0.5)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,9)
        print(90*(-1)**(checkPointz))
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPointz))
        #self.DriveTrain.center("Black", direction='-1')
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,20)
        if checkPointz in [0, 2]:
            offset = -90
        else:
            offset = 90
        self.baghandler.scanBags(checkPointz, offset)
        if RobotContainer.getLoaded()[2] != None and RobotContainer.getLoaded()[2] in Gameboard.humans:
            if(Gameboard.getDistance(checkPointz, Gameboard.humans.index(RobotContainer.getLoaded()[2])) == 1):
                self.DeichPutDown(checkPointz, dislocated=0)
                return(checkPointz)

        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -24)
        return checkPointz

    def männliDriver(self, checkPoint):
        männli = Gameboard.humans

        #Drive to the turning point
        if checkPoint == 0 or checkPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90)
        else:
            angle = self.DriveTrain.optimizeAngle(-90)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.driveToLine(self.rc.SPEED, self.rc.LINE)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 11.5)

        if checkPoint == 0 or checkPoint == 2:
            angle = -90
        else:
            angle = 90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        sleep(1)
        #Drive to the blocks
        self.DriveTrain.driveForward(self.rc.SPEED, 17)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-95)

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
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPointz))
        #self.DriveTrain.center("Black", direction='-1')
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,20)
        if checkPointz in [0, 2]:
            offset = 90
        else:
            offset = -90

        if Gameboard.sand[checkPointz] in Gameboard.houses:
            self.DriveTrain.turnAngle(self.rc.TURN_SPEED, offset)
            self.baghandler.pickUp(checkPointz, driveBack="0") 

        if RobotContainer.getLoaded()[2] != None and RobotContainer.getLoaded()[2] in Gameboard.humans:
            if(Gameboard.getDistance(checkPointz, Gameboard.humans.index(RobotContainer.getLoaded()[2])) == 1):
                self.DeichPutDown(checkPointz, dislocated=0)
                return(checkPointz)

        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -23)

    
    
    def DeichPutDown(self, checkPoint, dislocated = 1):
        color = RobotContainer.getLoaded()[2]
        humans = Gameboard.humans
        if color in humans:
            if dislocated == 0:
                if checkPoint in [0, 2]:
                    angle = 90
                else:
                    angle = -90
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
                self.DriveTrain.driveForward(self.rc.SPEED, 57)
                self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
                self.DriveTrain.center("Black")
                self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -9)
                self.Gripper2.movemotor(50, False)
                sleep(0.5)
                self.DriveTrain.driveForward(self.rc.SPEED, 32)
            else:
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
                #self.DriveTrain.center("Black", direction='-1')
                self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-36)
                self.Gripper2.movemotor(50,False)
                self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 36)
                RobotContainer.setLoaded(0, None)
                Gameboard.setBlockDelivered(color)
        else:
            print("Color not in humans")
