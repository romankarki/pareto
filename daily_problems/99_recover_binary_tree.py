from typing import Optional


class TreeNode:

    def __init__(self, val, left, right):
        self.val = val 
        self.left = left
        self.right = right


class Solution: 
    
    def recover_tree(self, root: Optional[TreeNode]) -> None:
        self.prev = None 
        self.first = None 
        self.second = None 

        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev 
                self.second = node  
            self.prev = node
            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val