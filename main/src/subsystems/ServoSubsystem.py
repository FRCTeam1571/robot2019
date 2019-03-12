import wpilib
from wpilib import Servo

from wpilib.command.subsystem import Subsystem

from robotmap import *


class ServoSubsystem(Subsystem):
    def __init__(self):
        self.servo = Servo(servoPort)

    def moveServo(self, value):
        self.servo.set(value)
