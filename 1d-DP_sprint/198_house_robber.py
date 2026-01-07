from typing import List 


class Solution: 


    def hourse_robber_bruteforce (self, nums: List[int]) -> int : 
        def dfs(i: int) -> int: 
            if i >= len(nums):
                return 0 
            # choice: rob this one -> skip next, or skip this one
            return max(nums[i] + dfs(i+2), dfs(i+1))
        
        return dfs(0)
    



s = Solution()

arr = [2,3,5,8,9,11, 19, 1, 12]
print(s.hourse_robber_bruteforce(arr))