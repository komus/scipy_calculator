# Scientific Python Calculator

Scientific Python Calculator (scipy_calculator) is a library for doing mathematics computation. It works similar to a calculator.

:raised_hands: This is my first python package. It will be improved over time. Feel free to contribute to this beautiful work of art.

## Installation
:warning: scipy_calculator is only tested with python 3. 

**Installation via PYPI**
```sh
$ pip install scipy_calculator
```
**Installation via Github**
this is for the stable released version
```sh
$ pip install git+https://github.com/komus/scipy_calculator
```

scipy_calculator uses multipledispatch dependency and pytest for automated test

## Usage
The calculator can be used for basic mathematical computation. The calculator has a memory that caches the last result until it is reset. The cached result is used in the next computation if not reset. 

The `reset` is used to clear the cache

Examples will be shown below

## Sample Code
```python
	from calculator import Calculator
```
### Addition
```python

```

#### Subtraction
#### Multiply
#### Division
#### Average
`average` method accepts LIST of `int` and `float` to return the computed average
```python
>>> grade = [62, 78.9, 35.78, 90.23, 89.12, 45.78]
>>> avg_grade = my_cal.average(grade)
>>> avg_grade
66.96833333333335
```
Adding or subtracting without reseting, will add/subtract the value from the last result
```python
>>> my_cal.sum(10)
76.96833333333335
```



#### Modulo
#### Root
#### Power