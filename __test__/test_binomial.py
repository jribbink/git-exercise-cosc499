
from functools import reduce
from unittest import TestCase
import unittest
from commands.binomial import BinomialCommand

class BinomialTesting(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_binomial_zero_terms(self):
        bin = BinomialCommand()
        terms = bin.calculate(0)
        expected = [[1, 0, 0]]
        self.assertEqual(terms, expected)

    def test_binomial_one_term(self):
        bin = BinomialCommand()
        terms = bin.calculate(1)
        expected = [[1, 0, 1], [1, 1, 0]]
        self.assertEqual(terms, expected)

    def test_binomial_two_terms(self):
        bin = BinomialCommand()
        terms = bin.calculate(2)
        expected = [[1, 0, 2], [2, 1, 1], [1, 2, 0]]
        self.assertEqual(terms, expected)

    def test_fibonacci_six_terms(self):
        bin = BinomialCommand()
        terms = bin.calculate(6)
        expected = [[1, 0, 6], [6, 1, 5], [15, 2, 4], [20, 3, 3], [15, 4, 2], [6, 5, 1], [1, 6, 0]]
        self.assertEqual(terms, expected)

    def test_binomial_throws_below_zero(self):
        bin = BinomialCommand()
        with self.assertRaises(Exception):
            bin.calculate(-1)
