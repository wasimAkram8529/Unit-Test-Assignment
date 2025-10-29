import pytest
from app.calc import add, div

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_division_success():
    assert div(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)
