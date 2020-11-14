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

# driveTrain.turnToHouse(1)

s_point = "R3"

driveTrain.driveCheckpoints(s_point, 3, 0, 0, '11')

checkpoint = 3
offset = 0

Motors.Gripper1.colorSensor.rgb
Motors.Gripper2.colorSensor.rgb
Gameboard.setHouse(0, "Blue")
Gameboard.setHouse(1, "Green")
Gameboard.setBrick(2, "Yellow")
Gameboard.setBrick(3, "Red")
Gameboard.setSand(2, "Blue")
Gameboard.setSand(3, "Green")
Gameboard.setHuman(0, "Red")
Gameboard.setHuman(1, "Yellow")
Gameboard.bricksArranged = []

while checkpoint not in ["R1", "R2", "R3", "R4", "R5", "R6"]:
    action = Gameboard.calculateMove(checkpoint)
    print("[Main]   Action:  " + str(action))
    print("[Main]   Offset:  " + str(offset))
    print("[Main]   Checkpoint:  "  + str(checkpoint))
    if action[0] == 0:
        Gameboard.setOrderDelivered(checkpoint)
    elif action[0] == 1:
        if(Gameboard.houses[checkpoint] != RobotContainer.getLoaded()[1]):
            driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
            offset = 0
            print("Executed drive to point")
        else:
            if offset == 180:
                print("Offset is 180")
                driveTrain.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, RobotContainer.BLUELINE + RobotContainer.REDLINE, 5)
                driveTrain.turnAngle(RobotContainer.TURN_SPEED, 180)
                driveTrain.followLine(RobotContainer.SLOW_SPEED, RobotContainer.AGGRESSION, RobotContainer.BLUELINE + RobotContainer.REDLINE, 3)
        checkpoint = action[1]
        offset = 180
        bagHandler.deliver(checkpoint, 0)
    elif action[0] == 2:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        offset = -90
        checkpoint = action[1]        
        checkpoint, offset = deichHandler.DeichPutDown(checkpoint)
        offset = 180
    elif action[0] == 3:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        orderHandler.scannhouse(checkpoint)
        offset = 0
    elif action[0] == 4:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        checkpoint = deichHandler.männliDriverWithScan(checkpoint)
        print(checkpoint)
        offset = 180
    elif action[0] == 5:
        deichHandler.scanHumans(checkpoint, 0)
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
        bagHandler.pickUp(checkpoint)
        offset = 180
    elif action[0] == 8:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        deichHandler.DeichPickUp(checkpoint)
        offset = 180
    elif action[0] == 9:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 180)
        checkpoint = action[1]
        checkpoint = deichHandler.männliDriver(checkpoint)
        offset = 180
    elif action[0] == 10:
        if action[1] == 2:
            c_offset = 90
        else:
            c_offset = -90
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        offset = 0
        checkpoint = action[1]
        offset = deichHandler.pickUpBoth(checkpoint, s_offset_b=0)
    elif action[0] == 11:
        driveTrain.driveCheckpoints(checkpoint, "R5", offset, 0)
        checkpoint = 6
        offset = 0