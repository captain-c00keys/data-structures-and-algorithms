"""Hash table code."""
INITIAL_CAPACITY = 1024


class Node:
    """Node Class."""

    def __init__(self, key, value):
        """Empty Node."""
        self.key = key
        self.value = value
        self.next = None


class HashTable(object):
    """Hash Table."""

    def __init__(self):
        """Intialize hash table."""
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_key(self, key):
        """Loops through keys."""
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def set(self, key, value):
        """Insert node into buckets."""
        self.size += 1
        index = self.hash_key(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def get(self, key):
        """Find node in buckets."""
        index = self. hash_key(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        """Delete node in buckets."""
        index = self.hash_key(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size += 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result

