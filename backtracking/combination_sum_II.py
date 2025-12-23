from typing import List

class Solution:


    def combination_sum_ii(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if total > target or i >= len(candidates):
                return 
            
            curr.append(candidates[i])
        
            dfs(i+1, curr, total + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates == candidates[i+1]:
                i += 1
            dfs(i+1, curr, total)

        dfs(0, [], 0)


        return res 