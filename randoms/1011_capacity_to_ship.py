from typing import List

class Solution:

    def find_cargo_capacity(self, weights: List[int], days: int) -> int:
        if len(weights) < days:
            return 0 
        maxx = max(weights)
        if len(weights) == days:
            return maxx
        total = sum(weights)
        if days == 1:
            return total 
        l, r = maxx, total
        ans = total 
        while l <= r:
            m = (l+r) // 2

            if self.can_ship(weights, days, m):
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        return ans 
    

    def can_ship(self, weights, days, capacity):
       ships, currCap = 1, capacity
       for w in weights:
           if currCap - w < 0:
               ships += 1
               if ships > days:
                   return False
               currCap = capacity
           currCap -= w
       return True 


