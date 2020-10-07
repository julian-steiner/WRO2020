#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
from GameBoard import Gameboard
import time
from ev3dev2 import power

driveTrain = DriveTrain()
gripper = Gripper()
board = Gameboard(driveTrain)

line = ["Black", "Brown"]
blueLine = ["Green", "Blue"]
speed = 30
aggression = 1.55

battery = power.PowerSupply()
print(battery.measured_volts)
driveTrain.driveCheckpoints(0, 1, 0, 90)

    

# driveTrain.driveForward(speed, 27)
# driveTrain.turnAngle(20, 90)
# driveTrain.followToLine(speed, aggression, blueLine, line)
# # driveTrain.driveForward(speed, 15)
# driveTrain.followLine(speed, aggression, blueLine, 15)
# color = gripper.RomerColor()[0]
# board.setHouse(0, color)
# print(color)
# if(color != "None"):
#         driveTrain.driveForward(-100, 7)
#         driveTrain.driveForward(100, 5)
#         driveTrain.driveForward(speed, 2)
#         driveTrain.turnAngle(20, 180)
#         driveTrain.followToLine(speed, aggression, blueLine, line)    
# else:
#         driveTrain.driveForward(-20, 4)
#         # driveTrain.turnAngle(-20,90)
#         driveTrain.turnToLine(-20,  line)
#         driveTrain.followToLine(speed, aggression, line, line)
#         gripper.lowerMotor(-60)
#         time.sleep(1)
#         gripper.moveMotor(0, 0)
#         driveTrain.driveForward(25, 12)
#         color = gripper.RomerColor()[0]
#         print(gripper.RomerColor()[0])
#         print(color)
#         board.setSand(0, color)
#         gripper.moveMotor(20, 130)
#         time.sleep(1)
#         driveTrain.driveForward(20, -12)


# print("----Houses----")
# print(board.houses)
# print("----Sand----")
# print(board.sand)
# print("----Bricks----")
# print(board.bricks)
# while True:
#     input("")
#     print(gripper.color1.rgb)
#     print(gripper.RomerColor()[0])