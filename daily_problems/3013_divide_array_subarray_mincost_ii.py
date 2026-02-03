from typing import List
from heapq import heappush, heappop


class Solution: 


    def min_cost(self, nums: List[int], k: int, dist: int) -> int: 
        '''
         nums = [1,3,2,6,4,2] and k = 3 


         here I have to select nums[0] = 1 for cost calc

         so there is case like 

         [1] [3,2,6,4,2] -> select 2 break points from 
         [1] [3,2,6,4] -> select k break points
         [1] [2,6,4,2] -> select k break points
         [1] [6,4,2] -> select k break points
         [1] [4,2] -> select k break points 
        '''
        # brute force - O(n**2 log(n))

        k -= 1
        result = float('inf')
        print('input = ', nums)
        print("k = k - 1 =", k)

        for start in range(1, len(nums) - k + 1):
            print("------------------------------")
            end = min(start + dist, len(nums) - 1)
            if end - start + 1 < k : 
                break 

            print("start =", start,"and end =", end)

            window = sorted(nums[start: end + 1])
            print("window=",window)
            cost = nums[0] + sum(window[:k])
            print("cost = ", nums[0] ,"+ sum of", window[:k] )
            print("result = min of", result,"and", cost )
            result = min(result, cost)
            print("cost =", cost,"and result=", result)
        return result 
    


s = Solution()

s.min_cost([1,3,2,6,4,2], 3, 3)