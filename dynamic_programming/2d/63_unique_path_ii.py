class Solution:


    def unique_ii_dp(self, grid):

        R, C = len(grid), len(grid[0])
        if grid[R-1][C-1] == 0:
            return 0
        
        dp = [[0] * (C+1) for _ in range(R+1)]
        dp[R-1][C-1] = 1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if grid[r][c] == 0:
                    dp[r][c] = 0 
                    continue
                dp[r][c] += dp[r+1][c] + dp[r][c+1]
        return dp[0][0]