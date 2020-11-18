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

checkpoint = 0
offset = 0
driveTrain.driveCheckpoints("R6", 0, offset, 0, '11')

# checkpoint = 3
# offset = 0
# driveTrain.driveCheckpoints(6, 3, offset, 0, '11')
Motors.Gripper1.colorSensor.rgb
Motors.Gripper2.colorSensor.rgb
Gameboard.setHouse(0, "Blue")
Gameboard.setHouse(3, "Green")
Gameboard.setHuman(3, "Yellow")
Gameboard.setHuman(0, "Red")
Gameboard.setBrick(2, "Yellow")
Gameboard.setSand(1, "Green")
Gameboard.bricksArranged = []

while checkpoint != "R6":
    action = Gameboard.calculateMove(checkpoint)
    print("[Main]   Action:  " + str(action))
    print("[Main]   Offset:  " + str(offset))
    print("[Main]   Checkpoint:  "  + str(checkpoint))
    if action[0] == 0:
        Gameboard.setOrderDelivered(action[1])
    elif action[0] == 1:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        offset = 0
        bagHandler.deliver(checkpoint, 0)
    elif action[0] == 2:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]        
        deichHandler.DeichPutDown(checkpoint)
        offset = 180
    elif action[0] == 3:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        orderHandler.scannhouse(checkpoint)
        offset = 0
    elif action[0] == 4:
        checkpoint = deichHandler.männliDriver(checkpoint, True)
        offset = 180
    elif action[0] == 5:
        deichHandler.scanHumans(checkpoint, True)
        driveTrain.driveForward(RobotContainer.SPEED, -22)
        driveTrain.turnAngle(RobotContainer.TURN_SPEED, -90 * (-1) ** checkpoint)
    elif action[0] == 6:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        checkpoint = deichHandler.WorstCase(checkpoint)
        offset = 180
    elif action[0] == 7:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        bagHandler.pickUp(checkpoint, False)
        offset = 180
    elif action[0] == 8:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        deichHandler.DeichPickUp(checkpoint)
        offset = 180
    elif action[0] == 9:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        checkpoint = deichHandler.männliDriver(checkpoint, False)
        offset = 180
    elif action[0] == 10:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        deichHandler.pickUpBoth(checkpoint)
        offset = 180
    elif action[0] == 11:
        driveTrain.driveCheckpoints(checkpoint, "R6", offset, 0)
        checkpoint = "R6"
        offset = 0