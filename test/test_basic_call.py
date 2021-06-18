from calculator import Calculator


def test_add():
    assert Calculator().sum(10, 2) == 12
    assert Calculator().sum(2) == 2

    cal = Calculator()
    assert cal.sum(2) == 2
    assert cal.sum(2, 4) == 8
    assert cal.sum([10, 12.90, 14, 5, 7]) == 56.9

    cal.reset

    assert cal.sum(3, 2) == 5


def test_subtract():
    assert Calculator().subtract(2) == -2
    assert Calculator().subtract(10, 6) == 4

    cal = Calculator()
    assert cal.subtract(10, 4) == 6
    assert cal.subtract(2) == 4
    assert cal.subtract(3, 1) == 0

    cal.reset
    assert cal.subtract(2, 7) == -5


def test_power():
    assert Calculator().power(5, 3) == 125
    assert Calculator().power(3.5, 3) == 42.875

    cal = Calculator()
    assert cal.power(2, 5) == 32
    assert cal.sum(3) == 35

    cal.reset

    assert cal.power(2, 2) == 4
    assert cal.subtract(3) == 1


def test_multiply():
    val = [2, 4, 5, 2, 1]
    assert Calculator().multiply(val) == 80
    assert Calculator().multiply(10, 4) == 40

    cal = Calculator()
    assert cal.multiply(12, 2) == 24
    assert cal.subtract(4) == 20

    assert cal.multiply(1000) == 1000


def test_divide():
    assert Calculator().divide(10) == 0
    assert Calculator().divide(10, 2) == 5

    cal = Calculator()
    assert cal.divide(100, 5) == 20
    assert cal.sum(10) == 30
    assert cal.divide(2) == 15
    assert cal.divide(0) == 'err'
    assert cal.divide(10.78, 0) == 'err'
    assert cal.divide(0, 78) == 0


def test_modulo():
    assert Calculator().modulo(10, 2) == 0
    assert Calculator().modulo(15, 4) == 3

    cal = Calculator()
    assert cal.modulo(10, 0) == 'err'
    assert cal.modulo(14.67, 3) == 2.67



def test_root():
    assert Calculator().root(27, 3) == 3
    assert Calculator().root(32, 5) == 2

    cal = Calculator()
    cal.root(-8, 2) == -2
