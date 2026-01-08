from typing import List
from itertools import combinations

class Solution: 


    def max_dot_product(self, nums1: List[int], nums2: List[int]) -> int: 

        def all_subsequences(arr: List[int]) -> List[List[int]]: 
            subs = [] 
            for length in range(1, len(arr) + 1): 
                subs.extend(combinations(arr, length))
            return subs 
        
        subs1 = all_subsequences(nums1)
        subs2 = all_subsequences(nums2)

        ans = float('-inf')

        for a in subs1: 
            for b in subs2: 
                if len(a) == len(b): 
                    dot = sum(x * y for x, y in zip(a,b))
                    ans = max(ans, dot)
        return ans 


    def max_dot_product_recursion(self, nums1: List[int], nums2: List[int]) -> int: 
        m, n = len(nums1), len(nums2)

        def dfs(i, j, taken): 
            if i == m or j == n: 
                return 0 if taken else float('-inf')
            
            #take both 
            take = nums1[i] *  nums2[j] + dfs(i+1, j+1, True)

            skip1 = dfs(i +1, j, taken)

            skip2 = dfs(j, j+1, taken)

            return max(take, skip1, skip2)
            

        return dfs(0, 0, False)


    def max_dot_product_memoized(self, nums1: List[int], nums2: List[int]) -> int: 
        m, n = len(nums1), len(nums2)

        def dfs(i, j, taken): 

            if i == m or i== n:
                return 0 if taken else float('-inf')
            
            

            return max(
                nums1[i] * nums2[j] + dfs(i + 1, j + 1, True),
                dfs(i + 1, j, taken), 
                dfs(i +1, j+1, taken)
                       )


        return dfs(0, 0, False)




