from Gripper2 import Gripper2
from Gripper import Gripper
from Motors import Motors
from RobotContainer import RobotContainer
from DriveTrain import DriveTrain
from time import sleep

def Gripper1PickUp(startpoint,ofset,housecolor):
    return False

class DeichHandler:
    def __init__(self,Gripper,Gripper2,DriveTrain,time):
        self.Gripper = Gripper
        self.Gripper2 = Gripper2
        self.DriveTrain = DriveTrain
        self.rc = RobotContainer
        self.time = time
    
    def DeichPickUp(self,chekpoint,männli):
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 90*(-1)**chekpoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-14)
        self.Gripper2.movemotor(50,True)
        self.time.sleep(1)
        color = self.Gripper2.RomerColorPU()
        print(color, männli)
        if color[0] not in männli:
            self.Gripper2.movemotor(50,False)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,14)
        self.DriveTrain.turnToLine((-1)**chekpoint*(self.rc.TURN_SPEED),"Black")
        return color
    
    def männlidriver(self,chekpoint,männli):
        color = []
        self.DriveTrain.turnToLine((-1)**(chekpoint + 1)*self.rc.TURN_SPEED,"Black")
        self.time.sleep(0.2)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED, 4.2*(-1)**chekpoint)
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-43.75)
        color.append(self.Gripper2.RomerColorPD())
        self.DriveTrain.driveForward(self.rc.SPEED,17.75)
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,20*(-1)**chekpoint)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**chekpoint,"Black")
        self.DriveTrain.turnAngle(self.rc.TURN_SPEED,8*(-1)**(chekpoint +1))
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,-68)
        self.Gripper2.movemotor(50,True)
        self.time.sleep(1)
        color.append(self.Gripper2.RomerColorPU())
        if color[0] != color[1]:
            self.Gripper2.movemotor(50,False)
            self.time.sleep(1)
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,8)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED*(-1)**(chekpoint + 1),"Black")
        self.DriveTrain.followLine(self.rc.SPEED,self.rc.AGGRESSION,self.rc.LINE,24)
        self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
        self.Gripper.PickUp()
        if color[0] != color[1]:
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            self.DriveTrain.turnToLine(self.rc.TURN_SPEED,"Black")
            if chekpoint % 2 == 1:
                chekpoint -= 1
            if chekpoint % 2 == 1:
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
        self.DriveTrain.driveForward(self.rc.SLOW_SPEED,13)

#gripper2.movemotor(50,True)

#while True:
#     print(gripper2.RomerColorPD())
#    print(motors.Gripper2.colorSensor.rgb)

print(deichhandler.männlidriver(0,[]))