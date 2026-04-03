class Node:
    def __int__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

    def remove(self, node):
        pass

    def insert(self, node):
        pass

    def get(self, key: int):
        pass

    def put(self, key: int, value: int):
        pass