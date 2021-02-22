import unittest

from csvReader.CSVReader import readCSV
from src.Calculator import Calculator


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def testInstantiateCalculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def testAddition(self):
        rows = readCSV("tests/csvFiles/Addition.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.add(x, y), expectedResult)

    def testSubtraction(self):
        rows = readCSV("tests/csvFiles/Subtraction.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertEqual(self.calculator.subtract(x, y), expectedResult)

    def testDivision(self):
        rows = readCSV("tests/csvFiles/Division.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.divide(x, y), expectedResult)

    def testMultiplication(self):
        rows = readCSV("tests/csvFiles/Multiplication.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            y = float(row["Value 2"])
            self.assertAlmostEqual(self.calculator.multiply(x, y), expectedResult)

    def testSquare(self):
        rows = readCSV("tests/csvFiles/Square.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.square(x), expectedResult)

    def testSquareRoot(self):
        rows = readCSV("tests/csvFiles/SquareRoot.csv")
        for row in rows:
            expectedResult = float(row["Result"])
            x = float(row["Value 1"])
            self.assertAlmostEqual(self.calculator.squareRoot(x), expectedResult)

    def testResultProperty(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == "__main__":
    unittest.main()
