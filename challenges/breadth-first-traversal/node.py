class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.right = None
        self.left = None
    
    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val
