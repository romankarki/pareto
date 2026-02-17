from typing import Optional
from collections import deque

class TreeNode:

    def __init__(self, val, left, right):
        self.val = val 
        self.left = left
        self.right = right



class Solution:

    def is_symmetric_iterative(self, root: Optional[TreeNode]) -> bool:

        q = deque([(root, root)])

        while q:

            left, right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False 
            if left.val != right.val:
                return False 
            
            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True 