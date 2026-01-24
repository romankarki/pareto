from typing import List 



class Solution: 




    def min_ops_to_sort(self, arr: List[int]) -> int: 
        '''
         [5,2,3,1]
         [5,2,4]
         [5, 6]

        '''

        def is_sorted(numbers):
            for i in range(0, len(numbers) - 1):
                if numbers[i] > numbers[i+1]:
                    return False
            return True 


        nums = arr[:]

        ops = 0 
        while not is_sorted(nums):
            min_pair = nums[0] + nums[1]
            idx = 0 

            for i in range(1, len(nums) - 1):
                curr = nums[i] + nums[i+1]
                if min_pair > curr: 
                    idx = i 
                    min_pair = curr 
            
            nums[idx] = min_pair
            nums.pop(idx+1)
        return ops 