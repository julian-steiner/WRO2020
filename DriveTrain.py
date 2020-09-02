from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank
import RobotContainer

class DriveTrain:
    def __init__(self):
        self.rc = RobotContainer.RobotContainer()
        self.driveColorLeft = ColorSensor(self.rc.DRIVE_COLOR_LEFT)
        self.driveColorRight = ColorSensor(self.rc.DRIVE_COLOR_RIGHT)
        self.driveLeft = LargeMotor(self.rc.DRIVE_LEFT)
        self.driveRight = LargeMotor(self.rc.DRIVE_RIGHT)
        self.tank_drive = MoveTank(self.rc.DRIVE_LEFT, self.rc.DRIVE_RIGHT)
    
    def followLine(self, speed, aggression, LineColor, distance):
        def lineDrive():
            leftColor = self.driveColorLeft.color_name
            rightColor = self.driveColorRight.color_name

            if leftColor in LineColor:
                if rightColor in LineColor:
                    self.tank_drive.off()
                else:
                    self.tank_drive.on(SpeedPercent(speed/aggression), SpeedPercent(speed))
            else:
                if rightColor in LineColor:
                    self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed/aggression))
                else:
                    self.tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
        
        if distance == 0:
            lineDrive()

        else:
            self.driveLeft.reset()
            self.driveRight.reset()
            motor1 = self.driveLeft.rotations
            motor2 = self.driveRight.rotations
            dist = (motor1 + motor2) / 2
            rotations = distance / (self.rc.WHEEL_DIAMETER * 3.14159)
            if dist <= 0:
                dist *= -1
            while rotations > dist:
                motor1 = self.driveLeft.rotations
                motor2 = self.driveRight.rotations
                dist = (motor1 + motor2) / 2
                if dist <= 0:
                    dist *= -1
                lineDrive()

    def driveToLine(self, speed, aggression, LineColor, StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.followLine(-20, 9, LineColor, 0)

    def driveForward(self, speed, distance):
        rotations = distance / (self.rc.WHEEL_DIAMETER * 3.14159)
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations)
    
    def turnAngle(self, speed, angle):
        distance = (self.rc.WHEEL_DISTANCE * 3.14159 * angle) / 360
        rotations = distance / (self.rc.WHEEL_DIAMETER * 3.14159) 
        self.tank_drive.on_for_rotations(SpeedPercent(speed), SpeedPercent(-speed), rotations)

    def getSensorStates(self, colors):
        values = [0, 0]
        sensor_values = [self.driveColorLeft.color_name, self.driveColorRight.color_name]
        for i in range(len(sensor_values)):
            if sensor_values[i] in colors:
                values[i] = 1
        return values
