from typing import List 

class Solution:


    def subarray_sum_divisble_by_k(self, nums: List[int], k: int) -> int:
        res = prefix_sum  = 0 

        remain = {0: 1}

        for num in nums:
            prefix_sum += num 
            mod = prefix_sum % k 
            res += remain.get(mod, 0)

            remain[mod] = 1 + remain.get(mod, 0)

        return res 