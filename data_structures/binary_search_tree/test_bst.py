from bst import BST
import pytest

def test_insert():
    bst = BST()
    assert len(bst) == 0
    assert bst.insert(6).val == 6
    assert bst.current.val == 6

@pytest.fixture
def small_bst():
    bst = BST([3,2,5])
    return bst

# def test_insert_direction(small_bst):
#     assert pre_order == 5

# def test_pre_order():
#     assert _walk