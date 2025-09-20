import unittest

import sys, os

print("__file__", __file__)
code_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("code_path: ", code_path)

sys.path.append(code_path)

from libs import binary_search


class TestBinarySearch(unittest.TestCase):

    # 1. Basic functionality
    def test_basic(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 1), 0)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 4)

    # 2. Not found cases
    def test_not_found(self):
        self.assertEqual(binary_search([10, 20, 30], 5), -1)
        self.assertEqual(binary_search([10, 20, 30], 40), -1)
        self.assertEqual(binary_search([10, 20, 30], 25), -1)

    # 3. Edge cases
    def test_edge_cases(self):
        self.assertEqual(binary_search([], 5), -1)
        self.assertEqual(binary_search([7], 7), 0)
        self.assertEqual(binary_search([7], 3), -1)

    # 4. Duplicates
    def test_duplicates(self):
        self.assertIn(binary_search([1, 2, 2, 2, 3], 2), (1, 2, 3))
        self.assertIn(binary_search([5, 5, 5, 5], 5), (0, 1, 2, 3))
        self.assertEqual(binary_search([5, 5, 5, 5], 7), -1)

    # 5. Large inputs
    def test_large_input(self):
        big = list(range(1_000_000))
        self.assertEqual(binary_search(big, 5), 5)
        self.assertEqual(binary_search(big, 999_999), 999_999)


if __name__ == "__main__":
    unittest.main()
