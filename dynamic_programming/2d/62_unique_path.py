class Solution:

    def unique_path(self, m: int, n: int) -> int:
        self.ans = 0 
        def dfs(r, c):
            if (r,c) == (m-1, n-1):
                self.ans += 1
                return 
            if r >= m or c >= n or r < 0 or c < 0:
                return 
            
            dfs(r+1, c )
            dfs(r, c+1)

        dfs(0, 0)
        return self.ans
    

    def unique_dp(self, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1


        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += dp[r +1][c] + dp[r][c+1]
        return dp[0][0]




m, n = 3, 7

s = Solution()

print("Possibel paths", s.unique_dp(m, n))