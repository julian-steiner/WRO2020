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
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 86)
deichHandler.männliDriver(3, False)
driveTrain.followLine(RobotContainer.FAST_SPEED,RobotContainer.AGGRESSION,RobotContainer.LINE,60)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 15)
driveTrain.turnAngle(RobotContainer.TURN_SPEED, -90)
driveTrain.driveForward(RobotContainer.FAST_SPEED, -13)
gripper2.movemotor(100, -1)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 7)
driveTrain.turnAngle(RobotContainer.TURN_SPEED, 89)
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 72)
driveTrain.driveCheckpoints(1, 0, -90, 90, end_distance=10)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 22)
deichHandler.männliDriver(0, False)
driveTrain.followLine(RobotContainer.FAST_SPEED,RobotContainer.AGGRESSION,RobotContainer.LINE,60)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 16)
driveTrain.turnAngle(RobotContainer.TURN_SPEED, 90)
driveTrain.driveForward(RobotContainer.FAST_SPEED, -13)
gripper2.movemotor(100, -1)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 7)
driveTrain.turnAngle(RobotContainer.TURN_SPEED, 90)
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 60)
bagHandler.pickUp(1, False)
driveTrain.driveCheckpoints(0, 1, 180, 90, end_distance=10)
bagHandler.deliver(0, 0)
driveTrain.driveForward(RobotContainer.SPEED, -22)
driveTrain.driveCheckpoints(0, 1, 90, 90)
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 40)
driveTrain.driveForward(RobotContainer.FAST_SPEED, 40)
driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 65)
bagHandler.pickUp(3, False)
driveTrain.driveCheckpoints(2, 3, 180, 90, end_distance=10)
bagHandler.deliver(0, 0)
driveTrain.driveForward(RobotContainer.SPEED, -25)



# driveTrain.turnAngle(RobotContainer.TURN_SPEED, -90)
# driveTrain.followLine(RobotContainer.FAST_SPEED, RobotContainer.AGGRESSION, RobotContainer.LINE, 60)


