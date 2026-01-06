from typing import Optional
from collections import deque

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:


    def max_level_sum(self, root: Optional[TreeNode]) -> int: 
        ans = 1 
        total = root.val 

        level = 1 
        q = deque([root])
        while q: 
            length = len(q)
            level += 1
            level_sum = 0 
            for _ in range(0, length):
                node = q.popleft()

                if node.left: 
                    level_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    level_sum += node.right.val
                    q.append(node.right)
            if level_sum > total and q : 
                total = level_sum
                ans = level 
        return ans 