from typing import List 


class Solution: 


    def min_pair_sum(self, nums: List[int]) -> int: 
        '''
         input -> [3, 5, 2, 3]
         output -> 7 
         exp: 
         (3,2) and (5,2) max is 7
         len ip is even 
         [2,3,3,5]
        '''

        nums.sort()

        l, r = 0, len(nums) - 1
        ans = float('-inf')

        while l < r : 

            pair_sum = nums[l] + nums[r]

            ans = max(ans, pair_sum)


            l += 1
            r -= 1

        return ans 