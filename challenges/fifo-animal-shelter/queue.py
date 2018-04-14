class Node:
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __repr__(self):
        return self.val


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
        return self

    def enqueue(self, val):
        node = Node(val)
        if self._len == 0:
            self.back = node
            self.front = node
        else:
            self.back = node
        self._len += 1
        return self.back.val, self.front.val

    def dequeue(self):
        if len(self) == 0:
            return False
        else:
            current = self.front
            self.front = current._next
            return current
