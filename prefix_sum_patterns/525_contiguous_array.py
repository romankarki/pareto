from typing import List 

class Solution:


    def contigous_array(self, nums: List[int]) -> int: 
        prefix_map = {0: -1}

        max_len = 0 
        running_sum = 0 

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1 

            if running_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[running_sum])
            else: 
                prefix_map[running_sum] = i  

        return max_len 