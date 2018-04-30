"""Solution algorithm for the Queue."""
from queue import Queue


class Node:
    """The node."""

    def __init__(self, val, next=None):
        """Initialize the node."""
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        """Is used in tests. This is for the dev."""
        pass

    def __str__(self):
        """Is for the user."""
        pass


class KTree:
    """The K-tree."""

    def __init__(self, iter=[]):
        """Intitialize the k-tree."""
        self.root = None
        self.len = 0
        for item in iter:
            self.insert(item)

    def __repr__(self):
        """Dev presentation."""
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        """User presentation."""
        return self.root.val

    def __len__(self):
        """Size of tree."""
        return self.len

    def pre_order(self, operation):
        """Perform operation on each node breadth first for pre-order."""
        def recurse(node):
            child_list = []
            for node in node:
                operation(node)
                for child in node.children:
                    child_list.append(child)

            if len(child_list):
                recurse(child_list)

        if self.root:
            recurse([self.root])

    def post_order(self, operation):
        """Perform operation on each node breadth first for post-order."""
        def recurse(node):
            child_list = []
            for node in node:
                operation(node)
                for child in node.children:
                    child_list.append(child)

            if len(child_list):
                recurse(child_list)

        if self.root:
            recurse([self.root])

    def insert(self, val):
        """Perform insert operation"""
        node = Node(val)
        current = self.root
        self.len += 1
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
 

# def bfs(graph, root): 
#     visited = set()
#     queue = collections.deque([root])
#     visited.add(root)
#     while queue: 
#         vertex = queue.popleft()
#         for neighbour in graph[vertex]: 
#             if neighbour not in visited: 
#                 visited.add(neighbour) 
#                 queue.append(neighbour)