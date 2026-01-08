from typing import List
from itertools import combinations

class Solution: 


    def max_dot_product(self, nums1: List[int], nums2: List[int]) -> int: 

        def all_subsequences(arr: List[int]) -> List[List[int]]: 
            subs = [] 
            for length in range(1, len(arr) + 1): 
                subs.extend(combinations(arr, length))
            return subs 
        
        subs1 = all_subsequences(nums1)
        subs2 = all_subsequences(nums2)

        ans = float('inf')

        for a in subs1: 
            for b in subs2: 
                if len(a) == len(b): 
                    dot = sum(x * y for x, y in zip(a,b))
                    ans = max(ans, dot)
        return ans 