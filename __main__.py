
import os
from commands.exit import ExitCommand

# Cross platform clear console
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

commands = [
  ExitCommand()
]

while True:
  clear()
  print("Basic Calculator by Jordan Ribbink")
  print()
  print("\n".join(["{}. {}".format(i, s.name) for i,s in enumerate(commands)]))
  print()

  commands[int(input("Please enter a command: "))].run()