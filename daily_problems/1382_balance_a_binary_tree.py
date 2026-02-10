class Solution:

    def balancebst(self, root):

        def inorder(node):
            if not node:
                return [] 
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        

        def build_blance(arr):

            if not arr: 
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = build_blance(arr[:mid])
            root.right = build_blance(arr[mid+1:])
            return root 
        
        sorted_vals = inorder(root)

        return build_blance(sorted_vals)




class TreeNode:
    def __init__(self, val, left, right):
        self.val = val 
        self.right = right
        self.left = left 
        