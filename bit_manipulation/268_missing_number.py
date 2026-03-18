class Solution:


    def missing_number(self, nums):
        n = len(nums)
        xorr = n 
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
