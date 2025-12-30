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