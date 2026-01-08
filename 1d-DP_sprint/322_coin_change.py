from typing import List 


class Solution: 


    def coin_change(self, coins: List[int], target: int) -> int: 
        self.ans = float('inf')
        def dfs(i: int, total: int): 
            if total == target: 
                self.ans = min(self.ans, i )
            if total > target: 
                return 
            
            for coin in coins: 
                dfs(i+1, total+coin)

        dfs(0, 0)
        return self.ans if self.ans != float('inf') else -1  


    def coin_change_reframe(self, coins: List[int], amount: int) -> int: 

        def dfs(total):
            if total == amount: 
                return 0 
            
            if total > amount: 
                return float('inf')
            
            ans = float('inf')

            for coin in coins: 
                res = dfs(total+coin)
                if res != float('inf'): 
                    ans = min(ans, 1 + res)
            return ans 


        res = dfs(0)

        return res if res != float('inf') else -1 


    def coin_change_deduct(self, coins: List[int], amount: int) -> int:
        def dfs(rem: int) -> int: 
            if rem == 0: 
                return 0 
            res = float('inf')
            for c in coins: 
                if rem - c >= 0:
                    res = min(res, 1+dfs(rem - c))
            return res 


        min_coins = dfs(amount)
        
        return -1 if min_coins == float('inf') else min_coins

    def coin_change_dp(self, coins: List[int], amount: int) -> int:

        '''
        coins = [1, 3, 5] target = 11 

        dp = [0 1 2 min(1 + dp(2), 1 + dp(0)) _ _ _ _ _ _ _ _]
        '''
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0 

        for i in range(1, len(dp)): 
            for c in coins: 
                if amount >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[-1] if dp[-1] != float('inf') else -1






s = Solution()

print(s.coin_change_dp([1,2,5], 11))