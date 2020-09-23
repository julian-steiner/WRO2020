#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
import time

driveTrain = DriveTrain()
gripper = Gripper()

line = ["Black", "Brown"]
blueLine = ["Green", "Blue"]
speed = 30
aggression = 2

driveTrain.driveForward(speed, 29)
driveTrain.turnAngle(20, 90)
driveTrain.followToLine(speed, aggression, blueLine, line)
driveTrain.driveForward(speed, 15)
color = gripper.RomerColor()[0]
if(color != 2):
        driveTrain.driveForward(-100, 7)
        driveTrain.driveForward(100, 7)
else:
        driveTrain.driveForward(speed,15)
        driveTrain.turnAngle(20,90)
        driveTrain.followToLine(speed, aggression, line, line)
        gripper.lowerMotor(100)
print(color)

# while True:
#     input("")
#     print(gripper.color1.rgb)
#     print(gripper.RomerColor()[0])