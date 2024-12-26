import wpilib
import commands2
import typing
from subsystems.drivesubsystem import DriveSubsystem

class ArcadeDrive(commands2.Command):
  def __init__(
      self,
      drive: DriveSubsystem,
      speed: typing.Callable[[], float],
      rotation: typing.Callable[[], float]
  ):
    self.drive = drive
    self.speed = speed
    self.rotation = rotation

    self.addRequirements(self.drive)

  def execute(self):
    self.drive.arcadeDrive(self.speed(), self.rotation())
