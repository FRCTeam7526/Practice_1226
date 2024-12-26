import wpilib
import commands2
import commands2.button
from commands.arcadedrive import ArcadeDrive
from commands.speedlimit import SpeedLimit
from subsystems.drivesubsystem import DriveSubsystem

class RobotContainer:
  def __init__(self):
    self.stick = commands2.button.CommandXboxController(0)

    self.drive = DriveSubsystem()

    self.configureButtonBindings()

    self.drive.setDefaultCommand(
      ArcadeDrive(
        self.drive,
        lambda: self.stick.getRightY(),
        lambda: self.stick.getLeftX()
      )
    )

  def configureButtonBindings(self):
    self.stick.b().onTrue(
      SpeedLimit(
        self.drive,
        True
      )
    )

    self.stick.a().onTrue(
      SpeedLimit(
        self.drive,
        False
      )
    )