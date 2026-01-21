from typing import List 


class Solution: 


    def max_size(self, nums: List[int], k) -> int: 

        mp = {0: - 1}

        prefix = 0 
        res = 0 

        for i,x in enumerate(nums): 
            prefix += x
            if prefix-k in mp: 
                res = max(res, i - mp[prefix-k])
            if prefix not in mp: 
                mp[prefix] = i 
        return res