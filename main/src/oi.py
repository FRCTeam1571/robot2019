import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from subsystems.DriveTrainSubsystem import DriveTrain
from subsystems.ArmSubsystem import ArmSystem
from commands.PneumaticsCommand import PneumaticsCommand, Toggle
# from commands.ServoCommand import ServoCommand

from robotmap import *

class OI():

    def __init__(self):
        self.driveRobot = DriveTrain()
        self.arm = ArmSystem()
        self.pneumatics = PneumaticsCommand()
        # self.servo = ServoCommand()

        self.armToggle = Toggle(self.pneumatics.extendArm, self.pneumatics.retractArm)
        self.gripToggle = Toggle(self.pneumatics.openGrip, self.pneumatics.closeGrip)

        self.joystick = Joystick(0)

        self.armUpButton = JoystickButton(self.joystick, 6)
        self.armDownButton = JoystickButton(self.joystick, 4)
        self.stopButton = JoystickButton(self.joystick, 10)

        ''' Extension and retraction variables - syntax: ''' # JoystickButton(self.joystick, [appointed button number])
        # self.armExtendButton = JoystickButton(self.joystick, 5)
        # self.armRetractButton = JoystickButton(self.joystick, 3)
        # self.armToggle = False
        # self.armLast = False
        # self.grabToggle = False
        # self.grabLast = False


        self.armButton = JoystickButton(self.joystick, 2)
        self.gripButton = JoystickButton(self.joystick, 1)
        
    
    def poll(self):

        ''' Axis control - syntax: ''' # self.joystick.get[axis]()
        self.xAxis = self.joystick.getX()
        self.yAxis = self.joystick.getY()
        self.zAxis = self.joystick.getZ()


        self.driveRobot.drive(self.xAxis, self.yAxis, self.zAxis)

        # print(self.armUpButton.get())
        self.arm.armMove(0.5, self.armUpButton.get(), self.armDownButton.get())



        


        self.armToggle.togglePneumatics(self.armButton.get())
        self.gripToggle.togglePneumatics(self.gripButton.get())

        # self.servo.servoSet(self.joystick.getTwist())

    