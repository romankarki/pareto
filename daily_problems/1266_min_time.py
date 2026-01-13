from typing import List
# from math import abs

class Solution:


    def min_time(self, points: List[List[int]]) -> int: 

        total = 0 
        for i in range(len(points) - 1):
            curr = points[i]
            nxt = points[i+1]

            dx = abs(curr[0] - nxt[0])
            dy = abs(curr[1] - nxt[1])

            total += max(dx, dy)
        return total