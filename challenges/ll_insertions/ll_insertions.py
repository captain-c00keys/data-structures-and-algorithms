from node import Node

class LinkedList:
    def __init__(self, iter = []):
        self.head = None
        self._len = 0

        for item in iter:
            self.head = Node(item, self.head)
            self._len += 1

    def __len__(self):
        return self._len

    def __str__(self):
        lis = []
        current = self.head
        for _ in range(self._len+1):
            lis.append(current)
            current = current._next
        return str(lis)

    def insert(self, val):
        try:
            self.head = Node(val, self.head)
            self._len += 1
        except TypeError:
            raise TypeError('no value')

    def find(self, val):
        if self.head == None:
            return False
        elif self.head == val:
            return True
        else:
            current = self.head
            nxt = current._next
            if nxt.val == val:
                return True
            else:
                while nxt.val != val and nxt is not None:
                    current = nxt
                    nxt = current._next
                if nxt.val == val:
                    return True
                return False


    def append(self, value):
        current = self.head
        self._len += 1
        while current._next:
            current = current._next
        current._next = Node(value)



    def insert_before(self, value, newval):
        current = self.head
        self._len += 1
        while current._next:
            if current._next.val == value:
                newval = current._next
            current = current._next
        current._next = Node(value)


    def insert_after(self, value, newval):
        current = self.head
        self._len += 1
        while current._next:
            if current.val == value:
                position = current._next
                current._next = Node(newval)
                current._next._next = position
            current = current._next
