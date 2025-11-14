import pytest
from age import categorize_byAge

def test_child_age():
    assert categorize_byAge(4) == "Child"

def test_teenager_age():
    assert categorize_byAge(10) == "Teenager"

def test_adult_age():
    assert categorize_byAge(19) == "Adult"

def test_golden_age():
    assert categorize_byAge(65) == "Golden Age"

def test_invalid_age():
    assert categorize_byAge(130) == "Invalid age: 130"
    assert categorize_byAge(121) == "Invalid age: 121"

    #python -m pytest .\test_age2.py -v (ez kell a futtatáshoz)
    # Ez a fájl pytest-tel van írva, míg a test_age.py unittest-tel.