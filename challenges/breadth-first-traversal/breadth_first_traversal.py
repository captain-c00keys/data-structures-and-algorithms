from queue import Queue


def breadth_first_traversal(tree, operation):
    if tree.root is None:
        return False
    operation(tree.root.val)
    q = Queue()
    if tree.root.left:
        q.enqueue(tree.root.left)
    if tree.root.right:
        q.enqueue(tree.root.right)
    top = q.front
    while top:
        node = top.val
        operation(node.val)
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)
        top = top.next