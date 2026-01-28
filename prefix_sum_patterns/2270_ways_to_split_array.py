from typing import List 



class Solution:


    def ways_to_split(self, nums:List[int]) -> int: 
        '''
        zero indexed array 
        sum of first i+1 elements >= sum of n-i-1 elements
        sum from 0 to i >= sum i+1 to n-1
        '''

        splits = 0 

        total = sum(nums)

        r = 0 
        left_sum, right_sum = 0, total 

        while r < len(nums) -1: 
            left_sum += nums[r]
            right_sum -= nums[r]

            if left_sum >= right_sum:
                splits += 1
            r +=1

        return splits 