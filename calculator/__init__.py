""" This is the Calculator Class"""
from calculator.operations import Operations


class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1, value_2):
        """ This is the add method"""
        self.result = Operations.add(value_2, value_1)
        return self.result

    def subtract(self, value_1, value_2):
        """ This is the subtract method"""
        self.result = Operations.subtract(value_2, value_1)
        return self.result

    def multiply(value_2, value_1):
        self.result = Operations.multiply(value_2, value_1)
    def get_result(self):
        """ This is the get result method"""
        return self.result
