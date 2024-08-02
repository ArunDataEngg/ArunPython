# tests/test_income_tax.py

import pytest
from incomeTax import calculate_tax

def test_zero_gross_income():
    """Test with zero gross income"""
    gross_income = 0
    num_dependents = 0
    expected_tax = 0
    assert calculate_tax(gross_income, num_dependents) == expected_tax

def test_single_person_low_income():
    """Test with low income and no dependents"""
    gross_income = 20000
    num_dependents = 0
    expected_tax = 2000
    assert calculate_tax(gross_income, num_dependents) == expected_tax

def test_family_with_dependents():
    """Test with moderate income and 2 dependents"""
    gross_income = 60000
    num_dependents = 2
    expected_tax = 8647
    assert calculate_tax(gross_income, num_dependents) == expected_tax

def test_high_income_no_dependents():
    """Test with high income and no dependents"""
    gross_income = 150000
    num_dependents = 0
    expected_tax = 27347
    assert calculate_tax(gross_income, num_dependents) == expected_tax

def test_negative_gross_income():
    """Test with negative gross income (should raise ValueError)"""
    gross_income = -10000
    num_dependents = 0
    with pytest.raises(ValueError):
        calculate_tax(gross_income, num_dependents)