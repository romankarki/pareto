from typing import List
from collections import defaultdict

class Solution:

    def minLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        l, total = 0, 0 
        ans = float('inf')

        for r in range(len(nums)):
            counts[nums[r]] += 1

            if counts[nums[r]] == 1:
                #add only if it's the first time 
                total += nums[r]
            
            while total >= k:
                curr_len = r - l + 1
                ans = min(ans, curr_len)

                counts[nums[l]] -= 1
                if counts[nums[l]] == 0:
                    total -= nums[l]
                l += 1
        return ans if ans <= len(nums) else -1
    


s = Solution()

print(s.minLength([2,2,3,1], 4))
            