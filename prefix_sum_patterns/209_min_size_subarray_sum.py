from typing import List 


class Solution: 


    def min_subarray_len(self, target: int, nums: List[int]) -> int: 
        '''
        Example 1:
        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        Example 2:

        Input: target = 4, nums = [1,4,4]
        Output: 1
        Example 3:

        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0


        [2,3,1,2,4,3] and target = 7 

        - sorting is out of the way because we need subarray 

        sliding window in o(n)





        
        '''

        total = sum(nums)
        if total < target: 
            return 0

        if target in nums: 
            return 1 
        
        ans = float('inf')

        l, r = 0, 0 
        running_sum = 0 

        while r < len(nums):
            running_sum += nums[r]
            
            while running_sum >= target and l <= r: 
                ans = min(ans, r-l+1)
                running_sum -= nums[l]
                l += 1
            r += 1


        return ans