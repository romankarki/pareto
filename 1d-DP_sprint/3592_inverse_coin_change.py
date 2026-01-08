from typing import List


class Solution: 

    def make_ways(self, coins: List[int], n: int) -> List[int]: 
        dp  = [0] * (n+1)

        dp[0] = 1
        for c in coins: 
            for j in range(c, n+1):
                dp[j] += dp[j-c]

        return dp[1:]

    def brute_inverse(self, num_ways: int) -> List[int]: 
        pass

        # TODO : LATER TOO MUCH DIFFICULT FOR TODAY
        # n = len(num_ways)

        # for r in range(1, n+1): 
        #     for combo in combinations(range(1, n+1), r): 
        #         if make_ways(combo)

