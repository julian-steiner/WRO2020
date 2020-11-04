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
        RobotContainer.setLoaded(0, c_color)
        if c_color in männli and c_color != "None":
            self.Gripper2.movemotor(100,True)
        elif c_color == "None":
            self.DriveTrain.driveForward(self.rc.SPEED, 9)
        sleep(0.2)
        return self.driveToPoint(checkPoint, checkPointz)

# Zur mitte fahren

    def driveToPoint(self, checkPoint, checkPointz):
        sleep(0.5)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,9)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPoint + 1))
        self.DriveTrain.center("Black", direction='-1')
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,20)
        if checkPoint in [0, 2]:
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

        elif startpunkt == 1:
            if endpunkt == 0:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED,e_offset)
            elif endpunkt == 2:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 3:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 24)

        if startpunkt == 2:
            if endpunkt == 3:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED,e_offset)
            elif endpunkt == 0:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 1:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveForward(self.rc.SPEED, 100)

        if startpunkt == 3:
            if endpunkt == 2:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 0:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 1:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveForward(self.rc.SPEED, long_distance)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif endpunkt == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveForward(self.rc.SPEED, 100)


#gripper2.movemotor(50,True)

#while True:
#     print(gripper2.RomerColorPD())
#    print(motors.Gripper2.colorSensor.rgb)

#print(deichhandler.männlidriver(0,[]))