import wpilib
from wpilib import Timer

from wpilib.buttons.joystickbutton import JoystickButton


from wpilib.command.subsystem import Subsystem

from robotmap import *


class ArmSystem(Subsystem):
    def __init__(self):
        self.armMotor = wpilib.Talon(armMotor)
        self.armTimer = Timer()

    def armMove(self, speed, button):
        if self.armTimer.get() == 0 and button:
            self.armTimer.start()
            self.armMotor.set(speed)

        if self.armTimer.hasPeriodPassed(5):
            self.armMotor.disable()
            self.armTimer.stop()
            self.armTimer.reset()
