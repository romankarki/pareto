from typing import Optional, List
from collections import deque

class TreeNode: 

    def __init__(self, val, left, right):
        self.val = val 
        self.right = right 
        self.left = left 
    

class Solution: 

    def largestTreeLevels(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        q = deque([root])

        while q:
            lvl_size = len(q)
            maxima = float("-inf")
            for _ in range(lvl_size):

                node = q.popleft()
                maxima = max(maxima, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(maxima)
        
        return result 
        