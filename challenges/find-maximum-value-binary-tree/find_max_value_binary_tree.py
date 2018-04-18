
def find_maximum_value(tree):
    if tree.root is None:
        return False
    max_val = tree.root.val
    root = tree.root

    def _walk(root):
        nonlocal max_val
        if root is None:
            return max_val
        if root.val > max_val:
            max_val = root.val
        if root.left is not None:
            _walk(root.left)
        if root.right is not None:
            _walk(root.right)
    _walk(root)
    return max_val
