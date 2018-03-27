
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


firstNode = Node('John')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)
linkedList.length(Node)
linkedList.printList()


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
