from .k_tree import KTree as KT
from .k_tree import Node
import pytest


def test_node():
    """test K-tree node"""
    n = Node(1)
    assert n.val == 1
    assert n.children == []
    assert repr(n) == 'Node Val: 1'
    assert str(n) == 'Node value is 1'


def test_k_tree_repr_str(single_tree):
    """test KTree repr and str"""
    assert repr(single_tree) == '<Tree Root 1>'
    assert str(single_tree) == 'Tree root value is 1'


def test_insert_root_K_tree():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    assert tree.root.val == 1


def test_insert_children():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    child_vals = [node.val for node in tree.root.children]
    assert tree.root.val == 1
    assert tree.root.children[0].val == 2
    assert child_vals == [2, 3]


def test_insert_many_children():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 3)
    tree.insert(5, 3)
    assert tree.root.val == 1
    assert tree.root.children[1].children[0].val == 4
    assert tree.root.children[1].children[1].val == 5
