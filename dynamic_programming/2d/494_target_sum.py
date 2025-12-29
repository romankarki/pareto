from typing import List

class Solution:
    def target_sums_brute(self, nums: List[int], target: int) -> int:

        def backtrack(i, total):
            if i == len(nums):
                return total == target
            
            return backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])


        return backtrack(0, 0) 
        
    
    def target_sum_memo(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in memo:
                return memo[(i,total)]
            
            memo[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
            return memo[(i, total)]
        return backtrack(0,0)


s = Solution()

# print(s.target_sums_brute([1,2,3,4,5], 5))
print(s.target_sum_memo([1,2,3,4,5], 5))