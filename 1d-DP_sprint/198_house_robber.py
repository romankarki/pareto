from typing import List 


class Solution: 


    def house_robber_bruteforce (self, nums: List[int]) -> int : 
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> int: 
            if i >= len(nums):
                return 0 
            # choice: rob this one -> skip next, or skip this one
            return max(nums[i] + dfs(i+2), dfs(i+1))
        
        return dfs(0)


    def house_robber_memoization(self, nums: List[int]) -> int: 
        memo = {}
        def dfs(i: int) -> None:
            if i >= len(nums): 
                return 0 
            if i in memo: 
                return memo[i]

            rob_curr = nums[i] + dfs(i+2)

            skip_curr = dfs(i+1)

            memo[i] = max(rob_curr, skip_curr)
            return memo[i]
        
        return dfs(0)


    def repractise_memo(self, nums: List[int]) -> int: 
        from functools import lru_cache

        memo = {}

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i >= len(nums): 
                return 0 
            if i in memo: 
                return memo[i]

            take_curr = nums[i] + dfs(i+2)
            skip_curr = dfs(i+1)

            memo[i] = max(take_curr, skip_curr)

            return memo[i] 


        return dfs(0)
    


s = Solution()

arr = [2,3,5,8,9,11, 19, 1, 12]
print(s.house_robber_bruteforce(arr))
print(s.house_robber_memoization(arr))
print(s.repractise_memo(arr))