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




def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    q = deque([root])

    while  q: 
        level_size = len(q)
        current_level = [] 

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        result.append(current_level)


    return result