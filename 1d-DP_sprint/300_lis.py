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