from node import Node

class BST:

    def __init__(self, iter=[]):
        self.root = None
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    
    def __str__(self):
        return self.root.val

    def __len__(self):
        return self(len)

    def pre_order(self, operation):

        def _walk(node=Node):
            if node is None:
                return
            
            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)


    def in_order(self, operation):

        def _walk(node=Node):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)
            
            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)


    def post_order(self, operation):

        def _walk(node=Node):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)


    def insert(self, val):
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break
        return node


a = BST([1,2,3,4,5,6,7,8,9])
print(str(a.root.left.val))