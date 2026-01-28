from typing import List 
from collections import Counter

class Solution: 

    def count_subarrays(self, nums: List[int], k: int) -> int: 
        '''
          [3,2,1,4,5] and k = 4 

          pos = 3 (value = k = 4)

          #right side 
          balance = 0 -> counter = {0: 1}
          for 5 -> counter { 0: 1, 1: 1}

          #left side 
          now left balances
          i = 3 -> 4 -> balance = 0 -> add right_count[0] + right_count[1] = 2 
          i = 2 -> 1 -> balance = -1 -> right_count[1] + right_count[2] = 1 + 0 
        '''

        #one way is brute force like o(n**2) and calling o(n logn) for sorting and median 

        pos = nums.index(k)

        right_count = Counter()
        balance = 0 
        right_count[0] = 1

        for i in range(pos + 1, len(nums)):
            if nums[i] > k: 
                balance += 1
            else: 
                balance -= 1
            right_count[balance] += 1
        
        res = 0 
        balance = 0 
        for i in range(pos, -1, -1):
            if nums[i] > k: 
                balance += 1
            elif nums[i] < k:
                balance -= 1
            res += right_count[-balance]
            res += right_count[-balance + 1]
        return res 
