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