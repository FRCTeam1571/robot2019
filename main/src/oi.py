import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton


from subsystems.DriveTrainSubsystem import DriveTrain
from subsystems.arm import ArmSystem

from robotmap import *

class OI():

    def __init__(self):
        # self.driveRobot = DriveTrain()
        self.arm = ArmSystem()

        self.joystick = Joystick(0)

        self.upButton = JoystickButton(self.joystick, 6)
        self.downButton = JoystickButton(self.joystick, 4)

        

    def poll(self):

        self.xAxis = self.joystick.getX()
        self.yAxis = self.joystick.getY()
        self.zAxis = self.joystick.getZ()

        # self.driveRobot.drive(self.xAxis, self.yAxis, self.zAxis)

        
        self.arm.armMove(1.0, self.upButton.get())
        self.arm.armMove(-1.0, self.downButton.get())
