import math
import random

import pytest

from calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (10.5, 0.5, 11.0),
        (-7, -8, -15),
    ],
)
def test_add(left: float, right: float, expected: float) -> None:
    assert add(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 4, 6),
        (0, 5, -5),
        (-3, -2, -1),
        (5.5, 2.5, 3.0),
        (-10, 3, -13),
    ],
)
def test_subtract(left: float, right: float, expected: float) -> None:
    assert subtract(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (3, 4, 12),
        (-2, 5, -10),
        (0, 100, 0),
        (1.5, 2, 3.0),
        (-3, -6, 18),
    ],
)
def test_multiply(left: float, right: float, expected: float) -> None:
    assert multiply(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 2, 5),
        (9, 3, 3),
        (-12, 4, -3),
        (7.5, 2.5, 3.0),
        (-15, -5, 3),
    ],
)
def test_divide(left: float, right: float, expected: float) -> None:
    assert divide(left, right) == expected


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)


def test_bulk_operations_against_python_operators() -> None:
    rng = random.Random(2026)
    for _ in range(2000):
        left = rng.uniform(-1_000, 1_000)
        right = rng.uniform(-1_000, 1_000)
        divisor = rng.uniform(1, 1_000)

        assert math.isclose(add(left, right), left + right, rel_tol=1e-9)
        assert math.isclose(subtract(left, right), left - right, rel_tol=1e-9)
        assert math.isclose(multiply(left, right), left * right, rel_tol=1e-9)
        assert math.isclose(divide(left, divisor), left / divisor, rel_tol=1e-9)
