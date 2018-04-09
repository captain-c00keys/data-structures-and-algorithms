from bst import BST
import pytest


@pytest.fixture
def small_bst():
    bst = BST([3,2,5])
    return bst

@pytest.fixture
def empty_bst():
    return BST()