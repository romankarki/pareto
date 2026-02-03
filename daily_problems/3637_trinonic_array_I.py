from typing import List 


class Solution: 


    def is_trionic(self, nums: List[int]) -> bool: 
        change_in_rise = 1
        inc = nums[0] < nums[1]
        if nums[0] == nums[1]: 
            return False 
        
        if not inc: 
            return False
        
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i+1]: 
                if inc: 
                    pass
                else: 
                    change_in_rise += 1
                    inc = not inc
            elif nums[i] > nums[i+1]: 
                if not inc: 
                    pass 
                else: 
                    inc = not inc
                    change_in_rise += 1
            elif nums[i] == nums[i+1]:
                return False 
        return change_in_rise == 3
            

