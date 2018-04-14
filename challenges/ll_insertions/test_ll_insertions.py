import pytest
from ll_insertions import LinkedList as LL

x = LL([5, '3', 'tree', 5, 32])

def test_linkedlist_insert():
    x.insert(4)
    assert x.head.val == 4

def test_linkedlist_insert_empty():
    with pytest.raises(TypeError) as e:
        x.insert()
    assert str(e.value) == "insert() missing 1 required positional argument: 'val'"

def test_insert_iterable():
    assert LL([1, 2, 3, 4, 5, 6])._len == 6
