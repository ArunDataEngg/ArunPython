import pytest

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("Please provide a string Argument")
    return x.capitalize()

def isEven(num):
    if not isinstance(num, int):
        raise TypeError("Please provide a number")
    return num%2

def test_capital_case():
    assert capital_case("Python training")=='Python training'

def test_raise_exception_on_non_string_argumnets():
    with pytest.raises(TypeError):
        capital_case(9)

def test_isEven():
    assert isEven(20)==0

def test_raises_exception_on_non_integer_arguments():
    with pytest.raises(TypeError):
        isEven("A")