import sys
import pytest
sys.path.append("../src")
from calculator import Calculator

cal = Calculator()


def test_add():
    assert cal.add(10) == 10
    assert Calculator().add(12.0) == 12.0


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


def test_root():
    m_cal = Calculator()
    assert m_cal.add(16) == 16
    assert m_cal.root(2) == 4
    with pytest.raises(Exception):
        Calculator().root(2)


def test_reset():
    cal.reset()
    assert cal.memory_val == 0


def test_add_not_int_or_float():
    assert Calculator().add(True) == 1
    with pytest.raises(Exception):
        Calculator().add('True')


def test_subtract_not_int_or_float():
    assert Calculator().subtract(True) == -1
    with pytest.raises(Exception):
        Calculator().subtract('True')


def test_multiply_not_int_or_float():
    assert Calculator().multiply(True) == 0
    with pytest.raises(Exception):
        Calculator().multiply('True')


def test_divide_not_int_or_float():
    assert Calculator().divide(True) == 0
    with pytest.raises(Exception):
        Calculator().divide('True')


def test_modulo_not_int_or_float():
    assert Calculator().modulo(True) == 0
    with pytest.raises(Exception):
        Calculator().modulo('True')


def test_root_not_int_or_float():
    with pytest.raises(Exception):
        Calculator().root('True')


def test_zero__modulo_division():
    assert Calculator().modulo(0) == None


def test_root_memory_less_than_zero():
    with pytest.raises(Exception):
        Calculator().root(2)


def test_root_value_less_than_zero():
    with pytest.raises(Exception):
        my_cal = Calculator()
        my_cal.add(16)
        my_cal.root(-1)
