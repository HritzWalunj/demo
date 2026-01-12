"""import packages"""
import pytest
from calculator.calculator import add, subtract, multiply, divide


def test_add():
    """test add function"""
    assert add(2,3) == 5

def test_subtract():
    """test substact function"""
    assert subtract(3,2) == 1

def test_multiply():
    """test multiply function"""
    assert multiply(3,2) == 6

def test_divide():
    """test  divide function"""
    assert divide(6,2) == 3

def test_divide_by_zero():
    """test divede_by_zero function"""
    with pytest.raises(ValueError):
        divide(10,0)
