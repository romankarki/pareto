from typing import List

class Solution: 


    def __init__(self, nums: List[int]):
        self.number = nums 
        self.prefix = [] 

        c_sum  = 0 
        for num in nums: 
            c_sum += num
            self.prefix.append(c_sum)

    

    def sumRange(self, left: int, right: int) -> int: 

        r = self.prefix[right]
        l = self.prefix[left - 1] if (left-1) >= 0 else 0 

        return r-l