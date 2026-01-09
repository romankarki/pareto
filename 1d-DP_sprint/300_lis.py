from typing import List

class Solution: 


    def length_list(self, nums: List[int]) -> int: 

        def dfs(i: int, prev_idx: int) -> int: 
            if i == len(nums): 
                return 0 
            #don't pick 
            ans = dfs(i+1, prev_idx)

            #valid pick 
            if prev_idx == -1 or nums[i] > nums[prev_idx]: 
                ans = max(ans, 1 + dfs(i +1, i ))
        return dfs(0, -1)
    

    def length_of_lis(self, nums: List[int]) -> int: 

        n = len(nums)

        dp = [1] * n 

        for  i in range(n): 
            for j in range(i): 
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)