# A simple calculator
class Calculator:
    # empty constructor
    def __init__(self):
        pass

    # add method - given two numbers, return the addition
    def add(self, x1, x2):
        return x1 + x2

    # multiply method - given two numbers, return the
    # multiplication of the two
    def multiply(self, x1, x2):
        if x1 <= 0 & x2 <= 0:
            print("Input obtained does not consist of positive number")
            return 0
        else:
            return x1 * x2

    # subtract method - given two numbers, return the value
    # of first value minus the second
    def subtract(self, x1, x2):
        return x1 - x2
