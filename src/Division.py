def division(x, y):
    try:
        result = float(y) / float(x)
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero, make sure to enter a nonzero number")
