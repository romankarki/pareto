from typing import List

class Solution:


    def mindiff(self, nums: List[int], k: int) -> int: 
        if len(nums) < k :
            return 0 
        
        nums.sort()

        l, r = 0, k-1

        ans = float("inf")

        while r < len(nums):
            diff = nums[r] - nums[l]
            ans = min(diff, ans)

            r += 1
            l += 1
        return ans 
