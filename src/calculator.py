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

    def reset(self):
        """
            Reset memory to 0
        """
        self.__index = 0
        self.__operator = []

    def add(self, num: Union[int, float]):
        self.__index += num
        return self.__index

    def subtract(self, num: Union[int, float]):
        self.__index -= num
        return self.__index

    def multiply(self, num: Union[int, float]):
        self.__index *= num
        return self.__index

    def divide(self, num: Union[int, float]):
        try:
            self.__index /= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def modulo(self, num: Union[int, float]):
        try:
            self.__index %= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def sqrt(self, num: Union[int, float]):
        try:
            self.__index = num**(1./2)
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

