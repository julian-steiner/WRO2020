#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
from GameBoard import Gameboard
from SandBagHandling import BagHandler
from EvacuateOrderHandling import OrderHandling
from RobotContainer import RobotContainer
from DeichHandling import DeichHandler
from Motors import Motors
import time
from ev3dev2 import power

driveTrain = DriveTrain()
gripper = Gripper()
gripper2 = Gripper2()
bagHandler = BagHandler(driveTrain, gripper)
<<<<<<< Updated upstream
deichHandler = DeichHandler(gripper, gripper2, driveTrain, time, bagHandler)
Gameboard.setHouse(2, "Green")
Gameboard.setHouse(3, "Blue")
motors = Motors()

Gameboard.setHuman(3, "Yellow")
Gameboard.setBrick(2, "Yellow")
RobotContainer.setLoaded(0, "Yellow")
=======
deichhandler = DeichHandler(gripper,gripper2,driveTrain,time,bagHandler)
board.setHouse(3, "Green")
motors = Motors()

# print("Loaded " + str(RobotContainer.getLoaded()[0]))
# bagHandler.pickUp(2, 0, board.houses)

>>>>>>> Stashed changes

# deichHandler.scanHumans(3, -90)
# print(Gameboard.humans)
checkpoint = deichHandler.scanBlocks(3)
print(Gameboard.humans)
time.sleep(2)
checkpoint = 2
deichHandler.DeichPutDown(checkpoint)

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

<<<<<<< Updated upstream
=======
# driveTrain.turnToLine((-1)**(0 + 1)*RobotContainer.TURN_SPEED,"Black")
# time.sleep(0.2)
# driveTrain.turnAngle(RobotContainer.TURN_SPEED, 8*(-1)**0)
# time.sleep(0.2)
# driveTrain.driveForward(RobotContainer.SLOW_SPEED,-49.5)

# while True:
# #     # print(gripper2.RomerColorPD())
#     print(motors.Gripper2.colorSensor.rgb)

gripper2.movemotor(100,True)

deichhandler.deichbringer(0,2,-90)

#driveTrain.center("Black","-1")
>>>>>>> Stashed changes
