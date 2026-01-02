from typing import List
from collections import Counter

class Solution:


    def repeated_N_times(self, nums: List[int]) -> int:

        target = len(nums) // 2
        c = Counter(nums)

        for k, v in c.items():
            if v == target:
                return k 
        return -1