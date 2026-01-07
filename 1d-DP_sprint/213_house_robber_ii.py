from typing import List 


class Solution:
     
    def house_rob_ii_brute(self, nums: List[int]) -> int: 
        # it's important to have decisions if i've robbed the first one then can't do last one 
        n = len(nums)
        if n==1:
            return nums[0]
        
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, end: int) -> int: 
            if i > end: 
                return 0 
            return max(nums[i] + dfs(i+2, end), dfs(i+1, end))

        #either skip last and take first || skip first and take last
        return max(dfs(0, n-2), dfs(1, n-1))
    

    def hourse_robber_dp(self, n: List[int]) -> int:
        '''
        [1, 2, 3, 1]
        [4, 3, 3, 1] -> DP 

        dp[2] = max(dp[3], nums[2] + dp[4])

        '''
        if len(n) == 0:
            return n[0]
        
        def rob(nums: List[int]) -> int: 

            dp = [0] * (len(nums)+1)

            for i in range(len(nums)-1, -1, -1):
                
                if i == (len(nums) - 1):
                    dp[i] = nums[i]
                    continue
                
                dp[i] = max(dp[i+1], dp[i+2]+nums[i])

            return dp[0] 
        
        c1 = rob(n[0: len(n)-1])
        c2 = rob(n[1: ])

        return max(c1, c2)




s = Solution()

print(s.house_rob_ii_brute([2,3,2]))