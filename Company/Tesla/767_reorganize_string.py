import heapq
from collections import Counter

class Solution:

    def reorganize_string(self, s: str) -> str:
        counts = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        result = [] 

        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            result.append(ch1)
            result.append(ch2)

            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1+1, ch1))
            if cnt2 + 1 < 0: 
                heapq.heappush(heap, (cnt2 + 1, ch2))

        if heap:
            cnt, ch = heap[0]
            if -cnt > 1:
                return "" # impossible 
            result.append(ch)
            
        return "".join(result)