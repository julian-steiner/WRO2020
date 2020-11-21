from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from Motors import Motors
import time
import ev3dev2.power
from GameBoard import Gameboard
from RobotContainer import RobotContainer

class DriveTrain:
    def __init__(self):
        self.tank_drive = MoveTank(Motors.DriveTrain.leftPort, Motors.DriveTrain.rightPort)
        self.tank_drive.set_polarity("inversed")
        print("INitialized driveTrain")
        
    #getter
    def getSensorStates(self, colors):
        #returns if both sensors match to the color
        values = [0, 0]
        sensor_values = [Motors.DriveTrain.driveColorLeft.color_name, Motors.DriveTrain.driveColorRight.color_name]
        for i in range(len(sensor_values)):
            if sensor_values[i] in colors:
                values[i] = 1
        return values

    def getMotorRotations(self):
        return self.tank_drive.left_motor.rotations, self.tank_drive.right_motor.rotations
    
    #calculation functions
    def optimizeAngle(self, angle):
        if angle < -180:
            return angle + 360
        elif 180 < angle:
            return angle - 360
        if(RobotContainer.getLoaded()[0]):
            angle *= RobotContainer.LOADED_FACTOR
        return angle  

    #simple drive functions
    def driveForward(self, speed, distance):
        rotations = distance / (RobotContainer.WHEEL_DIAMETER * 3.14159)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)

    def turnAngle(self, speed, angle):
        self.tank_drive.off()
        time.sleep(0.2)
        angle *= -1
        angle = self.optimizeAngle(angle)
        if(RobotContainer.getLoaded()[0]):
            speed = RobotContainer.SLOW_TURN_SPEED
        rotations = (angle * RobotContainer.WHEEL_DISTANCE) / (360 * RobotContainer.WHEEL_DIAMETER)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(-speed), rotations)
        time.sleep(0.2)
    
    def driveToLine(self, speed,  StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
        self.tank_drive.stop()

    #line drive functions
    
    def followLine(self, speed, aggression, LineColor, distance):
        def lineDrive():
            if "Black" in LineColor:
                threshold = 70
                leftReflected = Motors.DriveTrain.driveColorLeft.reflected_light_intensity
                if(leftReflected < threshold):
                    self.tank_drive.on(speed, speed + RobotContainer.LOW_AGGRESSION)
                else:
                    self.tank_drive.on(speed + RobotContainer.LOW_AGGRESSION, speed)
            
            leftColor = Motors.DriveTrain.driveColorLeft.color_name
            rightColor = Motors.DriveTrain.driveColorRight.color_name

            if leftColor in LineColor:
                if rightColor in LineColor:
                    self.tank_drive.off()
                else:
                    self.tank_drive.on(SpeedPercent(speed - aggression), SpeedPercent(speed))
            else:
                if rightColor in LineColor:
                    self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed - aggression))
                else:
                    self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
        
        if distance == 0:
            lineDrive()

        else:
            Motors.DriveTrain.driveLeft.reset()
            Motors.DriveTrain.driveRight.reset()
            self.tank_drive.set_polarity("inversed")
            print("Resetted DriveTrain")
            motor1 = Motors.DriveTrain.driveLeft.rotations
            motor2 = Motors.DriveTrain.driveRight.rotations
            dist = (motor1 + motor2) / 2
            rotations = distance / (RobotContainer.WHEEL_DIAMETER * 3.14159)
            if dist <= 0:
                dist *= -1
            while rotations > dist:
                motor1 = Motors.DriveTrain.driveLeft.rotations
                motor2 = Motors.DriveTrain.driveRight.rotations
                dist = (motor1 + motor2) / 2
                if dist <= 0:
                    dist *= -1
                lineDrive()
            self.tank_drive.stop()

    def followToLine(self, speed, aggression, LineColor, StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.followLine(speed, aggression, LineColor, 0)
        self.tank_drive.stop()

    def center(self, color, direction = 1):
        speed = 5
        correction = 10
        if(direction == 1):
            while Motors.DriveTrain.driveColorLeft.color_name != color:
                self.tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
            while Motors.DriveTrain.driveColorRight.color_name != color:
                self.tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
            self.turnAngle(5,  -correction)
            self.tank_drive.off()
        else:
            while Motors.DriveTrain.driveColorRight.color_name != color:
                self.tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
            while Motors.DriveTrain.driveColorLeft.color_name != color:
                self.tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
            self.turnAngle(5,  correction)
            self.tank_drive.off()
                    
    def turnToLine(self, speed, lineColor):
        speed *= -1
        self.tank_drive.on(SpeedPercent(speed), -1*SpeedPercent(speed))
        if(speed > 0):
            while Motors.DriveTrain.driveColorRight.color_name not in lineColor:
                pass
            self.turnAngle(speed, 5)
            self.tank_drive.stop()
        else:
            while Motors.DriveTrain.driveColorLeft.color_name not in lineColor:
                pass
            self.turnAngle(speed, 5)
            self.tank_drive.stop()

    # complex drive functions
            
    def driveCheckpoints(self, point1, point2, s_offset, e_offset, end_distance = '12'): 
        long_distance = 128
        end_distance = float(end_distance)
        if  Gameboard.deliveredBags in Gameboard.houses:
            end_distance = '10'
        
        # case if the bot is already at the point
        if point1 == point2:
            self.turnAngle(RobotContainer.TURN_SPEED, -s_offset)
        
        # set the line colors 
        if point1 in [0, 1]:
            line_c = RobotContainer.BLUELINE
        else:
            line_c = RobotContainer.REDLINE
        if point2 in [0, 1]:
            line_c_second = RobotContainer.BLUELINE
        else:
            line_c_second= RobotContainer.REDLINE

        #drive across the width
        if Gameboard.getDistance(point1, point2) == 1:
            self.turnAngle(RobotContainer.TURN_SPEED, 180 - s_offset)
            self.followToLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c, RobotContainer.LINE)
            self.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c, end_distance)
            self.turnAngle(RobotContainer.TURN_SPEED, e_offset)
        
        #drive across the length
        elif Gameboard.getDistance(point1, point2) == 2:
            self.turnAngle(RobotContainer.TURN_SPEED, 180 - s_offset)
            self.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION,  line_c, 25)
            self.turnAngle(RobotContainer.TURN_SPEED, 90*(-1)**(point1))
            self.driveForward(RobotContainer.FAST_SPEED, long_distance)
            self.turnAngle(RobotContainer.TURN_SPEED, 90*(-1)**(point2+1))
            self.followToLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c_second, RobotContainer.LINE)
            self.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c_second, end_distance)
            self.turnAngle(RobotContainer.TURN_SPEED, e_offset)
        
        #drive to the startPoint
        elif point1 in [0, 1, 2, 3] and point2 in ["R6",  "R5"]:
            if point1 in [0,  1] and point2 == "R6" or point1 in [2, 3] and point2 == "R5":
                dist = 24
            else:
                dist = 100
            self.turnAngle(RobotContainer.TURN_SPEED, 180 - s_offset)
            self.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c, 27)
            self.turnAngle(RobotContainer.TURN_SPEED, 90*(-1)**point1)
            self.driveForward(RobotContainer.SPEED, dist)
        
        #drive from the startPoint to the checkpoint
        elif point1 in ["R5", "R6"] and point2 in [0, 1, 2, 3]:
            if point2 in [0,  1] and point1 == "R6" or point2 in [2, 3] and point1 == "R5":
                dist = 25
            else:
                dist = 100
            self.driveForward(RobotContainer.SPEED, dist)
            self.turnAngle(RobotContainer.TURN_SPEED, 90*(-1)**(point2 + 1))
            self.followToLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c_second, RobotContainer.LINE)
            self.followLine(RobotContainer.SPEED, RobotContainer.AGGRESSION, line_c_second, end_distance)
            self.turnAngle(RobotContainer.TURN_SPEED, e_offset)