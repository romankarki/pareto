from typing import List

class Solution:


    def permute_recursion(self, nums: List[int]) -> List[List[int]]:
        '''
        Docstring for permute_recursion
        
        :param self: Description
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: List[int]

        dry_run::
            - get and element from second to end of array 
            [1,2,3] -> [2,3] -> [3]
            -  
        Time: O(n! * n^2)
        Space: O(n! * n)
        '''
        if len(nums) == 0:
            return [[]]

        perms = self.permute_recursion(nums[1:])
        print("nums ->", nums)
        print("perms ->", perms)

        res = []
        for p in perms:
            for i in range(len(p)+ 1):

                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                print("p_copy", p_copy)
                res.append(p_copy)
        print("returning response", res)
        print("----------------------------------------") 
        return res
    
    def permute_iterative(self, nums:List[int]) -> List[List[int]]:
        '''
        Docstring for permute_iterative
        
        :param self: Description
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: List[int]

        Time = O(n!* n^2)
        Space = O(n! * n)
        '''
        perms  =[[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
    

    def permute_backtracking(self, nums:List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False]* len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums:List[int], pick: List[bool]) -> List[List[int]] :
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return 
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False

s = Solution()

# print(s.permute_recursion([1,2,3]))
# print(s.permute_iterative([1,2,3]))
print(s.permute_backtracking([1,2,3]))
