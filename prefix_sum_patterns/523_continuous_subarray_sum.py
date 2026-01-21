from typing import List 


class Solution: 


    def check_subarray_sum(self, nums: List[int], k: int) -> bool: 
        '''
        input = [23, 2, 4, 6, 7] and k = 6 
        output = true
        exp: [2,4] is sum 6 and len >= 2 and is multiple of k 


        input = [23, 2, 6, 4, 7] and k = 6 
        output = true
        exp: total sum is 42 of len >= 2 and is multiple of k = 6 

        brute force will be o(n**2) & o(1)
        optimal o(n) & o(n)
        '''
        mp = {0: -1} # remainder : index
        prefix = 0

        for i, x in enumerate(nums): 
            prefix = (prefix + x) % k
            if prefix in mp: 
                if i - mp[prefix] > 1: 
                    return True 
            else: 
                mp[prefix] = i 

        return False  
    

    def check_subarray_intuitive(self, nums: List[int], k: int) -> bool: 

        remain = {} # remainder: index
        total = 0
        prefix = 0 
        for i,x in enumerate(nums): 
            total += x
            prefix = (total) % k
            if prefix not in remain: 
                remain[prefix] = i
            elif (i - remain[prefix]) > 1:
                return True  

        return False 



    def brute_force(self, nums: List[int], k: int) -> bool: 
        #o(n**2) 
        for i in range(0, len(nums) - 1): 
            total = 0 + nums[i]
            for j in range(i+ 1, len(nums)): 
                total += nums[j]
                if total % k == 0: 
                    return True 
        
        return False 





s = Solution()

print(s.brute_force([23, 2, 6, 4, 7, 13], 13))
print(s.brute_force([23, 2, 6, 4, 7], 6))




