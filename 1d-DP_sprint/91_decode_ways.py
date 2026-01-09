class Solution: 


    def decode_ways(self, s: str) -> int: 

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            
            if s[i] == '0': 
                return 0 
            
            res = dfs(i+1)

            if i + 1< len(s) and 10 <= int(s[i: i+2]) <= 26:
                res += dfs(i+2)
            return res
        
        return dfs(0)
    
    

    def decode_ways_dp(self, s: str) -> int:
        '''
        s -> "11106"
        dp [0 0 1 0 1 1]
        '''
        n = len(s)
        dp = [0] * (n+1)

        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else: 
                dp[i] = dp[i+1]
                if (i+1 < n and 10 <= int(s[i: i+2]) <= 26):
                    dp[i] += dp[i+2]


        return dp[0]


s = Solution()
print(s.decode_ways("12"))