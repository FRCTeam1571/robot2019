import wpilib
from wpilib import drive
import ctre

from wpilib.command.subsystem import Subsystem

from robotmap import *

class DriveTrain(Subsystem):
    def __init__(self):
        self.frontLeftMotor = ctre.wpi_talonsrx.WPI_TalonSRX(frontLeftTalonSRX)
        self.rearLeftMotor = ctre.wpi_talonsrx.WPI_TalonSRX(rearLeftTalonSRX)

        self.frontRightMotor = ctre.wpi_talonsrx.WPI_TalonSRX(frontRightTalonSRX)
        self.rearRightMotor = ctre.wpi_talonsrx.WPI_TalonSRX(rearRightTalonSRX)
        

        self.mecanumDrive = wpilib.drive.MecanumDrive(
            self.frontLeftMotor, self.rearLeftMotor, self.frontRightMotor, self.rearRightMotor)

    def drive(self, ySpeed, xSpeed, zRotation, gyroAngle=0.0):
        self.mecanumDrive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)