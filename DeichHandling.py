from Gripper2 import Gripper2
from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from SandBagHandling import BagHandler
from time import sleep

class DeichHandler:
    def __init__(self,Gripper,Gripper2,DriveTrain,time,BagHandler):
        self.Gripper = Gripper
        self.Gripper2 = Gripper2
        self.DriveTrain = DriveTrain
        self.rc = RobotContainer
        self.baghandler = BagHandler
        self.time = time
    
    def DeichPickUp(self,checkPoint,männli):
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**checkPoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-14)
        self.Gripper2.movemotor(50,True)
        self.time.sleep(1)
        color = self.Gripper2.RomerColorPU()
        if color[0] not in männli:
            self.Gripper2.movemotor(50,False)
        else:
            RobotContainer.setLoaded(0,color)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,14)
        self.DriveTrain.turnToLine((-1)**checkPoint*(self.rc.TURN_SPEED),"Black")
        return color
    
    def männlidriver(self,checkPoint,männli,houseColors):
        color = []
        # self.DriveTrain.turnToLine((-1)**(checkPoint + 1)*self.rc.TURN_SPEED,"Black")

        # self.time.sleep(0.2)
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 5.7*(-1)**checkPoint)
        # self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-43.75)
        # color.append(self.Gripper2.RomerColorPD())
        # self.DriveTrain.driveForward(self.rc.SPEED,17.75)
        if checkPoint == 0 or checkPoint == 2:
            angle = self.DriveTrain.optimizeAngle(90)
        else:
            angle = self.DriveTrain.optimizeAngle(-90)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
        self.DriveTrain.center("Black")
        self.DriveTrain.followToLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.LINE, ["Black", "Brown"])
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, 15.5)
        sleep(2)
        c_color = self.Gripper.RomerColor([70, 18, 20] ,[51, 27, 11], [0, 0, 1], "Red", "Yellow", "None")
        if(c_color == "None"):
            self.DriveTrain.driveForward(self.rc.APPROACH_SPEED, 1)
        c_color = self.Gripper.RomerColor([70, 18, 20] ,[51, 27, 11], [0, 0, 1], "Red", "Yellow", "None")
        color.append(c_color)
        print(Motors.Gripper1.colorSensor.rgb)
        print(color)
# Drehen
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED,110*(-1)**checkPoint)
        # self.DriveTrain.driveForward(self.rc.SPEED,-2)
        # self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(checkPoint + 1),"Black")
        # self.DriveTrain.turnAngle(self.rc.TURN_SPEED,4.4*(-1)**(checkPoint +1))
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED, -4)
        if checkPoint == 0 or checkPoint == 2:
            angle = -90
        else:
            angle = 90
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, angle)
# Zu Betonblöcke fahren
        self.DriveTrain.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 15)
        self.DriveTrain.driveForward(self.rc.SPEED,-90)
        color.append(self.Gripper2.RomerColorPU()[0])
        self.DriveTrain.center("Black")
        if color[0] == color[1]:
            self.Gripper2.movemotor(50,True)
        print(color[0], color[1])
# Zur mitte fahren
        sleep(1)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,8)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(checkPoint + 1))
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,24)
        if checkPoint % 2 == 1:
            checkPointz = checkPoint - 1
        if checkPoint % 2 == 0:
            checkPointz = checkPoint + 1
        self.baghandler.pickUp(checkPointz,-90,houseColors)
        if color[0] != color[1]:
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            if checkPoint % 2 == 1:
                checkPoint -= 1
            if checkPoint % 2 == 0:
                checkPoint += 1
        else:
            self.DriveTrain.turnToLine((-1)**(checkPoint + 1)*self.rc.TURN_SPEED,"Black")
            self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,57)
            self.DriveTrain.turnToLine((-1)**(checkPoint + 1)*self.rc.TURN_SPEED,"Black")
            self.DeichPutDown()
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,24)
        männli.append(color[0])
        return checkPoint
    
    def DeichPutDown(self):
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-13)
        self.Gripper2.movemotor(50,False)
        RobotContainer.setLoaded(0, None)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,13)

#gripper2.movemotor(50,True)

#while True:
#     print(gripper2.RomerColorPD())
#    print(motors.Gripper2.colorSensor.rgb)

#print(deichhandler.männlidriver(0,[]))