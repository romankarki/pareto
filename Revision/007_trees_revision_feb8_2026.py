from typing import Optional, List
from collections import deque

class TreeNode: 

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    


def traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def traverse_tree(node):
        if not node:
            return 
        
        traverse_tree(node.left)
        result.append(node.val)
        traverse_tree(node.right)
    
    traverse_tree(root)
    return result 



