
from functools import reduce
from unittest import TestCase
import unittest
from commands.fibonaci import FibonacciCommand

'''
Fibonacci unit tests
'''
class FibonacciTesting(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_fibonacci_base_case_zero(self):
        fib = FibonacciCommand()
        self.assertEqual(fib.calculate(0), 0)

    def test_fibonacci_base_case_one(self):
        fib = FibonacciCommand()
        self.assertEqual(fib.calculate(1), 1)

    def test_fibonacci_valid_below_100(self):
        fib = FibonacciCommand()
        nums = [fib.calculate(n) for n in range(0, 100)]
        for i, n in enumerate(nums[2:]):
            j = i + 2
            self.assertEqual(n, nums[j-1] + nums[j-2])

    def test_fibonacci_throws_below_zero(self):
        fib = FibonacciCommand()
        with self.assertRaises(Exception):
            fib.calculate(-1)
