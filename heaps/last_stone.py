from typing import List
import heapq

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        if len(stones) == 1:
            return abs(stones[0])
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            diff = abs(second - first)

            if diff != 0:
                heapq.heappush(stones, diff)
        
        if len(stones) == 0:
            return 0
        

        return abs(stones[0])
        