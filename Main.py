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

gripper.lowerMotor(-100)
time.sleep(0.5)
gripper.lowerMotor(70)
driveTrain.turnAngle(RobotContainer.TURN_SPEED, -90)
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 65)
deichHandler.männliDriver(3, False)
