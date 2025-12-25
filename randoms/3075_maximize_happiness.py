from typing import List

class Solution:

    def maximum_happiness(self, hapinees: List[int], k : int) -> int:

        hapinees.sort()

        picks = []

        to_deduct = 0 
        for _ in range(0, k):
            curr = hapinees.pop()
            pick = curr - to_deduct
            if pick < 0 :
                pick = 0 
            picks.append(pick)
            to_deduct += 1
        return sum(picks)
        