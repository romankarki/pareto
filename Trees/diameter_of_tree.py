from typing import Optional


class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.right = right 
        self.left = left 
    

class Solution:


    def diameter(self, root : Optional[TreeNode]) -> int:
        # may or maynot go through the root node 
        if not root:
            return 0
        
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)

        di = left_height + right_height

        sub = max(self.diameter(root.left), self.diameter(root.right))
        

        return max(di, sub)


    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))