from node import Node
from linked_list import LinkedList as LL

class Insert(LL):

    def append(self, val):

        if self.head = None:
            self.head = Node(self, val)

        cur = self.head
        if not cur.next:
            cur._next = Node(val)
        while cur.next:
            cur = cur.next
        newnode = Node(val)
        cur.next = newnode