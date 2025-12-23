from typing import List

class Solution:

    def combination_sum(self, nums: List[int], target: int)->List[List[int]]:
        res = []
        def dfs(i, curr, sums):
            if sums == target:
                res.append(curr.copy())
                return 
            
            if i >= len(nums) or sums > target:
                return 
            curr.append(nums[i])
            dfs(i, curr, sums + nums[i])
            curr.pop()
            dfs(i+1, curr, sums)

        dfs(0, [], 0)
        return res 