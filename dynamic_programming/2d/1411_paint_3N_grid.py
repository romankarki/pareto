from typing import List
from typing import Tuple


class Solution:

    def num_of_ways_bruteforce(self, n: int) -> int:
        patterns = []
        for a in range(0, 3):
            for b in range(0, 3):
                for c in range(0, 3):
                    if a != b and b != c:
                        patterns.append((a,b,c))
        
        def solve(row_index: int, prev_row_colors: tuple[int, int, int]) -> int:
            if row_index == n:
                return 1
            total = 0
            for curr_color in range(0, 3):
                if curr_color != prev_row_colors[0] and curr_color != prev_row_colors[1]:
                    total += solve(row_index + 1, [prev_row_colors[1], curr_color])
            return total
        return solve(0, (-1, -1, -1))
        
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
    

    def num_ways_bottom_up(self, n: int) -> int:
        '''
        pseudo code:
        dp[row][pattern] = ways 
        dp[0][pattern] = 1 for all patterns 
        for row in 1....,n:
            for curr_pattern:
                dp[row][curr] += dp[row-1][prev]
                if compatible(prev, curr)
        
        answer = sum(dp[n][*])
        
        '''
        pass



ip = 300
s = Solution()
op = s.num_of_ways(ip)
print(op)
    