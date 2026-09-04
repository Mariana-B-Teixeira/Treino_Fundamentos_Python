import pytest
import fuel

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("-1/1")
    with pytest.raises(ValueError):
        fuel.convert("0/-1")

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/100") == 1
    assert fuel.convert("99/100") == 99

def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(-1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(50) == "50%"

def convert():
    assert fuel.gauge(75) == "75"
    assert fuel.gauge(50) == "50"
