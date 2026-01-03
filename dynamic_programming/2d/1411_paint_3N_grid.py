from typing import List


class Solution:

    def num_of_ways(self, n: int) -> int:

        M = 10**9 + 7

        patterns = []
        #colors are 0, 1 and 2 
        for a in range(0, 3):
            for b in range(0, 3):
                for c in range(0, 3):
                    if a != b and b != c:
                        patterns.append((a,b,c))

        

        def is_ok(p1: List[int], p2: List[int]) -> bool:
            return all( p1[i] != p2[i] for i in range(3))


        memo = {}

        # from functools import lru_cache

        # @lru_cache(None)
        def dfs(row, prev):
            if row == n: 
                return 1 
            total = 0 
            if (row, prev) in memo:
                return memo[(row, prev)]

            for pattern in patterns:
                if prev is None or is_ok(prev, pattern):
                    total += dfs(row+1, pattern)
            memo[(row, prev)] = total % M
            return memo[(row,  prev)]

        return dfs(0, None)



ip = 300
s = Solution()
op = s.num_of_ways(ip)
print(op)
    