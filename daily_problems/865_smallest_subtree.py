from typing import Optional


class TreeNode: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.right = right 
        self.left = left 
        

class Solution: 


    def subtree_with_all_deep_node(self, root: Optional[TreeNode]) -> TreeNode: 

        def dfs(node: TreeNode) -> tuple[int, int]: 
            if not node: 
                return (0, None)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth: 
                return (left_depth + 1, left_node)
            
            if right_depth > left_depth:
                return (right_depth + 1, right_node)
            
            return (left_depth + 1, node)

        return dfs(root)[1]
    


    def subtree_with_deepest_node(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        def dfs(node: Optional[TreeNode]) -> tuple[int, TreeNode]: 
            if not node: 
                return (0, None)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            if left_depth > right_depth: 
                return (left_depth + 1, left_node)

            if right_depth > left_depth: 
                return (right_depth + 1, right_node)
            return (left_depth + 1, node)
        

        return dfs(root)[1]



    def subtree_smallest_deepest(self, root: TreeNode) -> TreeNode: 

        '''
                    3             -> (4, 2) ==> ans is Treenode(2)
                 /     \
                /       \
               5         1        -> (3, 2) (2, 1)
            /     \    /     \
           6       2  0       8   -> (1, 6) (2, 2)  (1, 0) (1, 8)
                  /  \
                 7    4 
                (1,7) (1,4)
        
        '''

        def dfs(node: TreeNode) -> tuple[int, TreeNode]: 

            if not node: 
                return (0, None)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            if left_depth > right_depth: 
                return (left_depth + 1, left_node)
            
            if right_depth > left_depth: 
                return (right_depth +1, right_node)
            

            return (left_depth + 1, node)
        

        return dfs(root)[1]