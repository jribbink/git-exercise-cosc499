from abc import ABC, abstractmethod


class Command(ABC):
  def __init__(self, name) -> None:
    self.name = name
    super().__init__()

  @abstractmethod
  def run(self) -> None:
    pass