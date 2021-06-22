from typing import Union


class Calculator:
    """
        Basic Calculator Operations.
    
        This class handles basic operations of a calculator.
    
        Mathematics Operations:
        - Addition
        - Subtraction
        - Multiplication
        - Division
        - Modulo
        - Sqrt
    """
    def __init__(self) -> None:
        self.__index = 0
        self.__operator = []

    @property
    def memory_val(self):
        '''
            returns the current memory value
        '''
        return self.__index

    @staticmethod
    def __validate_input(number: Union[int, float]):
        if not isinstance (number, int) and not isinstance(number, float):
            raise TypeError("accepted types is int or float")

    def reset(self):
        """
            Reset memory to 0
        """
        self.__index = 0
        self.__operator = []

    def add(self, num: Union[int, float]):
        self.__validate_input(num)
        self.__index += num
        return self.__index

    def subtract(self, num: Union[int, float]):
        self.__validate_input(num)
        self.__index -= num
        return self.__index

    def multiply(self, num: Union[int, float]):
        self.__validate_input(num)
        self.__index *= num
        return self.__index

    def divide(self, num: Union[int, float]):
        self.__validate_input(num)
        try:
            self.__index /= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def modulo(self, num: Union[int, float]):
        self.__validate_input(num)
        try:
            self.__index %= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def root(self, num: Union[int, float]):
        self.__validate_input(num)
        if self.__index <= 0:
            raise ValueError(f"memory value must be greater than zero")
        if num <= 0:
            raise ValueError("root must be greater than 0")

        self.__index = self.__index**(1./num)
        return self.__index