
#!/usr/bin/env python3
#Modified: 3/30

# For Solenoids:
# False = Up
# True = Down

import wpilib
# from wpilib import drive
# import ctre


class Scooter(wpilib.IterativeRobot):

    def robotInit(self):
        self.rightPhotoSwitch = wpilib.DigitalInput(1)
        self.leftPhotoSwitch = wpilib.DigitalInput(0)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        print(self.rightPhotoSwitch.get(), self.leftPhotoSwitch.get())

    def teleopInit(self):
        pass
        

    def teleopPeriodic(self):
        pass


#Runs function upon ready
if __name__ == "__main__":
    wpilib.run(Scooter,
               physics_enabled=True)
