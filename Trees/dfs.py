from typing import Optional
from collections import deque

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right

    


class Solution:

    def invert_Tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invert_Tree(root.left)
        self.invert_Tree(root.right)
        

        return root

    

    def invert_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root :
            return None
        
        q = deque([root])

        while q:
           node = q.popleft()

           node.left, node.right = node.right, node.left
           if node.left:
               q.append(node.left) 
           if node.right:
               q.append(node.right)
        return root