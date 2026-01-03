from typing import List

class Solution:

    def minLength(self, nums: List[int], k: int) -> int:
        res= len(nums) * 2
        for i in range(0, len(nums)):
            total = 0 
            count = 0 
            seen = set()
            n = []
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    total += nums[j]
                    seen.add(nums[j])
                count += 1
                # seen.add(nums[j])
                n.append(nums[j])
                if total >= k:
                    # print(n)
                    res = min(res, count)
                    break
        if res > len(nums):
            return -1
        return res

    def min_length_at_k(self, nums: List[int], k: int) -> int:
        
        pass