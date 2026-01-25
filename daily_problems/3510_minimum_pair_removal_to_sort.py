from typing import List 
import heapq


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


    def greedy(self, nums: List[int]) -> int: 
        
        n = len(nums)
        if n <= 1: 
            return  0 
        
        next_arr = list(range(1, n+1))
        next_arr[-1] = -1 
        prev_arr = list(range(-1, n-1))

        removed = [False] * n 
        vals = list(nums)

        inversions = 0 
        for i in range(n-1):
            if vals[i] > vals[i+1]:
                inversions += 1
        if inversions == 0 :
            return 0 
        
        pass