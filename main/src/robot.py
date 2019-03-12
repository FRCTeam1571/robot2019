#!/usr/bin/env python3

import wpilib
from wpilib.command import Command
from wpilib.command import Scheduler
from commandbased import CommandBasedRobot

import oi

class NEWO(CommandBasedRobot):

    def robotInit(self):

        Command.getRobot = lambda x=0: self

        wpilib.CameraServer.launch("vision.py:main")

        self.oi = oi.OI()

    def autonomousPeriodic(self):
        Scheduler.getInstance().run()
        self.oi.poll()
        pass

    def teleopPeriodic(self):
        # self.disabled = False
        Scheduler.getInstance().run()
        self.oi.poll()

    def disabledPeriodic(self):
        pass
        # self.disabled = True


if __name__ == "__main__":
    wpilib.run(NEWO)
