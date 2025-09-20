import sys, os
import pytest

# Add project root so we can import binary_search.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs import binary_search


# 1. Basic functionality
def test_basic():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4


# 2. Not found cases
def test_not_found():
    assert binary_search([10, 20, 30], 5) == -1
    assert binary_search([10, 20, 30], 40) == -1
    assert binary_search([10, 20, 30], 25) == -1


# 3. Edge cases
def test_edge_cases():
    assert binary_search([], 5) == -1
    assert binary_search([7], 7) == 0
    assert binary_search([7], 3) == -1


# 4. Duplicates
def test_duplicates():
    assert binary_search([1, 2, 2, 2, 3], 2) in (1, 2, 3)
    assert binary_search([5, 5, 5, 5], 5) in (0, 1, 2, 3)
    assert binary_search([5, 5, 5, 5], 7) == -1


# 5. Large input
def test_large_input():
    big = list(range(1_000_000))
    assert binary_search(big, 5) == 5
    assert binary_search(big, 999_999) == 999_999


@pytest.mark.parametrize("arr,target,expected", [
    ([1, 3, 5, 7, 9], 5, 2),
    ([1, 3, 5, 7, 9], 1, 0),
    ([1, 3, 5, 7, 9], 9, 4),
    ([10, 20, 30], 5, -1),
    ([10, 20, 30], 40, -1),
])
def test_various(arr, target, expected):
    assert binary_search(arr, target) == expected

