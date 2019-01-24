
#!/usr/bin/env python3
#Modified: 

# For Solenoids:
# False = Up
# True = Down

import wpilib
from wpilib import drive, Timer, SendableChooser
import ctre
from networktables import NetworkTables
#import funct

#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #self.left_motor = wpilib.Spark(0)
        #self.right_motor = wpilib.Spark(1)
        #self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.stick = wpilib.Joystick(1)
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
        if self.stick.getTriggerPressed():
            print("Hello World")
        
        self.Robotmg()
        self.POVrobot()

    def disabledPeriodic(self):
        print("this wont run")

    def Robotmg(self):
        if self.stick.getRawButton(4):
            print("your slowly learning")
        
    def POVrobot(self):
        POVdegree = self.stick.getPOV(0)

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
    wpilib.run(MyRobot)
