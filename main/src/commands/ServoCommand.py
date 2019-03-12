import wpilib

from wpilib.command import TimedCommand

from subsystems.ServoSubsystem import ServoSubsystem

class ServoCommand(TimedCommand):
    def __init__(self):
        self.ServoSubsystem = ServoSubsystem()
        

    def numMap(self, x, in_min, in_max, out_min, out_max):
        '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servoSet(self, twist):
        twistMap = self.numMap(twist, -1.0, 1.0, 0.0, 1.0)
        self.ServoSubsystem.moveServo(twistMap)


