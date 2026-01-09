class Solution: 


    def decode_ways(self, s: str) -> str: 

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
    
    

        


s = Solution()
print(s.decode_ways("12"))