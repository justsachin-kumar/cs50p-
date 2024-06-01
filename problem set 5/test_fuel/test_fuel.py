from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("4/4") == 100
    assert convert('3/4') == 75
    assert convert('2/3') == 67
    assert convert('1/3') == 33

    assert convert('1/3') == 33


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

 

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"

