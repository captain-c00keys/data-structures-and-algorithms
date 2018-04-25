from queue import Queue

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.right = None
        self.left = None
    
    def __repr__(self):
        """This is used in tests. This is for the dev"""
        pass
        
    def __str__(self):
        """This is for the user"""
        pass

class KTree:

    def __init__(self, iter=[]):
        self.root = None
        self.len = 0
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    
    def __str__(self):
        return self.root.val

    def __len__(self):
        return self.len

    def pre_order(self, operation):
        '''Perform operation on each node breadth first for pre-order'''
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
        '''Perform operation on each node breadth first for post-order'''
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
        '''Perform insert operation'''
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