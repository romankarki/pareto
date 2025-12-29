from typing import List

class Solution:
    def target_sums_brute(self, nums: List[int], target: int) -> int:

        def backtrack(i, total):
            if i == len(nums):
                return total == target
            
            return backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])


        return backtrack(0, 0) 
        


s = Solution()

print(s.target_sums_brute([1,2,3,4,5], 5))