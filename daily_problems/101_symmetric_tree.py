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
    

    def issymmetric_recursive(self, root):

        def is_mirror(left, right):
            if not left and not right:
                return True 
            if not left or not right:
                return False 
            
            if left.val != right.val:
                return False 
            
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root, root)