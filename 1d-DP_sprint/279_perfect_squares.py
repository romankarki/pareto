class Solution: 


    def perfect_nums_brute(self, num: int) -> int: 
        '''
            sqrt(n) ** n 
            to memoized -> sqlr(n) * n
        '''
        from functools import lru_cache

        @lru_cache(None)
        def dfs(rem: int) -> int: 
            if rem == 0: 
                return 0 
            
            res = float('inf')
            i = 1 
            while i*i <= rem : 
                res= min(res, 1 + dfs(rem - i*i ))
                i += 1
            return res
        
        return dfs(num)
    



    def perfect_nums_dp(self, nums: int) -> int: 

        '''
        12 -> 4 + 4 + 4
        [0 1 2 3 1 _ _ _ _ _ _ _]
        '''
        dp = [float('inf')] * (nums+1)
        dp[0] = 0 
    

        for i in range(1, nums+1):
            j = 1 
            while j * j <= i: 
                dp[i] = min(dp[i], 1 + dp[i - j*j])
                j += 1
        return dp[nums]


