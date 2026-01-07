from typing import Optional, List


class TreeNode: 

    def __init__(self, val = 0, left = None, right = None):
        self.val = 0 
        self.right = right 
        self.left = left 




class Solution:

    def split_tree(self, root: Optional[TreeNode]) -> List[int]: 
        '''
        split trees like 
        Given tree: [1, 2, 3, 4, 5, 6, null]
        sums at every level 
                  1
                /   \
               2     3
              /  \   /  
             4    5  6
        sums at every level will be ->[4, 5, 11, 6, 9, 21]
        '''

        node_sums = []
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0 
            s = dfs(node.left) + dfs(node.right) + node.val
            node_sums.append(s)
            return s 


        total = dfs(root)
        print("Total Sum is", total)
        print("Each node splitted sum is", node_sums)
        
        return node_sums