from typing import List

class Solution:

    def bin_subarray_sum(self, nums: List[int], goal: int) -> int: 
        res = prefix_sum = 0 

        seen = {0: 1}
        for num in nums: 
            prefix_sum += num 
            diff = prefix_sum - goal

            res += seen.get(diff, 0 )

            seen[prefix_sum] = 1 + seen.get(prefix_sum, 0)

        return res