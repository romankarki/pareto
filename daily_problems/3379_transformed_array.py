from typing import List 



class Solution: 


    def construct(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [ ]

        for i in range(0, len(nums)): 
            curr = nums[i]
            new_idx = (curr + i ) % n
            result.append(nums[new_idx])
        return result 