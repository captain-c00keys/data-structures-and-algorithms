import pytest
from ll_merge import LinkedList as LL
from ll_mergeList import merge_lists as ml

def test_insert_iterable():
    assert LL([1, 2, 3, 4])._size == 4


def test_find_none(empty_ll):
    assert empty_ll.find(1) is False


def test_find(small_ll):
    assert small_ll.find(2) is True


def test_not_found(small_ll):
    assert small_ll.find(5) is False


def test_empty_list(empty_ll):
    assert len(empty_ll) == 0


def test_length(small_ll):
    assert len(small_ll) == 4