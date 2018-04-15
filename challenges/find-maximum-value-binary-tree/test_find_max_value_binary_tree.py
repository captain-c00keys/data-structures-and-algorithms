import pytest
from bst import BST
from find_maximum_value_binary_tree import find_maximum_value


@pytest.fixture
def empty_bst():
    return BST()
 

@pytest.fixture
def small_bst():
    return BST([4, 3, 3.5, 2, 5, 6, 7])


@pytest.fixture
def large_bst():
    return BST([4, 10, 2, 3, 17, 24, 45])


def test_empty_bst(empty_bst):
    assert find_maximum_value(empty_bst) is False

def test_small_bst(small_bst):
    assert find_maximum_value(small_bst) == 7

def test_large_bst(large_bst):
    assert find_maximum_value(large_bst) == 45