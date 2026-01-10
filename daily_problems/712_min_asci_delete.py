class Solution: 


    def min_ascii_diff(self, s1: str, s2: str) -> int: 
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int) -> int: 

            if i == len(s1):
                return sum([ord(c) for c in s2[j:]])

            if j == len(s2): 
                return sum([ord(c) for c in s1[i:]])

            if s1[i]  == s2[j]: 
                return dfs(i+1, j+1)


            return min(
                ord(s1[i]) + dfs(i+1, j),
                ord(s2[j]) + dfs(i, j+1)
                )
        
        return dfs(0, 0)