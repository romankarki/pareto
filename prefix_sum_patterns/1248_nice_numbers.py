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
        nums = [1, 1, 2, 1, 1]   k = 3 
        output is 2 i.e. (1,1,2,1) or (1,2,1,1)

        prefix_count = {
            0: 1,
           -2: 0,
            1: 1,
           -1: 0,
            2: 2,
            3: 1, 
            4: 1

        }
        odd_sum = 0+1 -> 1 | 1+1 -> 2 | 2+0 -> 2 | 2+1 -> 3
        [1, 1, 2, 1, 1]
        '''
        # O(n) O(n)


        prefix_count= Counter({0: 1})
        odd_sum = 0 
        result = 0 

        for num in nums: 
            odd_sum += num % 2 
            result += prefix_count[odd_sum - k]
            prefix_count[odd_sum] += 1

        return result 


    def space_optimized(self, nums, k):
        def atmost(goal):
            left = count = oddCount = 0 
            for right in range(len(nums)):
                oddCount += nums[right] % 2
                while oddCount > goal: 
                    oddCount -= nums[left] % 2
                    left += 1
                count += right - left + 1
            return count 

        return atmost(k) - atmost(k-1)

    

s = Solution()

print(s.nice_numbers([1,1,2,1,1], 3))