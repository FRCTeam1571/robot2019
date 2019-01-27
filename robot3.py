import wpilib
from wpilib import drive
import ctre



class Scooter(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot Initiation'''
        self.controller = wpilib.XboxController(0)

        self.frontRight = ctre.WPI_TalonSRX(0)
        self.rearRight = ctre.WPI_TalonSRX(1)
        self.frontLeft = ctre.WPI_TalonSRX(2)
        self.rearLeft = ctre.WPI_TalonSRX(3)

        self.swerve = wpilib.drive.MecanumDrive(self.frontLeft, self.rearLeft, self.frontRight, self.rearRight)

        

        self.kLeft = self.controller.Hand.kLeft
        self.kRight = self.controller.Hand.kRight

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        self.TriggerLeft = self.controller.getTriggerAxis(self.kLeft)
        self.TriggerRight = self.controller.getTriggerAxis(self.kRight)
        self.BumperLeft = self.controller.getBumper(self.kLeft)
        self.BumperRight = self.controller.getBumper(self.kRight)

        self.swerve.driveCartesian(
            self.controller.getY(self.kLeft), self.controller.getX(self.kLeft), self.controller.getX(self.kRight))


#Runs function upon ready
if __name__ == "__main__":
    wpilib.run(Scooter)
