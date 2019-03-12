import wpilib
from wpilib import Timer
import ctre

from wpilib.buttons.joystickbutton import JoystickButton


from wpilib.command.subsystem import Subsystem

from robotmap import *


class ArmSystem(Subsystem):
    def __init__(self):
        self.armMotor = ctre.wpi_talonsrx.WPI_TalonSRX(armMotor)
        self.armTimer = Timer()

        self.bottomStopSwitch = wpilib.DigitalInput(bottomStop)
        self.topStopSwitch = wpilib.DigitalInput(topStop)
        self.bendSwitchOne = wpilib.DigitalInput(2)
        self.bendSwitchTwo = wpilib.DigitalInput(3)

    def armMove(self, speed, startButton, stopButton):
        # print(self.stopSwitch.get())
        # print(self.topStopSwitch.get(), self.bottomStopSwitch.get())
        # print(self.bendSwitchOne.get(), self.bendSwitchTwo.get())
        if self.armTimer.get() == 0 and startButton:
            self.armTimer.start()
            self.armMotor.set(speed)

        if self.armTimer.hasPeriodPassed(5) or self.bottomStopSwitch.get() or self.topStopSwitch.get() or stopButton:
            self.armMotor.disable()
            self.armTimer.stop()
            self.armTimer.reset()
