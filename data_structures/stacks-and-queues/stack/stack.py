from node import Node

class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0
        if type(iterable) is not list:
            raise TypeError('Not iterable')
        for item in iterable:
            self.push(item)

    def __repr__(self):
        return 'Top of stack is {self.top.val}'.format(self)

    def __str__(self):
        return 'Top of stack is {self.top.val}'.format(self)

    def __len__(self):
        return self._size

    def push(self, val):
        try:
            node = Node(val, self.top)
        except TypeError:
            return self.top
        self.top = node
        self._size += 1
        return self.top

    def pop(self):
        removed_node = self.top
        self.top = self.top._next
        self._size -= 1
        return removed_node.val

    def peek(self):
        return self.top.val
