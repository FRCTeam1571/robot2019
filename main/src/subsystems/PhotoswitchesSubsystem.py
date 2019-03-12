from wpilib import DigitalInput

from wpilib.command.subsystem import Subsystem

from robotmap import *


class Pneumatics(Subsystem):
    def __init__(self):
        self.rightSensor = DigitalInput(0)
        self.leftSensor = DigitalInput(1)

    def get(self, sensor):
        return not sensor.get()
