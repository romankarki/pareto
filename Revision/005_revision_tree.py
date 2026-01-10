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
    

    def pattern3_depth_1(self, root: Optional[TreeNode]) -> int: 
        if not root: 
            return 
        return 1 + max(
            self.pattern3_depth_1(root.left),
            self.pattern3_depth_1(root.right)
        )


    def pattern2_leveltraverse_2(self, root): 

        if not root: 
            return 
        res = [] 

        q = deque([root])

        while q: 
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q.append(level)
        return res
    

    def depth_of_tree(self, root): 
        if not root: 
            return 0
        
        return 1 + max(
            self.depth_of_tree(root.left), 
            self.depth_of_tree(root.right)
        )
    
    

    def diameter_of_tree(self, root): 
        self.ans = 0 

        def dfs(node): 
            if not node: 
                return 0 
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r)
            return 1 + max(l, r)

        dfs(root)
        return self.ans


    def diameter_of_tree_2(self, root) -> int: 


        self.ans = 0 
        def dfs(node): 
            if not node: 
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(l, r)
            return 1 + max(l, r)
        dfs(root)
        return self.ans
    
    def path_sum_pattern_1(self, root, target): 
        if not root: 
            return False
        if not root.left and not root.right: 
            return root.val == target
        return (
            self.path_sum_pattern_1(root.left, target - root.val) or 
            self.path_sum_pattern_1(root.right, target - root.val)
        )
    

    def path_sum_pattern(self, root, target): 

        if not root: 
            return False
        if not root.left and not root.right: 
            return root.val == target
        
        return (
            self.path_sum_pattern(root.left, target - root.val )
            or 
            self.path_sum_pattern(root.right, target - root.val)
        )


    def path_sum_ii(self, root, target): 

        self.ans = [] 
        def dfs(node, remain, path):
            if not node: 
                return 
            path.append(node.val)
            if not node.left and node.right and remain == node.val:
                self.ans(path.copy())
            
            else: 
                dfs(node.left, remain - node.val, path)
                dfs(node.right, remain - node.val, path)
            path.pop()
            

        dfs(root, target, [])
        return self.ans