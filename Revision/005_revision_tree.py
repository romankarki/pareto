from typing import Optional


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