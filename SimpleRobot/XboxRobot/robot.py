
#!/usr/bin/env python3
#Modified: 

# For Solenoids:
# False = Up
# True = Down

import wpilib
from wpilib import drive, Timer, SendableChooser
import ctre
from networktables import NetworkTables
import datetime
#import funct

#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
    
Methods inherited from class edu.wpi.first.wpilibj.GenericHID
    getAxisCount, getAxisType, getButtonCount, getName, getPort, getPOV, getPOV, getPOVCount, getRawAxis, getRawButton, getRawButtonPressed, getRawButtonReleased, 
    getType, getX, getY, setOutput, setOutputs, setRumble

class wpilib.XboxController(port)  : 
    boolean	getAButton()    Read the value of the A button on the controller.
    boolean	getAButtonPressed()     Whether the A button was pressed since the last check.
    boolean	getAButtonReleased()     Whether the A button was released since the last check.
    boolean	getBackButton()     Read the value of the back button on the controller.
    boolean	getBackButtonPressed()     Whether the back button was pressed since the last check.
    boolean	getBackButtonReleased()     Whether the back button was released since the last check.
    boolean	getBButton()     Read the value of the B button on the controller.
    boolean	getBButtonPressed()      Whether the B button was pressed since the last check.
    boolean	getBButtonReleased()     Whether the B button was released since the last check.
    boolean	getBumper(GenericHID.Hand hand)     Read the value of the bumper button on the controller.
    boolean	getBumperPressed(GenericHID.Hand hand)      Whether the bumper was pressed since the last check.
    boolean	getBumperReleased(GenericHID.Hand hand)     Whether the bumper was released since the last check.
    boolean	getStartButton()     Read the value of the start button on the controller.
    boolean	getStartButtonPressed()     Whether the start button was pressed since the last check.
    boolean	getStartButtonReleased()     Whether the start button was released since the last check.
    boolean	getStickButton(GenericHID.Hand hand)     Read the value of the stick button on the controller.
    boolean	getStickButtonPressed(GenericHID.Hand hand)     Whether the stick button was pressed since the last check.
    boolean	getStickButtonReleased(GenericHID.Hand hand)     Whether the stick button was released since the last check.
    double	getTriggerAxis(GenericHID.Hand hand)     Get the trigger axis value of the controller.
    double	getX(GenericHID.Hand hand)     Get the X axis value of the controller.
    boolean	getXButton()     Read the value of the X button on the controller.
    boolean	getXButtonPressed()     Whether the X button was pressed since the last check.
    boolean	getXButtonReleased()     Whether the X button was released since the last check.
    double	getY(GenericHID.Hand hand)     Get the Y axis value of the controller.
    boolean	getYButton()     Read the value of the Y button on the controller.
    boolean	getYButtonPressed()     Whether the Y button was pressed since the last check.
    boolean	getYButtonReleased()     Whether the Y button was released since the last check.
