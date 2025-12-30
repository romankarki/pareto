from typing import List

class Solution:

    def laststone_recur(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = (stone_sum+1)//2
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i,total)]  = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
            return dp[(i, total)]
        return dfs(0,0) 
    

    def laststone_bottomup(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n+1)]

        for i in range(1, n+1):
            for t in range(target+1):
                if t >= stones[i-1]:
                    dp[i][t] = max(dp[i-1][t], dp[i-1][t-stones[i-1]]+ stones[1-1])
                else:
                    dp[i][t] = dp[i-1][t]
        return stone_sum - 2 * dp[n][target]