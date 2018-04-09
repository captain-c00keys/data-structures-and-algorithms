from bst import BST

def fizzBuzzTtree(BST):

    def _walk(node):
        if node is None:
            return

        if node.left is not None:
            _walk(node.left)
        
        x = node.val
        if x % 3 == 0 and x % 5 == 0:
            node.val = ('fizzbuzz')
        elif x % 3 == 0:
            node.val = ('fizz')
        elif x % 5 == 0:
            node.val = ('buzz')
        else:
            node.val
        if node.right is not None:
            _walk(node.right)

    _walk(BST.root)
    return BST
