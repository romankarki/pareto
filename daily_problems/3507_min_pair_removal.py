from typing import List 


class Solution: 


    def min_pair_removal(self, nums: List[int]) -> int: 

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True 
        
        arr = nums[:]
        ops = 0 
        while not is_sorted(arr):
            min_sum = arr[0] + arr[1]
            idx  = 0 
            for i in range(1, len(arr)-1):
                if (arr[i] + arr[i+1]) < min_sum:
                    min_sum = arr[i] + arr[i+1]
                    idx = i 
            
            arr[idx] = min_sum
            arr.pop(idx + 1)
            ops +=1 


        return ops