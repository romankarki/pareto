from typing import List
from heapq import heappush, heappop


class Solution: 


    def min_cost(self, nums: List[int], k: int, dist: int) -> int: 
        '''
         nums = [1,3,2,6,4,2] and k = 3 
        '''
        # brute force - O(n**2 log(n))

        k -= 1
        result = float('inf')

        for start in range(1, len(nums) - k + 1):
            end = min(start + dist, len(nums) - 1)
            if end - start + 1 < k : 
                break 

            window = sorted(nums[start: end + 1])
            cost = nums[0] + sum(window[:k])
            result = min(result, cost)
        return result 