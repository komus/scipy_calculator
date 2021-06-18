from .calculator import Calculator

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
cal.reset
print(cal.subtract(20.2, 10))
print(cal.operator)

print(cal.power(3, 3))
val = [2, 4, 5, 2, 1]

print(cal.multiply(val))
print(cal.multiply(3, 2))
print(cal.multiply(1000))
