from typing import List

class Solution: 



    def trionic_ii_sum(self, nums: List[int]) -> int: 
        n = len(nums)

        '''
        f[i][state] = max sum ending at i in 'state'
        (0: inc, 1: inc-dec, 2: inc-dec-inc)
        init with -infinity 
        '''
        f = [[-float('inf')] * 3 for _ in range(n)] 

        for i in range(n):
            f[i][0] = nums[i]
            if i > 0 and nums[i] > nums[i-1]: 
                f[i][0] = max(f[i][0], f[i-1][0] + nums[i])
            
            if i > 0 and nums[i] < nums[i-1]:
                if f[i-1][0] != -float('inf'):
                    f[i][1] = max(f[i][1], f[i-1][0] + nums[i])
                
                if f[i-1][1] != -float('inf'):
                    f[i][1] = max(f[i][1], f[i-1][1] + nums[i])
            
            if i > 0 and nums[i] > nums[i-1]:
                if f[i-1][1] != -float('inf'):
                    f[i][2] = max(f[i][2], f[i-1][1] + nums[i])
                if f[i-1][2] != -float('inf'):
                    f[i][2] = max(f[i][2], f[i-1][2] + nums[i])

        ans = max(row[2] for row in f)
        return ans 
    



s = Solution()

print(s.trionic_ii_sum([0,-2,-1,-3,0,2,-1]))