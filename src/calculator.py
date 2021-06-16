from typing import List
import math

class Calculator:
    operands = []
    operator = []
    

    def average(item:list[float]) -> float:
        return sum(item)/len(item)



grade = [10, 12.90, 14, '',7]
cal = Calculator.average(grade)