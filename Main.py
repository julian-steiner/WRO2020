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

Gameboard.setBrick(2, "Yellow")
Gameboard.setHuman(3, "Yellow")
Gameboard.setHouse(3, "Blue")
Gameboard.setSand(2, "Blue")

deichHandler.männliDriver(3)

print(Gameboard.bricks)
print(Gameboard.humans)
