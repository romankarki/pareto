from typing import Optional, List
from collections import deque

class TreeNode: 

    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 


def traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def traverse_tree(node):
        if not node:
            return 
        
        traverse_tree(node.left)
        result.append(node.val)
        traverse_tree(node.right)
    
    traverse_tree(root)
    return result 




def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    q = deque([root])

    while  q: 
        level_size = len(q)
        current_level = [] 

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        result.append(current_level)


    return result


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    q = deque([root])
    
    while q:
        level_size= len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        last_item = current_level[-1]
        result.append(last_item)
    return result 


def max_depth(root: Optional[TreeNode]) -> int: 
    '''
    o(n) time 
    o(h) space
    '''
    if not root: 
        return 0 
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth) 


def max_depth_bfs_optimal(root) -> int: 
    '''
    o(n) time 
    o(w) space
    '''

    if not root:
        return 0 
    
    q = deque([root])
    max_depth = 0 

    while q:
        node, depth = q.popleft()

        max_depth = max(max_depth, depth)

        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    
    return max_depth


def is_balanced(root): 

    def check_height(node):
        if not node:
            return 0 
        
        left = check_height(node.left)
        if left == -1:
            return -1 
        
        right = check_height(node.right)
        if right == -1:
            return -1 
        
        if abs(left -right) > 1: 
            return -1
        
        return max(left, right) + 1

    return check_height(root) != -1

class Sol: 

    def diameter_tree(self, root) -> int: 
        self.ans = 0 
        def dfs(node):
            if not node:
                return 0 
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r)
            return 1 + max(l, r)

        return self.ans 
    
##pathsum patterns

def hasPathSum(root, target_sum):
    ''' O(n) -> time & O(h) -> space'''

    if not root:
        return False 
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return hasPathSum(root.left, remaining) or hasPathSum(root.right, remaining)




class PathSum:


    def sum_ii(self, root, target):

        self.ans = []
        self.dfs(root, target, [])
        return self.ans 
    

    def dfs(self, root, target, path):
        if not root:
            return
        
        path.append(root.val)
        if not root.left and not root.right: 
            if root.val == target:
                self.ans.append(path.copy())
        
        self.dfs(root.left, target - root.val, path)
        self.dfs(root.right, target - root.val, path)

        path.pop()
        