"""


class XboxRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #self.left_motor = wpilib.Spark(0)
        #self.right_motor = wpilib.Spark(1)
        #self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer() 

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            print("Hello World")
        #    self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        #else:
        #    self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        if self.controller.getTriggerPressed():
            print("Hello World")
        
        self.Robotmg()
        self.POVrobot()

    def disabledInit(self):
        currentDT = datetime.datetime.now() 
        #if currentDT.second % 10.0 == 1:
        print("Disabled Setup")

    def disabledPeriodic(self):
        currentDT = datetime.datetime.now() 
        if currentDT.second % 15.0 == 1:
            print("this wont run")

    def Robotmg(self):
        if self.controller.getRawButton(4):
            print("your slowly learning")
        
    def POVrobot(self):
        POVdegree = self.controller.getPOV(0)

        int = 8
        POVdegreeCases = {
            0: "this is up or default 360",
            45: "this is up, right",
            90: "This is right",
            135: "This is down right",
            180: "this is down",
            225: "this is down left",
            270: "this is left",
            315: "this is up left"
        }

        POVdegreeString = POVdegreeCases.get(POVdegree, "Invalid value")
        if POVdegree >= 0:    
            print(POVdegreeString)



if __name__ == "__main__":
    wpilib.run(XboxRobot)

	
	
	
	
	
# class Scooter(wpilib.IterativeRobot):

    # def robotInit(self):
        # '''Robot Initiation'''
        # self.controller = wpilib.XboxController(0)

        # wpilib.CameraServer.launch("vision.py:main")

        # self.colorSensor = funct.ColorSensor(10, 11, 12, 13, 14, 15) # Color sensor for sorting
        # self.colorSensor.setFrequency(20)
        # self.correctColor = 'r' # Color for the color sensor to look for
        # self.sortMotor = wpilib.NidecBrushless(3, 3) # Nidec motor for sorting
        # self.sortSwitch = wpilib.DigitalInput(0) # Switch to stop sorting motor

        # self.camServo = wpilib.Servo(2) # Camera servo motor
        # self.intake = wpilib.Talon(1) # Intake motor

        # self.door = wpilib.Talon(0) # Door motor
        # self.topSwitch = wpilib.DigitalInput(2) # Top switch for door motor
        # self.bottomSwitch = wpilib.DigitalInput(1) # Bottom switch for door motor



        # # self.rf = rangefinder.MaxUltrasonic(0)

        # # Talon SRX #
        # # Right drivetrain
        # self.fr_motor = ctre.wpi_talonsrx.WPI_TalonSRX(2)  # 2
        # self.rr_motor = ctre.wpi_talonsrx.WPI_TalonSRX(3)  # 3
        # self.right = wpilib.SpeedControllerGroup(self.fr_motor, self.rr_motor)

        # Left drivetrain
        # self.fl_motor = ctre.wpi_talonsrx.WPI_TalonSRX(0)  # 0
        # self.rl_motor = ctre.wpi_talonsrx.WPI_TalonSRX(1)  # 1
        # self.left = wpilib.SpeedControllerGroup(self.fl_motor, self.rl_motor)

        # self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    # def disabledInit(self):
        # # self.haveColor = False
        # # self.timer.reset()
        # # self.timer.start()
        # pass


    # def disabledPeriodic(self):
        # pass

        



    # def autonomousInit(self):
        # """This function is run once each time the robot enters autonomous mode."""
        # self.haveColor = False
        # # self.timer.reset()
        # # self.timer.start()
        # # self.select = self.chooser.getSelected()


    # def autonomousPeriodic(self):
        # """This function is called periodically during autonomous."""


    # def teleopInit(self):
        # """This function is run once each time the robot enters teleop mode"""
        # self.kLeft = self.controller.Hand.kLeft
        # self.kRight = self.controller.Hand.kRight
        # self.haveColor = False
        # # self.timer.reset()
        # # self.timer.start()
        # self.doorSpeed = -0.5
        # self.shutter = False
        # self.top = False
        # self.bottom = False
        # self.recent = False




    # def teleopPeriodic(self):

        # """This function is called periodically during operator control."""
        # # Sets triggers and bumpers each loop
        # self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
        # self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
        # self.BumperLeft = self.controller.getBumper(self.kLeft)
        # self.BumperRight = self.controller.getBumper(self.kRight)

        # servoMap = funct.numMap(self.controller.getX(self.kRight), -1.0, 1.0, 0.0, 1.0)
        # self.camServo.set(servoMap)

        # # Intake Motor Control#
        # if self.BumperRight:
            # self.intake.set(0.7)
        # else:
            # self.intake.set(0.0)

        # # Color Sensor #
        # funct.colorSorter(self)

        
        # # Door Control #
        # if self.controller.getYButtonPressed():
            # if self.topSwitch.get():
                # self.doorSpeed = 0.6
                # self.top = True
            # elif self.bottomSwitch.get():
                # self.doorSpeed = -0.6
                # self.bottom = True
            
            # self.door.set(self.doorSpeed)
            
            # self.shutter = False

        # if self.bottom and not self.top and self.topSwitch.get():
            # self.door.disable()
            # print("On Top")
            # self.bottom = False
        # if self.top and not self.bottom and self.bottomSwitch.get():
            # self.door.disable()
            # print("On Bottom")
            # self.top = False


        # # Nidec Control: Experimental #
        # # if self.controller.getAButton():
            # # self.sortMotor.set(0.05)
        # # else:
            # # self.disableSwitch = False

        # # if self.sortSwitch.get() and self.disableSwitch:
            # # self.sortMotor.disable()
            # # self.disableSwitch = False
        # # else:
            # # self.sortMotor.enable()
        
        # # self.disableSwitch = True

        # # if self.sortSwitch.get() and not self.recent:
            # # self.recent = True
        # # elif self.sortSwitch.get() and self.recent:
            # # self.recent = False
        
        # # if self.controller.getAButton() and (not self.sortSwitch.get() or not self.recent):
            # # self.sortMotor.set(0.05)
        # # else:
            # # self.sortMotor.set(0.0)

        # # if not self.controller.getAButton() and self.sortSwitch.get():
            # # print("Yes")
            # # self.sortMotor.set(0.0)
        # # elif self.controller.getAButton():
            # # print("No")
            # # self.sortMotor.set(0.1)
        

        




        # # Drive System #
        # # Making drive slower so the robot does not suffer from brownouts
        # self.rotation = self.controller.getX(self.kLeft) * 0.9
        # self.speed = self.TriggerLeft * 0.9
        # # Backwards Control
        # if self.BumperLeft:
            # self.speed = self.speed * -1
        # # Drive #
        # self.drive.arcadeDrive(self.speed, self.rotation)


# # Runs function upon ready
# if __name__ == "__main__":
    # wpilib.run(Scooter,
            # physics_enabled=True)
