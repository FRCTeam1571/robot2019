import wpilib

from wpilib.command import TimedCommand
from wpilib.command import Command

from subsystems.PneumaticsSubsystem import Pneumatics

class PneumaticsCommand(TimedCommand):
    def __init__(self):
        self.PneumaticsSubsystem = Pneumatics()
        # TimedCommand.requires(subsystems.PneumaticsSubsystem)

    def extendArm(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.armSolenoid, 1)

    def retractArm(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.armSolenoid, 2)

    def offArm(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.armSolenoid, 0)

    def openGrip(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidOne, 1)
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidTwo, 1)

    def closeGrip(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidOne, 2)
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidTwo, 2)

    def offGrip(self):
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidOne, 0)
        self.PneumaticsSubsystem.controlSolenoid(self.PneumaticsSubsystem.gripSolenoidTwo, 0)

class Toggle(TimedCommand):
    def __init__(self, extend, retract):
        self.toggle = False
        self.last = False

        self.extend = extend
        self.retract = retract

    def togglePneumatics(self, button):
        if button and not self.last:
            self.toggle = not self.toggle
        
        self.last = button

        if self.toggle and self.last:
            self.extend()
        elif self.last:
            self.retract()