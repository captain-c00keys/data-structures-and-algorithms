from node import Node


class LinkedList(object):

    def __init__(self, iter = []):

        self.head = None
        self._size = 0

        for val in iter:
            self.head = Node(val, self.head)
            self.insert(val)
            self._size += 1

    def __len__(self):
        return self._size

    def __str__(self):
        el = []
        current = self.head
        for _ in range(self._size+1):
            el.append(current)
            current = current.next
        return el
        # import pdb; pdb.set_trace()

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1

    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next

        return False

