from typing import List


class Solution: 


    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        for each in nums: 
            total += each
            ans.append(total)
        return ans
        