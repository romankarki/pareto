from typing import List 


class Solution: 


    def min_removals(self, nums: List[int], k: int) -> int: 
        # O(n log(n))
        nums.sort()

        r = 0 
        n = len(nums)
        ans = n 

        for l in range(n):

            while r < n and nums[r] <= (k * nums[l]):
                r += 1
            
            ans = min(ans, n - (r - l) )
        return ans 