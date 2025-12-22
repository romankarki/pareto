class TreeNode:
    def __init__(self, val =0, left = None, right = None ):
        self.val = val 
        self.left = left 
        self.right = right


class Solution: 
    
    def lca_tree(self, root, p, q):
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            
            else:
                return curr
        return None

        
