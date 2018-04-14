from node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)

    def __len__(self):
        return self._len

    def __str__(self):
        string = " "
        current = self.front
        for _ in range(self._len):
            string += str(current.val) + " "
            current = current._next
        return string.rstrip()

    def enqueue(self, val):
        node = Node(val)
        if self._len == 0:
            self.back = node
            self.front = node
        else:
            self.back = node
        self._len += 1
        return self.back.val, self.front.val
        # node = Node(val)
        # node._next = self.back
        # node._prev = 

    def dequeue(self):
        if len(self) == 0:
            return False
        else:
            current = self.front
            self.front = current._next
            return current
