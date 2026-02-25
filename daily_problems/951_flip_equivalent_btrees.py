class Solution:


    def flip_equivalent(self, root1, root2):

        if root1 is root2:
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        

        return (
            self.flip_equivalent(root1.left, root2.left) and 
            self.flip_equivalent(root1.right, root2.right)
        ) or (
            self.flip_equivalent(root1.left, root2.right) and 
            self.flip_equivalent(root1.right, root2.left)
        )