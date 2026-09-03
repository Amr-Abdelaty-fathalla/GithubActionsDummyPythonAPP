import pytest
from src.math_operations import add, sub

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (2, 100, 102),
    (0.1, -0.2, -0.1),
    (0.001, 0.5, 0.501),

])

def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, -1),
    (-1, 1, -2),
    (2, 100, -98),
    (0.1, -0.2, 0.3),
    (0.001, 0.5, -0.499),
])

def test_sub(num1, num2, expected):
    assert sub(num1, num2) == pytest.approx(expected) # result approximate to expected by 1  * (10) ^ -6