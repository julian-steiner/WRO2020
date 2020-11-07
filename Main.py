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

gripper = Gripper()
gripper2 = Gripper2()
driveTrain = DriveTrain()
bagHandler = BagHandler(driveTrain, gripper)
deichHandler = DeichHandler(gripper, gripper2, driveTrain, bagHandler)
orderHandler = OrderHandling(driveTrain, gripper)

orderHandler.deliverOrder(0)


# checkpoint = 0
# driveTrain.driveCheckpoints(6, 0, 0, 0)

# while checkpoint != 6:
#     action = Gameboard.calculateMove(checkpoint)
#     print(action)
#     if action[0] == 0:
#         orderHandler.deliverOrder(checkpoint)
#     elif action[0] == 1:
#         driveTrain.driveCheckpoints(checkpoint, action[1], 0, 0)
#         checkpoint = action[1]
#         bagHandler.deliver(checkpoint, 0)
#     elif action[0] == 2:
#         checkpoint = deichHandler.DeichPutDown(checkpoint)
#     elif action[0] == 3:
#         Gameboard.setHouse(0, "Green")
#         Gameboard.setHouse(1, "None")
#     elif action[0] == 4:
#         deichHandler.scanHumans(checkpoint, 0, True)
#         checkpoint = deichHandler.scanBlocks(checkpoint, True)
#     elif action[0] == 5:
#         deichHandler.scanHumans(checkpoint, 0, True)
#         driveTrain.turnAngle(RobotContainer.TURN_SPEED, 180)
#         driveTrain.driveForward(RobotContainer.SPEED, 22)
#     elif action[0] == 6:
#         checkpoint = deichHandler.WorstCase(checkpoint)
#     elif action[0] == 7:
#         driveTrain.driveCheckpoints(checkpoint, action[1], 0, 0)
#         checkpoint = action[1]
#         bagHandler.pickUp(checkpoint)
#     elif action[0] == 8:
#         driveTrain.driveCheckpoints(checkpoint, action[1], 0, 0)
#         checkpoint = action[1]
#         deichHandler.DeichPickUp(checkpoint)
#     elif action[0] == 9:
#         checkpoint = deichHandler.männliDriver(checkpoint)
#     elif action[0] == 10:
#         driveTrain.driveCheckpoints(checkpoint, action[1], 0, 0)
#         checkpoint = action[1]
#         deichHandler.pickUpBoth(checkpoint)
#     elif action[0] == 11:
#         driveTrain.driveCheckpoints(checkpoint, 6, 0, 0)
#         checkpoint = 6


        

