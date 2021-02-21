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

    def testDivision(self):
        rows = readCSV("csvFiles/Division.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.divide(x, y), expectedResult)

    def testMultiplication(self):
        rows = readCSV("csvFiles/Multiplication.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.multiply(x, y), expectedResult)

    def testSquare(self):
        rows = readCSV("csvFiles/Square.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.square(x), expectedResult)


if __name__ == "__main__":
    unittest.main()
