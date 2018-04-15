def find_maximum_value(bst):

    def _walk(node, curr_max):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)
            if node.left > node.
            node.left=node.max
        operation(node)  

        if node.right is not None:
            _walk(node.right)
            node.left=node.max

    _walk(bst.root)
