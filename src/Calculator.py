from src.Operations import Operations


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = Operations.addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = Operations.subtraction(x, y)
        return self.result

    def divide(self, x, y):
        self.result = Operations.division(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = Operations.multiplication(x, y)
        return self.result

    def square(self, x):
        self.result = Operations.square(x)
        return self.result

    def squareRoot(self, x):
        self.result = Operations.squareRoot(x)
        return self.result
