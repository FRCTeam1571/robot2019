import wpilib
from wpilib import DoubleSolenoid

from wpilib.command.subsystem import Subsystem

from robotmap import *


class Pneumatics(Subsystem):
    def __init__(self):
        self.armSolenoid = DoubleSolenoid(0, 0, 1)
        self.gripSolenoidOne = DoubleSolenoid(0, 2, 3)
        self.gripSolenoidTwo = DoubleSolenoid(0, 4, 5)

    def controlSolenoid(self, solenoid, direction):
        solenoid.set(direction)
