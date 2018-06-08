from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        pass

    def push(self, val):

        node = Node(val)
        self.len += 1

        node._next = self.top
        self.top = node

        return self.top

    def pop(self):
        if self.top is None:
            raise IndexError('Stack is empty')
        self.len -= 1
        node = self.top
        self.top = self.top._next

        return node.val

    def peek(self):
        return self.top

