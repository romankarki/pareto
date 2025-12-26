from typing import List

class Solution:

    def permuteUnique(self, nums: List[int]) -> List[int]:
        self.res = []
        self.seen = set()
        self.backtrack([], nums, [False] * len(nums))

        return self.res
    

    def backtrack(self, perm, nums, pick):

        if len(perm)  == len(nums):
            c = perm[:]
            if c not in self.seen:
                self.res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                pick[i] = False
                perm.pop()