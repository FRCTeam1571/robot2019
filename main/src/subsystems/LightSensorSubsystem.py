import wpilib

from wpilib.command.subsystem import Subsystem


class LightSensor(Subsystem):
    def __init__(self, dioNum):
        self.sensor = wpilib.DigitalInput(dioNum)

    def getState(self):
        return self.sensor.get()