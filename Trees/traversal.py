class Solution:

    def postorder_traversal(self, root):

        res = []

        def postorder(node):
            if not node:
                return 
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)


        postorder(root)
        return res
    

    def preorder_traversal(self, root):

        res = []

        def preorder(node):
            if not node:
                return 

            res.append(node.val)
            preorder(node.left)
            preorder(node.right) 


        preorder(root)
        return res
    

    def inorder_traversal(self, root):
        res = []


        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        

        inorder(root)

        return res