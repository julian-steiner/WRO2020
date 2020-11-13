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

driveTrain.driveCheckpoints("R6", 0, 0, 0, '11')

checkpoint = 0
offset = 0

# checkpoint = 3
# offset = 0
# driveTrain.driveCheckpoints("R6", 3, offset, 0, '11')
Motors.Gripper1.colorSensor.rgb
Motors.Gripper2.colorSensor.rgb
Gameboard.setHouse(2, "Blue")
Gameboard.setHouse(3, "Green")
Gameboard.setBrick(0, "Yellow")
Gameboard.setBrick(1, "Red")
Gameboard.setSand(1, "Blue")
Gameboard.setSand(0, "Green")
Gameboard.humans = [0, 0, "Red", "Yellow"]
Gameboard.bricksArranged = []

while checkpoint != 6:
    action = Gameboard.calculateMove(checkpoint)
    print("[Main]   Action:  " + str(action))
    print("[Main]   Offset:  " + str(offset))
    print("[Main]   Checkpoint:  "  + str(checkpoint))
    if action[0] == 0:
        Gameboard.setOrderDelivered(action[1])
    elif action[0] == 1:
        if(Gameboard.houses[checkpoint] != RobotContainer.getLoaded()[1]):
            driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
            offset = 0
            print("Executed drive to point")
        else:
            if offset == 180:
                print("Offset is 180")
                driveTrain.driveForward(RobotContainer.SPEED, 5)
                driveTrain.turnAngle(RobotContainer.TURN_SPEED, 180)
                driveTrain.driveForward(RobotContainer.SLOW_SPEED, 3)
        checkpoint = action[1]
        offset = 180
        bagHandler.deliver(checkpoint, 0)
    elif action[0] == 2:
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
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
        # driveTrain.turnAngle(RobotContainer.TURN_SPEED, 180)
        # driveTrain.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 22)
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
        driveTrain.driveCheckpoints(checkpoint, action[1], offset, 0)
        checkpoint = action[1]
        deichHandler.pickUpBoth(checkpoint)
        offset = 180
    elif action[0] == 11:
        driveTrain.driveCheckpoints(checkpoint, 6, offset, 0)
        checkpoint = 6
        offset = 0