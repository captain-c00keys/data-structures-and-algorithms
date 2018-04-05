class LinkedList:
    def __init__(self, iter=[]):
        self.current = None
        self.head = None
        self._size = 0

        for item in reversed(iter):
            self.insert(item)

    def __len__(self):
        return self._size
