class TreeNode:
    def __init__(self, val, left, right):
        self.val = val 
        self.right = right
        self.left = left

class Solution:


    def sum_to_leaf(self, root):
        self.total = 0 
        def dfs(node, curr):
            if not node:
                return 
            curr += str(node.val)

            if not node.left and not node.right:
                self.total += int(curr, 2)
                return 
            
            dfs(node.left, curr)
            dfs(node.right, curr)


        dfs(root, "")



        return self.total 