from typing import List 

class Solution:


    def contigous_array(self, nums: List[int]) -> int: 
        '''
        Basic concept:
        1. Running sum +1 for 1 and -1 for 0 
        2. if running_sum seen in prefix_map -> found the diff between i - prefix at that
        in that case equal 0 and 1 is there 
        3. track the max lenght for this behaviour  
        '''
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