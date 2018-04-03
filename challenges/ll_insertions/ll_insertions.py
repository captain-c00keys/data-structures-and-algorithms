from node import Node

class LinkedList(object):

    def __init__(self, iter = []):

        self.head = None
        self._size = 0

        for val in iter:
            self.head = Node(val, self.head)
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

    def insert(self):
        self.head = Node(val, self.head)
        self._size += 1


    def find(self, val):
        if self.head == None:
            return False
        elif self.head == val
            return True
        else:
            current = self.head
            cnext = current.next
            if cnext.val == val:
                return True
            else:
                while cNext.val != val and cnext is not None:
                    current = cnext
                    cNext = current.next
                if cnext.val == val:
                    return True
                return False