#!/usr/bin/env micropython
from DriveTrain import DriveTrain
from ev3dev2.sound import Sound
from Gripper import Gripper
from Gripper2 import Gripper2
import time

driveTrain = DriveTrain()
gripper = Gripper()
test = Sound()

gripper.lowerMotor(-30) #Configure Gripper
driveTrain.driveToLine(-20, 8, ["Green", "Blue"], ["Black", "Brown"])
driveTrain.driveForward(-40, 13)
driveTrain.turnAngle(-20, 90)
driveTrain.followLine(-20, 9, ["Black", "Brown"], 10)
driveTrain.driveForward(-40, -40)
driveTrain.driveForward(-20, -7)
print(gripper.getColors()) #Drive and watch the color
test.speak(gripper.getColors()[1])
time.sleep(0.5)
driveTrain.driveForward(-20, 5)
driveTrain.followLine(-20, 10, ["Black", "Brown"], 40)
print("Started Turning")
driveTrain.turnAngle(20, 180)
print("Ended Turning")
driveTrain.driveToLine(-20, 6, ["Black", "Brown"],["Black", "Brown"]) #Go back and turn
gripper.lowerMotor(30)
driveTrain.driveForward(-20, 15)
gripper.moveMotor(40, 130) #Collect the wooden piles
time.sleep(0.5)
driveTrain.driveForward(20, 10)

gripper2 = Gripper2()
print("*")
gripper2.movemotor(30,True)
time.sleep(2)
gripper2.movemotor(30,False)
time.sleep(10)