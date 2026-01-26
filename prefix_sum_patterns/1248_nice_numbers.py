from typing import List 
from collections import defaultdict


class Solution: 


    def nice_numbers(self, nums: List[int], k: int): 
        prefix = 0 
        mp = defaultdict(int)
        mp[0] = 1
        res = 0 
        
        for x in nums: 
            prefix += x % 2
            res += mp[prefix - k]
            mp[prefix] += 1
        

        print(mp)

        
        return res 
    

s = Solution()

print(s.nice_numbers([1,1,2,1,1], 3))