import pytest
from working import convert

def test_am_pm_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11:15 AM to 1:30 PM") == "11:15 to 13:30"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_input_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:21 AM to 5:42 PM") == "09:21 to 17:42"
    assert convert("11 AM to 1 PM") == "11:00 to 13:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_invalid_input():
    with pytest.raises(ValueError, match="invalid format"):
        convert("invalid input")
    with pytest.raises(ValueError, match="invalid format"):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError, match="invalid format"):
        convert("9 AM to 5PM")
