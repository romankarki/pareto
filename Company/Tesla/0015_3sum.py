from typing import List 

class Solution: 


    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i,a in enumerate(nums):
            if a > 0:
                break 

            l, r = i + 1, len(nums) - 1
            req = 0 - a
            if i > 0 and nums[i-1] == nums[i]:
                continue 
                
            while l < r: 
                total = nums[l]  + nums[r]
                if total == req:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1 
                    continue 

                if total > req:
                    r -= 1 
                else: 
                    l += 1
        return ans 