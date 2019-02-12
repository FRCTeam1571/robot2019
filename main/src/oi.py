import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton


from subsystems.DriveTrainSubsystem import DriveTrain

class OI():

    def __init__(self):
        self.driverobot = DriveTrain()

        self.joystick = Joystick(0)

    def poll(self):

        self.xAxis = self.joystick.getX()
        self.yAxis = self.joystick.getY()
        self.zAxis = self.joystick.getZ()

        self.driverobot.drive(self.xAxis, self.yAxis, self.zAxis)
