#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
from GameBoard import Gameboard
from SandBagHandling import BagHandler
from RobotContainer import RobotContainer
from Motors import Motors
import time
from ev3dev2 import power

driveTrain = DriveTrain()
gripper = Gripper()
gripper2 = Gripper2()
board = Gameboard(driveTrain)
bagHandler = BagHandler(driveTrain, gripper)
board.setHouse(3, "Green")
motors = Motors()

driveTrain.driveCheckpoints(2, 1, 0, 180)
driveTrain.driveCheckpoints(1, 6, 180, 0)

# print("Loaded " + str(RobotContainer.getLoaded()[0]))
# bagHandler.pickUp(2, 0, board.houses)

# RobotContainer.setLoaded("Green", 0)
# bagHandler.deliver(2, 0, board.houses)
# RobotContainer.setLoaded(None, None)
# print(RobotContainer.getLoaded()[0])
# driveTrain.driveCheckpoints(3, 2, 0, 0)




# driveTrain.followToLine(30, 10, ["Yellow", "Red"], ["Black"])
# while True:
#     left, right = Motors.DriveTrain.driveColorLeft.rgb, Motors.DriveTrain.driveColorRight.rgb
#     white = [[255, 223, 200]]
#     yellow = [[250, 170, 113], [250, 200, 139]]
#     red = [[240, 85, 85], [250, 160, 130]]
#     black = [[180, 170, 170], [190, 170, 130]]
#     green = [[150, 160, 130], [200, 190, 140]]
#     blue = [[120, 120, 120], [230, 206, 219]]
    # print(left, right, driveTrain.RomerColor([black, white], ["Black", "White"]))
    # print(left, right, driveTrain.RomerColor([red, yellow, white], ["Red", "Yellow", "White"]))

# while True:
#     rgb = motors.Gripper1.colorSensor.rgb
#     print(gripper.RomerColor([13, 12, 20] ,[15, 12, 29], [0, 0, 1], "Green", "Blue", "None") + " " + str(rgb))

# line = ["Black", "Brown"]
# blueLine = ["Green", "Blue"]
# speed = 30
# aggression = 1.55

# battery = power.PowerSupply()
# print(battery.measured_volts)
# driveTrain.driveCheckpoints(3, 1, 0, 0)
# board.setHouse(1, gripper.RomerColor()[0])
# driveTrain.driveCheckpoints(1, 0, 0, 0)
# board.setHouse(0, gripper.RomerColor()[0])
# driveTrain.driveCheckpoints(0, 3, 0, 0)
# board.setHouse(3, gripper.RomerColor()[0])

# print(board.houses)

    

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

#gripper2.movemotor(50,True)

#while True:
#     print(gripper2.RomerColorPD())
#    print(motors.Gripper2.colorSensor.rgb)

