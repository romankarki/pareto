from typing import List 


class Solution: 


    def inordertraversal(self, root):

        if not root:
            return []
        
        self.result = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.result.append(node.val)
            dfs(node.right)
        
        dfs(root)

        return self.result 
    

    def depth_of_tree(self, root):
        if not root:
            return 0 
        
        return 1 + max(self.depth_of_tree(root.left), self.depth_of_tree(root.right))
    


    def diameter_of_tree(self, root):


        if not root:
            return 0 
        
        self.ans = 0 
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            self.ans = max(self.ans, l + r)
            return 1 + max(l,r)


        dfs(root)

        return self.ans 
    

    def path_sum(self, root, target):
        if not root: 
            return False
        
        if not root.left and not root.right:
            return root.val == target
        
        remaining = target - root.val 

        return self.path_sum(root.left, remaining) or self.path_sum(root.right, remaining)
    

    def path_sum_ii(self, root, target):

        self.ans = [] 

        def dfs(node, target, path):
            if not node:
                return 
            
            path.append(root.val)
            if not root.left and not root.right:
                if target == root.val:
                    self.ans(path.copy())
                    path.pop()
                    return 
            
            dfs(node.left, target - root.val, path)
            dfs(node.right, target - root.val, path)
            path.pop()

        dfs(root, target, [])
        return self.ans