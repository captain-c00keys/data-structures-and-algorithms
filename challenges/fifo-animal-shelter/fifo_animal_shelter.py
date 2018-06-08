from node import Node


class AnimalShelter:
    
    def __init__(self, iterable=[]):
        self.oldest = None
        self.newest = None
        self._len = 0

        for item in iterable:
            self.enqueue(item)
    
    def __repr__(self):
        return 'Queue front: {}'.format(self.oldest.val)

    def __str__(self):
        lis = ""
        current = self.oldest
        while current:
            lis += str(current.val) + " "
            current = current.next
        return lis.rstrip()

    def enqueue(self, amiamal):
        node = Node(amiamal)
        if self._len == 0:
            self.oldest = self.newest = node
            self._len += 1
            return node
        self.newest.next = node
        self.newest = node
        self._len += 1
        return node

    def dequeue(self, pref=None):
        try:
            if pref is None:
                if self._len == 0:
                    return False
                else:
                    self._len -= 1
                    return self.oldest
            temp = self.oldest
            while temp.next:
                temp = temp.next
            if temp.val == pref:
                self._len -= 1
                return temp
            else:
                return False
        except IndexError:
            return False