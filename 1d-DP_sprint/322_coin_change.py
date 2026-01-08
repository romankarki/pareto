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


    



s = Solution()

print(s.coin_change([1,2,5], 11))