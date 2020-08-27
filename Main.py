#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from Gripper import Gripper
import time

driveTrain = DriveTrain()
gripper = Gripper()

gripper.lowerMotor(30)
driveTrain.driveToLine(-20, 8, ["Green", "Blue"], ["Black", "Brown"])
driveTrain.driveForward(-40, 13)
driveTrain.turnAngle(-20, 90)
driveTrain.followLine(-20, 9, ["Black", "Brown"], 10)
driveTrain.driveForward(-40, -40)
driveTrain.driveForward(-20, -7)
time.sleep(3)
driveTrain.followLine(-20, 10, ["Black", "Brown"], 40)
driveTrain.turnAngle(20, 180)
driveTrain.driveToLine(-20, 10, ["Black", "Brown"],["Black", "Brown"])
gripper.lowerMotor(-30)
driveTrain.driveForward(-20, 15)
gripper.lowerMotor(-40)
