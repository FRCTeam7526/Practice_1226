import wpilib
import wpilib.drive
import commands2
from phoenix5 import WPI_TalonFX

class DriveSubsystem(commands2.Subsystem):
  def __init__(self):
    self.left1 = WPI_TalonFX(1)
    self.left2 = WPI_TalonFX(2)
    self.right1 = WPI_TalonFX(3)
    self.right2 = WPI_TalonFX(4)

    self.left1.setInverted(True)
    self.left2.setInverted(True)
    self.left2.follow(self.left1)
    self.right2.follow(self.right1)

    self.drive = wpilib.drive.DifferentialDrive(self.left1, self.right1)
    self.drive.setDeadband(0.05)

  def arcadeDrive(self, speed: float, rotation: float):
    self.drive.arcadeDrive(speed, rotation)

  def resetEncoders(self):
    self.left1.setSelectedSensorPosition(0)
    self.left2.setSelectedSensorPosition(0)
    self.right1.setSelectedSensorPosition(0)
    self.right2.setSelectedSensorPosition(0)

  def setMaxOutput(self, value: float):
    self.drive.setMaxOutput(value)

  def getLeftVelocity(self):
    return self.left1.getSelectedSensorVelocity()