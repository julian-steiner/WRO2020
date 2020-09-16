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
driveTrain.driveForward(20, 29)
driveTrain.turnAngle(20, 90)
driveTrain.followToLine(20, 4, blueLine, line)
driveTrain.driveForward(20, 20)
print()


