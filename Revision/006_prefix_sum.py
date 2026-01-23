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
    

    def cont_subarray_sum_523(self, nums: List[int], k: int) -> bool: 
        """
        Problem Statement: 
        input = [23, 2, 4, 6, 7] for k = 6
        output = True 
        2+4 = 6 (contiguous)

        sum(input) = 42 % 6 == 0 


        Answer: Optimal 
        k = 6
        remain = {
            5: 0, 
            1: 1, 
            5: 2

        }

        k = 13 
        [23, 2, 4, 6, 7] 
        remain = {
            10: 0, 
            12: 1, 
            3 : 2, 
            9 : 3,
            3 : 4
        }

        k = 13
        [23, 2, 6, 4, 7]
         23 25 31 35  42
         10 12 2  6   3
         0   1 2  3   4


         [23,  2,  4,  6,  7]
          23  25   29  35  42
          10  12   3   9    3


        """

        remain = {0: -1} # remainder : index

        total = prefix = 0 
        
        for i, x in enumerate(nums):
            total += x
            prefix = total % k 
            if prefix not in remain:
                remain[prefix] = i
            elif (i - remain[prefix] > 1): 
                return True 
        
        return False 



        #brute force  
        for i in range(0, len(nums) - 1):
            total = nums[i] # I'm skipping for len == 1
            for j in range(i+1, len(nums)):
                total += nums[j]
                if total % k == 0:
                    return True 
        

        remain = {}
        total = prefix = 0 

        return False 
    


    def is_cont_subarray_sum_modulo(self, nums: List[int], k: int) -> bool:
        remain = {0: -1} # remainder : index and 0 remainder for -1 not started 

        prefix = total = 0

        for i, num in enumerate(nums): 
            total += num 
            prefix = total % k
            if prefix not in remain: 
                remain[prefix] = i
            elif (i - remain[prefix]) >= 2:
                return True 
        return False 







s = Solution()
print(s.prefix_sum_pattern_560_subarray_equals_k([1,2,3], 3))