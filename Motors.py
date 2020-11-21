from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3, INPUT_4, INPUT_1

class Motors:
    class DriveTrain:
        leftPort = OUTPUT_C
        rightPort = OUTPUT_B
        driveLeft = LargeMotor(leftPort)
        driveRight = LargeMotor(rightPort)
        driveColorLeft = ColorSensor(INPUT_4)
        driveColorRight = ColorSensor(INPUT_3)
    class Gripper1:
        gripperMotor = MediumMotor(OUTPUT_A)
        colorSensor = ColorSensor(INPUT_1)
    class Gripper2:
        gripperMotor = MediumMotor(OUTPUT_D)
        colorSensor = ColorSensor(INPUT_2)
    
def colorRecognition(test_val, color_rgbs, color_names):
    differences = []
    for color in color_rgbs:
        color_diff = 0
        for a in range(3):
            color_diff += (color[a] - test_val[a])**2
        differences.append(color_diff)
    return color_names[differences.index(min(differences))]
