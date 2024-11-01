import pytest
from fizzbuzz import Solution

@pytest.fixture
def solution():
    return Solution()

def test_fizzbuzz_15(solution):
    ...