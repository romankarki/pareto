from typing import List

class Solution:


    '''
    Docstring for Solution

    Universal Pattern for backtracking in general 

    def backtrack(path, remaining_path):
        if is_valid_solution:
            result.append(path[:])
            return 
        
        for choice in remaining_options:
            if not is_valid(choice):
                continue
            
            #Make move
            path.append(choice)

            #recursion call 
            backtrack(path, updated_options)

            #undo move (backtrack)
            path.pop()
    '''

    '''
        Q1. Description: Given an integer array nums of unique elements, 
        return all possible subsets (the power set). 
        Input: nums = [1, 2, 3] 
        Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # generate powersets 
        # Time -> O(n * 2**n)
        # Space -> O(n)
        res = []
        
        def backtrack(index: int, subset: List[int]) -> None:
            res.append(subset[:])

            for i in range(index, len(nums)):
                #making a choice
                subset.append(nums[i])

                #going with a choice
                backtrack(i + 1, subset)

                #retracting a choice to try another 
                subset.pop()
        backtrack(0, [])
        return res


    '''
    Description: Given an array of distinct integers candidates and a target,
    return a list of all unique combinations where the chosen numbers sum to target. 
    You may use the same number multiple times.
      Input: candidates = [2, 3, 6, 7], target = 7 
      Output: [[2, 2, 3], [7]]
    '''

    def combination_sum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time : O(N ** (T/M))
        # Space: O(T/M)
        res = []

        def backtrack(index: int, curr: List[int], total: int) -> None:
            #base case: found result 
            if total == target:
                res.append(curr.copy())
                return 
            
            #pruning 
            if total > target:
                return 

            for i in range(index, len(nums)):
                curr.append(nums[i])

                backtrack(i, curr, total + nums[i])
                curr.pop()
            
        
        backtrack(0, [], 0)
        return res





s = Solution()

print(s.subsets([1,2,3]))
print(s.combination_sum([1,2,3,6,7], 7))


