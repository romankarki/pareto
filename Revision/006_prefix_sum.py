from typing import List 


class Solution: 

    def prefix_sum_pattern_560_subarray_equals_k(self, nums: List[int], k: int) -> bool | int: 
        '''
        [1, 2, 3] k = 3
        [1,2] & [3]


        prefix : { 
            0: 1, 
            1: 1,
            3: 1,
            6: 1
        }
        '''

        res = curr_sum = 0 

        prefix = { 0: 1 }

        for num in nums: 
            curr_sum += num 
            diff = curr_sum - k 
            res += prefix.get(diff, 0)
            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        
        print("prefix", prefix)
        return res
    


    def subarrray_sum_equals_k(self, nums: List[int], k:int) -> int: 

        curr_sum = res = 0 
        prefix = {0: 1}
        for num in nums: 
            curr_sum += num 
            diff = curr_sum - k 
        # if there is curr sum of 3 then it depends on how many ways we can create the diff
            res += prefix.get(diff, 0) 
            prefix = 1 + prefix.get(curr_sum, 0)

        return res 


    def subarray_sum_equals_k(self, nums: List[int], k: int) -> int: 
        curr_sum = res = 0 
        prefix = {} # 0: 1

        for num in nums: 
            curr_sum += num 

            diff = curr_sum - k #overshoot from desired 

            # sum = 6 -> diff = 3 -> 
            # CASE I: prefix : {3: 1} implies there is a way to make 3 and we made 6
            # there should be another way of making 3 -> +1 to res

            #CASE II: prefix = {}
            # sum = 6 -> diff = 3 -> there is no way to make 3 
            # 6 is made up of big numbers a solo 6 or 4+2 or so on 
            res += prefix.get(diff, 0) 
            if diff == 0 : 
                res += 1

            prefix[curr_sum] = 1 + prefix.get(curr_sum, 0)
        return res 







s = Solution()
print(s.prefix_sum_pattern_560_subarray_equals_k([1,2,3], 3))