from node import Node

class Stack:
    """Doc String"""
    def __init__(self, iterable=[]):
        self._current = None
        self.head = None
        self._size = 0

        for item in reversed(iter):
            self.insert(item)

    def push(self, val):
        pass

    def __len__(self):
        return self._size

    