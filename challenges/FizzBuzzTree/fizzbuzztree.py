from bst import BST

def fizzBuzzTtree(BST):

    def _walk(node):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)
        
        if node.val % 3 == 0 and node.val % 5 == 0:
            node.val = ('fizzbuzz')
        elif node.val % 3 == 0:
            node.val = ('fizz')
        elif node.val % 5 == 0:
            node.val = ('buzz')
        if node.right is not None:
            _walk(node.right)
    if BST.root is None:
        return False
    else:
        _walk(BST.root)
    return BST
