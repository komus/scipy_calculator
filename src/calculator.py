from typing import List
from multipledispatch import dispatch
import math


class Calculator:
    
    def __init__(self) -> None:
        self.__index = 0
        self.__operands = []
        self.__operator = []

    @property
    def memory_val(self):
        '''
            returns the current memory value
        '''
        return self.__index

    @property
    def reset(self):
        """
            Reset memory to 0
        """
        self.__index = 0
        self.__operands = []
        self.__operator = []

    def average(self, item: list[float]) -> float:
        self.__index = sum(item)/len(item)
        return self.__index

    @dispatch(list)
    def sum(self, item: list[float]) -> float:
        self.__index += sum(item)
        return self.__index

    @dispatch(int, int)
    def sum(self, a: int, b: int = 0) -> int:
        self.__index = self.__index + a + b
        return self.__index

    @dispatch(int)
    def sum(self, a: int) -> int:
        self.__index += a
        return self.__index

    @dispatch(object, object)
    def sum(self, a: float = 0, b: float = 0) -> object:
        self.__index += a + b
        return self.__index

    def subtract(self, a: float, b: float = None):
        pass





grade = [10, 12.90, 14, 5, 7]
cal = Calculator()
val = cal.sum(12)
print(f"sum is {val}")


cal.reset

print(cal.sum(grade))
print(cal.sum(1))
print(cal.average(grade))
print(cal.sum(4))
print(cal.memory_val)
