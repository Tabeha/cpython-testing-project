import math
import random
import unittest

from calculator import add, divide, multiply, subtract


class TestCalculatorUnittest(unittest.TestCase):
    def test_add(self) -> None:
        cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (10.5, 0.5, 11.0),
            (-7, -8, -15),
        ]
        for left, right, expected in cases:
            with self.subTest(operation="add", left=left, right=right):
                self.assertEqual(add(left, right), expected)

    def test_subtract(self) -> None:
        cases = [
            (10, 4, 6),
            (0, 5, -5),
            (-3, -2, -1),
            (5.5, 2.5, 3.0),
            (-10, 3, -13),
        ]
        for left, right, expected in cases:
            with self.subTest(operation="subtract", left=left, right=right):
                self.assertEqual(subtract(left, right), expected)

    def test_multiply(self) -> None:
        cases = [
            (3, 4, 12),
            (-2, 5, -10),
            (0, 100, 0),
            (1.5, 2, 3.0),
            (-3, -6, 18),
        ]
        for left, right, expected in cases:
            with self.subTest(operation="multiply", left=left, right=right):
                self.assertEqual(multiply(left, right), expected)

    def test_divide(self) -> None:
        cases = [
            (10, 2, 5),
            (9, 3, 3),
            (-12, 4, -3),
            (7.5, 2.5, 3.0),
            (-15, -5, 3),
        ]
        for left, right, expected in cases:
            with self.subTest(operation="divide", left=left, right=right):
                self.assertEqual(divide(left, right), expected)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_bulk_operations_against_python_operators(self) -> None:
        rng = random.Random(2026)
        for _ in range(2000):
            left = rng.uniform(-1_000, 1_000)
            right = rng.uniform(-1_000, 1_000)
            divisor = rng.uniform(1, 1_000)

            self.assertTrue(math.isclose(add(left, right), left + right, rel_tol=1e-9))
            self.assertTrue(
                math.isclose(subtract(left, right), left - right, rel_tol=1e-9)
            )
            self.assertTrue(
                math.isclose(multiply(left, right), left * right, rel_tol=1e-9)
            )
            self.assertTrue(
                math.isclose(divide(left, divisor), left / divisor, rel_tol=1e-9)
            )


if __name__ == "__main__":
    unittest.main()
