#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
import time

driveTrain = DriveTrain()
gripper = Gripper()
<<<<<<< HEAD

line = ["Black", "Brown"]
blueLine = ["Green", "Blue"]
driveTrain.driveForward(20, 29)
driveTrain.turnAngle(20, 90)
driveTrain.followToLine(20, 4, blueLine, line)
driveTrain.driveForward(20, 20)
print()
=======
test = Sound()
gripper2 = Gripper2()
def program():
    driveTrain.driveForward(-50,28)
    driveTrain.turnAngle(-20, 92)
    driveTrain.driveToLine(-20, 4, ["Green", "Blue"], ["Black", "Brown"])
    driveTrain.turnAngle(-20, 180)
    driveTrain.driveForward(30, 29)
    print(gripper.color2.color_name)

program() 
>>>>>>> newRobot


