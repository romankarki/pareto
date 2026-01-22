from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            found = -1
            for x in range(num):
                if ( x | (x+1)) == num:
                    found = x
                    break
            ans.append(found)
        return ans
    

    def min_array_bitwise(self, nums: List[int]) -> List[int]: 
        ans = []

        for num in nums: 
            if num == 2: 
                ans.append(-1)
                continue 

            res = -1 

            for j in range(1, 32): 
                if ((num >> j) & 1) == 0:
                    res = num ^ (1 << (j-1))
                    break 
            ans.append(res)

        return ans 
        