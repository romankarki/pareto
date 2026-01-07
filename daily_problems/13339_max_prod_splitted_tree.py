from typing import Optional


class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 
    

class Solution: 
    def max_product(self, root: Optional[TreeNode]) -> int: 
        all_sums = []

        def dfs(node: TreeNode) -> int:
            if not node: 
                return 0 
            s = dfs(node.left) + dfs(node.right) + node.val 
            all_sums.append(s)
            return s 


        total_sum = dfs(root)
        maximum = 0 
        for s in all_sums:
            maximum = max(maximum, s * (total_sum - s))
        print("Total", total_sum)
        print("All_sum", all_sums)
        return maximum % (10**9 + 7)
    

t2 = TreeNode(4, None, None)
t3 = TreeNode(5, None, None)
t1 = TreeNode(2, t2, t3)
l1 = TreeNode(6, None, None)
l2 = TreeNode(3, l1, None)
r0 = TreeNode(1, t1, l2)

s = Solution()
print(s.max_product(r0))