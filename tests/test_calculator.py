# tests/test_calculator.py
# Unit tests for the SecurePipe calculator application

import pytest
from src.calculator import add, subtract, multiply, divide, square_root


class TestAdd:
    def test_add_two_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_two_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_zero(self):
        assert add(0, 5) == 5


class TestSubtract:
    def test_subtract_two_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        assert subtract(3, 7) == -4


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_normal(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(10, 0)


class TestSquareRoot:
    def test_square_root_positive(self):
        assert square_root(9) == 3.0

    def test_square_root_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot take square root"):
            square_root(-4)
