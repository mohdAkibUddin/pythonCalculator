import unittest

from csvReader.CSVReader import readCSV
from src.Calculator import Calculator


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == "__main__":
    unittest.main()
