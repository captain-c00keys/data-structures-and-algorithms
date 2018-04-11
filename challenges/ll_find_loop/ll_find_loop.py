class Node:
    def __init__(self, val):
        self._val = val
        self._next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastnode = lastNode._next
            lastNode._next = newNode

    def __len__(self):
        self.head = None
        total = 0
        while cur._next is not None:
            total += 1
            cur = cur._next
        return total

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
