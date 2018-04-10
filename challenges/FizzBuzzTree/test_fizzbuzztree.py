from .fizzbuzztree import fizzbuzztree
from bst import BST

@pytest.fixture
def filled_bst():
    return BST([4, 3, 2, 1, 8, 6, 12, 9])

def test_for_post_order(BST):
    assert fizzbuzztree(BST) is False

def test_bst_in_order(filled_bst):
    filled_bst = fizzbuzztree(filled_bst)
    first = []
    filled_bst.in_order(first.append)
    assert first == [1, 2, 'fizz', 4, 'fizz', 8, 'fizz', 'fizz']

def test_bst_pre_order(filled_bst):
    filled_bst = fizzbuzztree(filled_bst)
    first = []
    filled_bst.pre_order(first.append)
    assert first == [4, 'fizz', 2, 1, 8, 'fizz', 'fizz', 'fizz']