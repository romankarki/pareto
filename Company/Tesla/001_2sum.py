class Solution: 


    def two_sum(self, nums, target):

        seen = {}
        
        for i, each in enumerate(nums): 
            req = target - each 

            if req in seen: 
                return [seen[req], i]
            seen[each] = i 
        return [-1, -1]
            