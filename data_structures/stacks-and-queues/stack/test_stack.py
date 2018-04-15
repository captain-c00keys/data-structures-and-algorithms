import pytest

def test_push_empty_stack(empty_stack):
    assert empty_stack.top is None


def test_push_add_val(empty_stack):
    empty_stack.push(5)
    assert empty_stack.top.val == 5


def test_push_add_multi_val(empty_stack):
    empty_stack.push(5)
    empty_stack.push(4)
    empty_stack.push(6)
    assert empty_stack.top.val == 6
    assert empty_stack.top._next.val == 4