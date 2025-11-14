import pytest
from calculator import sum, substract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_substract():
    assert substract(10, 5) == 5
    assert substract(-1, 1) == -2
    assert substract(-1, -1) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-4, 2) == -2
    assert divide(-4, -2) == 2
    assert divide(5, 0) == "Error: Division by zero is not allowed."
    #python -m pytest .\test_calculator.py (ez kell a futtatáshoz)