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
    

    def bottomUp(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[float("inf")] * (C + 1)  for _ in range(R+1)]
        dp[R-1][C] = 0 

        for r in range(R - 1, -1, -1):
            for c in range(C-1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]
    



grid = [[1,3,1],[1,5,1],[4,2,1]]

s = Solution()
print("minimum path sum of",grid,"is",s.bottomUp(grid))