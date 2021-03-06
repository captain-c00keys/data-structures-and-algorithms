import pytest
from .selection import selection_sort


def test_empty_selection_sort():
    """Test empty selection sort."""
    assert selection_sort([]) == []


def test_small_selection_sort():
    """Test small selection sort."""
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_large_selection_sort():
    """Test large selection sort."""
    assert selection_sort([12, 34, 56, 78, 910, 8765]) == [12, 34, 56, 78, 910,
                                                           8765]