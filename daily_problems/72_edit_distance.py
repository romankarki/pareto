class Solution: 


    def edit_distance(self, word1: str, word2: str) -> int: 

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == len(word1): 
                return len(word2) - j 

            if j == len(word2): 
                return len(word1) - i 


            if word1[i] == word2[j]: 
                return dfs(i+1, j+1)

            return min(
                1 + dfs(i+1, j+1),
                1 + dfs(i+1, j), 
                1 + dfs(i, j+1)
            ) 
        


        return dfs(0, 0)