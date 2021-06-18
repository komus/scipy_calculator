from typing import List
from multipledispatch import dispatch
import itertools


class Calculator:
    """
        Basic Calculator Operations.
    
        This class handles basic operations of a calculator.
    
        Mathematics Operations:
        - Power
        - Addition
        - Subtraction
        - Multiplication
        - Division
        - Modulo
        - Root
        - Average
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

    @property
    def operator(self):
        return self.__operator

    @property
    def reset(self):
        """
            Reset memory to 0
        """
        self.__index = 0
        self.__operator = []

    def average(self, item: list[float]) -> float:
        self.reset
        self.__index = sum(item)/len(item)
        self.__operator.append("average: " + ','.join(str(x) for x in item))
        return self.__index

    def sum(self, *args):
        if(len(args) > 1):
            if isinstance(args, tuple):
                for i in args:
                    self.__index += i
        else:
            if isinstance(*args, int):
                for ele in args:
                    self.__index += ele
            else:
                flat_list = list(itertools.chain(*args))
                for x in flat_list:
                    self.__index += x

        self.__operator.append("sum: " + ',' + str(args))
        return self.__index

    @dispatch(int)
    def subtract(self, a: int) -> int:
        self.__index -= a
        self.__operator.append("subtract: " + str(a))
        return round(self.__index, 0)

    @dispatch(float)
    def subtract(self, a: float) -> float:
        self.__index -= a
        self.__operator.append("subtract: " + str(a))
        return round(self.__index, 2)

    @dispatch(float, float)
    def subtract(self, a: float, b: float) -> float:
        if self.__index == 0:
            self.__index = a - b
        else:
            self.__index = self.__index - a - b
        self.__operator.append("subtract: " + str(a) + "," + str(b))
        return self.__index

    @dispatch(float, int)
    def subtract(self, a: float, b: int = None) -> float:
        if self.__index == 0:
            self.__index = a - b
        else:
            self.__index = self.__index - a - b
        self.__operator.append("subtract: " + str(a) + "," + str(b))
        return self.__index

    @dispatch(object, object)
    def subtract(self, a, b):
        if self.__index == 0:
            self.__index = a - b
        else:
            self.__index = self.__index - a - b
        self.__operator.append("subtract: " + str(a) + "," + str(b))
        return self.__index

    @dispatch(int, int)
    def power(self, base: int, super: int) -> int:
        pow = 1
        for x in range(super):
            pow *= base

        self.__index = pow
        return self.__index


    @dispatch(float, int)
    def power(self, base: float, super: int) -> float:
        pow = 1
        for x in range(super):
            pow *= base
        self.__index = pow
        return self.__index

    def multiply(self, *args):
        mult = 1
        if(len(args) > 1):
            if isinstance(args, tuple):
                for i in args:
                    mult *= i
        else:

            if isinstance(*args, int):
                for ele in args:
                    mult *= ele
            else:
                flat_list = list(itertools.chain(*args))
                for x in flat_list:
                    mult *= x

        self.__index = mult
        self.__operator.append("multiply: " + ',' + str(args))
        return self.__index

    @dispatch(int, int)
    def divide(self, numerator: int, denominator: int) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator/denominator
            return self.__index

    @dispatch(float, int)
    def divide(self, numerator: float, denominator: int) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator/denominator
            return self.__index

    @dispatch(int, float)
    def divide(self, numerator: int, denominator: float) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator/denominator
            return self.__index

    @dispatch(float, float)
    def divide(self, numerator: float, denominator: float):
        if denominator == 0:
            return 'err'

        else:
            self.__index = numerator/denominator
            return self.__index

    @dispatch(int)
    def divide(self, denominator: int) -> float:
        if denominator == 0:
            self.reset
            return 'err'
        else:
            self.__index /= denominator
            return self.__index

    @dispatch(float)
    def divide(self, denominator: float) -> float:
        if denominator == 0:
            self.reset
            return 'err'
        else:
            self.__index /= denominator
            return self.__index

    @dispatch(int, int)
    def modulo(self, numerator: int, denominator: int) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator % denominator
            return self.__index

    @dispatch(float, int)
    def modulo(self, numerator: float, denominator: int) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator % denominator
            return self.__index

    @dispatch(int, float)
    def modulo(self, numerator: int, denominator: float) -> float:
        if denominator == 0:
            self.reset
            return 'err'

        else:
            self.__index = numerator % denominator
            return self.__index

    @dispatch(float, float)
    def modulo(self, numerator: float, denominator: float):
        if denominator == 0:
            return 'err'

        else:
            self.__index = numerator % denominator
            return self.__index

    def root(self, base, root):
        if base > 0:
            rst = base**(1./root)
        else:
            rst = -(base**(1./root))
        self.__index = rst
        return self.__index
