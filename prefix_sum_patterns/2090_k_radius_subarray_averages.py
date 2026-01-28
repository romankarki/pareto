from typing import List


class Solution:


    def getAverages(self, nums: List[int], k: int) -> int: 
        '''
        
        nums of n integers 
        k radius average 
        i-k to i+k
        if no such available then it's -1 


        example: [7, 4, 3, 9, 1, 8, 5, 2, 6] for k = 3
        prefix = [7, 11, 14, 23, 24, 32, 37, 39, 45]
        k radius = [-1, -1, -1, ]
        '''

        ans = [-1] * (len(nums))

        l, m, r = 0, k, k+k

        prefix_sum = []
        total = 0 
        for num in nums: 
            total += num 
            prefix_sum.append(total)
        
        
        while r < len(nums): 
            if l == 0: 
                ans[m] = prefix_sum[r] // (r-l+1)
            else: 
                ans[m] = (prefix_sum[r] - prefix_sum[l-1]) // (r-l+1)
            
            l += 1
            r += 1
            m += 1

        return ans 