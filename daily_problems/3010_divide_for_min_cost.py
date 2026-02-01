from typing import List 



class Solution: 
    def min_cost(self, nums: List[int]) -> int: 

        first = nums[0]
        second_smallest = float('inf')
        third_smallest = float('inf')


        for i in range(1, len(nums)):
            if nums[i] < second_smallest: 
                third_smallest = second_smallest
                second_smallest = nums[i]
            elif nums[i] < third_smallest: 
                third_smallest = nums[i]
                
        return first + second_smallest + third_smallest