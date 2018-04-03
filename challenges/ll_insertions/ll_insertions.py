from node import Node

class LinkedList(object):

    def __init__(self, iter = []):

        self.head = None
        self.current = None
        self._size = 0

    def __repr__(self):
        return '<head>'

    def __len__(self):
        return self._size

    def __str__(self):
