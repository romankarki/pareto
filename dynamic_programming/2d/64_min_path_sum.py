from typing import List


class Solution:


    def minPathSum(self, grid: List[int]) -> int:
        self.ans = float('inf')

        R, C = len(grid), len(grid[0])

        def dfs(r, c, s):
            if (r,c) == (R-1, C-1):
                s += grid[r][c]
                print("dest", grid[r][c], "of", "r =", r,"and c =", c)
                print("-------------Destination ------------------------")
                self.ans = min(self.ans, s)

            if r >= R or c >= C or r < 0  or c < 0:
                return 
            
            s += grid[r][c]
            print("iterating", grid[r][c], "of", "r =", r,"and c =", c)
            dfs(r + 1, c, s)
            dfs(r, c+1, s)
        
        dfs(0,0,0)

        return self.ans 
    



grid = [[1,3,1],[1,5,1],[4,2,1]]

s = Solution()
print("minimum path sum of",grid,"is",s.minPathSum(grid))