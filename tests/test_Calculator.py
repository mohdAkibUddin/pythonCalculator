import unittest

from csvReader.CSVReader import readCSV
from src.Calculator import Calculator


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def testAddition(self):
        rows = readCSV("csvFiles/Addition.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.add(x, y), expectedResult)

    def testSubtraction(self):
        rows = readCSV("csvFiles/Subtraction.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.subtract(x, y), expectedResult)


if __name__ == "__main__":
    unittest.main()
