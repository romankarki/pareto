from typing import Optional
from collections import deque

class TreeNode: 
    def __init__(self, val = 0, left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 
    



class Revision: 

    def pattern1_dfs_1(self, root: Optional[TreeNode]) -> None: 
        if not root: 
            return 
        #pre
        self.pattern1_dfs_1(root.left)
        #in
        self.pattern1_dfs_1(root.right)
        #post
    

    def pattern2_bfs_1(self, root: Optional[TreeNode]) -> None:

        if not root: 
            return [] 
        
        q = deque([root])
        res = []
        while q: 
            level = [] 
            for _ in range(len(q)): 
                node = q.popleft()
                level.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(level)
        return res
