from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
from Motors import Motors
import ev3dev2.power
import RobotContainer

class DriveTrain:
    def __init__(self):
    
        self.rc = RobotContainer.RobotContainer()
        # self.driveColorLeft = ColorSensor(self.rc.DRIVE_COLOR_LEFT)
        # self.driveColorRight = ColorSensor(self.rc.DRIVE_COLOR_RIGHT)
        # self.driveLeft = LargeMotor(self.rc.DRIVE_LEFT)
        # self.driveRight = LargeMotor(self.rc.DRIVE_RIGHT)
        # self.tank_drive = MoveTank(self.rc.DRIVE_LEFT, self.rc.DRIVE_RIGHT)
        self.tank_drive = MoveTank(Motors.DriveTrain.leftPort, Motors.DriveTrain.rightPort)
        self.tank_drive.set_polarity("inversed")
    
    def followLine(self, speed, aggression, LineColor, distance):
        def lineDrive():
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
                print(dist * (self.rc.WHEEL_DIAMETER * 3.14159))
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
        angle *= -1
        rotations = (angle * self.rc.WHEEL_DISTANCE) / (360 * self.rc.WHEEL_DIAMETER)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(-speed), rotations)

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
        print("Started")
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
            self.tank_drive.stop()
            print("Stopped with positive number")
        else:
            while Motors.DriveTrain.driveColorLeft.color_name not in lineColor:
                pass
            self.tank_drive.stop()
            print("Stopped with negative number")       
            
    def getMotorRotations(self):
        return self.tank_drive.left_motor.rotations, self.tank_drive.right_motor.rotations
    
    def optimizeAngle(self, angle):
        if angle < -180:
            return angle + 360
        elif 180 < angle:
            return angle - 360
        return angle  

    def driveCheckpoints(self, point1, point2, s_offset, e_offset):            
        if point1 == 0:
            if point2 == 1:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 2:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 3:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
        elif point1 == 1:
            if point2 == 0:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 2:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 3:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
        if point1 == 2:
            if point2 == 3:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 0:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 1:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 13)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
        if point1 == 3:
            if point2 == 2:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 0:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, -90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, 14)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))
            elif point2 == 1:
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(180 - s_offset))
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 27)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(-90))
                self.driveForward(self.rc.SPEED, 130)
                self.turnAngle(self.rc.TURN_SPEED, 90)
                self.followToLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.BLUELINE, self.rc.LINE)
                self.followLine(self.rc.SPEED, self.rc.AGGRESSION, self.rc.REDLINE, 13)
                self.turnAngle(self.rc.TURN_SPEED, self.optimizeAngle(e_offset))