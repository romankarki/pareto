from typing import List 
from collections import defaultdict, Counter


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
    

    def nice_numbers_subarray(self, nums: List[int], k: int):

        '''
        
        '''


        prefix_count= Counter({0: 1})
        odd_sum = 0 
        result = 0 

        for num in nums: 
            odd_sum += num % 2 
            result += prefix_count[odd_sum - k]
            prefix_count[odd_sum] += 1

        return result 

    

s = Solution()

print(s.nice_numbers([1,1,2,1,1], 3))