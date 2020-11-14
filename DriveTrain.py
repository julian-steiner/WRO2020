from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from Motors import Motors
import time
import ev3dev2.power
import RobotContainer

class DriveTrain:
    def __init__(self):
    
        self.rc = RobotContainer.RobotContainer()
        self.tank_drive = MoveTank(Motors.DriveTrain.leftPort, Motors.DriveTrain.rightPort)
        self.tank_drive.set_polarity("inversed")
    
    def followLine(self, speed, aggression, LineColor, distance):
        def lineDrive():
            if "Black" in LineColor:
                threshold = 70
                leftReflected = Motors.DriveTrain.driveColorLeft.reflected_light_intensity
                if(leftReflected < threshold):
                    self.tank_drive.on(speed, speed + self.rc.LOW_AGGRESSION)
                else:
                    self.tank_drive.on(speed + self.rc.LOW_AGGRESSION, speed)
                        
            # leftColor = self.driveColorLeft.color_name
            # rightColor = self.driveColorRight.color_name
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
            motor1 = Motors.DriveTrain.driveLeft.rotations
            motor2 = Motors.DriveTrain.driveRight.rotations
            dist = (motor1 + motor2) / 2
            rotations = distance / (self.rc.WHEEL_DIAMETER * 3.14159)
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

    def driveToLine(self, speed,  StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
        self.tank_drive.stop()

    def driveForward(self, speed, distance):
        rotations = distance / (self.rc.WHEEL_DIAMETER * 3.14159)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)
    
    def turnAngle(self, speed, angle):
        self.tank_drive.off()
        time.sleep(0.2)
        angle *= -1
        angle = self.optimizeAngle(angle)
        if(RobotContainer.RobotContainer.getLoaded()[0]):
            speed = self.rc.SLOW_TURN_SPEED
        rotations = (angle * self.rc.WHEEL_DISTANCE) / (360 * self.rc.WHEEL_DIAMETER)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(-speed), rotations)
        time.sleep(0.2)

    def center(self, color, direction = 1):
        speed = 5
        if(direction == 1):
            while Motors.DriveTrain.driveColorLeft.color_name != color:
                self.tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
            while Motors.DriveTrain.driveColorRight.color_name != color:
                self.tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
            self.turnAngle(5,  -9)
            self.tank_drive.off()
        else:
            while Motors.DriveTrain.driveColorRight.color_name != color:
                self.tank_drive.on(SpeedPercent(-speed), SpeedPercent(speed))
            while Motors.DriveTrain.driveColorLeft.color_name != color:
                self.tank_drive.on(SpeedPercent(speed), SpeedPercent(-speed))
            self.turnAngle(5,  9)
            self.tank_drive.off()

    def getSensorStates(self, colors):
        values = [0, 0]
        sensor_values = [Motors.DriveTrain.driveColorLeft.color_name, Motors.DriveTrain.driveColorRight.color_name]
        for i in range(len(sensor_values)):
            if sensor_values[i] in colors:
                values[i] = 1
        return values

    def setConfigs(self, speed):
        self.tank_drive.reset()
        self.tank_drive.set_polarity("inversed")
        self.tank_drive.on(speed, -speed)
        while Motors.DriveTrain.driveColorRight.color_name not in ['Black', 'Brown']:
            pass

        while Motors.DriveTrain.driveColorLeft.color_name not in ['Black', 'Brown']:
            pass

        cl = self.getMotorRotations()[0]
        while Motors.DriveTrain.driveColorRight.color_name not in ['Black', 'Brown']:
            pass

        cl += ((self.getMotorRotations()[0] - cl)/2)
        self.tank_drive.stop()
        self.tank_drive.on_for_rotations(-speed, speed, (self.getMotorRotations()[0] - cl)/2)
        return cl*2*self.rc.WHEEL_DIAMETER
                    
    def turnToLine(self, speed, lineColor):
        speed *= -1
        self.tank_drive.on(SpeedPercent(speed), -1*SpeedPercent(speed))
        if(speed > 0):
            while Motors.DriveTrain.driveColorRight.color_name not in lineColor:
                pass
            self.turnAngle(speed, -6)
            self.tank_drive.stop()
        else:
            while Motors.DriveTrain.driveColorLeft.color_name not in lineColor:
                pass
            self.turnAngle(speed, 6)
            self.tank_drive.stop()
            
    def getMotorRotations(self):
        return self.tank_drive.left_motor.rotations, self.tank_drive.right_motor.rotations
    
    def optimizeAngle(self, angle):
        if angle < -180:
            return angle + 360
        elif 180 < angle:
            return angle - 360
        if(RobotContainer.RobotContainer.getLoaded()[0]):
            angle *= self.rc.LOADED_FACTOR
        return angle  

    # def turnToHouse(self, checkPoint):
    #     self.turnAngle(self.rc.TURN_SPEED, 120*-1**checkPoint)
    #     if(checkPoint == 0):
    #         while Motors.DriveTrain.driveColorLeft.color_name != "Blue":
    #             self.tank_drive.on(self.rc.SLOW_TURN_SPEED, -self.rc.SLOW_TURN_SPEED)
    #         self.turnAngle(self.rc.TURN_SPEED, -20)
    #         self.tank_drive.stop()
    #     elif (checkPoint == 1):
    #         while Motors.DriveTrain.driveColorRight.color_name != "Blue":
    #             print(Motors.DriveTrain.driveColorRight.color_name)
    #             self.tank_drive.on(-self.rc.SLOW_TURN_SPEED, self.rc.SLOW_TURN_SPEED)
    #         self.turnAngle(self.rc.TURN_SPEED, 20)
    #         self.tank_drive.stop()
    #     elif (checkPoint == 2):
    #         while Motors.DriveTrain.driveColorRight.color_name != "Red":
    #             self.tank_drive.on(-self.rc.SLOW_TURN_SPEED, self.rc.SLOW_TURN_SPEED)
    #         self.turnAngle(self.rc.TURN_SPEED, -20)
    #         self.tank_drive.stop()
    #     elif (checkPoint == 3):
    #         while Motors.DriveTrain.driveColorLeft.color_name != "Blue":
    #             self.tank_drive.on(self.rc.SLOW_TURN_SPEED, -self.rc.SLOW_TURN_SPEED)
    #         self.turnAngle(self.rc.TURN_SPEED, 20)
    #         self.tank_drive.stop()
    
    def driveCheckpoints(self, point1, point2, s_offset, e_offset, end_distance = '12'): 
        long_distance = 128
        end_distance = float(end_distance)
        if point1 == point2:
            self.turnAngle(self.rc.TURN_SPEED, e_offset - s_offset)
            if point1  == "1":
                self.turnToLine(self.rc.TURN_SPEED, "Blue")
            
        if point1 == 0:
            if point2 == 1:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif point2 == 2:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED,e_offset)
                self.turnAngle(self.rc.TURN_SPEED, s_offset - 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveCheckpoints(3, 2, 180, e_offset)
                
            elif point2 == 3:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.turnAngle(self.rc.TURN_SPEED, s_offset - 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, e_offset + 90)
            elif point2 == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveForward(self.rc.SPEED, 24)

        elif point1 == 1:
            if point2 == 0:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED,e_offset)
            elif point2 == 2:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.driveCheckpoints(1, 0, s_offset, 0)
                self.turnAngle(self.rc.TURN_SPEED, s_offset - 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveCheckpoints(3, 2, 180, e_offset)
            elif point2 == 3:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.driveCheckpoints(1, 0, s_offset, 0)
                self.turnAngle(self.rc.TURN_SPEED, s_offset - 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, e_offset + 90)
            elif point2 == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 24)

        if point1 == 2:
            if point2 == 3:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif point2 == 0:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.driveForward(self.rc.SPEED, 12)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, 90 - e_offset)
            elif point2 == 1:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.driveForward(self.rc.SPEED, 12)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveCheckpoints(0, 1, 180, e_offset)

            elif point2 == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.driveForward(self.rc.SPEED, 100)

        if point1 == 3:
            if point2 == 2:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.REDLINE, end_distance)
                self.turnAngle(self.rc.TURN_SPEED, e_offset)
            elif point2 == 0:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.turnAngle(self.rc.TURN_SPEED, 90 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, -90 + e_offset)
            elif point2 == 1:
                # self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                # self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                # self.turnAngle(self.rc.TURN_SPEED, -90)
                # self.driveForward(self.rc.FAST_SPEED, long_distance)
                # self.turnAngle(self.rc.TURN_SPEED, 90)
                # self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                # self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, end_distance)
                # self.turnAngle(self.rc.TURN_SPEED, e_offset)
                self.turnAngle(self.rc.TURN_SPEED, 90 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 25)
                self.driveForward(self.rc.SPEED, 40)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.LINE, 55)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveCheckpoints(0, 1, 180, e_offset)
            elif point2 == 6:
                self.turnAngle(self.rc.TURN_SPEED, 180 - s_offset)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 25)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.driveForward(self.rc.SPEED, 100)

        if point1 == "R6" or point1 == "R5":
            self.driveForward(self.rc.SPEED, 26)
            self.turnAngle(self.rc.TURN_SPEED, -90)
            if(point1 == "R6"):
                line = self.rc.BLUELINE
            else:
                line = self.rc.REDLINE
            self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, line, self.rc.LINE)
            self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, line, end_distance)

        if point1 == "R4" or point1 == "R1":
            self.driveForward(self.rc.SPEED, 30)
            if(point1 == "R1"):
                if point2 in [0, 1]:
                    self.turnAngle(self.rc.TURN_SPEED, 90)
                else:
                    self.turnAngle(self.rc.TURN_SPEED, -90)
            else:
                if point2 in [0, 1]:
                    self.turnAngle(self.rc.TURN_SPEED, -90)
                else:
                    self.turnAngle(self.rc.TURN_SPEED, 90)
            self.driveForward(self.rc.SPEED, 63)
            self.turnAngle(self.rc.TURN_SPEED, -90)
            if point2 in [0, 1]:
                line = self.rc.BLUELINE
            else:
                line = self.rc.REDLINE
            self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, line, self.rc.LINE)
            self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, line, end_distance)
        
        if point1 == "R2" or point1 == "R3":
            self.driveForward(self.rc.SPEED, 10)
            if(point1 == "R2"):
                if point2 in [0, 1]:
                    self.turnAngle(self.rc.TURN_SPEED, 90)
                else:
                    self.turnAngle(self.rc.TURN_SPEED, -90)
            else:
                if point2 in [0, 1]:
                    self.turnAngle(self.rc.TURN_SPEED, -90)
                else:
                    self.turnAngle(self.rc.TURN_SPEED, 90)
            self.driveForward(self.rc.SPEED, 64)
            self.turnAngle(self.rc.TURN_SPEED, -90)
            if point2 in [0, 1]:
                line = self.rc.BLUELINE
            else:
                line = self.rc.REDLINE
            self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, line, self.rc.LINE)
            self.followLine(self.rc.SLOW_SPEED, self.rc.AGGRESSION, line, end_distance)
