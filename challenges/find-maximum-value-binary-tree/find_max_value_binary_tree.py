class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.right = None
        self.left = None
    
    def __repr__(self):
        return 'Node Val: {}'.format(self.val)

    def __str__(self):
        return self.val


def find_maximum_value(self, operation):

    def _walk(node=Node):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)
            node.left=node.max
        operation(node)

        if node.right is not None:
            _walk(node.right)
            node.left=node.max

    _walk(self.root)
