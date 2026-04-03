from typing import List

class Solution:

    def max_profit(self, prices: List[int]) -> int: 
        if len(prices) == 1:
            return 0 
        l, r = 0, 1
        max_profit = 0
        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r 
                r += 1 
                continue
            max_profit = max(profit, max_profit)
            r += 1 

        return max_profit
    

    def max_profit_revision_1(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 
        
        l, r = 0, 1
        max_profit = 0 

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r 
                r += 1
                continue

            max_profit = max(max_profit, profit)
            r += 1
        return max_profit


    def max_profit_revision_2(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 
        
        l, r = 0, 1
        res = 0 

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r 
                r += 1
                continue 
            res = max(res, profit)
            r += 1

        return res 
