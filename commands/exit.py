from command import Command


class ExitCommand(Command):
  def __init__(self) -> None:
    super().__init__("Exit")

  def run(self) -> None:
    exit(0)