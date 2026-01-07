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