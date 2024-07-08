import pytest
from refueling import convert, gauge

def test_convert():

    # Valid fractions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/5") == 40
    assert convert("1/1") == 100
    assert convert("0/3") == 0

def test_gauge():
    # valid percentages
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(2) == "2%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
