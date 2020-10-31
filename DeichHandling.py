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
    
    def DeichPickUp(self,chekpoint,männli):
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**chekpoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-14)
        self.Gripper2.movemotor(50,True)
        self.time.sleep(1)
        color = self.Gripper2.RomerColorPU()
        if color[0] not in männli:
            self.Gripper2.movemotor(50,False)
        else:
            RobotContainer.setLoaded(0,color)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,14)
        self.DriveTrain.turnToLine((-1)**chekpoint*(self.rc.TURN_SPEED),"Black")
        return color
    
    def männlidriver(self,chekpoint,männli,houseColors):
        color = []
        self.DriveTrain.turnToLine((-1)**(chekpoint + 1)*self.rc.TURN_SPEED,"Black")
        self.time.sleep(0.2)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 5.7*(-1)**chekpoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-43.75)
        color.append(self.Gripper2.RomerColorPD())
        self.DriveTrain.driveForward(self.rc.SPEED,17.75)
# Drehen
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,110*(-1)**chekpoint)
        self.DriveTrain.driveForward(self.rc.SPEED,-2)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(chekpoint + 1),"Black")
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,4.4*(-1)**(chekpoint +1))
# Zu Betonblöcke fahren
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-66)
        self.Gripper2.movemotor(50,True)
        self.time.sleep(1)
        color.append(self.Gripper2.RomerColorPU())
        if color[0] != color[1]:
            self.Gripper2.movemotor(50,False)
            self.time.sleep(1)
        # else:
        #     RobotContainer.setLoaded(0,True)
# Zur mitte fahren
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,8)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,90*(-1)**(chekpoint + 1))
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,24)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
        if chekpoint % 2 == 1:
            chekpointz = chekpoint - 1
        if chekpoint % 2 == 0:
            chekpointz = chekpoint + 1
        self.baghandler.pickUp(chekpointz,90,houseColors)
        if color[0] != color[1]:
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            if chekpoint % 2 == 1:
                chekpoint -= 1
            if chekpoint % 2 == 0:
                chekpoint += 1
        else:
            self.DriveTrain.turnToLine((-1)**(chekpoint + 1)*self.rc.TURN_SPEED,"Black")
            self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,57)
            self.DriveTrain.turnToLine((-1)**(chekpoint + 1)*self.rc.TURN_SPEED,"Black")
            self.DeichPutDown()
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,24)
        männli.append(color[0])
        return chekpoint
    
    def DeichPutDown(self):
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-13)
        self.Gripper2.movemotor(50,False)
        RobotContainer.setLoaded(0,"None")
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,13)

#gripper2.movemotor(50,True)

#while True:
#     print(gripper2.RomerColorPD())
#    print(motors.Gripper2.colorSensor.rgb)

#print(deichhandler.männlidriver(0,[]))