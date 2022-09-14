from math import factorial
from command import Command


class BinomialCommand(Command):
  def __init__(self) -> None:
    super().__init__("Binomial expansion")

  def run(self) -> None:
    n = int(input("How many terms (x + y) would you like in your expansion? "))
    print()

    terms = self.calculate(n)
    result = "   ".join(["{} x{}y{}".format(c, i, j) for c, i, j in terms])
    print("Result: {}".format(result), end='')

    print()

  def calculate(self, n):
    if(n < 0): raise Exception("Not supported negative value of n")
    terms = []
    for i in range(0, n + 1): 
      c = int(factorial(n) / (factorial(n-i) * factorial(i)))
      terms.append([c, i, n - i])
    return terms