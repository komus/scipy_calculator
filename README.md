# Scientific Python Calculator

Scientific Python Calculator (scipy_calculator) is a library for doing mathematics computation. It works similar to a calculator.

:raised_hands: This is my first python package. It will be improved over time. Feel free to contribute to this beautiful work of art.

## Installation
:warning: scipy_calculator is only tested with python 3. 

**Installation via PYPI**
```sh
$ pip install scipy-calculator
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

my_cal = Calculator()
```
### Addition
```python
>>> my_cal.add(10)
10
```
#### Subtraction
`subtract`
```python
>>> my_cal.subtract(5)
5
```
because the memory was not reset, `5` was subtracted from previous value `10`


#### Division
For `divide`, zero division returns `None` and description
```python
>>> cal.divide(2)
2.5
```
```python
>>> cal.divide(0)
number cannot be zero => float division by zero
None

>>> cal.memory_val
2.5
```


#### Multiply
```python
>>> cal.multiply(2.5)
6.25
```
#### Modulo
```python
>>> cal.modulo(5)
1.25
```
#### Square root
```python
>>> cal.sqrt(16)
4
```

#### Reset
```python
>>> cal.reset()
>>> cal.memory_val
0
```