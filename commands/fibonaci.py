from command import Command


class FibonacciCommand(Command):
  def __init__(self) -> None:
    super().__init__("Calculate nth fibonacci number")

  def run(self) -> None:
    n = int(input("Which fibonacci number would you like to calculate? "))
    
    print("The fibbonnacci number for n={} is {}".format(n, self.calculate(n)))

  def calculate(self, n):
    if(n < 0):
      raise Exception("Fibonacci numbers are only supported for n >= 0")

    if(n == 0): return 0
    if(n == 1): return 1

    last = 0
    current = 1
    for _ in range(2, n + 1):
      temp = current
      current = last + current
      last = temp

    return current