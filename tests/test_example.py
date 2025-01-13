# test_example.py

import pytest
from src import main  # Replace `src.main` with the actual module to be tested

# Example test for a function
def test_add():
    result = main.add(2, 3)  # Replace `main.add` with the actual function
    assert result == 5, "Addition function failed"

# Example test for an edge case
def test_add_negative():
    result = main.add(-2, -3)  # Replace `main.add` with the actual function
    assert result == -5, "Addition function failed for negative numbers"

# Example test for an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        main.divide(1, 0)  # Replace `main.divide` with the actual function

# Parameterized test
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add_parametrized(a, b, expected):
    result = main.add(a, b)  # Replace `main.add` with the actual function
    assert result == expected, f"Addition failed for inputs {a} and {b}"
