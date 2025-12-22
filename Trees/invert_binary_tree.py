#inverting tree mean to just do bfs or dfs only
from collections import deque 
from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right



class Solution:

    def invert_tree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        root.left, root.right = root.right, root.left

        self.invert_tree_dfs(root.left)
        self.invert_tree_dfs(root.right)

        return root 


    def invert_tree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        

        return root 
    
    
