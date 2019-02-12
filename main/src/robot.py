#!/usr/bin/env python3

import wpilib
from wpilib import command
from wpilib.command import Command
from commandbased import CommandBasedRobot

import oi

class Thomas(CommandBasedRobot):

    def robotInit(self):

        Command.getRobot = lambda x=0: self

        self.oi = oi.OI()

    def autonomousInit(self):
        pass

    def teleopPeriodic(self):
        # self.disabled = False
        command.Scheduler.run(self)
        self.oi.poll()

    def disabledPeriodic(self):
        self.disabled = True

if __name__ == "__main__":
    wpilib.run(Thomas)
