import wpilib
import commands2
from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):
  def robotInit(self):
    self.container = RobotContainer()
  