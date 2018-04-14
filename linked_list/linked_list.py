from node import Node

class LinkedList:
    def __init__(self, iter=[]):
        self.head = None
        self.length = 0

        for item in reversed(iter):
            self.head = Node(item, self.head)
            self.length += 1

    def __len__(self):
        return self.length

    def insert(self, val):
        self.head = Node(val, self.head)
        self.length += 1

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


# firstNode = Node('John')
# linkedList = LinkedList()
# linkedList.insert(firstNode)
# secondNode = Node("Ben")
# linkedList.insert(secondNode)
# thirdNode = Node("Matthew")
# linkedList.insert(thirdNode)
# linkedList.length(Node)
# linkedList.printList()


#     def append(self,data):
#         new_node = node(data)
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = new_node
#
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next is not None:
#             total += 1
#             cur = cur.next
#         return total
#
#     def display(self):
#         elems = []
#         cur_node = self.head
#         while cur_node.next is not None:
#             cur_node=cur_node.next
#             elems.append(cur_node.data)
#         print(elems)
#
#     def get(self,index):
#         if index >= self.length():
#             print("ERROR: 'Get' Index out of range!")
#             return None
#         cur_idx=0
#         cur_node=self.head
#         while True:
#             cur_node=cur_node.next
#             if cur_idx==index:
#                 return cur_node.data
#             cur_idx+=1
#
#     def erase(self,index):
#         if index >= self.length():
#             print('Error')
#             return
#         cur_idx=0
#         cur_node=self.head
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx==index:
#                 last_node.next = cur_node.next
#                 return
#             cur_idx+=1
#
# my_list = LinkedList()
#
