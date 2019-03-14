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

    def armMove(self, speed, upButton, downButton):
        if upButton and not self.topStopSwitch.get():
            self.armMotor.set(speed)
        elif downButton and not self.bottomStopSwitch.get():
            self.armMotor.set(-speed)
        else:
            self.armMotor.disable()
        
        
        
