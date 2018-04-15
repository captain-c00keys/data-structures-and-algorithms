from node import Node

class LinkedList:
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1