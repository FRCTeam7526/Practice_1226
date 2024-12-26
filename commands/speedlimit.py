import wpilib
import commands2
from subsystems.drivesubsystem import DriveSubsystem

class SpeedLimit(commands2.Command):
  def __init__(
      self,
      drive: DriveSubsystem,
      mode: bool
  ):
    self.drive = drive
    self.mode = mode

    self.addRequirements(self.drive)

  def initialize(self):
    if self.mode == True:
      self.drive.setMaxOutput(0.5)
    else:
      self.drive.setMaxOutput(1)

  def isFinished(self):
    return True