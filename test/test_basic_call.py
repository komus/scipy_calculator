import sys
import pytest
sys.path.append("../src")
from calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(10) == 10


def test_subtract():
    assert cal.subtract(5) == 5

def test_divide():
    assert cal.divide(2) == 2.5

def test_memory_val():
    assert cal.memory_val == 2.5

def test_multiply():
    assert cal.multiply(0) == 0

def test_zero_division():
    assert cal.subtract(20) == -20
    assert cal.add(-10) == -30
    assert cal.divide(0) == None
    assert cal.memory_val == -30

def test_modulo():
    assert cal.modulo(3) == 0
    assert cal.memory_val == 0

def test_sqrt():
    assert cal.sqrt(16) == 4
    assert cal.memory_val == 4

def test_reset():
    cal.reset()
    assert cal.memory_val == 0