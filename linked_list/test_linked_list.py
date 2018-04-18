import pytest
from .linked_list import LinkedList as ll
from .node import Node as nd

@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2])


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2

def test_node_class():
    assert nd('3').val == '3'

def test_node_class_next():
    assert nd(0,4)._next == 4

def test_node_without_next():
    assert nd(3)._next == None
