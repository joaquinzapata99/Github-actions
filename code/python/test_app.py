import unittest
from app import add


class TestAdditionCalculator(unittest.TestCase):

    def test_add(self):
        """Test that the add function correctly adds two numbers"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
